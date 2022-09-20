from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomePage, SinPrivilegios, UserList, user_admin, HomeSinPrivilegios

app_name = 'bases_app'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('sin_privilegios', HomeSinPrivilegios.as_view(), name='sin_privilegios'),
    path('login/', auth_views.LoginView.as_view(template_name='bases/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='bases/login.html'), name='logout'),

    path('users-list/', UserList.as_view(), name='users_list'),
    path('user-add/', user_admin, name='user_add'),
    path('user-modify/<int:pk>', user_admin, name='user_modify'),

]