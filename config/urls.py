"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import UserModelViewSet
from projects.views import ProjectModelViewSet
from issues.views import IssueModelViewSet
from comments.views import CommentModelViewSet
from contributors.views import ContributorModelViewSet

router = routers.SimpleRouter()
router.register('user', UserModelViewSet, basename='user')
router.register('project', ProjectModelViewSet, basename='project')
router.register('issue', IssueModelViewSet, basename='issue')
router.register('comment', CommentModelViewSet, basename='comment')
router.register('contributor', ContributorModelViewSet, basename='contributor')
#router.register('admin/', admin.site.urls)
#router.register('auth/', include('rest_framework.urls'))
#router.register('account/', include('rest_registration.api.urls'))
#router.register('token/', TokenObtainPairView.as_view(), name='obtain_tokens')
#router.register('token/refresh/', TokenRefreshView.as_view(), name='refresh_token')

urlpatterns = [
    path('api/admin/', admin.site.urls),
    #path('api/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/account/', include('rest_registration.api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('api/', include(router.urls))
]
