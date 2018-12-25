from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from .forms import CreateCakeForm, EditCakeForm, \
                CreateIngredientForm, EditIngredientForm,\
                AddComponentForm, EditComponentForm, \
                CreateCakeFormForm, EditCakeFormForm
from .models import Cake, Ingredient, Component, CakeForm


def index(request):
    cakes = Cake.objects.order_by('-date_modified')
    return render(request, 'cake/index.html', {'cakes': cakes})


def create(request):
    if request.method == 'POST':
        form = CreateCakeForm(request.POST)
        if form.is_valid():
            cake = form.save()
            return HttpResponseRedirect(reverse('recipe', kwargs={'cake_id': cake.id}))
    else:
        form = CreateCakeForm()
    return render(request, 'cake/create.html', {'form': form})


def edit(request, cake_id):
    if request.method == 'POST':
        form = EditCakeForm(request.POST)
        if form.is_valid():
            form.key = cake_id
            form.save()
            return HttpResponseRedirect(reverse('recipe', kwargs={'cake_id': cake_id}))
    else:
        cake = get_object_or_404(Cake, pk=cake_id)
        form = EditCakeForm({'title': cake.title, 'weight': cake.weight,
                             'price': cake.price, 'key': cake_id})
        return render(request, 'cake/edit.html', {'form': form})


def recipe(request, cake_id):
    cake = get_object_or_404(Cake, pk=cake_id)
    return render(request, 'cake/recipe.html', {'cake': cake})


def delete(request, cake_id):
    cake = get_object_or_404(Cake, pk=cake_id)
    cake.delete()
    return HttpResponseRedirect(reverse('index'))


def ingredients_index(request):
    i = Ingredient.objects.order_by('title')
    return render(request, 'cake/ingredients.html', {'ingredients': i})


def ingredient_create(request):
    if request.method == 'POST':
        form = CreateIngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ingredients_index'))
    else:
        form = CreateIngredientForm()
    return render(request, 'cake/ingredient_create.html', {'form': form})


def ingredient_edit(request, ingredient_id):
    if request.method == 'POST':
        form = EditIngredientForm(request.POST)
        if form.is_valid():
            form.key = ingredient_id
            form.save()
            return HttpResponseRedirect(reverse('ingredients_index'))
    else:
        ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
        form = EditIngredientForm({'title': ingredient.title, 'weight': ingredient.weight,
                                   'measure': ingredient.measure, 'unit_price': ingredient.unit_price,
                                   'key': ingredient_id})
        return render(request, 'cake/ingredient_edit.html', {'form': form})


def ingredient_delete(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
    ingredient.delete()
    return HttpResponseRedirect(reverse('ingredients_index'))


def component_add(request, cake_id):
    if request.method == 'POST':
        form = AddComponentForm(request.POST)
        if form.is_valid():
            form._key = cake_id
            form.save()
            return HttpResponseRedirect(reverse('recipe', kwargs={'cake_id': cake_id}))
    else:
        form = AddComponentForm()
    return render(request, 'cake/component_add.html', {'form': form})


def component_edit(request, component_id):
    if request.method == 'POST':
        form = EditComponentForm(request.POST)
        if form.is_valid():
            form._key = component_id
            component = form.save()
            return HttpResponseRedirect(reverse('recipe', kwargs={'cake_id': component.cake.id}))
    else:
        component = get_object_or_404(Component, pk=component_id)
        form = EditComponentForm({'ingredient_id': component.ingredient.id, 'amount': component.amount,
                                  'usage': component.usage})
    return render(request, 'cake/component_edit.html', {'form': form})


def component_delete(request, component_id):
    component = get_object_or_404(Component, pk=component_id)
    cake_id = component.cake.id
    component.delete()
    return HttpResponseRedirect(reverse('recipe', kwargs={'cake_id': cake_id}))


def cake_forms_index(request):
    cake_forms = CakeForm.objects.order_by('-date_modified')
    return render(request, 'cake/cake_forms_index.html', {'cake_forms': cake_forms})


def cake_form_add(request):
    if request.method == 'POST':
        form = CreateCakeFormForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cake_forms_index'))
    else:
        form = CreateCakeFormForm()
    return render(request, 'cake/cake_form_add.html', {'form': form})


def cake_form_edit(request, cake_form_id):
    if request.method == 'POST':
        form = EditCakeFormForm(request.POST)
        if form.is_valid():
            form._key = cake_form_id
            form.save()
            return HttpResponseRedirect(reverse('cake_forms_index'))
    else:
        cake_form = get_object_or_404(CakeForm, pk=cake_form_id)
        form = EditCakeFormForm({'title': cake_form.title, 'weight': cake_form.weight,
                                   'key': cake_form.id})
        return render(request, 'cake/cake_form_edit.html', {'form': form})

def cake_form_delete(request, cake_form_id):
    cake_form = get_object_or_404(CakeForm, pk=cake_form_id)
    cake_form.delete()
    return HttpResponseRedirect(reverse('cake_forms_index'))
