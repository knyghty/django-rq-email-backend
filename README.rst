===============
Django-RQ-Email
===============

------------
Requirements
------------

* `Django <https://www.djangoproject.com/>`_
* `RQ <https://pypi.python.org/pypi/rq>`_
* `Django-RQ <http://pypi.python.org/pypi/django-rq>`_

------------
Installation
------------

* Install ``django-rq-email``:

.. code-block:: python

    pip install django-rq-email

* Add ``django_rq`` to ``INSTALLED_APPS`` in ``settings.py``:

.. code-block:: python

    INSTALLED_APPS = (
        # other apps
        'django_rq_email',
    )

You must then set ``django-rq-email`` as your ``EMAIL_BACKEND``::

    EMAIL_BACKEND = 'django_rq_email.backends.RqEmailBackend'

By default ``django-rq-email`` will use Django's builtin ``SMTP`` email backend
for the actual sending of the mail. If you'd like to use another backend, you
may set it in ``RQ_EMAIL_BACKEND`` just like you would normally have set
``EMAIL_BACKEND`` before you were using Celery. In fact, the normal installation
procedure will most likely be to get your email working using only Django, then
change ``EMAIL_BACKEND`` to ``RQ_EMAIL_BACKEND``, and then add the new
``EMAIL_BACKEND`` setting from above.

-----------
Inspiration
-----------

`Django-RQ-Email` was heavilty influenced by:

* `django-celery-email <https://bitbucket.org/pmclanahan/django-celery-email>`_
* `django-rq-mail <https://github.com/thoas/django-rq-mail>`_

---------
Changelog
---------

0.1.0
-----
* Initial release
