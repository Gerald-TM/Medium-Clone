from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Profile
from django.contrib.auth.decorators import login_required
from articles.models import Article

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name ='registration/signup.html'
    success_url = reverse_lazy('login')

@login_required(login_url='login')
def profile_view(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    if profile:
        profile_users_articles = Article.objects.all().filter(author=profile.user)
        # follow and unfollow logic
        if request.method == 'POST':
            current_user_profile = request.user.profile
            action = request.POST['follow']
            if action == 'unfollow':
                current_user_profile.follows.remove(profile)
            else:
                current_user_profile.follows.add(profile)
            current_user_profile.save()
        return render(request, 'profile.html', {'profile':profile, 'user_articles':profile_users_articles})
    else:
        return HttpResponse('<b>You have to create a profile</b>')
    
def no_profile_view(request):
    return render (request, 'no_profile.html')

    



