from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Recipe:  # Note that parens are optional if not inheriting from another class
  def __init__(self, title, culture, description):
    self.title = title
    self.culture = culture
    self.description = description

recipes = [
    Recipe('Pesto Pasta', 'italian', 'it is very good'),
    Recipe('Bolognese Pasta', 'italiano', 'it is good'),
    Recipe('Cabonara Pasta', 'italiana', 'it is the best')
]

def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# def recipes_index(request):
#     recipes = Recipe.objects.all()
#     return render(request, 'recipes/index.html', { 'recipes': recipes })
def recipes_index(request):
    return render(request, 'recipes/index.html', { 'recipes': recipes })