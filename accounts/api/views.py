from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.api.serializers import CustomAccountDisplaySerializer

class CurrentAccountAPIView(APIView):

    def get(self, request):
        serializer = CustomAccountDisplaySerializer(request.user)
        return Response(serializer.data)