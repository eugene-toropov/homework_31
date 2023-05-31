from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from ads.views.cat import root
from homework_27 import settings

urlpatterns = [
    path('', root),
    path('admin/', admin.site.urls),
    path('cat/', include('ads.urls.cat')),
    path('ad/', include('ads.urls.ad')),
    path('user/', include('users.urls.user')),
    path('location/', include('users.urls.location')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('selection', include('ads.urls.selection')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
