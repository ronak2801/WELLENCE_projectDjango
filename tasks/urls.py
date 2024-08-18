from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views  # Import auth_views
from tasks import views as tasks_views

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Combined Register/Login view as root
    path('', tasks_views.register_login_combined, name='register_login'),

    # User dashboard
    path('dashboard/', tasks_views.user_dashboard, name='user_dashboard'),

    # Landing page
    path('landing/', tasks_views.landing_page, name='landing_page'),

    # Logout
    path('logout/', tasks_views.CustomLogoutView.as_view(), name='logout'),

    # Task management URLs
    path('add-task/', tasks_views.add_task, name='add_task'),
    path('edit-task/<int:task_id>/', tasks_views.edit_task, name='edit_task'),
    path('delete-task/<int:task_id>/', tasks_views.delete_task, name='delete_task'),

    # Password reset URLs using auth_views
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
