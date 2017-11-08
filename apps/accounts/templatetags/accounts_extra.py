import re

from django import template
from django.core.urlresolvers import reverse, NoReverseMatch
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
	group = Group.objects.get(name=group_name)
	return group in user.groups.all()

@register.simple_tag(takes_context=True)
def active_url(context, url):
	try:
		pattern = "^" + reverse(url)
	except:
		pattern = url
	path = context["request"].path
	if re.search(pattern, path):
		return ("active")
	else:
		return ("")