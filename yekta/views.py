from django.shortcuts import render
from .models import URL
from .models import RequestLog
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib import messages


def saveResult(result, request):
    device = ""
    browser = ""
    result = result.first()
    result.numberOfVisits += 1
    if "Mobi" in request.headers['User-Agent']:
        device = "Mobile"
        result.numMobile += 1
    else:
        device = "Desktop"
        result.numDesktop += 1

    if "Chrome" in request.headers['User-Agent']:
        browser = "Chrome"
        result.numChrome += 1
    elif "Firefox" in request.headers['User-Agent']:
        browser = "Firefox"
        result.numFirefox += 1
    else:
        browser = "Safari"
        result.numSafari += 1
        
    result.save()

    RequestLog.objects.create(link=result.shortLink, ip=request.META.get('REMOTE_ADDR'), browser=browser, device=device)
    return HttpResponseRedirect(result.link)
    
    


def shortener(request, shortURL):
    result = URL.objects.filter(shortLink="http://127.0.0.1:8000/shortener/" + shortURL)

    if len(result) > 0:
        return saveResult(result, request)
    else:
        return HttpResponseNotFound("invalid")


def home(request):
	# context = {
 #        'posts': URL.objects.all()
 #    }
	return render(request, 'yekta/home.html')


def about(request):
    if request.method == 'POST':
        result = URL.objects.filter(shortLink=request.POST['userReq'])
        if len(result) > 0:
            return saveResult(result, request)
            
        else:
            messages.warning(request, 'Invalid URL!')

    return render(request, 'yekta/about.html', {'title': 'Redirect'})

