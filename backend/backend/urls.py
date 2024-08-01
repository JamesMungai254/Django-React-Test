
from django.contrib import admin
from django.urls import path,include
import rest_framework.urls
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView




urlpatterns = [
    path('admin/', admin.site.urls),
    #calls the view created to create a new user
    path('api/user/register/',CreateUserView.as_view(),name='register'),
    path('api/token/',TokenObtainPairView.as_view(),name='getToken'),
    path('api/token/refresh',TokenRefreshView.as_view(),name='refresh'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/',include('api.urls'))
]
