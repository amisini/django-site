from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm

def index(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    context = {
        'posts': posts,
    }
    return render(request, 'blog_index.html', context)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                content=form.cleaned_data['content'],
                post=post,
            )
            comment.save()

    context = {'post': post, 'comments': comments, 'form': form}

    return render(request, 'post_detail.html', context)