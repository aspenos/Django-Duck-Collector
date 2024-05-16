from django.contrib import admin
# Add the include function to the import
from django.urls import path, include
from .views import Home, DuckList, DuckDetail, FeedingListCreate, FeedingDetail, PondList, PondDetail, AddPondToDuck,CreateUserView, LoginView, VerifyUserView #additional imports

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    # '' represents the "starts with" path
    path('ducks/', DuckList.as_view(), name='duck_list'),
    path('ducks/<int:id>/', DuckDetail.as_view(), name='duck_detail'),
    path('ducks/<int:duck_id>/feedings/', FeedingListCreate.as_view(), name='feeding-list-create'),
	  path('ducks/<int:duck_id>/feedings/<int:id>/', FeedingDetail.as_view(), name='feeding-detail'),
    path('ponds/', PondList.as_view(), name='pond-list'),
    path('ponds/<int:id>/', PondDetail.as_view(), name='pond-detail'),
    path('ducks/<int:duck>/pond/<int:pond_id>/', AddPondToDuck.as_view(), name='add-pond-to-duck'),

]
