from django.db import models
from django.urls import reverse

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    culture = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    # needed to put get_absolute_url within the Recipe model or else update will not work
    def get_absolute_url(self):
        return reverse('detail', kwargs={'recipe_id': self.id})
    
    def __str__(self):
        return self.title
    
# MEASUREMENTS = (
#         ('cup', 'Cup'),
#         ('fl oz', 'Fluid Ounce'),
#         ('gal', 'Gallon'),
#         ('mL', 'Milliliter'),
#         ('L', 'Liter'),
#         ('pt', 'Pint'),
#         ('qt', 'Quart'),
#         ('tbsp', 'Tablespoon'),
#         ('tsp', 'Teaspoon'),
#         ('gal', 'Gallon'),
# )

class Ingredient(models.Model):
    name = models.CharField(max_length=100, default='')
    quantity = models.PositiveIntegerField(default=0)
    measurement = models.CharField(max_length=100, default='')
    
    # recipe_id FK
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Direction(models.Model):
    step = models.TextField('step', max_length=250, default='')
    
    # recipe_id FK
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return self.step