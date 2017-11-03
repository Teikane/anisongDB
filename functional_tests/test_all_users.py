# -*- coding: utf-8 -*-
from selenium import webdriver
from datetime import date
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils.translation import activate
from django.utils import formats

class HomeNewVisitorTest(StaticLiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		activate('en')

	def tearDown(self):
		self.browser.quit()

	def get_full_url(self, namespace):
		return self.live_server_url + reverse(namespace)

	def test_home_title(self):
		self.browser.get(self.get_full_url("home"))
		self.assertIn("AnisongDB", self.browser.title)

	def test_home_view_status_code(self):
		url = reverse("home")
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)

	def test_h1_css(self):
		self.browser.get(self.get_full_url("home"))
		h1 = self.browser.find_element_by_tag_name("h1")
		self.assertEqual(h1.value_of_css_property("color"),
						"rgb(200, 50, 255)")

	def test_home_files(self):
		self.browser.get(self.live_server_url + "/robots.txt")
		self.assertNotIn("Not Found", self.browser.title)
		self.browser.get(self.live_server_url + "/humans.txt")
		self.assertNotIn("Not Found", self.browser.title)

	def test_internationalization(self):
		for lang, h1_text in [('en', 'Welcome'), ('jp', 'Yoroshiku'),]:

			activate(lang)
			self.browser.get(self.get_full_url("home"))
			h1 = self.browser.find_element_by_tag_name("h1")
			self.assertEqual(h1.text, h1_text)

	def test_localization(self):
		today = date.today()
		for lang in ['en','jp']:
			activate(lang)
			self.browser.get(self.get_full_url("home"))
			local_date = self.browser.find_element_by_id("local-date")
			non_local_date = self.browser.find_element_by_id("non-local-date")
			self.assertEqual(formats.date_format(today, use_l10n=True), local_date.text)
			self.assertEqual(today.strftime('%Y-%m-%d'), non_local_date.text)

	def test_time_zone(self):
		self.browser.get(self.get_full_url("home"))
		tz = self.browser.find_element_by_id("time-tz").text
		utc = self.browser.find_element_by_id("time-utc").text
		ty = self.browser.find_element_by_id("time-ty").text
		self.assertNotEqual(tz, utc)
		self.assertNotIn(ty, [tz, utc])
