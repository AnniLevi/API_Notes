from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


api_urls = [
    path('', include('api.urls')),
    path('auth/', include('rest_framework.urls', namespace='drf'), name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
    path('job-finder/', include('find_job.urls'))
]
