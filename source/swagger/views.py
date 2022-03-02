# pylint: disable=line-too-long
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    """
    This class for using both HTTP and Https in swagger
    reference: https://stackoverflow.com/a/68021739/7639845

    Another way is using url as comment bellow
    """

    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["https", "http"]  # https is default
        # schema.schemes = ["http", "https"]  # http is default
        return schema


SwaggerView = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    generator_class=BothHttpAndHttpsSchemaGenerator,
    # url='https://example.net/api/v1/', # Base URL, reference: https://stackoverflow.com/a/56090744/7639845
    public=True,
    permission_classes=(permissions.AllowAny,),
)
