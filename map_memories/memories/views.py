from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import GalleryForm
from .models import Gallery

def home(request):
    images = Gallery.objects.all()
    return render(request, 'memories/home.html', {
        'gallery_images': images,
    })


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Имя пользователя уже занято")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Почта уже зарегистрирована")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Аккаунт успешно создан!")
                return redirect('login')
        else:
            messages.error(request, "Пароли не совпадают")

    return render(request, 'memories/register.html')



def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Неверный логин или пароль")
    return render(request, 'memories/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def memories(request):
    city = request.GET.get("city", "")

    # Fetch all memories
    images = Gallery.objects.all()

    # Apply filters if selected
    if city:
        images = images.filter(city__iexact=city)

    # Get all distinct cities
    cities = Gallery.objects.values_list("city", flat=True).distinct()

    context = {
        "gallery_images": images,
        "cities": cities,
        "selected_city": city
    }
    return render(request, "memories/memories.html", context)

def gallery_images(request):
    print('a')
    if request.method == 'POST':
        print('b')
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GalleryForm()
    return render(request,  "memories/gallery.html", {'form': form})

def success(request):
    return render(request,  "memories/home.html")

def display_gallery_images(request):
    images = Gallery.objects.all()
    return render(request, 'memories/display_gallery_images.html', {'gallery_images': images})