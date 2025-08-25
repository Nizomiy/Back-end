from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LinksModelViewSet, NewsModelViewSet, FooterModelViewSet, NewsLinkModelViewSet

router = DefaultRouter()
router.register(r'links', LinksModelViewSet, basename='links')
router.register(r'news', NewsModelViewSet, basename='news')
router.register(r'footer', FooterModelViewSet, basename='footer')
router.register(r'news-links', NewsLinkModelViewSet, basename='news-links')

urlpatterns = [
    path('', include(router.urls)),
]
