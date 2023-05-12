from django import template
from django.utils.html import format_html
from blog.models import Post

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


@register.simple_tag
def row(extra_classes=""):
  return format_html('<div class="row {}">', extra_classes)


@register.simple_tag
def endrow():
  return format_html("</div>")

@register.simple_tag
def col(extra_classes=""):
  return format_html('<div class="col {}">', extra_classes)


@register.simple_tag
def endcol():
  return format_html("</div>")

@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
  print(post.pk)
  posts = Post.objects.exclude(pk=post.pk)[:5]
  return {"title": "Recent Posts", "posts": posts}
