from django import template



register = template.Library()


@register.inclusion_tag('include/nav.html')
def show_main_menu():
  return

