from django.urls import path
from . import views

urlpatterns = [
    path('login_user/', views.title_page_view, name='title_page'),
    path('logout_user/', views.logout_user, name = 'logout_user'),
    path('', views.portfolio_page_view, name='portfolio_page'),
    path('about/', views.about_page_view, name='about_page'),
    path('create_project', views.create_project_view, name='create_project'),
    path('project/<int:project_id>/', views.project_detail_view, name='project_detail'),
    path('project/<int:detail_id>/edit/', views.edit_details_view, name='edit_details'),
    path('project/<int:project_id>/add_detail/', views.add_project_detail_view, name='add_project_detail'),
    
]

