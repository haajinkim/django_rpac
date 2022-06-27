
from django.urls import path
from user import views
urlpatterns = [
    path('login/',views.Loginview.as_view()),
    path('logout/',views.Loginview.as_view()),
    path('user/', views.Userview.as_view()),
    path('follow/',views.Followview.as_view()),
    path('follow/<int:user_id>/',views.Followview.as_view())
]