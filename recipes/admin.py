from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django import forms
from .models import Category, Recipe

class CategoryAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin) #registra a categoria no admin

class RecipeAdmin(admin.ModelAdmin):
    ...

admin.site.register(Recipe, RecipeAdmin) #registra a receita no admin




















class CustomUserChangeForm(forms.ModelForm): #formulario customizado para alterar usuario
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            # Usa HiddenInput para não mostrar a senha
            'password': forms.HiddenInput(),
        }

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm

# Substitui o UserAdmin padrão pelo customizado
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)





# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
# from django import forms
#
# class CustomUserChangeForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'
#         widgets = {
#             'password': forms.TextInput(attrs={'readonly': 'readonly'}),
#         }
#
# class CustomUserAdmin(UserAdmin):
#     form = CustomUserChangeForm
#
# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)