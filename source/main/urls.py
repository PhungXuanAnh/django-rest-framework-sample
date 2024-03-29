"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from swagger.views import SwaggerView
import debug_toolbar

api_v1_urls = [
    path("api/v1/", include("music.urls")),
    path("api/v1/", include("user.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("swagger/", SwaggerView.with_ui("swagger", cache_timeout=0)),
]

urlpatterns += api_v1_urls
# pylint: disable=line-too-long
urlpatterns += static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)  # Reference: https://docs.djangoproject.com/en/4.0/howto/static-files/#serving-static-files-during-development


urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
