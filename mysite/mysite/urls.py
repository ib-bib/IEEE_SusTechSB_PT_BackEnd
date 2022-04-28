from django.contrib import admin
from django.urls import path, include  # Imported the include function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    # Used the include function here to route to polls
]
