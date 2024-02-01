#!/usr/bin/env python
import sys
import django.test.utils

from django.conf import settings


settings.configure(
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory;"}},
    INSTALLED_APPS=[
        "django_rq",
        "django_rq_email_backend",
    ],
    MIDDLEWARE_CLASSES=[
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
    ],
)


def runtests(*test_args):
    django.setup()
    runner_class = django.test.utils.get_runner(settings)
    test_runner = runner_class(verbosity=1, interactive=True, failfast=False)
    failures = test_runner.run_tests(["django_rq_email_backend"])
    sys.exit(failures)


if __name__ == "__main__":
    runtests()
