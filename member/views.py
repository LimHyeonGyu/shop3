from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from member.forms import UserForm, ProfileForm
from product.models import Product
from member.models import Profile
from django.db import transaction

class HotListView(ListView):
    queryset = Product.objects.filter(pro_hot=True)
    template_name = 'member/index.html'


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.author = user
            profile.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            login(request, user)
            return redirect('home')
    else:
        form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'member/signup.html', {'form':form, 'profile_form':profile_form})