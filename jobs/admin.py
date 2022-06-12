from jobs.serializers import SliderSerializer
from django.contrib import admin
from .models import  Slider,ProjectDetail, Index, Services, About, AboutBackgroundImage



class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'services_image',
                
                    ]



class AboutBackgroundImageAdmin(admin.ModelAdmin):
    list_display = ['id','image_bg_about',
                   
                    ]


class AboutAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'text_about',
                    'vission',
                    'letter',
                    'history_text',
                
                 'text_about_ar',
                    'vission_ar',
                    'letter_ar',
                    'history_text_ar',
                    'image_middle_about',
                

                    ]




class SliderAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'slide_image_index',
                    'slide_title_index',
                    'slide_subtitle_index',
                     'slide_title_index_ar',
                    'slide_subtitle_index_ar',

                    ]


class IndexAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'text_about_index',
                     'text_about_index_ar',
                    'text_project_index',
                    'text_project_index_ar',
                    ]


              
class ProjectDetailAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'project_image_one',
                   

                    'project_date',
                
                    'project_desc1',
                    'project_desc2',
                 
                    'project_desc1_ar',
                    'project_desc2_ar',
                   
                    ]



admin.site.register(ProjectDetail, ProjectDetailAdmin)
admin.site.register(AboutBackgroundImage, AboutBackgroundImageAdmin)


admin.site.register(Index, IndexAdmin)
admin.site.register(Slider, SliderAdmin)

admin.site.register(Services, ServicesAdmin)

admin.site.register(About, AboutAdmin)
