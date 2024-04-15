from django.urls import path
from .views import (
    ProductListVIew,
    ProductByIDView,
    DeleteProductByID,
    CreateProductView,
    UpdateProductView,
    CategoryListView,
    DeleteCategoryByID,
    UpdateCategoryView,
    GetCategoryByIDView,
    CreateCategoryView
    )

urlpatterns =[
    path('product/create',CreateProductView.as_view(),name='new_product'),
    path('products',ProductListVIew.as_view(),name='all_products'),
    path('product/<int:id>',ProductByIDView.as_view(),name='product'),
    path('product/<int:id>/update',UpdateProductView.as_view(),name='update_product'),
    path('product/<int:id>/delete',DeleteProductByID.as_view(),name='del_product'),

    path('category/create',CreateCategoryView.as_view(),name='new_category'),
    path('category/<int:id>',GetCategoryByIDView.as_view(),name='category'),
    path('category/<int:id>/update',UpdateCategoryView.as_view(),name='update_category'),
    path('category/<int:id>/delete',DeleteCategoryByID.as_view(),name='del_category'),
    path('categories/',CategoryListView.as_view(),name='all_category'),
]