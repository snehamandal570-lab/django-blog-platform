from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment

def home(request):
    query = request.GET.get('q')

    if query:
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = Post.objects.all()

    return render(request, 'home.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post)

    if request.method == "POST":
        name = request.POST.get("name")
        content = request.POST.get("content")

        Comment.objects.create(
            post=post,
            name=name,
            content=content
        )

        return redirect('post_detail', id=post.id)

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments
    })


@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        category = request.POST.get("category")

        Post.objects.create(
            title=title,
            content=content,
            category=category,
            author=request.user
        )

        return redirect("home")

    return render(request, "create_post.html")


@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if post.author != request.user:
        return redirect('home')

    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.category = request.POST.get("category")
        post.save()

        return redirect('post_detail', id=post.id)

    return render(request, 'edit_post.html', {'post': post})


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    if post.author == request.user:
        post.delete()

    return redirect('home')