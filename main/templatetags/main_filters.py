from django import template

register = template.Library()


@register.filter
def addclass(field, class_names):
    return field.as_widget(attrs={'class': class_names})
