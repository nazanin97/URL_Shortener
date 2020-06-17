from django.shortcuts import render
from .models import URL

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
            return render(request, 'yekta/about.html', {'content': result.first().link, 'device': request.headers, 'browser': request.headers['User-Agent']})
    else:    
	    return render(request, 'yekta/about.html', {'title': 'Redirect'})