# Generated by Django 4.0.3 on 2022-08-23 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_userinformation_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referBy', models.CharField(max_length=100, null=True)),
                ('upload_file', models.FileField(upload_to='')),
                ('date', models.DateField()),
                ('typeofrecord', models.CharField(choices=[('Diagnosis Report', 'Diagnosis Report'), ('Prescription', 'Prescription'), ('Others', 'Others')], max_length=100, null=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.userinformation')),
            ],
        ),
    ]
