========================
django-rq-email-backend
========================

.. image:: https://travis-ci.org/jefftriplett/django-rq-email-backend.png?branch=master
    :target: https://travis-ci.org/jefftriplett/django-rq-email-backend
    :alt: Build Status

.. image:: https://coveralls.io/repos/jefftriplett/django-rq-email-backend/badge.png?branch=master
    :alt: Coverage Status

.. image:: https://requires.io/github/jefftriplett/django-rq-email-backend/requirements.png?branch=master
    :target: https://requires.io/github/jefftriplett/django-rq-email-backend/requirements/?branch=master
    :alt: Requirements Status

.. image:: https://badge.fury.io/py/django-rq-email-backend.png
    :target: http://badge.fury.io/py/django-rq-email-backend
    :alt: Latest Package Version

.. image:: https://pypip.in/d/django-rq-email-backend/badge.png
    :target: https://crate.io/packages/django-rq-email-backend?version=latest
    :alt: Download Status

------------
Requirements
------------

* `Django <https://www.djangoproject.com/>`_
* `RQ <https://pypi.python.org/pypi/rq>`_
* `Django-RQ <http://pypi.python.org/pypi/django-rq>`_

------------
Installation
------------

* Install ``django-rq-email-backend``:

.. code-block:: python

    pip install django-rq-email-backend

* Add ``django_rq`` to ``INSTALLED_APPS`` in ``settings.py``:

.. code-block:: python

    INSTALLED_APPS = (
        # other apps
        'django_rq_email_backend',
    )

You must then set ``django_rq_email_backend`` as your ``EMAIL_BACKEND``::

    EMAIL_BACKEND = 'django_rq_email_backend.backends.RQEmailBackend'

By default ``django-rq-email-backend`` will use Django's builtin ``SMTP`` email backend
for the actual sending of the mail. If you'd like to use another backend, you
may set it in ``RQ_EMAIL_BACKEND`` just like you would normally have set
``EMAIL_BACKEND`` before you were using Celery. In fact, the normal installation
procedure will most likely be to get your email working using only Django, then
change ``EMAIL_BACKEND`` to ``RQ_EMAIL_BACKEND``, and then add the new
``EMAIL_BACKEND`` setting from above.

-----------
Inspiration
-----------

`django-rq-email-backend` was heavilty influenced by:

* `django-celery-email <https://bitbucket.org/pmclanahan/django-celery-email>`_
* `django-rq-mail <https://github.com/thoas/django-rq-mail>`_

---------
Changelog
---------

0.1.3
-----
* Fixed exception handler to bubble up error if send_email fails.

0.1.2
-----
* Fixed broken installation.

0.1.1
-----
* Renamed project to avoid potential confusion with `django-rq-mail`.

0.1.0
-----
* Initial release
