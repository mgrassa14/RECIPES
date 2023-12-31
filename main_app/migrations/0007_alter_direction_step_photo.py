# Generated by Django 4.2 on 2023-08-15 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_rename_directions_direction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direction',
            name='step',
            field=models.TextField(default='', max_length=250, verbose_name='step'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.recipe')),
            ],
        ),
    ]
