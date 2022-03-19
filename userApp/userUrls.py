from django.urls import path
from .import views

urlpatterns = [
    path('user-register/',views.UserReg.as_view(),name='userregister'),
    # path("Show-Users/",views.ViewAll.as_view(),name="userview"),
    path('show-slots/',views.Avalability.as_view(),name='timeView'),

]