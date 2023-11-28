from django import template

register = template.Library()

"""
Calculation for summing up price by taking
price of each product and multiplying
by quantity added to bag
"""


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
