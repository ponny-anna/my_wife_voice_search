from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from django.urls import reverse_lazy

from .models import Property, VoiceActor, SampleVoice
from .forms import VoiceActorForm

class Index(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['propertys'] = Property.objects.all()

        return ctx


class VoiceList(ListView):

    context_object_name = 'voices'
    template_name = "voice_list.html"

    def get_queryset(self):
        queryset = SampleVoice.objects.select_related('property_name').filter(property_name_id=self.kwargs.get('pk')).select_related('voice_actor')
        return queryset


class VoiceActorDetail(DetailView):

    model = VoiceActor
    context_object_name = 'voice_actor'
    template_name = "voice_actor_detail.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['voice_list'] = SampleVoice.objects.filter(voice_actor_id=self.kwargs.get('pk')).select_related('property_name')

        return ctx


class VoiceActoreCreate(CreateView):

    model = VoiceActor
    form_class = VoiceActorForm
    template_name = "voice_actor_create.html"
    success_url = reverse_lazy('index')
