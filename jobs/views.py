from email.message import EmailMessage
from django.shortcuts import redirect, render
from django.http import HttpResponse
from rest_framework import generics, permissions
from .models import  Replay, Slider, ProjectDetail, Index, Services, About
from .serializers import  ReplaySerializer, SliderSerializer, IndexSerializer, AboutBackgroundImage, ServicesSerializer, AboutSerializer
from django.http import HttpRequest
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .filters import projectDetailFilter
from django.core.paginator import Paginator
from django.utils.translation import get_language, activate

from django.core.mail import send_mail,  EmailMessage

def reply(request):
    """Renders the create replay page."""
    assert isinstance(request, HttpRequest)
    queryset = Replay.objects.all()
    serializer_class = ReplaySerializer(queryset, many=True)

    return render(request, 'reply.html',
                  {
                      'data': serializer_class.data,
                  }
                  )

def index(request):
    assert isinstance(request, HttpRequest)
    queryset = Index.objects.all()
    serializer_class = IndexSerializer(queryset, many=True)

    projects = ProjectDetail.objects.all()

    # Show many contacts per page for stories
    paginator_story = Paginator(projects, 10000000000000000)
    page_number_story = request.GET.get('page')
    page_obj_story = paginator_story.get_page(page_number_story)

    # Show many contacts per page for what we are doing
    page_number = request.GET.get('page')
    slider_show = Slider.objects.all()[:4]
    context = {
        'data': serializer_class.data,
        'slider_show': slider_show,
        'project': page_obj_story,
    }
    return render(request, 'index.html', context)



def services(request):
    """Renders the create volunteer page."""
    assert isinstance(request, HttpRequest)
    queryset = Services.objects.all()
    about_image_bg = AboutBackgroundImage.objects.all()

    serializer_class = ServicesSerializer(queryset, many=True)

    return render(request, 'services.html',
                  {
                      'data': serializer_class.data,
                      'about_image_bg' : about_image_bg,
                  }
                  )


def contact(request):
    about_image_bg = AboutBackgroundImage.objects.all()

    if request.method == 'POST':
        print("hello")
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        data = {
            'name': name,
            'email' : email,
            'message' : message,
        }
        print(data)
      
        message = ''' 
        New message :{}
        From: {}
        '''.format(data['message'], data['email'])

        if name and message and email:
            try:
                send_mail(data['name'], message, from_email= 'info@ashuor.org',recipient_list= ['contact@ashuor.org'],  fail_silently=False)

            except  Exception as error:
                print("error")
                print(error)
                return HttpResponse('Invalid header found.')
    return render(request, 'contact.html',
    {
                      'about_image_bg' : about_image_bg,
                  })


def translate(language):
    cur_language = get_language()
    try:
        activate(language)
    finally:
        activate(cur_language)






def about(request):
    """Renders the create about page."""
    assert isinstance(request, HttpRequest)
    queryset = About.objects.all()
    serializer_class = AboutSerializer(queryset, many=True)
    about_image_bg = AboutBackgroundImage.objects.all()

    return render(request, 'about.html',
                  {
                      'data': serializer_class.data,
                      'about_image_bg' : about_image_bg
                  }
                  )





def projects_list(request):

    stories = ProjectDetail.objects.all().order_by('-project_date')
    # filters
    myfilter = projectDetailFilter(request.GET, queryset=stories)
    stories = myfilter.qs
    about_image_bg = AboutBackgroundImage.objects.all()

    # Show many contacts per page.
    paginator = Paginator(stories, 10000000000000000)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if stories:
        context = {'project': page_obj, 'myfilter': myfilter,'about_image_bg':about_image_bg
      }  # template name

    else:
        context = {'message': "There are no stories available at the moment."}
    return render(request, 'projects.html', context)


def projects_detail(request, id):
    """Renders the create volunteer page."""
    stories = ProjectDetail.objects.get(id=id)
    about_image_bg = AboutBackgroundImage.objects.all()

    context = {'project': stories, 'about_image_bg':about_image_bg}
    return render(request, 'projects_detail.html', context)

