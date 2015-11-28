import datetime
from .models import SiteOwner, Image
from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse

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


def create_site_owner(name, email, phone):
    return SiteOwner.objects.create(name=name, email=email, phone=phone)

    
class OwnersViewTests(TestCase):
    def test_index_view_with_zero_owners(self):
        response = self.client.get(reverse('main:owners'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['owners'], [])


    def test_index_view_with_one_owners(self):
        create_site_owner('sean', 'sean.lin@live.com', '0431071978')
        response = self.client.get(reverse('main:owners'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['owners'], ['<SiteOwner: sean<sean.lin@live.com>>'])
