from django.contrib import messages, auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movies
from .forms import FormMovie


# Create your views here.

def fun_mov(request):
    mov1 = Movies.objects.all()
    cont = {'mov_list': mov1}
    return render(request, 'mov.html', cont)


def fun_detail(request, movID):
    return HttpResponse("Movies no : %s " % movID)


def fun_detail2(request, movID):
    mv = Movies.objects.get(id=movID)
    return render(request, 'det.html', {'singleMov': mv})


def fun_add1(request):
    if request.method == 'POST':
        name = request.POST['mv_name']
        des = request.POST['mv_des']
        year = request.POST['mv_year']
        img = request.FILES['mv_img']
        objMov = Movies(name=name, des=des, year=year, img=img)
        objMov.save()

    return render(request, 'movadd.html')


def fun_edit(request, movID):
    movie = Movies.objects.get(id=movID)
    form = FormMovie(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('movapp:show1')
    return render(request, 'movedit.html', {'form1': form, 'movie': movie})


def fun_del(request, movID):
    movie = Movies.objects.get(id=movID)
    if request.method == 'POST':
        movie.delete()
        return redirect('movapp:show1')

    return render(request, 'movdel.html', {'movie': movie})
