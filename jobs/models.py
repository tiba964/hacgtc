from django.db import models
from .validators import validate_file_extension, validate_image_extension
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from datetime import date




class Services(models.Model):
    services_image = models.FileField(
        validators=[validate_image_extension], upload_to='background/services/', blank=True, )
class AboutBackgroundImage(models.Model):
    image_bg_about = models.FileField(
        validators=[validate_image_extension], upload_to='background/services/', blank=True, )


class Replay(models.Model):
    image_bg_volunteer = models.FileField(
        validators=[validate_image_extension], upload_to='background/volunteer/', )



class About(models.Model):
    image_middle_about = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/',blank=True, null=True )
    text_about = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_about_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    vission = models.TextField(
        max_length=1000, default='',  blank=True,)
    vission_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    letter = models.TextField(
        max_length=1000, default='',  blank=True,)
    letter_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    history_text = models.TextField(
        max_length=1000, default='',  blank=True,)
    history_text_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
 




class ProjectDetail(models.Model):
    
    project_image_one = models.FileField(
        validators=[validate_image_extension], default='',upload_to='background/stories_detail/', blank=True)
    
    project_date = models.DateField(default=date.today, blank=True)
    project_desc1 = models.CharField(
        max_length=120, default='', blank=True)
    project_desc2 = models.TextField(
        max_length=1000, default='', blank=True)
   
    project_desc1_ar = models.CharField(
        max_length=120, default='', blank=True)
    project_desc2_ar = models.TextField(
        max_length=1000, default='', blank=True)
   
    
    class Meta:
        ordering = ['-project_date']

   
class Slider(models.Model):
    slide_image_index = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', blank=True, )
    slide_title_index = models.CharField(
        max_length=300, default='', blank=True, )
    slide_title_index_ar = models.CharField(
        max_length=300, default='', blank=True, )
    slide_subtitle_index = models.CharField(
        max_length=300, default='', blank=True, )
    slide_subtitle_index_ar = models.CharField(
        max_length=300, default='', blank=True, )


  
   
class Index(models.Model):
   
    text_about_index = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_about_index_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_project_index = models.TextField(
        max_length=1000, default='', blank=True, )
    text_project_index_ar = models.TextField(
        max_length=1000, default='', blank=True, )
 


