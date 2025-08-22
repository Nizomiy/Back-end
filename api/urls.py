from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PagesViewSet, TitleViewSet, SectionsViewSet

router = DefaultRouter()
router.register(r'pages', PagesViewSet)
router.register(r'titles', TitleViewSet)
router.register(r'sections', SectionsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]