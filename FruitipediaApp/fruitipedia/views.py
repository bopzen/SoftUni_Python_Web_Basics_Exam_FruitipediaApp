from django.shortcuts import render, redirect

from FruitipediaApp.fruitipedia.forms import ProfileForm, FruitCreateForm, FruitEditForm, FruitDeleteForm, \
    ProfileEditForm, ProfileDeleteForm
from FruitipediaApp.fruitipedia.models import Profile, Fruit


def index(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile
    }
    return render(request, 'common/index.html', context)


def dashboard(request):
    profile = Profile.objects.first()
    fruits = Fruit.objects.all()
    context = {
        'profile': profile,
        'fruits': fruits
    }
    return render(request, 'common/dashboard.html', context)


def create_fruit(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'fruit/create-fruit.html', context)


def fruit_details(request, pk):
    profile = Profile.objects.first()
    fruit = Fruit.objects.filter(pk=pk).get()
    context = {
        'profile': profile,
        'fruit': fruit
    }
    return render(request, 'fruit/details-fruit.html', context)


def edit_fruit(request, pk):
    profile = Profile.objects.first()
    fruit = Fruit.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = FruitEditForm(instance=fruit)
    else:
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'profile': profile,
        'fruit': fruit,
        'form': form
    }
    return render(request, 'fruit/edit-fruit.html', context)


def delete_fruit(request, pk):
    profile = Profile.objects.first()
    fruit = Fruit.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = FruitDeleteForm(instance=fruit)
    else:
        form = FruitDeleteForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'profile': profile,
        'fruit': fruit,
        'form': form
    }
    return render(request, 'fruit/delete-fruit.html', context)


def create_profile(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = ProfileForm()
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    profile = Profile.objects.first()
    fruits = Fruit.objects.all()
    context = {
        'profile': profile,
        'fruits': fruits
    }
    return render(request, 'profile/details-profile.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profile/delete-profile.html', context)
