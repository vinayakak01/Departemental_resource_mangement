# Generated by Django 4.0.3 on 2022-05-20 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_remove_labs_id_pcs_labid_alter_labs_bnum_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labs',
            name='bNum',
        ),
        migrations.RemoveField(
            model_name='labs',
            name='cap',
        ),
        migrations.RemoveField(
            model_name='labs',
            name='chairNum',
        ),
        migrations.RemoveField(
            model_name='labs',
            name='fNum',
        ),
        migrations.RemoveField(
            model_name='labs',
            name='pcNum',
        ),
    ]