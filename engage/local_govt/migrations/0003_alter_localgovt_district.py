# Generated by Django 4.2.7 on 2024-12-21 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_alter_district_name_alter_union_name_and_more'),
        ('local_govt', '0002_alter_localgovt_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localgovt',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='locations.district', verbose_name='district'),
        ),
    ]