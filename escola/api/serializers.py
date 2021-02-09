from rest_framework import serializers
from api.models import Aluno, Gabarito, Prova

class AlunoSerializer(serializers.HyperlinkedModelSerializer):
    def validate(self, data):
        if Aluno.objects.all().count() == 100:
            raise serializers.ValidationError('Quantidade máxima de alunos excedida')
        return data
    class Meta:
        model = Aluno
        fields = ['nome', 'sobrenome', 'media']

class GabaritoSerializer(serializers.HyperlinkedModelSerializer):
    def validate(self, data):
        soma = data['peso_1'] + data['peso_2'] + data['peso_3'] + data['peso_4'] + data['peso_5']
        if soma > 10 or soma < 0:
            raise serializers.ValidationError('A nota total da prova deve ser maior que 0 e menor que 10')
        return data
    class Meta:
        model = Gabarito
        fields = ['questao_1', 'questao_2', 'questao_3', 'questao_4', 'questao_5', 'peso_1', 'peso_2', 'peso_3', 'peso_4', 'peso_5']

class ProvaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prova
        fields = ['questao_1', 'questao_2', 'questao_3', 'questao_4', 'questao_5', 'nota', 'gabarito', 'aluno']