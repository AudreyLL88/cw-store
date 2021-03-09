from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BlogForm, CommentForm
from .models import BlogPost, BlogComment

# Create your views here.


def blog(request):
    """ A view to return the index page """

    blogposts = BlogPost.objects.all()

    context = {
        'blogposts': blogposts,
    }

    return render(request, 'blog/blog.html', context)


@login_required
def add_blogpost(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blogpost = form.save()
            messages.success(request, 'Successfully added blog post!')
            return redirect(reverse('blog_detail', args=[blogpost.id]))
        else:
            messages.error(request, 'Failed to add blog post. Please ensure the form is valid.')
    else:
        form = BlogForm()
    template = 'blog/add_blogpost.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def blog_detail(request, blogpost_id):
    """ A view to show individual blog details """

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)

    context = {
        'blogpost': blogpost,
    }

    return render(request, 'blog/blog_detail.html', context)


@login_required
def edit_blogpost(request, blogpost_id):
    """ Edit a blog post """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blogpost)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog post!')
            return redirect(reverse('blog_detail', args=[blogpost.id]))
        else:
            messages.error(request, 'Failed to update the blog post. Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blogpost)
        messages.info(request, f'You are editing {blogpost.blog_title}')

    template = 'blog/edit_blogpost.html'
    context = {
        'form': form,
        'blogpost': blogpost,
    }

    return render(request, template, context)


@login_required
def delete_blogpost(request, blogpost_id):
    """ Delete Blog post forever"""

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)

    if request.user == blogpost.author:
        blogpost.delete()
        return redirect(reverse('blog'))
    else:
        messages.error(request, 'You cannot do that !')
        return redirect(reverse('blog'))


@login_required
def blog_comment(request, blogpost_id):
    """ Allows user to add a comment """

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_user = request.user
            comment.blogpost = blogpost
            comment.save()
            messages.success(request, 'Thank you for your comment !')
            return redirect(reverse('blog_detail', args=[blogpost.id]))
        else:
            messages.error(request,
                           'Oops something went wrong. \
                            Please try again.')
    else:
        form = CommentForm(instance=blogpost)
    template = 'blog/add_comment.html'
    context = {
        'form': form,
        'blogpost': blogpost,
    }

    return render(request, template, context)


@login_required
def delete_comment(request, comment_id):
    """ Delete comment forever"""

    comment = get_object_or_404(BlogComment, pk=comment_id)

    if request.user == comment.comment_user:
        comment.delete()
        messages.success(request, 'Your comment is deleted !')
        return redirect(reverse('blog'))
    else:
        messages.error(request, 'You cannot do that !')
        return redirect(reverse('blog'))
