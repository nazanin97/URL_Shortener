from django.shortcuts import render
from .models import URL
from django.http import HttpResponseRedirect
from django.contrib import messages

def home(request):
    
	context = {
        'posts': URL.objects.all()
    }
	return render(request, 'yekta/home.html', context)

def about(request):
    if request.method == 'POST':
        result = URL.objects.filter(shortLink=request.POST['userReq'])
        if len(result) == 0:
            messages.warning(request, 'Invalid URL!')
            return render(request, 'yekta/about.html', {'title': 'Redirect'})
        else:
            
            result = result.first()
            result.numberOfVisits += 1
            if "Mobi" in request.headers['User-Agent']:
                result.numMobile += 1
            else:
                result.numDesktop += 1

            if "Chrome" in request.headers['User-Agent']:
                result.numChrome += 1
            elif "Firefox" in request.headers['User-Agent']:
                result.numFirefox += 1
            else:
                result.numSafari += 1
                
            result.save()    
            return HttpResponseRedirect(result.link)
            # return render(request, 'yekta/about.html', {'content': result.link, 'device': request.headers})
    else:    
	    return render(request, 'yekta/about.html', {'title': 'Redirect'})