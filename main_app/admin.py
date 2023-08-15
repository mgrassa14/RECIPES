from django.contrib import admin
from .models import Recipe, Ingredient, Direction, Photo

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Direction)
admin.site.register(Photo)