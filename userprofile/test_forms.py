# Automated tests were never run as intended. 
from django.test import TestCase, override_settings
from django.test.utils import override_settings
from .forms import CustomSignupForm


@override_settings(DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
})
class TestCustomSignupForm(TestCase):
    
    def test_custom_signup_form(self):
        form_data = {
            'username': 'automatedtestuser',
            'password1': 'complex_password',
            'password2': 'complex_password',
            'biography': 'Just a test biography',
            'cycling_skills': 'Intermediate',
            'preferred_ride_type': 'Mountain',
            'maintenance_skills': 'Basic'
        }
        form = CustomSignupForm(data=form_data)
        self.assertTrue(form.is_valid())

        user = form.save()
        self.assertIsNotNone(user.id)
