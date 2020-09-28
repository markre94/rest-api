from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)
router.register('groups', views.GroupView)
router.register('programmers', views.ProgrammerView)


urlpatterns = [
    path('', include(router.urls))
]