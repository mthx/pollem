from rest_framework import serializers
from .models import Poll, Choice


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'choice_text', 'votes')


class PollSerializer(serializers.HyperlinkedModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    depth = 2
    class Meta:
        model = Poll
        fields = ('id', 'question_text', 'choices')
