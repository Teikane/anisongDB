# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils.translation import activate

class TestHomePage(TestCase):

	# Test index page template
	# Inputs:	None
	# Outputs:	None
	def test_uses_index_template(self):
		activate('en')
		response = self.client.get(reverse("home"))
		self.assertTemplateUsed(response, "anisongdb/index.html")

	# Test base page template
	# Inputs:	None
	# Outputs:	None
	def test_uses_base_template(self):
		activate('en')
		response = self.client.get(reverse("home"))
		self.assertTemplateUsed(response, "base.html")

