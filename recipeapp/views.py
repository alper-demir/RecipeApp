from django.shortcuts import render
from recipeapp.models import Post
from recipeapp.models import maincoursedb
from recipeapp.models import sweetdb
from recipeapp.models import vegetabledb

def index(request):
    context = {
        "post": Post.objects.all()
    }
    return render(request, 'index.html', context)

def sweet(request):
    context = {
        "sweet": sweetdb.objects.all()
    }
    return render(request, 'sweet.html', context)

def vegetable(request):
    context = {
        "vegetable": vegetabledb.objects.all()
    }
    return render(request, 'vegetable.html', context)

def maincourse(request):
    context = {
        "maincourse": maincoursedb.objects.all()
    }
    return render(request, 'maincourse.html', context)

def maincourse_detail(request, id):

    post = maincoursedb.objects.get(id=id)


    return render(request, 'partials/maincourse/maincourse-detail.html', {
        "post": post
    })

def sweet_detail(request, id):

    post = sweetdb.objects.get(id=id)


    return render(request, 'partials/sweet/sweet-detail.html', {
        "post": post
    })

def vegetable_detail(request, id):

    post = vegetabledb.objects.get(id=id)


    return render(request, 'partials/vegetable/vegetable-detail.html', {
        "post": post
    })
