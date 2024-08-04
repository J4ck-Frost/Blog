from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from django.contrib import messages
from django.core.paginator import Paginator
from datetime import datetime

# Create your views here.

def index(request): 
    limit = 3
    page = request.GET.get('page', 1)
    keyword = request.GET.get('keyword','')
    sort = request.GET.get('sort','-created_At')
    if keyword:
        posts = Post.objects.filter(title__contains=keyword).order_by(sort)  # Order by created_At or any other field
    else:
        posts = Post.objects.all().order_by(sort)  # Order by created_At or any other field
    #paging
    post_paginator = Paginator(posts, limit)
    post_paginator = post_paginator.get_page(page)
    
    return render(request, 'index.html', {'posts': post_paginator, 'keyword': keyword, 'len_posts': len(posts)})

def post(request, pk):
    post =Post.objects.get(id=pk)
    return render(request, 'post.html',{'post':post})

def newPost(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        if title and body:
            post = Post.objects.create(title = title, body = body, created_At=datetime.now() )
            post.save()
            return redirect('/')
        else:
            messages.info(request, 'Title and Body cannot be empty.')
    return render(request, 'newPost.html')

def editPost(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        if title and body:
            post.title = title
            post.body = body
            post.save()
            return redirect('post', pk=pk)
        else:
            error_message = 'Title and Body cannot be empty.'
            return render(request, 'post.html', {'post': post, 'error_message': error_message, 'editing': True})
    return render(request, 'post.html', {'post': post})

    
def delete(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
    return redirect('/')

def error(request, exception=None):
    return render(request, 'error.html')