# Generated by Django 4.2.2 on 2023-07-22 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_social', '0005_delete_customuser_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='friends',
            field=models.ManyToManyField(to='mini_social.customuser'),
        ),
    ]
