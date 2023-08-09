from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe
from .forms import IngredientForm, DirectionForm

# Create your views here.

def add_ingredient(request, recipe_id):
    form = IngredientForm(request.POST)
    if form.is_valid():
        new_ingredient = form.save(commit=False)
        new_ingredient.recipe_id = recipe_id
        new_ingredient.save()
    return redirect('detail', recipe_id=recipe_id)

def add_direction(request, recipe_id):
    form = DirectionForm(request.POST)
    if form.is_valid():
        new_direction = form.save(commit=False)
        new_direction.recipe_id = recipe_id
        new_direction.save()
    return redirect('detail', recipe_id=recipe_id)

class RecipeCreate(CreateView):
  model = Recipe
  fields = ['title', 'culture', 'description']
  success_url = '/recipes/'
  
class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['culture', 'description']
    
class RecipeDelete(DeleteView):
    model = Recipe
    success_url = '/recipes/'

def recipes_index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', { 'recipes': recipes })

def recipes_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingredient_form = IngredientForm()
    direction_form = DirectionForm()
    return render(request, 'recipes/detail.html', { 'recipe': recipe, 'ingredient_form': IngredientForm, 'direction_form': DirectionForm })

def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')