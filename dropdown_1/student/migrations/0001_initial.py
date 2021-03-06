# Generated by Django 3.2.6 on 2021-08-12 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=30)),
                ('country_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.country')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.country')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.state')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.state'),
        ),
    ]
