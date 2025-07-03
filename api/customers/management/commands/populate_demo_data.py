from django.core.management.base import BaseCommand
from customers.models import Customer
from sales.models import Sale
from django.utils import timezone
from datetime import timedelta
import random

class Command(BaseCommand):
    help = 'Popula o banco com clientes e vendas de demonstração.'

    def handle(self, *args, **options):
        Customer.objects.all().delete()
        Sale.objects.all().delete()

        nomes = [
            ('Ana Beatriz', 'ana.b@example.com', '1992-05-01'),
            ('Carlos Eduardo', 'cadu@example.com', '1987-08-15'),
            ('Beatriz Souza', 'bia.souza@example.com', '1995-03-10'),
            ('João Pedro', 'jp@example.com', '1990-12-22'),
            ('Marina Lima', 'marina.lima@example.com', '1985-07-30'),
            ('Lucas Martins', 'lucas.m@example.com', '1993-04-12'),
            ('Juliana Rocha', 'juliana.r@example.com', '1989-09-18'),
            ('Fernando Alves', 'fernando.alves@example.com', '1986-01-25'),
            ('Patrícia Gomes', 'patricia.g@example.com', '1991-06-03'),
            ('Rafael Oliveira', 'rafael.o@example.com', '1994-11-11'),
            ('Camila Torres', 'camila.t@example.com', '1990-10-05'),
            ('Thiago Lima', 'thiago.l@example.com', '1988-02-17'),
            ('Aline Costa', 'aline.c@example.com', '1992-08-21'),
            ('Eduardo Nunes', 'eduardo.n@example.com', '1987-03-14'),
            ('Larissa Mendes', 'larissa.m@example.com', '1996-05-22'),
            ('Bruno Henrique', 'bruno.h@example.com', '1989-07-09'),
            ('Vanessa Barros', 'vanessa.b@example.com', '1993-12-03'),
            ('Felipe Souza', 'felipe.s@example.com', '1991-01-19'),
            ('Natália Ramos', 'natalia.r@example.com', '1990-06-27'),
            ('André Luiz', 'andre.l@example.com', '1985-10-13'),
            ('Isabela Ferreira', 'isabela.f@example.com', '1994-09-30'),
            ('Leonardo Batista', 'leonardo.b@example.com', '1988-04-08'),
            ('Tatiane Silva', 'tatiane.s@example.com', '1993-03-26'),
            ('Gustavo Moreira', 'gustavo.m@example.com', '1995-07-02'),
            ('Renata Almeida', 'renata.a@example.com', '1990-02-06'),
        ]

        clientes = []
        for i, (nome, email, nascimento) in enumerate(nomes):
            user = Customer.objects.create_user(
                username=f'user{i+1}',
                full_name=nome,
                email=email,
                birth_date=nascimento,
                password='12345678'
            )
            clientes.append(user)

        self.stdout.write(self.style.SUCCESS(f'{len(clientes)} clientes criados.'))

        for cliente in clientes:
            num_vendas = random.randint(1, 5)
            for _ in range(num_vendas):
                dias_atras = random.randint(0, 10)
                data_venda = timezone.now().date() - timedelta(days=dias_atras)
                valor = random.randint(50, 500)
                Sale.objects.create(
                    customer=cliente,
                    amount=valor,
                    sale_date=data_venda
                )

        self.stdout.write(self.style.SUCCESS('Vendas criadas para todos os clientes.'))
