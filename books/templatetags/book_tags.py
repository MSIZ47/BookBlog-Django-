# HOW TO CREATE AND USE TEMPLATE FILTERS?
# First we import template from django then we need variable called 'register' that is the templateLibrary instance
# then we create our custom template tag as a function under the '@register.filter' decorator.
# In order to use that as a template tag we should load this file called 'book_tags.py' in any template we want to use.

from django import template
register = template.Library()

@register.filter
def to_lowercase(value):
    return value.lower()
