from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
import uuid

from .models import Url

# Create your views here.

def index(request):
    return render(request,'index.html')

@csrf_exempt
def create(request):
    
    if request.method == 'POST':
        
        body =json.loads(request.body.decode('utf-8'))
    
        url = body['link']
        uid = str(uuid.uuid4())[:6]
        new_url = Url(link=url, uuid=uid)

        new_url.save()
        dict={}
        dict['shortnedURL']='http://localhost:8000/original/'+uid
        return JsonResponse(dict)


def getOriginal(request,pk):
    print(pk)
    originalUrl= Url.objects.get(pk=pk)

    return redirect(originalUrl.link)