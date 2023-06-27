from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

from information.views import IndexView

static_urlpatterns = [

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('information/', include('information.urls', namespace='information')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('cosmicstore/', include('store.urls', namespace='cosmostore')),
    path('users/', include('users.urls', namespace='users')),
    path('accounts/', include('allauth.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
