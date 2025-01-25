from django.shortcuts import render
from .models import Blog, BlogImage, Category, Comment
from django.shortcuts import get_object_or_404
# Create your views here.

def blog_page(request):
    bloglar = Blog.objects.all()
    kategoriyalar = Category.objects.all()

    context = {
        'bloglar': bloglar,
        'kategoriyalar': kategoriyalar
    }
    return render(request, template_name='index.html', context=context)


def about_page(request):
    return render(request, template_name='about.html')


def contact_page(request):
    return render(request, template_name='contact.html')


def blog_detail_page(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comment = Comment.objects.filter(blog_id=blog_id)
    kategoriyalar = Category.objects.all()

    if request.method == "post":
        pass
    # birinchi_rasm = 
    # ikkinchi_rasm = 
    context = {
        "blog": blog,
        'kategoriyalar': kategoriyalar,
        'komment': comment

    }
    return render(request, template_name='post.html', context=context)