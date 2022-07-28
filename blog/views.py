
from django.contrib.auth import authenticate
from django.shortcuts import render,HttpResponse,HttpResponseRedirect

from .forms import SignupForm,loginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import post
from django.contrib.auth.models import Group
from .serializers import PostSer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView

# Create your views here.
class getapi(ListAPIView):
    queryset = post.objects.all()
    serializer_class = PostSer

class postapi(CreateAPIView):
    queryset = post.objects.all()
    serializer_class = PostSer

class Retriveapi(RetrieveAPIView):
    queryset = post.objects.all()
    serializer_class = PostSer

class Destroyeapi(DestroyAPIView):
    queryset = post.objects.all()
    serializer_class = PostSer
def home(request):
    posts= post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

def dash(request):
    if request.user.is_authenticated:
        posts= post.objects.all()
        return render(request,'blog/dashboard.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/login/')
def about(request):
    return render(request,'blog/about.html')
def log(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = loginForm(request=request,data= request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass =form.cleaned_data['password']
                user = authenticate(username=uname,password= upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully....')
                return HttpResponseRedirect('/dashboard/')
            
        else:
            form = loginForm()

        return render(request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

def contact(request):
    return render(request,'blog/contact.html')
def navbar(request):
    return render(request,'blog/navbar.html')
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request,'congratulations !! tou are register successfully...')
            user=form.save()
            group = Group.objects.get(name= 'auther')
            user.groups.add(group)
        form = SignupForm(request.POST)
    else:
        form = SignupForm()
    return render(request,'blog/signup.html',{'form':form})
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
def addpost(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            fm = PostForm(request.POST)
            if fm.is_valid():
                fm.save()
            fm = PostForm()
        else:
            fm = PostForm()
        return render( request,'blog/addpost.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')

    
  
def update(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request,'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
def user_deletpost(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer