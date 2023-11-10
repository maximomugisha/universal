from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter
from django.urls import include, path
from .views import *

from api.swagger import swagger_schema_view  # use your own import path

# Routers provide an easy way of automatically determining the URL conf.
router: ExtendedSimpleRouter = ExtendedSimpleRouter()
users_router = router.register('users', UserViewSet, basename='users')
users_router.register('profile', ProfileViewSet, basename='profile',
                         parents_query_lookups=['officer__id'])
users_router.register('contacts', ContactViewSet, basename='contacts',
                         parents_query_lookups=['officer__id'])
users_router.register('biographies', BiographyViewSet, basename='biographies',
                         parents_query_lookups=['officer__id'])
users_router.register('hobbies', HobbyViewSet, basename='hobbies',
                         parents_query_lookups=['officer__id'])
users_router.register('skills', SkillViewSet, basename='skills',
                         parents_query_lookups=['officer__id'])
users_router.register('works', WorkViewSet, basename='works',
                         parents_query_lookups=['officer__id'])


router2 = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'profiles', ProfileViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'biographies', BiographyViewSet)
router.register(r'hobbies', HobbyViewSet)
router.register(r'hobby_categories', HobbyCategoryViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'works', WorkViewSet)
router.register(r'skill_categories', SkillCategoryViewSet)
router.register(r'full_user_details', UserDetailViewSet, basename='full_user_details')
router.register(r'user_details', NewUserDetailViewSet, basename='user_details')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('auth/', include('trench.urls')),
    path('auth/', include('trench.urls.jwt')),
    path('current_user/', LoggedInUserView.as_view()),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('swagger/', swagger_schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', swagger_schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
