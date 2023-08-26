# Generated by Django 4.1.4 on 2022-12-26 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_tracking_pack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracking',
            name='Pack',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='services.company', verbose_name='shipping name'),
        ),
    ]
