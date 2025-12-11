from django.shortcuts import render

def my_recipes(request):
    return render(request, 'recipes/my_recipes.html') 
