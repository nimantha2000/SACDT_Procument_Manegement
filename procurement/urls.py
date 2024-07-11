from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('user/', views.user_dashboard, name='user_dashboard'),
    path('procurement/create/', views.create_procurement, name='create_procurement'),
    path('procurement/<int:id>/', views.view_procurement, name='view_procurement'),
    path('procurement/<int:id>/step/<int:step>/', views.continue_step, name='continue_step'),
    path('', views.admin_dashboard, name='root_dashboard'),  # Add this line
]
