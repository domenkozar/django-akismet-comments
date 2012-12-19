Django moderator for checking django.contrib.comments spam against akismet service.


INSTALL
=======

::

    $ pip install django-akismet-comments


USAGE
=====

- First, you need to specify ``AKISMET_API_KEY`` in ``settings.py``
- Add ``django_akismet_comments`` to ``INSTALLED_APPS`` in ``settings.py``
- Register your models::
   
    from django.contrib.comments.moderation import moderator
    from django_akismet_comments import AkismetModerator

    ...

    # where News is your model you want to moderate for comments
    moderator.register(News, AkismetModerator)


Settings
========

``AKISMET_API_KEY``
    The api key of Akismet of your url.


DEVELOP
=======

::

    $ git clone https://github.com/iElectric/django-akismet-comments.git django-akismet-comments
    $ cd django-akismet-comments
    $ virtualenv .
    $ source bin/activate
    $ python setup.py develop
    $ easy_install django-akismet-comments[test]
