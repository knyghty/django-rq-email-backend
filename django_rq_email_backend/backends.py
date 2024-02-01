from django.core.mail.backends.base import BaseEmailBackend

from .tasks import send_email


class RQEmailBackend(BaseEmailBackend):
    def __init__(self, fail_silently=False, **kwargs):
        super().__init__(fail_silently)
        self.init_kwargs = kwargs

    def send_messages(self, email_messages, **kwargs):
        kwargs["_backend_init_kwargs"] = self.init_kwargs
        return [send_email.delay(message, **kwargs) for message in email_messages]
