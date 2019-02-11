from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from django.urls import reverse_lazy
from django.db.models import Prefetch

from .models import Property, VoiceActor, SampleVoice
from .forms import VoiceActorForm, SampleVoiceForm, PropertyForm

class Index(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['propertys'] = Property.objects.all()

        return ctx


class VoiceList(ListView):

    model = SampleVoice
    context_object_name = 'voices'
    template_name = "voice_list.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['voice_list']    = SampleVoice.objects.all().select_related('voice_actor').filter(property_name__pk=self.kwargs.get('pk'))
        sample_voice_id       = list(set([str(x.get('id')) for x in ctx['voice_list'].values('id')]))
        sample_voice_id       = ', '.join(sample_voice_id)
        ctx['property_list'] = Property.objects.raw('SELECT * FROM property AS p JOIN sample_voice_property_name AS s ON s.property_id = p.id WHERE s.samplevoice_id IN (%s)' % sample_voice_id)
        return ctx


class VoiceActorDetail(DetailView):

    model = VoiceActor
    context_object_name = 'voice_actor'
    template_name = "voice_actor_detail.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['voice_list'] = SampleVoice.objects.filter(voice_actor_id=self.kwargs.get('pk'))
        sample_voice_id       = list(set([str(x.get('id')) for x in ctx['voice_list'].values('id')]))
        sample_voice_id       = ', '.join(sample_voice_id)
        print(sample_voice_id)
        ctx['property_list'] = Property.objects.raw('SELECT * FROM property AS p JOIN sample_voice_property_name AS s ON s.property_id = p.id WHERE s.samplevoice_id IN (%s)' % sample_voice_id)

        return ctx


class VoiceActoreCreate(CreateView):

    model = VoiceActor
    form_class = VoiceActorForm
    template_name = "voice_actor_create.html"
    success_url = reverse_lazy('index')

class SampleVoiceCreate(CreateView):

    model = SampleVoice
    form_class = SampleVoiceForm
    template_name = "sample_voice_create.html"
    success_url = reverse_lazy('index')

class PropertyCreate(CreateView):

    model = Property
    form_class = PropertyForm
    template_name = "property_create.html"
    success_url = reverse_lazy('index')