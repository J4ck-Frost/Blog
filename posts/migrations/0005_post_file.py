# Generated by Django 5.0.3 on 2024-08-09 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(null=True, upload_to='files/'),
        ),
    ]
