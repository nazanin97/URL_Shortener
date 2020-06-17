from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from yekta.models import URL
import random
import string


def add(s):
    k = random.randint(0, len(s) - 1)
    l = random.choice(string.ascii_letters)
    x = s[:k] + l + s[k:]
    return x

def delete(s):
    k = random.randint(0, len(s) - 1)
    x = s[:k] + s[k+1:]
    return x

def edit(s):
    k = random.randint(0, len(s) - 1)
    l = random.choice(string.ascii_letters)
    x = s[:k] + l + s[k+1:]
    return x


def generate_similar_string(myString):

    r = random.randint(1, 3)
    if r == 1:
        myString = add(myString)
    elif r == 2:
        myString = edit(myString)
    else:
        myString = delete(myString)
    return myString


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('login')

	else:
		form = UserRegisterForm()
	
	return render(request, 'users/register.html', {'form': form})


def encode(id):
    # base 62 characters
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(characters)
    ret = []
    # convert base10 id into base62 id for having alphanumeric shorten url
    while id > 0:
        val = id % base
        ret.append(characters[val])
        id = id // base
    # since ret has reversed order of base62 id, reverse ret before return it
    return "".join(ret[::-1])



def main(request):
	
	id = random.randint(10 ** 6,10 ** 20) + len(URL.objects.all())

	if request.method == 'POST':

		# if user didn't enter anything, don't do anything
		if request.POST.get('userLink') == '':
			return render(request, 'users/main.html')

		
		# if user didn't check his own url and wants to save it
		if request.POST.get('button') == 'save' and request.POST.get('userChosenLink') != '' and request.POST.get('checkMessage') != 'valid':
			return render(request, 'users/main.html', {'longURL': request.POST.get('userLink'), 'message': 'Check-your-address-first!', 'data': request.POST.get('userChosenLink')})
		
		# if user entered his own url and wants to check it
		if request.POST.get('button') == 'check' and request.POST.get('userChosenLink') != '':
			query = "http://127.0.0.1:8000/shortener/" + request.POST.get('userChosenLink')
			if len(URL.objects.filter(shortLink=query)) == 0:
					return render(request, 'users/main.html', {'longURL': request.POST.get('userLink'), 'data': request.POST.get('userChosenLink'), 'message': 'valid'})	
			else:
				while True:
					temp = generate_similar_string("" + request.POST.get('userChosenLink'))
					query = "http://127.0.0.1:8000/shortener/" + temp
					if len(URL.objects.filter(shortLink=query)) == 0:
						return render(request, 'users/main.html', {'longURL': request.POST.get('userLink'), 'data': request.POST.get('userChosenLink'), 'message': 'invalid', 'suggestionLink': temp})


		# if user wants us to generate short link		
		if request.POST.get('button') == 'getShortLink':
			shorten_url = encode(id)
			query = "http://127.0.0.1:8000/shortener/" + shorten_url
			while len(URL.objects.filter(shortLink=query)) != 0:
				shorten_url = encode(random.randint(id , id + 100))
				query = "shortLink='http://127.0.0.1:8000/shortener/'" + shorten_url
			return render(request, 'users/main.html', {'content': "http://127.0.0.1:8000/shortener/" + shorten_url, 'longURL': request.POST.get('userLink')})


		# if user has checked his url and he wants to save that
		if request.POST.get('button') == 'save' and request.POST.get('userChosenLink') != '' and request.POST.get('checkMessage') == 'valid':
			URL.objects.create(link=str(request.POST.get('userLink')), shortLink= "http://127.0.0.1:8000/shortener/" + request.POST.get('userChosenLink'),
				numberOfVisits=0, numberOfUsers=0, creator=request.user)
			messages.success(request, f'New URL created !')
			return render(request, 'users/main.html', {'message': ''})

		if request.POST.get('button') == 'save' and request.POST.get('checkMessage') == 'invalid':
			
			return render(request, 'users/main.html', {'longURL': request.POST.get('userLink'), 'data': request.POST.get('userChosenLink'), 'message': 'invalid'})


		# if user wants to save our short link
		if request.POST.get('button') == 'save' and request.POST.get('ourShortLink') != '':
			URL.objects.create(link=request.POST.get('userLink'), shortLink= request.POST.get('ourShortLink'),
				numberOfVisits=0, numberOfUsers=0, creator=request.user)
			messages.success(request, f'New URL created !')
			return render(request, 'users/main.html', {'message': ''})

		else:
			return render(request, 'users/main.html')

		
	else:
		return render(request, 'users/main.html')
 

@login_required
def profile(request):
	userURLs = URL.objects.filter(creator=request.user)
	print(userURLs)
	return render(request, 'users/profile.html', {'urls': userURLs})



