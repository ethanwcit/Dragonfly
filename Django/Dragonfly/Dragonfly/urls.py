from django.contrib import admin
from django.urls import path, include
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
app_name = "Dragonfly"
urlpatterns = [
    path('admin/', admin.site.urls, name="adminpage"),
    path('',include('accounts.urls')),
    path('studenthomepage',views.studenthomepage, name="studenthomepage"),
    path('parenthomepage',views.parenthomepage, name="parenthomepage"),
    path('teacherhomepage',views.teacherhomepage, name="teacherhomepage"),
    path('tasks/', include('tasks.urls')),
]

#allows django to know where files are stored
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
