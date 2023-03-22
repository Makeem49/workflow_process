from django.urls import path

from grant_access import views


urlpatterns = [
    path('permission/create/', \
            views.GrantPermissionCreateListView.as_view(), name='permission-list-create'),
    path('permission/update/<int:pk>', \
            views.GrantPermissionUpdateView.as_view(), name='permission-update'),
    path('permission/delete/',  \
            views.GrantPermissionDeleteView.as_view(), name='permission-delete'),
    path('permission/<str:process_name>/<str:stage_name>/<int:pk>/', \
            views.AssignStagePermissionView.as_view(), name='assign-permission-to-stage'),
    path('permission/<str:process_name>/<str:stage_name>/<str:step_name>/<int:pk>/', \
            views.AssignStepPermissionView.as_view(), name='assign-permission-to-steps'),
    path('permission/<str:process_name>/<int:pk>/', \
            views.AssignProcessPermissionView.as_view(), name='assign-permission-to-process'),


    path('group/create/', views.GrantGroupCreateListView.as_view(), name='group-list-create'),
    path('group/update/<int:pk>/', views.GrantGroupUpdateView.as_view(), name='group-update'),
    path('group/delete/<int:pk>/', views.GrantGroupDeleteView.as_view(), name='group-delete'),

    path('group/<str:group_name>/<int:pk>/', views.AssignGroupPermissionView.as_view(), name='assign-permission-to-group'),

    path('group/<str:process_name>/add/<int:pk>/', views.AssignGroupProcessView.as_view(), name='assign-group-to-process'),

    path('group/<str:process_name>/<str:stage_name>/add/<int:pk>/', views.AssignGroupStageView.as_view(), name='assign-group-to-stage'),

    path('group/<str:process_name>/<str:stage_name>/<str:step_name>/add/<int:pk>/', views.AssignGroupStepView.as_view(), name='assign-group-to-step'),
]