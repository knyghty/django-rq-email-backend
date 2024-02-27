import logging

from django.conf import settings
from django.core.mail import get_connection
from django_rq import job

RQ_EMAIL_DEFAULT_QUEUE = getattr(settings, "RQ_EMAIL_DEFAULT_QUEUE", "default")
RQ_EMAIL_BACKEND = getattr(
    settings, "RQ_EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend"
)
logger = logging.getLogger(__name__)


@job(RQ_EMAIL_DEFAULT_QUEUE)
def send_email(message, **kwargs):
    conn = get_connection(
        backend=RQ_EMAIL_BACKEND, **kwargs.pop("_backend_init_kwargs", {})
    )
    extra = {"to": message.to, "subject": message.subject}
    try:
        result = conn.send_messages([message])
    except Exception:
        logger.exception("Failed to send email message, retrying.", extra=extra)
    else:
        logger.debug("Successfully sent email message.", extra=extra)
        return result
