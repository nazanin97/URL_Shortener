from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from yekta.models import URL





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
	id = 10000000000 + len(URL.objects.all())

	if request.method == 'POST':
		shorten_url = encode(id)
		if 'save' in request.POST:
			URL.objects.create(link="http://127.0.0.1:8000/shorter/" + shorten_url, numberOfVisits=0, numberOfUsers=0)
		
		
		return render(request, 'users/main.html', {'content': "http://127.0.0.1:8000/shorter/" + shorten_url})
	else:
		return render(request, 'users/main.html')
        # urls = URL.objects.all
     #    context = {
     #    # 'posts': URL.objects.all()
    	# }
        
        # increase cnt for next url
       	


@login_required
def profile(request):
	userURLs = URL.objects.filter(creator=request.user)
	print(userURLs)
	return render(request, 'users/profile.html', {'urls': userURLs})



