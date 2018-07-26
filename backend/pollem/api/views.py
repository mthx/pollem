from django.db.models import F
from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
import logging

from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer


logger = logging.getLogger(__name__)


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all().order_by('-id')
    serializer_class = PollSerializer

    @action(methods=['post'], detail=True, permission_classes=[AllowAny])
    def vote(self, request: Request, pk=None):
        choice_id = request.data['choice']
        
        if choice_id:
            logger.info('Got {}'.format(choice_id))
            updated = Choice.objects.filter(pk=choice_id).update(votes=F('votes') + 1)
            if updated:
                return self.retrieve(pk);
        return Response(status=status.HTTP_400_BAD_REQUEST)
            

