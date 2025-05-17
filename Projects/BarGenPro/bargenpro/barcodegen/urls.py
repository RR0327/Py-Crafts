from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('generate/', views.generate_barcode, name='generate_barcode'),
    path('products/', views.product_list, name='product_list'),
    path('upload-csv/', views.upload_csv, name='upload_csv'),
    path('download/png/<int:pk>/', views.download_png, name='download_png'),
    path('download/pdf/<int:pk>/', views.download_pdf, name='download_pdf'),
    path('export/csv/', views.export_products_csv, name='export_products_csv'),
    path('export/pdf/', views.export_products_pdf, name='export_products_pdf'),
]
