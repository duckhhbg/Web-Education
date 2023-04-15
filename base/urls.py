from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('update_user/', views.updateUser, name="update-user"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('create-subject/', views.createSubject, name="create-subject"),
    path('subject/<str:pk>/', views.Subject, name="subject"),
    path('create-chapter/<str:pk>', views.createChapter, name="create-chapter"),
    path('chapter/<str:pk>',views.Chapter,name="chapter"),
    path('major/<str:pk>', views.Major, name="major"),
    path('teacher',views.Teacher,name='teacher'),
    path('delete-subject/<str:pk>',views.deleteSubject,name="delete-subject")
]