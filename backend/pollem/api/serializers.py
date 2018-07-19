from rest_framework import serializers
from .models import Poll, Choice


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ('choice_text', 'votes')


class PollSerializer(serializers.HyperlinkedModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    depth = 2
    class Meta:
        model = Poll
        fields = ('question_text', 'choices')
