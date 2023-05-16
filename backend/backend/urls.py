from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from information.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('information/', include('information.urls', namespace='information')),
    path('blog/', include('blog.urls', namespace='blog')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)