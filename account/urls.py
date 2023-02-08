from django.urls import path, include

from account import views

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('sign_up_views/', views.signUpView, name='sign_up'),
    path('sign_in_views/', views.signInView, name='sign_in'),
    path('log_out/',views.logoutView,name="log_out"),
    path('user_detail/', views.justUser, name="justUser"),
    path('user_detail/<int:pk>', views.justUserDetail, name="justUser_detail"),
    ]