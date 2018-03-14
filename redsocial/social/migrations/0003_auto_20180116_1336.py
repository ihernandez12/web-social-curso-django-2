# Generated by Django 2.0.1 on 2018-01-16 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_auto_20171219_0756'),
        ('social', '0002_auto_20171220_0850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower_relation', to='profile.Profile')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following_relation', to='profile.Profile')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='relation',
            unique_together={('following', 'follower')},
        ),
    ]