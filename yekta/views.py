from django.shortcuts import render
from .models import URL

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
	context = {
        'posts': URL.objects.all()
    }
	return render(request, 'yekta/home.html', context)

def about(request):
	return render(request, 'yekta/about.html', {'title': 'About'})