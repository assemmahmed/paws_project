from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('pets/', views.pets, name='pets'),
    path('add-pet/', views.add_pet_form, name='add_pet'),
    path('create-blog/', views.create_blog, name='create_blog'),
    path('blog/', views.get_blog, name='blogs'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
]


