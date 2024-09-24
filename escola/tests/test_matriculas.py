from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante, Curso, Matricula


class MatriculasTestCase(APITestCase):
    fixtures = ["prototipo_banco.json"]

    def setUp(self):
        # self.usuario = User.objects.create_superuser(username="admin", password="admin")
        self.usuario = User.objects.get(username="otavio")
        self.url = reverse("Matriculas-list")
        self.client.force_authenticate(user=self.usuario)
        # self.estudante = Estudante.objects.create(
        #     nome="Estudante Teste",
        #     email="estudante@gmail.com",
        #     cpf="77567543010",
        #     data_nascimento="2003-02-02",
        #     celular="11 98765-4321",
        # )
        # self.curso = Curso.objects.create(
        #     codigo="CTT", descricao="Curso Teste", nivel="B"
        # )
        self.estudante = Estudante.objects.get(pk=1)
        self.curso = Curso.objects.get(pk=1)
        self.matricula = Matricula.objects.create(
            estudante=self.estudante, curso=self.curso, periodo="M"
        )
        # self.matricula = Matricula.objects.get(pk=1)

    def test_requisicao_get_para_listar_matriculas(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_uma_matricula(self):
        """Teste de requisição POST para uma matricula"""
        dados = {
            "estudante": self.estudante.pk,
            "curso": self.curso.pk,
            "nivel": "M",
        }
        response = self.client.post(self.url, data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_uma_matricula(self):
        """Teste de requisição DELETE uma matricula"""
        response = self.client.delete(f"{self.url}2/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_put_para_atualizar_um_curso(self):
        """Teste de requisição PUT para um curso"""
        dados = {
            "estudante": self.estudante.pk,
            "curso": self.curso.pk,
            "periodo": "V",
        }
        response = self.client.put(f"{self.url}1/", data=dados)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
