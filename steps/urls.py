from django.urls import path
from steps import views

urlpatterns = [
    path('create/', views.StepCreateView.as_view(), name='step-create'),
    path('', views.StepListView.as_view(), name='step-list'),
    path('<str:step_name>/', views.StepDetailView.as_view(), name='step-detail'),
    path('<str:step_name>/update/', views.StepUpdateView.as_view(), name='step-update'),
    path('<str:step_name>/deactivate/', views.StepDeactivateView.as_view(), name='step-deactivate'),
]