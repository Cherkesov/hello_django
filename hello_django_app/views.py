from django.shortcuts import render
from hello_django_app.models import Recipe, Ingredient

# Create your views here.


def index(request):
    selected = list(map(int, request.GET.getlist('ingredient[]', [])))
    ingredients_list = Ingredient.objects.order_by('title')
    recipes_list = Recipe.objects.order_by('title') \
        # .filter(proportions__in=selected) \
        # .distinct()

    context = {
        'selected_ingredients': selected,
        'ingredients_list': ingredients_list,
        'recipes_list': recipes_list,
    }
    return render(request, 'index.html', context)
