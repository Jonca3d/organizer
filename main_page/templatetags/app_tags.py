from django import template



register = template.Library()


@register.inclusion_tag('include/nav.html')
def show_main_menu():
  return

@register.inclusion_tag('include/notification_area.html')
def show_notification_area():
  return

@register.inclusion_tag('include/other_information_area.html')
def show_other_information_area():
  return
