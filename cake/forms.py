from django.shortcuts import get_object_or_404
from datetime import datetime
from django import forms
from .models import Cake, Ingredient, Component


class CreateCakeForm(forms.Form):
    title = forms.CharField(max_length=100)
    weight = forms.IntegerField()
    price = forms.IntegerField()

    def save(self):
        cake = Cake(**self.cleaned_data)
        cake.save()
        return cake


class EditCakeForm(forms.Form):
    title = forms.CharField(max_length=100)
    weight = forms.IntegerField()
    price = forms.IntegerField()

    def save(self):
        cake = get_object_or_404(Cake, pk=self.key)
        cake.title = self.cleaned_data['title']
        cake.weight = self.cleaned_data['weight']
        cake.price = self.cleaned_data['price']
        cake.date_modified = datetime.now()
        cake.save()
        return cake


class CreateIngredientForm(forms.Form):
    measurements = (
        (1, 'кг.'),
        (2, 'г.'),
        (3, 'шт.'),
        (4, 'л.')
    )
    title = forms.CharField(max_length=100)
    weight = forms.FloatField()
    measure = forms.ChoiceField(choices=measurements)
    unit_price = forms.IntegerField()

    def save(self):
        ingredient = Ingredient(**self.cleaned_data)
        ingredient.save()
        return ingredient


class EditIngredientForm(forms.Form):
    measurements = (
        (1, 'кг'),
        (2, 'г'),
        (3, 'шт'),
        (4, 'л')
    )
    title = forms.CharField(max_length=100)
    weight = forms.FloatField()
    measure = forms.ChoiceField(choices=measurements)
    unit_price = forms.IntegerField()

    def save(self):
        ingredient = get_object_or_404(Ingredient, pk=self.key)
        ingredient.title = self.cleaned_data['title']
        ingredient.weight = self.cleaned_data['weight']
        ingredient.measure = self.cleaned_data['measure']
        ingredient.unit_price = self.cleaned_data['unit_price']
        ingredient.date_modified = datetime.now()
        ingredient.save()
        return ingredient


class AddComponentForm(forms.Form):
    def get_ingredients():
        return ([(x.id, '{0}, {1}'.format(x.title, x.get_measure_display())) for x in Ingredient.objects.all()])[:]

    ingredient_id = forms.ChoiceField(choices=get_ingredients)
    amount = forms.FloatField()
    usage = (
        (1, 'на 1 шт'),
        (2, 'на 1 кг'),
    )
    usage = forms.ChoiceField(choices=usage)

    def save(self):
        component = Component(**self.cleaned_data)
        component.cake = get_object_or_404(Cake, pk=self._key)
        component.ingredient = get_object_or_404(Ingredient, pk=int(self.cleaned_data['ingredient_id']))
        component.save()
        return component


class EditComponentForm(AddComponentForm):
    def save(self):
        component = get_object_or_404(Component, pk=self._key)
        component.ingredient = get_object_or_404(Ingredient, pk=int(self.cleaned_data['ingredient_id']))
        component.amount = self.cleaned_data['amount']
        component.usage = self.cleaned_data['usage']
        component.date_modified = datetime.now()
        component.save()
        return component
