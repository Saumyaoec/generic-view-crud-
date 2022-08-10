from django.urls import path, include
from . import views

app_name = "DepartmentApp"

urlpatterns = [
    path('home', views.home, name="department"),
    path('organization_create/',views.OrganizationCreateView.as_view(), name = "organizationcreate"),
    path('organization_list/',views.OrganizationListView.as_view()),
    path('department_create/',views.DepartmentCreateView.as_view(), name = "departmentcreate"),
    path('department_list/',views.DepartmentListView.as_view(), name = "departmentlist"),
    path('department_update/<uuid:pk>/',views.DepartmentUpdateView.as_view(), name = "departmentupdate"),
    path('department_deatil/<uuid:pk>/',views.DepartmentDetailView.as_view(), name = "departmentdetail"),
    path('department_delete/<uuid:pk>/', views.DepartmentDeleteView.as_view(), name = "departmentdelete"),
   

]
