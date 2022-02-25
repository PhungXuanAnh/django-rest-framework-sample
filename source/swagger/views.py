# pylint: disable=line-too-long
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

SwaggerView = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
      # url='https://example.net/api/v1/', # Base URL, reference: https://stackoverflow.com/a/56090744/7639845
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
