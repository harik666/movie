from . import views
from django.urls import path

app_name = 'movapp'

urlpatterns = [
    path('', views.fun_mov, name="show1"),
    path('mov/<int:movID>/', views.fun_detail, name="det"),
    path('movDet/<int:movID>/', views.fun_detail2, name="det2"),
    path('add/', views.fun_add1, name="add1"),
    path('edit/<int:movID>/', views.fun_edit, name="edit1"),
    path('del/<int:movID>/', views.fun_del, name="del1")

]
