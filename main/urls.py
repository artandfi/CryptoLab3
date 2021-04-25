from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'
urlpatterns = [
    path(
        '',
        views.home,
        name="home"
    ),
    path(
        'send_message',
        views.SendMessageView.as_view(),
        name='send_message'
    ),
    path(
        'signup/',
        views.signup,
        name='signup'
    )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)