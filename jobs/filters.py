import django_filters
from .models import ProjectDetail


class projectDetailFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = ProjectDetail
        fields = '__all__'
        exclude = ['project_image_one',
                

                  
                   'image_bg_project',
                   'id'
                   ]
