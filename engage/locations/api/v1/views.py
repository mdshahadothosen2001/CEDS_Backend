import json
import os 

from rest_framework.views import APIView
from rest_framework.response import Response

from engage.locations.api.v1.serializers import DivisionCreateSerializer, DistrictCreateSerializer, UpazilaCreateSerializer, UnionCreateSerializer


class DivisionCreateView(APIView):
    serializer_class = DivisionCreateSerializer

    def post(self, request):
        file_path = request.data.get('file_path')
        if not file_path:
            return Response('file_path path is required.')
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_data = json.load(file)
        except:
            return Response('bad request. {file_path}')
        division_data = []
        for item in file_data:
            fields = item.get('fields')
            name = fields[0].get('name')
            division_data.append(
                {
                    "id": item.get('pk'),
                    'name': name
                }
            )

        serializer = self.serializer_class(data=division_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class DistrictCreateView(APIView):
    serializer_class = DistrictCreateSerializer

    def post(self, request):
        file_path = request.data.get('file_path')
        if not file_path:
            return Response('file_path path is required.')
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_data = json.load(file)
        except:
            return Response('bad request. {file_path}')
        district_data = []
        for item in file_data:
            fields = item.get('fields')
            name = fields[0].get('name')
            district_data.append(
                {
                    "id": item.get('pk'),
                    'name': name,
                    'division': item.get('division_id')
                }
            )

        serializer = self.serializer_class(data=district_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class UpazilaCreateView(APIView):
    serializer_class = UpazilaCreateSerializer

    def post(self, request):
        file_path = request.data.get('file_path')
        if not file_path:
            return Response('file_path path is required.')
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_data = json.load(file)
        except:
            return Response('bad request. {file_path}')
        upazila_data = []
        for item in file_data:
            fields = item.get('fields')
            name = fields[0].get('name')
            upazila_data.append(
                {
                    "id": item.get('pk'),
                    'name': name,
                    'district': item.get('district_id')
                }
            )

        serializer = self.serializer_class(data=upazila_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class UnionCreateView(APIView):
    serializer_class = UnionCreateSerializer

    def post(self, request):
        file_path = request.data.get('file_path')
        if not file_path:
            return Response('file_path path is required.')
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_data = json.load(file)
        except:
            return Response('bad request. {file_path}')
        union_data = []
        for item in file_data:
            fields = item.get('fields')
            name = fields[0].get('name')
            union_data.append(
                {
                    "id": item.get('pk'),
                    'name': name,
                    'upazila': item.get('upazila_id')
                }
            )

        serializer = self.serializer_class(data=union_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
