from django.urls import path, include
from users import views

urlpatterns = [
    path('', views.UserListCreateView.as_view(), name='user-list-create'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('<int:pk>/deactivate/', views.UserDeactivateView.as_view(), name='user-deactivate'),
]