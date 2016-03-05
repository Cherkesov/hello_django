from django.db import models

# Create your models here.


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


class Recipe(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    image = models.ImageField(upload_to='recipe', null=True, blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    pass


class Proportion(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    measure = models.ForeignKey(Measure)
    value = models.PositiveIntegerField()
    recipe = models.ForeignKey(to=Recipe, related_name="proportions", null=False)

    def __str__(self):
        return '%d %s of %s' % (self.value, self.measure, self.ingredient)

    pass
