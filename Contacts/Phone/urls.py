from  django.urls import  path

from  . import  views
urlpatterns=[
    path('index',views.index,name="index"),
    path('<int:id>/details',views.details,name="details"),
    path('show_add',views.show_add,name="add"),
    path('',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('<int:id>',views.edit,name="edit"),
    path('accounts/login/',views.login,name="login")


]