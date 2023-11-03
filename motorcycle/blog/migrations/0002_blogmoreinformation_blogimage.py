# Generated by Django 4.2.6 on 2023-11-02 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogMoreInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_creation', models.DateField(auto_now_add=True)),
                ('more_information', models.TextField(verbose_name='More information')),
                ('blog', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='more_information', to='blog.blog')),
            ],
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_creation', models.DateField(auto_now_add=True)),
                ('image', models.FileField(upload_to='blog/more_images/')),
                ('generated_image_number', models.PositiveIntegerField(default=0, editable=False)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blog.blog')),
            ],
        ),
    ]
