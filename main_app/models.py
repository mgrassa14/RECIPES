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

class Photo(models.Model):
    url = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for recipe_id: {self.recipe_id} @{self.url}"    

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