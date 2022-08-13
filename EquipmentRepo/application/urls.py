from django.urls import path
from .import views

urlpatterns = [
    path('list/',views.AppList.as_view(),name="app-list"),
    path('list/<int:pk>',views.APPListDetails.as_view(),name="app-details"),
    path('userlist/',views.UserList.as_view(),name="user-list"),
    path('userlist/<int:pk>',views.UserListDetails.as_view(),name="user-details"),
]
