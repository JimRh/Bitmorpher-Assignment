from django.urls import path
from . import views


urlpatterns = [
    path('api/users',views.usercreateanduserlist),
    path('api/users/<str:username>',views.usermanage),
]
