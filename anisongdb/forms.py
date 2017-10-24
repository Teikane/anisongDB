from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

GENDER_CHOICES = (
	(1, ("Decline to state")),
	(2, ("Male")),
	(3, ("Female")),
	(4, ("Other"))
)

class SignUpForm(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text="Required for validation")
	dob = forms.DateField(required=False, help_text="Formats: 2017-10-24, 10/24/2017, and 10/24/17")
	gender = forms.ChoiceField(choices=GENDER_CHOICES, label="Gender", initial="", widget=forms.Select(), required=False)

	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)

		for fieldname in ["password1", "password2"]:
			self.fields[fieldname].help_text = None