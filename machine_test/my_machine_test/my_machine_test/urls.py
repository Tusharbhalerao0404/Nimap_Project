'''from django.contrib import admin
from django.urls import path , include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('my_machine_test_project.urls')),
]'''
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Add a simple view for the root URL
def home(request):
    return HttpResponse("Welcome to the API!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('my_machine_test_project.urls')),  # API URLs
    path('', home),  # Root URL, shows a welcome message
]
