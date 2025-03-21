# Generated by Django 4.1.13 on 2024-07-11 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Procurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('current_step', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_number', models.IntegerField()),
                ('file', models.FileField(upload_to='uploads/')),
                ('procurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='procurement.procurement')),
            ],
        ),
    ]
