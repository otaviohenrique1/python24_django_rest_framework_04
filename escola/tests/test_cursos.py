from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso
from escola.serializers import CursoSerializer


class CursosTestCase(APITestCase):
    fixtures = ["prototipo_banco.json"]

    def setUp(self):
        # self.usuario = User.objects.create_superuser(username="admin", password="admin")
        self.usuario = User.objects.get(username="otavio")
        self.url = reverse("Cursos-list")
        self.client.force_authenticate(user=self.usuario)
        # self.curso_01 = Curso.objects.create(
        #     codigo="CT01", descricao="Curso de teste 01", nivel="B"
        # )
        # self.curso_02 = Curso.objects.create(
        #     codigo="CT02", descricao="Curso de teste 02", nivel="I"
        # )
        self.curso_01 = Curso.objects.get(pk=1)
        self.curso_02 = Curso.objects.get(pk=2)

    def test_requisicao_get_para_listar_cursos(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_um_curso(self):
        """Teste de requisição GET um curso"""
        response = self.client.get(self.url + "1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_curso = Curso.objects.get(pk=1)
        dados_curso_serializados = CursoSerializer(instance=dados_curso).data
        self.assertEqual(response.data, dados_curso_serializados)

    def test_requisicao_post_para_criar_um_curso(self):
        """Teste de requisição POST para um curso"""
        dados = {
            "codigo": "CTT3",
            "descricao": "Curso teste 3",
            "nivel": "A",
        }
        response = self.client.post(self.url, data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_um_curso(self):
        """Teste de requisição DELETE um curso"""
        response = self.client.delete(f"{self.url}2/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_um_curso(self):
        """Teste de requisição PUT para um curso"""
        dados = {
            "codigo": "CTT1",
            "descricao": "Curso teste 1 atualizado",
            "nivel": "I",
        }
        response = self.client.put(f"{self.url}1/", data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
