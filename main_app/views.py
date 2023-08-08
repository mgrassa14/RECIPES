from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe
from .forms import IngredientsForm

# Create your views here.

def add_ingredients(request, recipe_id):
    form = IngredientsForm(request.POST)
    if form.is_valid():
        new_ingredient = form.save(commit=False)
        new_ingredient.recipe_id = recipe_id
        new_ingredient.save()
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
    ingredients_form = IngredientsForm()
    return render(request, 'recipes/detail.html', { 'recipe': recipe, 'ingredients_form': IngredientsForm })

def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')