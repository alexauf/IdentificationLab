from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from .views import GoogleSocialAuthView

urlpatterns = [
    path('', login_required(views.home), name='home'),
    path('login/', GoogleSocialAuthView.as_view(), name='login'),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
