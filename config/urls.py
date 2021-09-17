from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from member.views import *


urlpatterns = [
    path('', HotListView.as_view(), name='home'),
    path('jet/', include('jet.urls','jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('member/', include('member.urls')),
    path('product/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('accounts/', include('allauth.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# admin.sites.AdminSite.site_header = 'SHOP3 관리'
# admin.sites.AdminSite.site_title = 'SHOP3 관리'
# admin.sites.AdminSite.index_title = 'SHOP3 관리 HOME'   