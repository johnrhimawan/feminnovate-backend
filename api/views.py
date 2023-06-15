from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

# Create your views here.
# @api_view(['GET'])
# @permission_classes([AllowAny])
# def public(request):
#     return JsonResponse({'message': 'Hello from a public endpoint!'})

class PublicView(APIView):

    def get(self, request):
        return Response({
            '1': 'Never gonna give you up, never gonna let you down.',
            '2': 'Never gonna run around and desert you.',
            '3': 'Never gonna make you cry, never gonna say goodbye.',
            '4': 'Never gonna tell a lie and hurt you.'
        })
    