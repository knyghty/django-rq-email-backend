DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory;"}}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = "django_rq_email_backend.backends.RQEmailBackend"
RQ_EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS = [
    "django_rq",
    "django_rq_email_backend",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

RQ_QUEUES = {
    "default": {
        "ASYNC": False,
        "HOST": "localhost",
        "PORT": 6379,
        "DB": 0,
    }
}

SECRET_KEY = "django-insecure-dummy"
