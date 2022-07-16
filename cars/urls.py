from django.urls import path
from cars import views


urlpatterns = [
    path('',views.MainView.as_view(),name='index'),
    path("cars_list/<int:page>", views.listing, name="index-by-page"),
    path('cars/<int:id>/detail',views.carListView.as_view(), name='cars_detail'),
    path('brands/',views.brandListView.as_view(), name='brand_list'),
    path('brand/create',views.brandCreateView.as_view(), name='brand_create'),
    path('brand/<int:pk>/update',views.brandUpdateView.as_view(), name='brand_update'),
    path('brand/<int:pk>/delete',views.brandDeleteView.as_view(), name='brand_delete'),
    path('cars/create',views.CarsCreateView.as_view(), name='cars_create'),
    path('cars/<int:pk>/update',views.CarsUpdateView.as_view(),name='cars_update'),
    path('cars/<int:pk>/delete',views.CarsDeleteView.as_view(),name='cars_delete')
]
