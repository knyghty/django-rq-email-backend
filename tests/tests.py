import contextlib
import io
import logging
import unittest.mock

from django.core import mail
from django_rq import get_worker

from django_rq_email_backend.backends import RQEmailBackend


class EmailBrokenError(Exception):
    pass


class MockEmailConnection:
    def send_messages(self, email_messages, **kwargs):
        raise EmailBrokenError


class TestEmailBackend(unittest.TestCase):
    def setUp(self):
        self.backend = RQEmailBackend()
        self.message = mail.EmailMessage(
            subject="Subject",
            body="Message",
            from_email="foo@example.com",
            to=["bar@example.com"],
        )

    def test_send_email(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output), self.assertLogs(
            level=logging.DEBUG, logger="django_rq_email_backend.tasks"
        ) as recording:
            self.backend.send_messages([self.message])
            get_worker().work(burst=True)
        self.assertIn("To: bar@example.com", output.getvalue())
        self.assertEqual(
            "Successfully sent email message to ['bar@example.com'].",
            recording.records[0].getMessage(),
        )

    @unittest.mock.patch("django_rq_email_backend.tasks.get_connection")
    def test_send_email_with_exception_logs(self, mock_get_connection):
        mock_get_connection.return_value = MockEmailConnection()
        with self.assertLogs(
            level=logging.WARNING, logger="django_rq_email_backend.tasks"
        ) as recording:
            self.backend.send_messages([self.message])
            get_worker().work(burst=True)
        mock_get_connection.assert_called()
        self.assertEqual(
            "Failed to send email message to ['bar@example.com'], retrying.",
            recording.records[0].getMessage(),
        )
