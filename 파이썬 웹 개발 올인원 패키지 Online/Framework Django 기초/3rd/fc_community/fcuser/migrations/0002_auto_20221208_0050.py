# Generated by Django 2.1.7 on 2022-12-07 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fcuser',
            options={'verbose_name': '패스트캠퍼스 사용자', 'verbose_name_plural': '패스트캠퍼스 사용자'},
        ),
        migrations.RenameField(
            model_name='fcuser',
            old_name='registered_dttm',
            new_name='registered_dtm',
        ),
    ]
