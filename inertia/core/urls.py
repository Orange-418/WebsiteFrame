from django.contrib import admin
from django.urls import path, include
from inertiatools import views

urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),

    # Include URLs from the inertiatools application
    path('', include('inertiatools.urls')),

    # Home page URL
    path('', views.home, name='home'),

    # About page URL
    path('about/', views.about, name='about'),

    # Register page URL
    path('register/', views.register, name='register'),

    # Account page URL
    path('account/', views.account, name='account'),

    # Login page URL
    path('login/', views.login, name='login'),

    # Logout page URL
    path('logout/', views.logout, name='logout'),
]
