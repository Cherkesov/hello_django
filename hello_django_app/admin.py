from django.contrib import admin
from .models import Recipe
from .models import Ingredient
from .models import Measure
from .models import Proportion

# Register your models here.

class ProportionAdminInline(admin.TabularInline):
    model = Proportion
    pass


class RecipeAdmin(admin.ModelAdmin):
    inlines = (ProportionAdminInline,)
    pass


admin.site.register(Recipe, RecipeAdmin)

admin.site.register(Ingredient)
admin.site.register(Measure)
admin.site.register(Proportion)
