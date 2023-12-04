from django.shortcuts import render, get_object_or_404, redirect
from main import models
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, authenticate, logout


def index(request):
    
    search_post = request.GET.get('search')

    if search_post:
        posts = models.Article.objects.filter(Q(title__icontains=search_post))
        
    else:
        posts = models.Article.objects.all().order_by('-createdAt')[:6]
    
    
    return render(request,'main/index.html',{"posts": posts})

def all_articles(request):

    all = models.Article.objects.all().order_by('-createdAt')

    return render(request, 'main/allarticles.html', {"all": all})

def article(request,pk):
    article = get_object_or_404(models.Article,pk = pk)
    context = {
        "article" : article
    }
    return render(request,'main/article.html',context)

def author(request,pk):
    author = get_object_or_404(models.Author,pk = pk)
    context = {
        "author" : author
    }
    return render(request,'main/author.html',context)

def create_article(request):
    authors = models.Author.objects.all()
    context = {
        "authors" : authors
    }
    
    if request.method == "POST":
        article_data = {
            "title" : request.POST['title'],
            "content" : request.POST['content'],
        }

        new_author_name = request.POST['new_author_name']
        author = models.Author.objects.create(name=new_author_name)
    
        article = models.Article.objects.create(**article_data)
        article.authors.set([author])
 
        if 'image' in request.FILES:
            uploaded_file = request.FILES['image']
            article.img = uploaded_file
            article.save()
        context["success"] = True
        messages.success(request,"successfully registered")
        
    
    return render(request, 'main/create_article.html', context)

def delete_article(request, pk):
    # Get the article by its primary key
    article = get_object_or_404(models.Article, pk=pk)
    
    if request.method == 'POST':
        # Delete the article
        article.delete()
        
    
    # Redirect to the homepage or any other desired page
    return redirect('index')


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('index')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request,'main/login.html', context={"login_form":form})

def register_request(request):
    form = models.NewUserForm()
    
    if request.method == "POST":
        form = models.NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render (request,'main/register.html', context={"form":form})


def profile(request):  
    context = {      
    }
    return render (request, 'main/profile.html', context)

def logout_request(request):
    
    logout(request)
    
    return redirect('index')

    




			
			
		