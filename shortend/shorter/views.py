from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def shorter_redirect_view(request,*args,**kwargs):
    return HttpResponse("hello")

class shorterBaseView(View):
    def get(self, request, *args,**kwargs):
        return HttpResponse("Hello again")