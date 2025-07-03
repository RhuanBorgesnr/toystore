from django.contrib.auth.models import AbstractUser
from django.db import models

class Customer(AbstractUser):

    
    full_name = models.CharField(
        max_length=255,
        verbose_name="Nome completo"
    )
    email = models.EmailField(
        unique=True,
        verbose_name="E-mail"
    )
    birth_date = models.DateField(
        verbose_name="Data de nascimento"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em"
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizado em"
    )
    REQUIRED_FIELDS = ['full_name', 'birth_date', 'email']

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-created_at']

    def __str__(self):
        return self.full_name


