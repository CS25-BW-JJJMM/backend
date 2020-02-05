from django.contrib import admin
from django.urls import path, include,re_path
from django.conf.urls import include
from rest_framework import routers
from adventure.api import RoomViewSet,initialize
from adventure.urls import *
from api.urls import *
from django.views.generic import TemplateView
#from api.views import ChatView
from rest_framework.authtoken import views
from graphene_django.views import GraphQLView
router = routers.DefaultRouter()
router.register(r'rooms', RoomViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
 #   path('api/chat/' ,include(router.urls)),
    path('api/rooms/', include(router.urls)),
    path('api/adv/', include('adventure.urls')),
    re_path(r'^api-token-auth/', views.obtain_auth_token),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger_ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    
]
