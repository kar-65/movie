from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieapp.forms import movieform
from movieapp.models import movie


# Create your views here.
def index(request):
    movies = movie.objects.all()
    content={
        'list':movies
    }
    return render(request,'index.html',content)

def detail(request,movie_id):
    films = movie.objects.get(id=movie_id)
    #return HttpResponse("this is movie id %s" % movie_id)
    return render(request,'detail.html',{'movie':films})

def add_movie(request):
    if request.method=="POST":
        name= request.POST.get('name',)
        desc= request.POST.get('desc',)
        year=request.POST.get('year',)
        post=request.FILES['post']
        movies=movie(name=name,desc=desc,year=year,post=post)
        movies.save()
    return render(request,'add.html')

def update(request,id):
    movies= movie.objects.get(id=id)
    form=movieform(request.POST or None , request.FILES,instance=movies)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'update.html',{'form':form,'movie':movies})

def delete(request,id):
    if request.method == "POST":
        movies= movie.objects.get(id=id)
        movies.delete()
        return redirect('/')
    return render(request,'delete.html')