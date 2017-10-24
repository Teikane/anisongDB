# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils.translation import activate

class TestGoogleLogin(StaticLiveServerTestCase):

	fixtures = ["allauth_fixture"]

	# Use Firefox and wait for browser to open.
	# Inputs:	None
	# Outputs:	None
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		self.browser.wait = WebDriverWait(self.browser, 10)
		activate('en')

	# Deconstruct and terminate webdriver.
	# Inputs:	None
	# Outputs:	None
	def tearDown(self):
		self.browser.quit()

	# Webdriver will wait until it can locate an element.
	# Inputs:	An element's ID
	# Outputs: 	An element
	def get_element_by_id(self, element_id):
		return self.browser.wait.until(EC.presence_of_element_located(
			(By.ID, element_id)))

	# Webdriver will wait until ic can locate a button.
	# Inputs:	An element's ID
	# Outputs:	An element
	def get_button_by_id(self, element_id):
		return self.browser.wait.until(EC.element_to_be_clickable(By.ID, element_id))

	# Webdriver to retrieve full url and its reverse.
	# Inputs: namespace
	# Outputs: full url, reverse name
	def get_full_url(self, namespace):
		return self.live_server_url + reverse(namespace)

	def user_login(self):
		import json
		with open("anisongdb/fixtures/google_user.json") as f:
			credentials = json.loads(f.read())
		self.get_element_by_id("Email").send_keys(credentials["Email"])
		self.get_button_by_id("next").click()
		self.get_element_by_id("Passwd").send_keys(credentials["Passwd"])
		for btn in ["signIn", "submit_approve_access"]:
			self.get_button_by_id(btn).click()

	# Main module to test if elements exists for login/logout and useability.
	# Inputs: None
	# Outputs: None
	def test_google_login(self):
		self.browser.get(self.get_full_url("home"))
		google_login = self.get_element_by_id("google_login")
		with self.assertRaises(TimeoutException):
			self.get_element_by_id("logout")
		self.assertEqual(
			google_login.get_attribute("href"),
			self.live_server_url + "/accounts/google/login")
		google_login.click()
		with self.assertRaises(TimeoutException):
			self.get_element_by_id("google_login")
		google_logout = self.get_element_by_id("logout")
		google.logout.click()
		google_login = self.get_element_by_id("google_login")
