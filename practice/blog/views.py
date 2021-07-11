from django.shortcuts import redirect, render, get_object_or_404
from .models import Blog, Comment, Hashtag
from .forms import BlogForm, CommentForm, HashtagForm
# Create your views here.

def main(request):
    blogs = Blog.objects
    return render(request, 'blog/main.html', {'blogs': blogs})

def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:main')
    else:
        form = BlogForm()
        return render(request, 'blog/create.html', {'form' : form})

def read(request, blog_pk):
    blog = get_object_or_404(Blog, id = blog_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = blog
            form.save()
            return redirect('blog:read', blog.pk)
    else:
        form = CommentForm()
        return render(request, 'blog/read.html', {'blog': blog, 'form': form})

def update(request, blog_pk):
    blog = get_object_or_404(Blog, id = blog_pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance = blog)
        if form.is_valid():
            form.save()
            return redirect('blog:read', blog_pk)
    else:
        form = BlogForm(instance = blog)
        return render(request, 'blog/update.html', {'form' : form, 'blog_pk' : blog_pk})

def delete(request, blog_pk):
    blog = get_object_or_404(Blog, id = blog_pk)
    blog.delete()
    return redirect('blog:main')

def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, id = comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blog:read', comment.post_id.id)
    else:
        form = CommentForm(instance=comment)
        return render(request, 'blog/comment_update.html', {'form' : form, 'comment_id' : comment_id})

def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id = comment_id)
    comment.delete()
    return redirect('blog:main')

def hashtag_create(request):
    if request.method == 'POST':
        form = HashtagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:main')
    else:
        form = HashtagForm
        return render(request, 'blog/hashtag_create.html', {'form' : form})