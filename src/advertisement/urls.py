from django.urls import path, include


app_name = "api"

urlpatterns = [
    path('api/', include('advertisement.api.urls')),
]
