# Generated by Django 3.1.7 on 2021-06-17 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_escudos'),
    ]

    operations = [
        migrations.CreateModel(
            name='USUARIO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=20)),
                ('password', models.TextField(max_length=20)),
            ],
        ),
    ]