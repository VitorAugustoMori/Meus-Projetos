from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views




class RecipeViewsTest(TestCase):
    def test_recipe_home_views_function_correct(self):
        view = resolve(reverse('recipe:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_views_function_correct(self):
        view = resolve(reverse('recipe:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_recipe_views_function_correct(self):
        view = resolve(reverse('recipe:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)