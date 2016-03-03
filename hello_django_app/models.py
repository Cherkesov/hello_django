from django.db import models

# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    # proportions = models.

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    pass


class Ingredient(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    pass


class Measure(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    pass


class Proportion(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    measure = models.ForeignKey(Measure)
    value = models.PositiveIntegerField()
    recipe = models.ForeignKey(Recipe)
    pass
