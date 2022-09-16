from django.urls import path
from inv.views import CategoriaView, CategoriaNew, CategoriaEdit, SubCategoriaView, SubCategoriaEdit, SubCategoriaNew, \
    SubCategoriaDel, MarcaView, MarcaNew, MarcaEdit

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
    path('subcategorias/del/<int:pk>', SubCategoriaDel.as_view(), name='subcategoria_del'),

    #Marcas
    path('marcas/', MarcaView.as_view(), name='marcas_list'),
    path('marcas/add/', MarcaNew.as_view(), name='marca_add'),
    path('marcas/edit/<int:pk>', MarcaEdit.as_view(), name='marca_edit'),
]