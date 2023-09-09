from django.contrib import admin
from django.urls import path, include
from . import views
from . import settings
from django.conf.urls.static import static


#url routing
urlpatterns = [
    path('server/admin/', admin.site.urls),
    path('server/team/', views.teamData),
    path('server/team/<str:year>', views.teamDataByYear),
    path('', include('Events.urls')),
    path('', include('Speakers.urls')),
    path('', include('ProblemStatements.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)