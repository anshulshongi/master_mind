# Generated by Django 4.0.3 on 2022-03-31 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_blog_more_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cut_off',
            field=models.CharField(max_length=5000),
        ),
    ]
