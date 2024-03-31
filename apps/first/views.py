from django.shortcuts import render
from apps.first.models import InfoUser,Numbers,Service
# Create your views here.

def index(request):
    infouser = InfoUser.objects.latest('id')
    numbers = Numbers.objects.latest('id')
    service = Service.objects.all()
    return render(request,"index.html",locals())