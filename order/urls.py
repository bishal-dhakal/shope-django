from django.urls import path
from .views import (
    CreateOrderView,
    UpdateOrderView,
    OrdersView,
    OrdersByIdView,
    OrdersByUser
)

urlpatterns =[
    path('create',CreateOrderView.as_view(),name='make_order'),
    path('<int:id>/update',UpdateOrderView.as_view(),name='update_order'),
    path('<int:id>',OrdersByIdView.as_view(),name='orderbyid'),
    path('all',OrdersView.as_view(),name='all_order'),
    path('user',OrdersByUser.as_view(),name='users_order'),
]