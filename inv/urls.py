from django.urls import path
from inv.views import *

app_name = 'inv_app'

urlpatterns = [
    #Categorías
    path('categorias/', CategoriaView.as_view(), name='categorias_list'),
    path('categorias/add/', CategoriaNew.as_view(), name='categoria_add'),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/inactivar/<int:id>', categoria_inactivar, name='categoria_inactivar'),

    #SubCategorías
    path('subcategorias/', SubCategoriaView.as_view(), name='subcategorias_list'),
    path('subcategorias/add/', SubCategoriaNew.as_view(), name='subcategoria_add'),
    path('subcategorias/edit/<int:pk>', SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategorias/inactivar/<int:id>', subcategoria_inactivar, name='subcategoria_inactivar'),

    #Marcas
    path('marcas/', MarcaView.as_view(), name='marcas_list'),
    path('marcas/add/', MarcaNew.as_view(), name='marca_add'),
    path('marcas/edit/<int:pk>', MarcaEdit.as_view(), name='marca_edit'),
    path('marcas/inactivar/<int:id>', marca_inactivar, name='marca_inactivar'),

    #Unidades de Medidas
    path('unimedidas/', UniMedidaView.as_view(), name='unimedidas_list'),
    path('unimedida/add/', UniMedidaNew.as_view(), name='unimedida_add'),
    path('unimedida/edit/<int:pk>', UniMedidaEdit.as_view(), name='unimedida_edit'),
    path('unimedida/inactivar/<int:id>', unimedida_inactivar, name='unimedida_inactivar'),

    #Unidades de Medidas
    path('products/', ProductoView.as_view(), name='productos_list'),
    path('producto/add/', ProductoNew.as_view(), name='producto_add'),
    path('producto/edit/<int:pk>', ProductoEdit.as_view(), name='producto_edit'),
    path('producto/inactivar/<int:id>', producto_inactivar, name='producto_inactivar'),
]