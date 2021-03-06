# Generated by Django 2.0b1 on 2017-12-20 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_auto_20171219_0756'),
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=140, verbose_name='Texto')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Fecha')),
            ],
            options={
                'verbose_name': 'respuesta',
                'verbose_name_plural': 'respuestas',
            },
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(max_length=140, verbose_name='Texto'),
        ),
        migrations.AddField(
            model_name='response',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.Message', verbose_name='Mensaje'),
        ),
        migrations.AddField(
            model_name='response',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.Profile', verbose_name='Perfil'),
        ),
    ]
