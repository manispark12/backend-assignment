from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from .views import FAQListView

urlpatterns = [
    # Your existing FAQ endpoint
    path('faqs/', FAQListView.as_view(), name='faq-list'),

    # Schema and documentation views
    path('schema/', SpectacularAPIView.as_view(), name='schema'),  # Generates OpenAPI schema
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Swagger UI
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc-ui'),  # ReDoc UI
]
