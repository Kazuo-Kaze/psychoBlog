from django.shortcuts import get_object_or_404, render
from django.db.models import Q
import random 
# Create your views here.
from .models import Post, Category

def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'core/frontpage.html', { 'posts': posts})

# def collections(request):
#     categories = Category.objects.all()
#     return render(request, 'core/collections.html', { 'categories': categories})


def details(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug)
    similar_products = list(post.category.posts.exclude(id=post.id))

    if len(similar_products) >= 2:
        similar_products = random.sample(similar_products, 2)
    return render(request, 'core/detail.html', {'post': post, 'recents': similar_products})


def categorydetails(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'core/collectionCategory.html', {'category': category})


def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(Q(title__icontains=query) | Q(shortDis__icontains=query))

    return render(request, 'core/search.html', {'posts': posts, 'query': query})

def bio(request):
    return render(request, 'core/bio.html')

def contact(request):
    return render(request, 'core/contact.html')