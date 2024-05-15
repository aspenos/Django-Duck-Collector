from django.contrib import admin
# Add the include function to the import
from django.urls import path, include
from .views import Home, DuckList, DuckDetail #additional imports

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    # '' represents the "starts with" path
    path('ducks/', DuckList.as_view(), name='duck_list'),
    path('ducks/<int:id>/', DuckDetail.as_view(), name='duck_detail'),
]
