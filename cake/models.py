from django.db import models
from math import ceil


class CakeForm(models.Model):
    title = models.CharField(max_length=100)
    weight = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    version = models.IntegerField(default=1)


class Ingredient(models.Model):
    measurements = (
        (1, 'кг'),
        (2, 'г'),
        (3, 'шт'),
        (4, 'л')
    )
    title = models.CharField(max_length=100)
    weight = models.FloatField()
    measure = models.PositiveIntegerField(choices=measurements, default=1)
    unit_price = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    version = models.PositiveIntegerField(default=1)


class Cake(models.Model):
    title = models.CharField(max_length=100)
    weight = models.PositiveIntegerField()
    price = models.PositiveIntegerField(default=0)

    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    version = models.PositiveIntegerField(default=1)

    def get_cost_price(self):
        cost_price = 0
        for component in self.component_set.all():
            cost_price = cost_price + component.get_cost_price()
        return ceil(cost_price)


class Component(models.Model):
    usage = (
        (1, 'шт'),
        (2, 'кг'),
    )
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    usage = models.IntegerField(choices=usage, default=2)
    amount = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    version = models.PositiveIntegerField(default=1)

    def get_total_amount(self):
        if self.usage == 1:
            total_amount = self.amount
        else:
            total_amount = self.amount * self.cake.weight / 1000
        if self.ingredient.measure == 3:
            total_amount = int(ceil(total_amount))
        return total_amount

    def get_cost_price(self):
        return ceil(self.get_total_amount() * self.ingredient.unit_price / self.ingredient.weight)
