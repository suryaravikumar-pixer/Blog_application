from django.shortcuts import render

posts = [
    {
        'author':'AynRand',
        'title':'Fountainhead',
        'content':'The Fountainhead tells the story of the desperate battle waged by architect Howard Roark.',
        'date_posted':'July 10, 2021',
    },
    {
        'author':'Howard',
        'title':'Atlas',
        'content':'Second post content ',
        'date_posted':'July 10, 2021',
    }
]

def home(request):
    context = {
        'posts':posts
    }
    """The created dictionary context passed as third argument to the render function,
    by doing it will pass our data into our template. """
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})