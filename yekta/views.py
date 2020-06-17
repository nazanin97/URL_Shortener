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
    if request.method == 'POST':
        result = URL.objects.filter(shortLink=request.POST['userReq'])
        if len(result) == 0:
            return render(request, 'yekta/about.html', {'title': 'Redirect'})
        else:
            return render(request, 'yekta/about.html', {'content': result.first().link, 'device': request.headers, 'browser': request.headers})
    else:    
	    return render(request, 'yekta/about.html', {'title': 'Redirect'})