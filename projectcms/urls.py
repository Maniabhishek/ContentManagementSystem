from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth import login, views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appcms.urls')),
    path('appuser/', include('appuser.urls')),
    path('logout/', auth_views.LogoutView.as_view(template_name='appuser/logout.html'),
         name='loggingout'),
    path('api/home/', include('appcms.api.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('api/user/', include('appuser.api.urls'))

]
# this is just for development purpose mot recommended in peoduction
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
