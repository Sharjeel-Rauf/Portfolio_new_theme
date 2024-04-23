from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.title_page_view, name='title_page'),
    path('logout_user/', views.logout_user, name = 'logout_user'),
    path('', views.portfolio_page_view, name='portfolio_page'),
    path('about/', views.about_page_view, name='about_page'),
    path('create_project', views.create_project_view, name='create_project'),
    path('edit_project/<int:project_id>/', views.edit_project_view, name='edit_project'),
    path('delete_project/<int:project_id>/', views.delete_project_view, name='delete_project'),
    path('summary/add/', views.add_summary, name='add_summary'),
    path('summary/edit/', views.edit_summary, name='edit_summary'),
    path('user_profile/add/', views.add_user_profile, name='add_user_profile'),
    path('user_profile/edit/', views.edit_user_profile, name='edit_user_profile'),
    path('project/<int:project_id>/', views.project_detail_view, name='project_detail'),
    path('project/<int:detail_id>/edit/', views.edit_details_view, name='edit_details'),
    path('project/<int:project_id>/add_detail/', views.add_project_detail_view, name='add_project_detail'),
    path('edit-profile-description/', views.profile_description_edit, name='add_edit_profile_description'),
    
]

