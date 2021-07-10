from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from crm.views import start_page, services_page, booking_page, masters_page, login_page,\
                      register_page, logout_user, account_page

urlpatterns = [
    path('admin', admin.site.urls),
    path('', start_page, name='start'),
    path('services', services_page, name='services'),
    path('booking', booking_page, name='booking'),
    path('masters', masters_page, name='masters'),
    path('login', login_page, name='login'),
    path('logout', logout_user, name='logout'),
    path('register', register_page, name='register'),
    path('account', account_page, name='account')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
