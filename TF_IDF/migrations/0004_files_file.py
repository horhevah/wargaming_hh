# Generated by Django 3.2.7 on 2021-09-11 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TF_IDF', '0003_remove_files_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='file',
            field=models.FileField(null=True, upload_to='files'),
        ),
    ]