from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
def app(request):
    #post=Blog.objects.all()
    post1=Job.objects.all()
    return render(request,"base.html",{'post1':post1})
# Create your views here.
