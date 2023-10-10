from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponse
from users.models import Profile
from django.contrib.auth.decorators import login_required
import os
# Create your views here.


# class HomePageView(TemplateView):
#     template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


def membership_page(request):
    return render(request, 'membership.html')


def terms_page(request):
    return render(request, 'terms.html')


def privacy_page(request):
    return render(request, 'privacy.html')


def help_page(request):
    return render(request, 'help.html')

@login_required(login_url='login')
def following(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    return render(request, 'follows.html', {'profile': profile})

@login_required(login_url='login')
def followers(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    return render(request, 'followers.html', {'profile': profile})
