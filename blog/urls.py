from django.contrib import admin
from django.urls import path, include  # <-- include를 반드시 추가해야 합니다.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),    # <-- 기본 주소 접속 시 blog 앱으로 넘겨줍니다.
]