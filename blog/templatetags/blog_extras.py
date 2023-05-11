from django import template
from django.utils.html import format_html

register = template.Library()

@register.filter
def author_details(user, current_user):

  if not user:
    return ''

  if user == current_user:
    return format_html("<strong>me</strong>")
  if user.first_name and user.last_name:
    name = f'{user.first_name} {user.last_name}'
  else:
    name = f'{user.username}'
  if user.email:
    prefix = format_html('<a href="mailto:{}">', user.email)
    suffix = format_html("</a>")
  else:
    prefix = ""
    suffix = ""

  return format_html('{}{}{}', prefix, name, suffix)
