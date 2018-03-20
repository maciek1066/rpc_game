# Generated by Django 2.0.3 on 2018-03-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='ending_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='round',
            name='creator_move',
            field=models.IntegerField(choices=[(3, 'scissors'), (1, 'rock'), (2, 'paper')], null=True),
        ),
        migrations.AlterField(
            model_name='round',
            name='opponent_move',
            field=models.IntegerField(choices=[(3, 'scissors'), (1, 'rock'), (2, 'paper')], null=True),
        ),
    ]
