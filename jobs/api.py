# views

from .models import ProjectDetail
from .serializers import ProjectDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET'])
def projects_api(request):
    all_stories = ProjectDetail.objects.all()
    data = ProjectDetailSerializer(all_stories, many=True).data
    return Response({'data': data})


@api_view(['GET'])
def project_detail_api(request, id):
    story_detail_detail = ProjectDetail.objects.get(id=id)
    data = ProjectDetailSerializer(story_detail_detail).data
    return Response({'data': data})


class ProjectDetailListApi(generics.ListAPIView):
    queryset = ProjectDetail.objects.all()
    serializer_class = ProjectDetailSerializer


class ProjectDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectDetailSerializer
    queryset = ProjectDetail.objects.all()
    lookup_field = 'id'
