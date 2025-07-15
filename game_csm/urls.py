"""
URL configuration for game_csm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from rest_framework.routers import DefaultRouter
from players.urls import router as players_router
from quests.urls import router as quests_router
from core.urls import router as core_router
from items.urls import router as item_router
from core.views import RegisterApiView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


main_router = DefaultRouter()
main_router.registry.extend(players_router.registry)
main_router.registry.extend(quests_router.registry)
main_router.registry.extend(core_router.registry)
main_router.registry.extend(item_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(main_router.urls)),
    path('api/register', RegisterApiView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] 
