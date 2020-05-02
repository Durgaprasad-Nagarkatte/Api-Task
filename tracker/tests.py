from django.test import TestCase
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Tracker
from datetime import datetime

# Create your tests here.
User = get_user_model()

class ActivityTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123', password2='abc123', first_name='Durga', last_name='Prasad', Timezone='UTC', User_id='WERTY1234')
        testuser1.save()
        # Create a blog post
        test_tracker = Tracker.objects.create(
        user=testuser1, start_utc_time=datetime.now(), end_utc_time=datetime.now())
        test_tracker.save()

    def test_blog_content(self):
        activity = Tracker.objects.get(id=1)
        user = f'{activity.user}'
        start_utc_time = f'{activity.start_utc_time}'
        end_utc_time = f'{activity.end_utc_time}'
        self.assertEqual(user, 'testuser1')