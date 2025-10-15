from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('<int:id>', views.ver_medicamento, name='ver_medicamento'),
    path('agregar/', views.agregar_medicamento, name='agregar_medicamento'),
    path('editar/<int:id>/', views.editar_medicamento, name='editar_medicamento'),
    path('borrar/<int:id>/', views.borrar_medicamento, name='borrar_medicamento'),
]