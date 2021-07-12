from django.shortcuts import render
from .models import Post



def home(request):
    context = {
        'posts':Post.objects.all()
    }
    """The created dictionary context passed as third argument to the render function,
    by doing it will pass our data into our template. """
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})