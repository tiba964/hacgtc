from django.urls import path
from . import views
from django.contrib import admin
from . import views
from . import api

app_name = 'jobs'

urlpatterns = [
    path('', views.index, name='index'),
    path('reply/', views.reply, name='reply'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),

    path('about/', views.about, name='about'),



    path('projects/', views.projects_list, name='project'),
    path('project_detail/<int:id>', views.projects_detail, name='projects_detail'),

    # api
    path('api/projects', api.projects_api, name='projects_api'),
    path('api/projects/<int:id>', api.project_detail_api, name='project_detail_api'),


    # class based views
    path('api/v2/projects', api.ProjectDetailListApi.as_view(),
         name='ProjectDetailListApi'),
    path('api/v2/projects/<int:id>',
         api.ProjectDetailDetail.as_view(), name='ProjectDetailDetail'),
]
