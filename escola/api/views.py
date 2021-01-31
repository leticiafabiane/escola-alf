from api.models import Aluno, Gabarito, Prova
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import AlunoSerializer, GabaritoSerializer, ProvaSerializer
from rest_framework import status

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all().order_by('-nome')
    serializer_class = AlunoSerializer
    permission_classes = [permissions.IsAuthenticated]

class GabaritoViewSet(viewsets.ModelViewSet):
    queryset = Gabarito.objects.all().order_by('-id')
    serializer_class = GabaritoSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProvaViewSet(viewsets.ModelViewSet):
    queryset = Prova.objects.all().order_by('-id')
    serializer_class = ProvaSerializer
    permission_classes = [permissions.IsAuthenticated]

class AprovacaoView(viewsets.ModelViewSet):
    queryset = Aluno.objects.filter(media__gte='7')
    serializer_class = AlunoSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']

