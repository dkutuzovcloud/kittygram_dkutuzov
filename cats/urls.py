from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CatViewSet, CategoryViewSet, UserCreateView

router = SimpleRouter()
router.register('cats', CatViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [  # ← ОБЯЗАТЕЛЬНО эта строка!
    path('api/', include(router.urls)),
    path('api/auth/users/', UserCreateView.as_view(), name='create_user'),
    path('api/auth/jwt/create/', TokenObtainPairView.as_view(), name='token_create'),
    path('api/auth/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]