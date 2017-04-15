from django.shortcuts import render
from blog.models import Post

context_dict = {}

def blog(request):
    posts_list = Post.objects.filter()
    context_dict['posts'] = posts_list
    return render(request, 'blog/blog.html', context_dict)

def post(request):
    #post = Post.objects.get(id=id_post)
    return render(request, 'blog/post.html')

