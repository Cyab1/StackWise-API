from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.http import JsonResponse
from django.utils import timezone

from contacts.views import ContactCreateView, ContactListView, ContactUpdateView
from testimonials.views import TestimonialCreateView, TestimonialUpdateView

START_TIME = timezone.now()

def health_check(request):
    uptime = (timezone.now() - START_TIME).total_seconds()
    return JsonResponse({
        'status': 'ok',
        'version': '1.0.0',
        'uptime_seconds': uptime,
    })

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/projects/', include('projects.urls')),
    path('api/testimonials/', include('testimonials.urls')),
    path('api/services/', include('services.urls')),
    path('api/contact/', ContactCreateView.as_view(), name='contact-create'),
    path('api/health/', health_check, name='health-check'),

    # Auth
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Admin (JWT protected)
    path('api/admin/contacts/', ContactListView.as_view(), name='admin-contacts-list'),
    path('api/admin/contacts/<int:pk>/', ContactUpdateView.as_view(), name='admin-contacts-update'),
    path('api/admin/testimonials/', TestimonialCreateView.as_view(), name='admin-testimonials-create'),
    path('api/admin/testimonials/<int:pk>/', TestimonialUpdateView.as_view(), name='admin-testimonials-update'),

    # Docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]