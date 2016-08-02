from django import template

register = template.Library()

@register.filter(name='pf')
def price_format(value):
    return  ('$ ' + '{0:,}'.format(int(value)).__str__()).replace(',', '.') + ' pesos'