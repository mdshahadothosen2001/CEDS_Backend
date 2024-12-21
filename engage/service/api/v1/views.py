from django.shortcuts import get_list_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from engage.service.api.v1.serializers import ServiceSerializer
from engage.service.models import Service


class ServiceListView(APIView):
    def get(self, request):
        localgovt_id = request.query_params.get('localgovt_id')
        if localgovt_id:
            services = get_list_or_404(Service, localgovt__id=localgovt_id)
            serializer = ServiceSerializer(services, many=True)

            data = {
                "success": True,
                "message": "Service list retrieved successfully.",
                "data": serializer.data
            }
            return Response(data)
        
        data = {
                "success": False,
                "message": "Service list can't retrieved successfully.",
                "data": []
            }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
