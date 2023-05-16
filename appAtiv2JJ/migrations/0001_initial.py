# Generated by Django 3.2.13 on 2023-05-15 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('aniversario', models.DateField()),
                ('primeiraparticipacao', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Técnicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('entradanoct', models.DateField()),
                ('pagamento', models.BooleanField()),
            ],
        ),
    ]
