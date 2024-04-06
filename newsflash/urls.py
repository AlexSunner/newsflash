from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("contact/", include("contact.urls"), name="contact-urls"),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("", include("hello_news.urls"), name="hello_news-urls"),
]
