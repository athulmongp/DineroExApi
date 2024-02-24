from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.deatils.as_view()),
    path('Login/',views.CustomLoginView.as_view()),
    path('person2/<int:pk>',views.deatils2.as_view()) ,

    # ----moduleList-----
    path('moduleListCreation',views.ModuleListCreationview.as_view()) ,
    path('moduleListGet',views.ModuleListGetview.as_view()) ,
    path('moduleListEdit/<int:pk>',views.ModuleListEditView.as_view()) ,
    path('moduleListDelete/<int:pk>',views.ModuleListDeleteView.as_view()) ,

    # ----moduleListPermission-----

    path('moduleListtPermissionCreation',views.ModuleListPermissionCreationview.as_view()) ,
    path('moduleListtPermissionGet',views.ModuleListPermissionGetview.as_view()) ,
    path('moduleListPermissionEdit/<int:pk>',views.ModuleListPermissionEditView.as_view()) ,
    path('moduleListPermissionDelete/<int:pk>',views.ModuleListPermissionDeleteView.as_view()) ,
]

  