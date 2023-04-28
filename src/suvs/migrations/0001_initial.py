# Generated by Django 4.2 on 2023-04-24 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SUV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suv_make', models.CharField(max_length=255)),
                ('suv_model', models.CharField(max_length=255)),
                ('milage', models.IntegerField(null=True)),
                ('release', models.IntegerField(null=True)),
                ('color', models.CharField(default='white', max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('caption', models.CharField(default='No video', max_length=255)),
                ('video', models.FileField(blank=True, null=True, upload_to='videoSUV/')),
            ],
        ),
    ]
