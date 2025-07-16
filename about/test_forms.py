from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields with valid data """
        form = CollaborateForm({
            'name': 'tom',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_form_is_invalid_empty_name(self):
        """ Test form is invalid when name field is empty """
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(),
                         msg="Form should not be valid"
                         "when name field is empty")

    def test_form_is_invalid_empty_email(self):
        """ Test form is invalid when email field is empty """
        form = CollaborateForm({
            'name': 'tom',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(),
                         msg="Form should not be valid"
                         "when email field is empty")

    def test_form_is_invalid_empty_message(self):
        """ Test form is invalid when message field is empty """
        form = CollaborateForm({
            'name': 'tom',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(),
                         msg="Form should not be valid"
                         "when message field is empty")
