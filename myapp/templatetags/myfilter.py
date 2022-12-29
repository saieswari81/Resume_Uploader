from django import template
register = template.Library()


@register.filter(name='remove_special')
def remove_chars(value, args):
    # print('value: ', value)  # only for debugging purpose
    # print('args: ', args)

    for character in args:
        # print('character: ', character)
        value = value.replace(character, "")
    return value
