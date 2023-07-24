from django.urls import path
from registerform import views
from registerform.views import user

urlpatterns = [
    path('',views.home),
    # path('user',views.user),
     path('user/', user, name='user'),
     path('success', views.success),
     path('details', views.details),
    
    
]
