from django.contrib import admin
from django.urls import path
import myapp.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myapp.views.main, name='main'),
    path('login/',myapp.views.login, name='login'),
    path('logout/',myapp.views.logout, name='logout'),
    path('create/',myapp.views.create, name='create'),
    path('createmember/',myapp.views.createmember, name='createmember'),
    path('<int:member_id>/delete/',myapp.views.delete, name='delete'),
    path('<int:member_id>/changework/',myapp.views.changework, name='changework'),
    path('<int:member_id>/codeconfirm/',myapp.views.codeconfirm, name='codeconfirm'),
    
]
