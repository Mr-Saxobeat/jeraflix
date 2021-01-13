from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.api.serializers import CustomAccountDisplaySerializer, ProfileSerializer
from accounts.models import Profile

class CurrentAccountAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CustomAccountDisplaySerializer(request.user)
        return Response(serializer.data)


class ListCreateProfileView(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_profile_id = self.request.session['current-profile']
        current_profile = Profile.objects.get(pk=current_profile_id)
        current_account = current_profile.account
        all_profiles = current_account.profiles.all().order_by('name')
        return all_profiles

    def perform_create(self, serializer):
        account = self.request.user
        serializer.save(account=account)


class RestrieveProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


