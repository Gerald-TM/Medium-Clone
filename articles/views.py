from django.shortcuts import render, get_object_or_404, redirect, HttpResponse,HttpResponseRedirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleCreateForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.

# Create View that that redirects you to the detail page.
@login_required(login_url='login')
def create_view(request):
    form = ArticleCreateForm()
    if request.method == 'POST':
        form = ArticleCreateForm(request.POST)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return redirect('detail', pk=form.save().id)
    else:
        form = ArticleCreateForm()

    return render(request, 'article_create.html', {'form': form})

# List View to list all your articles

# @login_required(login_url='login')
def list_view(request):
    model = Article
    article_list = model.objects.all().order_by('-publish')
    return render(request, 'home.html', {'article_list': article_list})

# Detail View to show just an individual article.
@login_required(login_url='login')
def detail_view(request, pk):
    model = Article
    article_detail = get_object_or_404(model, id=pk)
    total = article_detail.total_likes()
    return render(request, 'article_detail.html', {'detail': article_detail, 'total':total })

# Update View
@login_required(login_url='login')
def update_view(request, pk):
    object = get_object_or_404(Article, id=pk)
    if object.author == request.user:
        form = ArticleCreateForm(instance=object)
        if request.method == 'POST':
            form = ArticleCreateForm(request.POST, instance=object)
            if form.is_valid():
                form.save()
                return redirect('detail', pk=form.save().id)
        else:
            form = ArticleCreateForm(instance=object)
        return render(request, 'article_update.html', {'form': form})
    else:
        return HttpResponse('<b>403 Forbidden</b>')
        

# Delete View
@login_required(login_url='login')
def delete_view(request, pk):
    obj = get_object_or_404(Article, id=pk)
    if obj.author == request.user:
        if request.method == 'POST':
            obj.delete()
            return redirect('home')
        return render(request, 'article_delete.html', {'objct': obj})
    else:
        return HttpResponse('<b>403 Forbidden</b>')

# Like view
def likes_view(request, pk):
    obj = get_object_or_404(Article, id=pk)
    if obj.likes.filter(id= request.user.id):
        obj.likes.remove(request.user)
    else:
        obj.likes.add(request.user)
        
    return redirect('detail', pk=obj.id)