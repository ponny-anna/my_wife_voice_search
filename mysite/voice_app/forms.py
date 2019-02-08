from django import forms
from .models import VoiceActor

class VoiceActorForm(forms.ModelForm):

    class Meta:
        model = VoiceActor
        fields = "__all__"#['name', 'age', 'sex', 'birthday', 'image']