from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('name/', views.name, name='name'),
    path('my_form/', views.my_form, name='my_form'),
    path('index_app1/', views.index_app1, name='index_app1'),
    path('my_form/edit_form/<int:id>/', views.edit_form, name='edit_form'),
    path('my_form/delete/<int:id>/', views.delete, name='delete'),
    path('form_up_image/', views.form_up_image, name='form_up_image'),
    path('form_up_pdf/', views.form_up_pdf, name='form_up_pdf'),
    path('form_up_pdf/delete_pdf/<int:id>/', views.delete_pdf, name='delete_pdf'),
    path('form_up_image/delete_img/<int:id>/', views.delete_img, name='delete_img'),
    path('form_up_video', views.form_up_video, name='form_up_video'),
    path('form_up_video/delete_video/<int:id>/', views.delete_video, name='delete_video'),
    path('form_up_audio/', views.form_up_audio, name='form_up_audio'),
    path('form_up_audio/delete_audio/<int:id>/', views.delete_audio, name='delete_audio'),
    path('contact/', TemplateView.as_view(template_name='firstapp/contact.html',
                                          extra_context={
                                              'work': 'Разработка программных продуктов'
                                          }
                                          )),
    re_path(r'^contact/', views.contact, name='contact'),
    path('', views.index, name='index'),
    re_path(r'^about/', views.about, name='about'),
    #re_path(r'^product/(?P<product_id>\d+)/', views.product, name='product'),
    re_path(r'^products/$', views.products, name='products'),  # Маршрут по умолчанию
    path('products/<int:product_id>/', views.products, name='products'),
    path('products/', views.products, name='products'),  # Маршрут по умолчанию
    #re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users, name='users'),
    path('users/<int:id>/<name>/', views.users, name='users'),
    path('users/', views.users, name='users'),  # Маршрут по умолчанию
    path('details/', views.details, name='details'),
    path('access/<int:age>/', views.access, name='access'),
    path('home/', views.home, name='home')

]