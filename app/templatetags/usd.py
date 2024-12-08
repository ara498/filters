from django import template

register=template.Library()
def swap(value):
    return value.swapcase()
register.filter('swapping',swap)    
@register .filter('sp')
def split(value,arg):
    return value.split()
#register.filter('splitting',split) 
@register.filter('index')
def index(value,i):
    return value.index(i)  