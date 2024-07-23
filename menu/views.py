from django.shortcuts import render


def index(request):
    return render(request, 'menu/index.html')


def example_view(request, menu_name):
    context = {
        'menu_name': menu_name,
    }
    return render(request, 'main/draw_menu.html', context)
