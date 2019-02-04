from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from .models import Property, VoiceActor, SampleVoice

class Index(TemplateView):
    
    template_name = "index.html"


class VoiceActorDetail(DetailView):

    model = VoiceActor
    template_name = "voice_actor_detail.html"

class VoiceList(ListView):

    model = SampleVoice
    template_name = "voice_list.html"