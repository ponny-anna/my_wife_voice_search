from django.contrib import admin
from .models import VoiceActor, SampleVoice, Property

@admin.register(VoiceActor)
class VoiceActorAdmin(admin.ModelAdmin):
    pass


@admin.register(SampleVoice)
class SampleVoiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    pass
