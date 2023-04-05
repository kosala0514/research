"""pythonteacher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from pythonteacherapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('addnew', views.addnew, name='addnew'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('updatetestmark', views.updatetestmark, name='updatetestmark'),
    path('delete/<int:id>', views.delete, name='delete'),
    # path('login', views.login),
    path('register', views.register, name='register'),
    path('execute_code', views.execute_code, name='execute_code'),

    # medium level
    path('chapter', views.chapter, name='chapter'),
    path('assignment', views.assignment, name='assignment'),
    path('upload_file', views.upload_file, name='upload_file'),

    # path('postsignIn/', views.postsignIn),
    # path('postsignUp/', views.postsignUp),
    # path('pretest/', views.pretest),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
