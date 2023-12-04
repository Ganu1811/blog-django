from django.urls import path

from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('article/<int:pk>', views.article, name = 'get_article'),
    path('author/<int:pk>', views.author, name = 'get_author'),
    path('article', views.create_article, name='create_article'),
    path('article/<int:pk>/delete/', views.delete_article, name='delete_article'),
    path('login', views.login_request, name='login'),
    path('logout',views.logout_request, name='logout'),
    path("register", views.register_request, name='register'),
    path("allarticles", views.all_articles, name='allarticles'),
    path('profile', views.profile, name = 'profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
