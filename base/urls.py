from django.urls import path
from . import views

urlpatterns = [
    path('',views.lobby),
    path('room/',views.room),
    path('get_token/',views.getToken),
    path('create_member/',views.createMember),
    path('delete_member/',views.deleteMember),
]
 