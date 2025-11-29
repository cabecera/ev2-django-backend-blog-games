from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import EditorSignUpForm, ViewerSignUpForm

def register_editor(request):
    # asegura que grupos/perms ya fueron creados por post_migrate signal
    if request.method == 'POST':
        form = EditorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True  # puede acceder al panel admin
            user.save()
            grp = Group.objects.get(name='Editors')
            user.groups.add(grp)
            return redirect('login')
    else:
        form = EditorSignUpForm()
    return render(request, 'accounts/register_editor.html', {'form': form})

def register_viewer(request):
    if request.method == 'POST':
        form = ViewerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            user.save()
            grp = Group.objects.get(name='Viewers')
            user.groups.add(grp)
            return redirect('login')
    else:
        form = ViewerSignUpForm()
    return render(request, 'accounts/register_viewer.html', {'form': form})
