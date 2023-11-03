# Generated by Django 4.2.6 on 2023-11-01 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motorcycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Motorcycle name')),
                ('date_of_creation', models.DateField(auto_now_add=True)),
                ('type', models.CharField(blank=True, default='Motorcycle', editable=False, max_length=11)),
                ('price_1_to_7_days', models.PositiveIntegerField(verbose_name='Price 1 to 7 days rent')),
                ('price_8_to_14_days', models.PositiveIntegerField(verbose_name='Price 8 to 14 days rent')),
                ('price_15_to_21_days', models.PositiveIntegerField(verbose_name='Price 15 to 21 days rent')),
                ('price_22_to_30_days', models.PositiveIntegerField(verbose_name='Price 22 to 30 days rent')),
                ('main_image', models.FileField(upload_to='motorcycle/main_images/', verbose_name='Motorcycle main image')),
            ],
        ),
        migrations.CreateModel(
            name='MotorcycleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_creation', models.DateField(auto_now_add=True)),
                ('image', models.FileField(upload_to='motorcycle/more_images/')),
                ('generated_image_number', models.PositiveIntegerField(default=0, editable=False)),
                ('motorcycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='motor.motorcycle')),
            ],
        ),
        migrations.CreateModel(
            name='MotorcycleDeposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_creation', models.DateField(auto_now_add=True)),
                ('deposit', models.PositiveIntegerField(verbose_name='Motorcycle deposit price')),
                ('motorcycle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='deposit', to='motor.motorcycle')),
            ],
        ),
    ]
