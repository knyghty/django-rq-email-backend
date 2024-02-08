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
    try:
        result = conn.send_messages([message])
    except Exception:
        logger.warning("Failed to send email message to %r, retrying.", message.to)
        logger.exception()
    else:
        logger.debug("Successfully sent email message to %r.", message.to)
        return result
