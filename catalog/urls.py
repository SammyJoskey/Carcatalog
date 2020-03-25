from django.urls import path
from .views import CarList
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', CarList.as_view(), name='carcatalog')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)