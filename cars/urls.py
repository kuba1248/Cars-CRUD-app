from django.urls import path
from cars import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.MainView.as_view(),name='index'),
    path("cars_list/<int:page>", views.listing, name="index-by-page"),
    path('cars/<int:id>/detail',views.carListView.as_view(), name='cars_detail'),

    path('brandsp/', views.brandSpisokView.as_view(), name='brand_spisok'),
    path('brandsp/<int:page>', views.listing2, name='brand-by-page'),

    # path("brands/", views.brandListView.as_view(), name='brand_list'),
    # path("brands/<int:page>",views.listing2, name='brand-by-page'),

    path('brandsp/<int:id>/detail', views.brandDetailView.as_view(), name='brand_detail'),

    path('brand/create',views.brandCreateView.as_view(), name='brand_create'),
    path('brand/<int:pk>/update',views.brandUpdateView.as_view(), name='brand_update'),
    path('brand/<int:pk>/delete',views.brandDeleteView.as_view(), name='brand_delete'),
    path('cars/create',views.CarsCreateView.as_view(), name='cars_create'),
    path('cars/<int:pk>/update',views.CarsUpdateView.as_view(),name='cars_update'),
    path('cars/<int:pk>/delete',views.CarsDeleteView.as_view(),name='cars_delete')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)