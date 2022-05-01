# Generated by Django 4.0.3 on 2022-04-29 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FIR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=36)),
                ('details', models.CharField(max_length=500)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('suspect', models.CharField(max_length=100)),
                ('status', models.CharField(default='NEW', max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('priority', models.CharField(default='MEDIUM', max_length=20)),
                ('bureau_notes', models.CharField(default='NONE', max_length=500)),
                ('officer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.officer')),
                ('victim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.victim')),
            ],
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=500)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('fir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fir.fir')),
            ],
        ),
    ]