from rest_framework import serializers
from .models import  Replay, Slider,ProjectDetail, AboutBackgroundImage, Index, Services, About
from django.core.mail import send_mail



class ProjectDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectDetail
        fields = '__all__'
        ordering = ['-project_date']



class AboutBackgroundImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutBackgroundImage
        fields = '__all__'





class ServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = '__all__'



class ReplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Replay
        fields = '__all__'

class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = '__all__'




class IndexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Index
        fields = '__all__'


class SliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slider
        fields = '__all__'



