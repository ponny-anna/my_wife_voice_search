from django.contrib import admin
from .models import VoiceActor, SampleVoice, Property, SampleVoiceProperty

@admin.register(VoiceActor)
class VoiceActorAdmin(admin.ModelAdmin):
    pass


@admin.register(SampleVoice)
class SampleVoiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    pass

@admin.register(SampleVoiceProperty)
class SampleVoicePropertyAdmin(admin.ModelAdmin):
    pass

