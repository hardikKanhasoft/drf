"""
URL configuration for mypro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from apps.common.swagger import schema_view
from django.urls import re_path, include


api_v1_urls = [
    re_path("app1/", include(("apps.app1.api_v1.urls", "app1"), namespace="app1")),
    re_path("app2/", include(("apps.app2.api_v1.urls", "app2"), namespace="app2")),
    re_path("crud2_using_APIView/", include(("apps.crud2_using_APIView.api_v1.urls", "crud2_using_APIView"), namespace="crud2_using_APIView")),
    re_path("crud3_using_genetic_api_vew_and_mixins/", include(("apps.crud3_using_genetic_api_vew_and_mixins.api_v1.urls", "crud3_using_genetic_api_vew_and_mixins"), namespace="crud3_using_genetic_api_vew_and_mixins")),
    re_path("crud4_using_concrete_views/", include(("apps.crud4_using_concrete_views.api_v1.urls", "crud4_using_concrete_views"), namespace="crud4_using_concrete_views")),
    re_path("crud5_using_viewsets/", include(("apps.crud5_using_viewsets.api_v1.urls", "crud5_using_viewsets"), namespace="crud5_using_viewsets")),
    re_path("crud6_using_model_viewsets/", include(("apps.crud6_using_model_viewsets.api_v1.urls", "crud6_using_model_viewsets"), namespace="crud6_using_model_viewsets")),
    re_path("crud7_using_serializers/", include(("apps.crud7_using_serializers.api_v1.urls", "crud7_using_serializers"), namespace="crud7_using_serializers")),
    re_path("accounts/", include(("apps.accounts.api_v1.urls", "accounts"), namespace="accounts")),

]
urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path("api/v1/", include(api_v1_urls)),
]
