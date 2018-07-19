from .models import Poll, Choice
from rest_framework import viewsets
from .serializers import PollSerializer, ChoiceSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all().order_by('-id')
    serializer_class = PollSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer