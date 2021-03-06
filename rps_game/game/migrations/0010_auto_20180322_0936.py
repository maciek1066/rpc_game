# Generated by Django 2.0.3 on 2018-03-22 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_auto_20180321_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='creator_move',
            field=models.IntegerField(blank=True, choices=[(1, 'rock'), (2, 'paper'), (3, 'scissors')], null=True),
        ),
        migrations.AlterField(
            model_name='round',
            name='opponent_move',
            field=models.IntegerField(blank=True, choices=[(1, 'rock'), (2, 'paper'), (3, 'scissors')], null=True),
        ),
    ]
