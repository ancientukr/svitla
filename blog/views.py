from django.shortcuts import render
from blog.models import Post

context_dict = {}
post_list = {}
def blog(request):
    posts_list = Post.objects.filter()
    context_dict['posts'] = posts_list
    return render(request, 'blog/blog.html', context_dict)

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    post_list['post'] = post
    return render(request, 'blog/post.html', post_list)

