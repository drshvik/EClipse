from django.shortcuts import render,redirect
from .forms import AddPostForm
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request,template_name='post/index.html',context={'posts':posts})

def userposts(request):
    posts = Post.objects.filter(user=request.user)
    return render(request,template_name = 'post/myposts.html',context={'posts':posts})

def post(request,id):
    post = Post.objects.get(id=id)
    return render(request,template_name= 'post/post.html',context={'post':post})

def addpost(request):
    form = AddPostForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            post =  form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('index')
        
    else:
        form = AddPostForm()

    return render(request,template_name='post/addpost.html',context={'form':form})

def otherprofile(request,id):
    post = Post.objects.get(id=id)
    return render(request, template_name='post/otherprofile.html',context={'post':post})

def myprofile(request):
    user = request.user
    return render(request, template_name='post/myprofile.html',context={'user':user})