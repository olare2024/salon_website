from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from appointments.views import (
    home, appointment, contact, services, book, success, search
)
from accounts.views import (
    LoginUser, RegisterUser, logout_view, ActivateAccount, DashboardView, PasswordChangeView
)
from payment.views import payhome, paycancel, payreturn, stripesuccess, checkout, stripecheckout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('appointment', appointment, name='appointment'),
    path('contact', contact, name='contact'),
    path('service', services, name='services'),
    path('activate/<uidb64>/<token>/<status>', ActivateAccount.as_view(), name='activate'),
    path('logout', logout_view, name='logout'),
    path('login', LoginUser.as_view(), name='login'),  # Modify here
    path('register', RegisterUser.as_view(), name='register'),  # Modify here
    path('password', PasswordChangeView.as_view(), name='password'),  # Modify here
    path('checkout', checkout, name='checkout'),
    path('paymenthome', payhome, name='payment_home'),
    path('paymentreturn', payreturn),
    path('paymentcancel', paycancel),
    path('hardurl', include('paypal.standard.ipn.urls')),
    path('booking', book, name='book'),
    path('search', search, name='search'),
    path('success', success, name='success'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),  # Modify here
    path('stripecheckout', stripecheckout, name='stripe_checkout'),
    path('stripesuccess', stripesuccess, name='stripe_success'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
