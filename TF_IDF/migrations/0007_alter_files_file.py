# Generated by Django 3.2.7 on 2021-09-11 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TF_IDF', '0006_alter_files_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(null=True, upload_to='files/'),
        ),
    ]
