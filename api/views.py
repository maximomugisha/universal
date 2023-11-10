from rest_framework import viewsets, generics
from .serializers import *
from rest_framework import permissions
from rest_framework.permissions import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import status
class CustomForbidden(APIException):
    status_code = status.HTTP_404_NOT_FOUND

from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
# ViewSets define the view behavior.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [permissions.IsAuthenticated]


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillCategoryViewSet(viewsets.ModelViewSet):
    queryset = SkillCategory.objects.all()
    serializer_class = SkillCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class HobbyViewSet(viewsets.ModelViewSet):
    queryset = Hobby.objects.all()
    serializer_class = HobbySerializer
    permission_classes = [permissions.IsAuthenticated]


class HobbyCategoryViewSet(viewsets.ModelViewSet):
    queryset = HobbyCategory.objects.all()
    serializer_class = HobbyCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]


class BiographyViewSet(viewsets.ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


# Registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = [permissions.IsAuthenticated]



class UserDetailViewSet(viewsets.ModelViewSet):
    """
        API for (Viewing Only) User details.
        """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    http_method_names = ['get', 'head']
    permission_classes = [permissions.IsAuthenticated]


class NewUserDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Users to be created or edited with all their details.
    """
    queryset = User.objects.all().order_by('-id')  # descending order
    serializer_class = NewUserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class LoggedInUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(self.request.user)
        user = request.user
        uid = user.id
        try:
            return Response(serializer.data)
        except Exception:
            raise CustomForbidden
            # return Response({'Error': 'No Auth Token Received'})