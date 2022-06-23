
from django.urls import path
from user import views
urlpatterns = [
    path('login/',views.Loginview.as_view()),
    path('logout/',views.Loginview.as_view()),
    path('user/', views.Userview.as_view())
]