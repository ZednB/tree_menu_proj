from django import template

from menu.models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    try:
        menu = Menu.objects.get(name=menu_name)
        menu_items = MenuItem.objects.filter(menu=menu).select_related('parent').order_by('parent_id', 'id')

        menu_tree = []
        menu_dict = {}

        # Сначала создаем все узлы
        for item in menu_items:
            node = {
                'item': item,
                'children': [],
                'is_active': request.path == item.get_url(),
                'is_open': request.path.startswith(item.get_url()),
            }
            menu_dict[item.id] = node

        # Теперь связываем родительские и дочерние элементы
        for item in menu_items:
            node = menu_dict[item.id]
            if item.parent_id:
                parent_node = menu_dict.get(item.parent_id)
                if parent_node:
                    parent_node['children'].append(node)
            else:
                menu_tree.append(node)

        return {
            'menu': menu_tree,
        }
    except Menu.DoesNotExist:
        return {
            'menu': None,
        }
