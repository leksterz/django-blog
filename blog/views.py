from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Blaze ENT',
        'title': 'Blog Post #1',
        'content': 'First post Content babu',
        'date_posted': 'August 27, 2022'
    },
    {
        'author': 'NANCY ENT',
        'title': 'Blog Post #2',
        'content': 'First post Content Lo',
        'date_posted': 'August 7, 2022'
    },
    {
        'author': 'NANCY ENT',
        'title': 'Blog Post #2',
        'content': '2nd post Content Chief',
        'date_posted': 'August 8, 2022'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

