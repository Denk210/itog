# Generated by Django 5.1.4 on 2024-12-15 08:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_type', models.CharField(choices=[('title', 'Присвоение ученого звания'), ('duplicate', 'Получение дубликата'), ('replacement', 'Замена аттестата'), ('cancellation', 'Аннулирование звания')], max_length=100)),
                ('education_document', models.FileField(upload_to='documents/')),
                ('application_document', models.FileField(upload_to='documents/')),
                ('additional_document', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('status', models.CharField(default='Отправлено на рассмотрение', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Мужской'), ('female', 'Женский')], max_length=10)),
                ('passport_series', models.CharField(max_length=4)),
                ('passport_number', models.CharField(max_length=6)),
                ('registration_address', models.CharField(max_length=255)),
                ('actual_address', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
