import debug_toolbar
from django.contrib import admin
from django.urls import path , include , re_path
from core.routers import router
from containers import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("__debug__/", include("debug_toolbar.urls")),
    path('', include('frontend.urls')),
]

urlpatterns += [
    re_path('add_container/', views.add_container, name='add-container'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]