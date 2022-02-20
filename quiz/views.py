from rest_framework import generics
from rest_framework.response import Response
from .models import Quizzes, Question
from .serializers import QuizSerializer, RandomQuestionSerializer, QuestionSerializer
from rest_framework.views import APIView


class StartQuiz(APIView):
    def get(self, request, **kwargs):
        quiz = Quizzes.objects.filter(category__name=kwargs['title'])
        serializer = QuizSerializer(quiz, many=True)
        return Response(serializer.data)


class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()

    def list(self, request, *arg, **kwargs):
        queryset = Quizzes.objects.all()
        response = []
        for idx, quiz in enumerate(queryset):
            response.append({
                'title': quiz.title,
                'questions_count': len(quiz.question.all())
            })
        return Response(response)

class RandomQuestionTopic(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuizQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)