from django.urls import path

from engage.locations.api.v1.views import DivisionCreateView, DistrictCreateView, UpazilaCreateView, UnionCreateView


urlpatterns = [
    path('division-create/', DivisionCreateView.as_view(), name='division_create'),
    path('district-create/', DistrictCreateView.as_view(), name='district_create'),
    path('upazila-create/', UpazilaCreateView.as_view(), name='upazila_create'),
    path('union-create/', UnionCreateView.as_view(), name='union_create'),
]