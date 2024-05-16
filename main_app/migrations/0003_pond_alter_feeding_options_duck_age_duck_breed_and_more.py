# Generated by Django 5.0.6 on 2024-05-16 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_duck_age_remove_duck_breed_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='feeding',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='duck',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='duck',
            name='breed',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='duck',
            name='description',
            field=models.TextField(default='Unknown', max_length=250),
        ),
        migrations.AddField(
            model_name='duck',
            name='name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='feeding',
            name='date',
            field=models.DateField(verbose_name='Feeding Date'),
        ),
    ]
