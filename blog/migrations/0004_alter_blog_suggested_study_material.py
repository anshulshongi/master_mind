# Generated by Django 4.0.3 on 2022-03-29 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_percentage_crietria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='suggested_study_material',
            field=models.CharField(max_length=10000),
        ),
    ]