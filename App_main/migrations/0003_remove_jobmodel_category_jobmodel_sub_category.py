# Generated by Django 4.0.4 on 2022-09-18 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_main', '0002_jobcategoriesmodel_subcategoriesmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobmodel',
            name='category',
        ),
        migrations.AddField(
            model_name='jobmodel',
            name='sub_category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sub_categories', to='App_main.subcategoriesmodel'),
            preserve_default=False,
        ),
    ]
