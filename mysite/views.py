from django.shortcuts import render
import random
# Create your views here.
def index (request):
	name = "CHEN"
	lottos= list()
	for i in range(6):
		lottos.append(random.randint(1,42))
	return render(request, 'index.html', locals())