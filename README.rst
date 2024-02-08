========================
django-rq-email-backend
========================

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

.. code-block:: bash

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
``EMAIL_BACKEND`` before you were using RQ. In fact, the normal installation
procedure will most likely be to get your email working using only Django, then
change ``EMAIL_BACKEND`` to ``RQ_EMAIL_BACKEND``, and then add the new
``EMAIL_BACKEND`` setting from above.

-----------
Inspiration
-----------

`django-rq-email-backend` was heavily influenced by:

* `django-celery-email <https://bitbucket.org/pmclanahan/django-celery-email>`_
* `django-rq-mail <https://github.com/thoas/django-rq-mail>`_
