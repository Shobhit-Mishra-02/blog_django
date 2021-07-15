from django import template
import markdown

register = template.Library()

@register.filter()
def markdown_convertor(value):
    value = markdown.markdown(value)
    return value