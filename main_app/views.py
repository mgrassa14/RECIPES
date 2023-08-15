from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

import uuid
import boto3
from .models import Recipe, Photo

from .forms import IngredientForm, DirectionForm


S3_BASE_URL = 'https://s3.us-west-1.amazonaws.com/'
BUCKET = 'recipeapp-8-14'

def add_photo(request, recipe_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = 'recipeApp' + uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to recipe_id or cat (if you have a cat object)
            Photo.objects.create(url=url, recipe_id=recipe_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', recipe_id=recipe_id)

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