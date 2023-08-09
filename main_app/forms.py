from django.forms import ModelForm
from .models import Ingredient, Direction

class IngredientForm(ModelForm):
  class Meta:
    model = Ingredient
    fields = ['quantity', 'measurement', 'name']
    
class DirectionForm(ModelForm):
  class Meta:
    model = Direction
    fields = ['step']