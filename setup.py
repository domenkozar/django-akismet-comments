# -*- coding: utf-8 -*-

import os

from setuptools import setup
from setuptools import find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name='django-akismet-comments',
    version='0.1',
    description='Django moderator for checking django.contrib.comments spam against akismet service.',
    long_description=read('README.rst') +
                     read('HISTORY.rst') +
                     read('LICENSE'),
    classifiers=[
        "Programming Language :: Python",
    ],
    author='Domen Kožar',
    author_email='domen@dev.si',
    url='',
    license='BSD',
    packages=find_packages(),
    install_requires=[
        'setuptools',
        'akismet',
    ],
    extras_require={
        'test': [
            'nose',
            'nose-selecttests',
            'coverage',
            'unittest2',
            'flake8',
        ],
        'development': [
            'zest.releaser',
        ],
    },
    entry_points="""
    """,
    include_package_data=True,
    zip_safe=False,
)
