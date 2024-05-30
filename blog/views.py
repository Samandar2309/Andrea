from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import ContactForm


def home(request):
    posts = Post.objects.all().order_by('-id')[:5]
    categories = Category.objects.annotate(post_count=Count('posts'))
    archives = Archives.objects.all()
    posts1 = SubPost.objects.all()
    tags = Tag.objects.all()
    contex = {
        'posts': posts,
        'categories': categories,
        'archives': archives,
        'posts1': posts1,
        'tags': tags
    }
    return render(request, 'index.html', contex)


def fashion(request):
    posts = Post.objects.all().order_by('-id')
    tags = Tag.objects.all()
    contex = {
        'posts': posts,
        'tags': tags
    }
    return render(request, 'fashion.html', contex)


def travel(request):
    travels = Travel.objects.all()
    tags = Tag.objects.all()
    category = Category.objects.all()
    archives = Archives.objects.all()
    post1 = SubPost.objects.all()
    contex = {
        'travels': travels,
        'tags': tags,
        'category': category,
        'archives': archives,
        'post1': post1
    }
    return render(request, 'travel.html', contex)


def about(request):
    about1 = About.objects.all()
    contex = {
        'about': about1
    }
    return render(request, 'about.html', contex)


def contact1_view(request, pk):
    contact1 = Contact1.objects.all()
    form = ContactForm()
    comments = Contact.objects.filter(post__id=pk).order_by('-id')
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/blog/{post.id}')
    contex = {
        'contact1': contact1,
        'form': form,
        'comments': comments
    }
    return render(request, 'contact.html', contex)
