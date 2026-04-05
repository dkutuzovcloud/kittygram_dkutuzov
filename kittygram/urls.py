from django.urls import path, include

from cats.views import CatList, CatDetail, CatViewSet

from cats.views import APICat
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('cats', CatViewSet)

urlpatterns = [
   # path('cats/', CatList.as_view()),
   #  path('cats/<int:pk>/', CatDetail.as_view()),
    path('', include(router.urls)),
]


