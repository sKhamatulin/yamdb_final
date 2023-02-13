from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from users.views import UserDetail, UserList, get_token_view, send_code_view

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('v1/auth/signup/', send_code_view),
    path('v1/auth/token/', get_token_view),
    path('v1/users/<str:username>/', UserDetail.as_view()),
    path('v1/users/', UserList.as_view()),
]
