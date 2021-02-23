from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('userapi.urls')),
    path('class/',include('classapi.urls')),
    path('query/',include('queryapi.urls')),
    #path('stream/',include('streamingapi.urls')),
]