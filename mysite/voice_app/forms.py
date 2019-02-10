from django import forms
from .models import VoiceActor, SampleVoice, Property

class VoiceActorForm(forms.ModelForm):

    class Meta:
        model = VoiceActor
        fields = "__all__"#['name', 'age', 'sex', 'birthday', 'image']
    
class SampleVoiceForm(forms.ModelForm):

    class Meta:
        model = SampleVoice
        fields = "__all__"

class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = "__all__"