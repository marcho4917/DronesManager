from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserAuthenticationForm, DroneForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Drone
import random
from faker import Faker


def home_view(request):
    return render(request, 'drones/home.html')


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
    else:
        form = UserRegisterForm()
    return render(request, 'drones/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('drone_list')
    else:
        form = UserAuthenticationForm()
    return render(request, 'drones/login.html', {'form': form})


@login_required
def drone_list(request):
    drones = Drone.objects.all()

    return render(request, 'drones/drone_list.html', {'drones': drones})


def add_drone(request):
    if request.method == 'POST':
        form = DroneForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            status = random.choice(['Active', 'Inactive', 'Service', 'Battery charge'])
            battery_level = form.cleaned_data['battery_level']
            if status == 'Service':
                current_location = 'Home'
            else:
                faker = Faker()
                latitude = faker.latitude()
                longitude = faker.longitude()
                current_location = f"{latitude}, {longitude}"
            drone = Drone.objects.create(
                name=name,
                status=status,
                battery_level=battery_level,
                current_location=current_location,
            )
            drone.save()
            return redirect('drone_list')
    else:
        form = DroneForm()
    return render(request, 'drones/add_drone.html', {'form': form})


def delete_drone(request, drone_id):
    if request.method == 'POST':
        Drone.objects.filter(pk=drone_id).delete()

    return redirect('drone_list')

