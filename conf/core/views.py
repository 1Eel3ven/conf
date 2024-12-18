from django.shortcuts import render
from django.views import generic
from .models import Post, Category


def IndexView(request):
    categories = Category.objects.all()
    posts = Post.objects.order_by('-pub_date')

    context = {
        'categories_list': categories, 
        'post_list': posts, 
    }

    return render(request, 'core/index.html', context)


class DetailView(generic.DetailView):
    model = Post
    template_name = 'core/detail.html'


def CategoryView(request, pk):
    categories = Category.objects.all()
    category = categories.get(pk=pk)

    posts = Post.objects.filter(categories__in=[category])

    context = {
        'categories_list': categories, 
        'category': category, 
        'post_list': posts, 
    }

    return render(request, 'core/index.html', context)


def AboutView(request):
    return render(request, 'core/about.html')
