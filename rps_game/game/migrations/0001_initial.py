# Generated by Django 2.0.3 on 2018-03-20 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_results', models.IntegerField(default=0)),
                ('opponent_results', models.IntegerField(default=0)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('ending_time', models.DateTimeField(null=True)),
                ('completed', models.BooleanField(default=False)),
                ('creator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL)),
                ('opponent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opponent', to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='won', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_move', models.IntegerField(choices=[(2, 'paper'), (1, 'rock'), (3, 'scissors')], null=True)),
                ('opponent_move', models.IntegerField(choices=[(2, 'paper'), (1, 'rock'), (3, 'scissors')], null=True)),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rounds', to='game.Game')),
            ],
        ),
    ]
