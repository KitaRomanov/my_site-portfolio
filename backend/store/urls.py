from django.urls import path

from store.views import ProductsListView, basket_add, basket_remove

app_name = 'store'
urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    # path('category/<int:category_id>', ProductsListView.as_view(), name='category'), #категории пока не требуются
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]