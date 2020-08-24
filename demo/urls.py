from django.urls import path
from demo.views import Upload

app_name = 'demo'

urlpatterns = [
    path('', Upload.as_view(), name='upload'),
]