from django.urls import path
from cake.views import *

urlpatterns = [
    path('', index, name='index'),
    path('create', create, name='create'),
    path('<int:cake_id>/edit', edit, name='edit'),
    path('<int:cake_id>/recipe', recipe, name='recipe'),
    path('<int:cake_id>/delete', delete, name='delete'),
    path('<int:cake_id>/component_add', component_add, name='component_add'),
    path('<int:component_id>/component_edit', component_edit, name='component_edit'),
    path('<int:component_id>/component_delete', component_delete, name='component_delete'),
    path('ingredients_index', ingredients_index, name='ingredients_index'),
    path('ingredient_create', ingredient_create, name='ingredient_create'),
    path('<int:ingredient_id>/ingredient_edit', ingredient_edit, name='ingredient_edit'),
    path('<int:ingredient_id>/ingredient_delete', ingredient_delete, name='ingredient_delete'),
    path('cake_forms_index', cake_forms_index, name='cake_forms_index'),
    path('cake_form_add', cake_form_add, name='cake_form_add'),
    path('<int:cake_form_id>/cake_form_edit', cake_form_edit, name='cake_form_edit'),
    path('<int:cake_form_id>/cake_form_delete', cake_form_delete, name='cake_form_delete'),
]
