from django.urls import path
from .views import Quiz, RandomQuestionTopic, StartQuiz
from django.conf import settings
from django.conf.urls.static import static

app_name = 'quiz'

urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('r/<str:topic>/', RandomQuestionTopic.as_view(), name='RandomQuestionTopic'),
    path('single/<str:title>/', StartQuiz.as_view(), name='quiz'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
