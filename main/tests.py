import datetime
from .models import Image
from django.test import TestCase
from django.utils import timezone

# Create your tests here.

class ImageMethodTests(TestCase):
    def test_was_uploaded_recently_with_future_image(self):
        """
        was_uploaded_recently() should return False for images whose uploaded_at is in the future
        """
        uploaded_at = timezone.now() + datetime.timedelta(days=30)
        image = Image(uploaded_at=uploaded_at)
        self.assertEqual(image.was_uploaded_recently(), False)


    def test_was_uploaded_recently_with_old_image(self):
        """
        was_uploaded_recently() should return False for images whose uploaded_at is older than 1 day
        """
        uploaded_at = timezone.now() - datetime.timedelta(days=2)
        image = Image(uploaded_at=uploaded_at)
        self.assertEqual(image.was_uploaded_recently(), False)


    def test_was_uploaded_recently_with_recent_image(self):
        """
        was_uploaded_recently() should return True for images whose uploaded_at is within last day(24 hours)
        """
        uploaded_at = timezone.now() - datetime.timedelta(hours=6)
        image = Image(uploaded_at=uploaded_at)
        self.assertEqual(image.was_uploaded_recently(), True)
