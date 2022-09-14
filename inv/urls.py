from django.urls import path
from inv.views import CategoriaView, CategoriaNew, CategoriaEdit, SubCategoriaView, SubCategoriaEdit, SubCategoriaNew

app_name = 'inv_app'

urlpatterns = [
    #Categorías
    path('categorias/', CategoriaView.as_view(), name='categorias_list'),
    path('categorias/add/', CategoriaNew.as_view(), name='categoria_add'),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),

    #SubCategorías
    path('subcategorias/', SubCategoriaView.as_view(), name='subcategorias_list'),
    path('subcategorias/add/', SubCategoriaNew.as_view(), name='subcategoria_add'),
    path('subcategorias/edit/<int:pk>', SubCategoriaEdit.as_view(), name='subcategoria_edit'),
]