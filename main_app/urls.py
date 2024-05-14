from django.contrib import admin
# Add the include function to the import
from django.urls import path, include
from .views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    # '' represents the "starts with" path
    path('', include('main_app.urls'))
]
