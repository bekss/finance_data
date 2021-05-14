from django.urls import path
from .views import ContentView, Detail, Json
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', ContentView.as_view(), name='content'),
    path('detail', Detail.as_view(), name='detail'),
    path('json/<slug:slug>/', Json.as_view(), name='json_company'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
