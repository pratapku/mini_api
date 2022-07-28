"""mini_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from .views import RegisterAPI
from django.contrib import admin
from django.urls import path ,include
from .views import Destroyeapi, Retriveapi, UserDetailAPI,RegisterUserAPIView, getapi, postapi
from rest_framework_simplejwt import views as jwt_views
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('dashboard/',views.dash,name='dash'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.log,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.user_logout,name='logout'),
   
    path('updat/<int:id>/',views.update,name='update'),
    path('deletpost/<int:id>/',views.user_deletpost,name='deletpost'),
    path('addpo/',views.addpost,name='add'),
    path('api/get/',getapi.as_view(), name='token_obtain_pair'),
    path('api/post/',postapi.as_view(), name='token_obtain_pair'),
    path('api/retrive/<int:pk>',Retriveapi.as_view(), name='token_obtain_pair'),
    path('api/destroye/<int:pk>',Destroyeapi.as_view(), name='token_obtain_pair'),
    
    path('api/register/',RegisterUserAPIView.as_view()),
    # path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),



]
