from django.urls import path
from .views import RegisterView, CustomTokenPairView,LogoutAllView,LogoutView

urlpatterns =[
    path('register',RegisterView.as_view(),name='register'),
    path('login', CustomTokenPairView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('logout_all', LogoutAllView.as_view(), name='logout_all'),
]