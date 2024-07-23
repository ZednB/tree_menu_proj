from django import template

from menu.models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('main/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu = Menu.objects.get(name=menu_name)
    items = MenuItem.objects.filter(menu=menu).select_related('parent')

    active_item = None
    for item in items:
        if request.path == item.get_url():
            active_item = item
            break

    def build_menu_tree(parent, active_item):
        tree = []
        for item in items:
            if item.parent == parent:
                children = build_menu_tree(item, active_item)
                tree.append({
                    'item': item,
                    'children': children,
                    'is_active': item == active_item,
                    'is_open': item == active_item or any(child['is_active'] for child in children),
                })
        return tree

    menu_tree = build_menu_tree(None, active_item)
    return {'menu': menu_tree}
