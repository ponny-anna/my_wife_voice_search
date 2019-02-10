from django.urls import path
from .views import Index, VoiceActorDetail, VoiceList, VoiceActoreCreate, SampleVoiceCreate, PropertyCreate

urlpatterns = [
    # TOP Page
    path('', Index.as_view(), name='index'),
    # 声優詳細
    path('actor/<int:pk>/', VoiceActorDetail.as_view(), name='actor_detail'),
    # 音声リスト
    path('voice/<int:pk>/', VoiceList.as_view(), name='voice_list'),
    # 声優Form
    path('acotr/create/', VoiceActoreCreate.as_view(), name='actor_create'),
    # 音声Form
    path('voice/create/', SampleVoiceCreate.as_view(), name='voice_create'),
    # プロパティForm
    path('property/create/', PropertyCreate.as_view(), name='property_create'),
]