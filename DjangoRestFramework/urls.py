"""DjangoRestFramework URL Configuration

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
from email.policy import default
from django.contrib import admin
from django.urls import path , include
from myApp.views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('courses' , CourseViewSet , basename= 'course') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employees' , employeeDashboard),
    path('api/users' , userDashboard),
    path('api/employees/<id>' , employeeDetails),
    # path('api/courses' , courseDashboard),
    # path('api/courses/<id>' , courseDetails),
    # path('api/courses' , CourseLists.as_view()),
    # path('api/courses/<pk>'  , CourseModification.as_view())
    path('api/', include(router.urls) ),
    path('api/instructor' , InstructorList.as_view()),
    path('api/subjects' , SubjectsList.as_view()),
    path('api/instructor/<pk>' , InstructorDetails.as_view() , name= 'instructor-detail'),
    path('api/subjects/<pk>' , SubjectDetails.as_view() , name= 'subjects-detail'),
]
