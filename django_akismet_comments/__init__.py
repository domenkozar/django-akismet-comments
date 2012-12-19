import warnings

from akismet import Akismet
from django.contrib.comments.moderation import CommentModerator

from django.conf import settings


class AkismetModerator(CommentModerator):

    def __init__(self, *a, **kw):
        if not hasattr(settings, 'AKISMET_API_KEY'):
            raise ValueError("You must define the AKISMET_API_KEY setting.")
        super(AkismetModerator, self).__init__(*a, **kw)

    def check_spam(self, request, comment):
        blog_url = request.build_absolute_uri('/')

        ak = Akismet(
            key=settings.AKISMET_API_KEY,
            blog_url=blog_url,
        )

        if ak.verify_key():
            data = {
                'user_ip': request.META.get('REMOTE_ADDR', '127.0.0.1'),
                'user_agent': request.META.get('HTTP_USER_AGENT', ''),
                'referrer': request.META.get('HTTP_REFERER', ''),
                'comment_type': 'comment',
                'comment_author_email': comment.user_email.encode('utf-8'),
                'comment_author_url': comment.user_url.encode('utf-8'),
                'comment_author': comment.user_name.encode('utf-8'),
            }

            return ak.comment_check(comment.comment.encode('utf-8'),
                                    data=data,
                                    build_data=True)
        else:
            warnings.warn("Invalid AKISMET_API_KEY.")

    def allow(self, comment, content_object, request):
        allow = super(AkismetModerator, self).allow(comment,
                                                    content_object,
                                                    request)

        spam = self.check_spam(
            request,
            comment,
        )

        return not spam and allow
