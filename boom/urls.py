from django.urls import path

from . import views


urlpatterns = [
    path("" , views.index, name='index'),

    path("pages/" , views.index, name='index'),

    path("producto/" , views.product, name='product'),
    path("info/" , views.info, name='info'),
    #path("info/" , views.info, name='product'),
  



  ] 

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
