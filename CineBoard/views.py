from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import login, logout 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from CineBoard.forms import MovieForm
from CineBoard.models import Movie


# Регистрация добавила в header способ регистрации под каталогами фильмов
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/logon/')
    else:
        form = UserCreationForm()
    return render(
        request,
        template_name='CineBoard/logon.html',
        context={'form': form}
    )



def logon_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home_page')
        else:
            form=AuthenticationForm()
        return render(
        request,
        template_name='CineBoard/registration.html',
        context={'form': form}
    )



def sign_out_view(request):
    logout(request)
    return redirect('home_page')




def add_movie_view(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/movie_list/')
    else:
        form=MovieForm  
    return render(
        request,
        template_name='CineBoard/add_movie.html',
        context={'form': form}
    )




def show_movie_view(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        return render(
        request,
        template_name='CineBoard/add_movie.html',
        context={'movie': movie}
    )



def edit_movie_view(request, id):
    movie_id =  get_object_or_404(Movie, id)
    if request.method == 'POST':
        form = MovieForm(request.POST,instance=movie_id),
        if form.is_valid():
            form.save()
            return redirect('/movie_list/')
        else:
            MovieForm(instance=movie_id)
            return render(
                request,
                template_name='CineBoard/edit_movie.html',
                context={
                'form': form,
                'movie_id': movie_id
                }
            )


def delete_movie_view(request, id):
    movie_id =get_object_or_404(Movie,id)
    movie_id.delete
    return redirect('/movie_list/')



# В movie_list изменила s на m
def search_view(request):
 query = request.GET.get('m','') 
 if query:
         movie = Movie.objects.filter(name_film__icontains=query)
 else:
    movie = Movie.objects.none()
    return render(
       request,
       template_name='CineBoard/movie_list.html',
      context={
            'movie': movie
      }
    )
