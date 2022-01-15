# Generated by Django 4.0.1 on 2022-01-14 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('pname', models.CharField(max_length=100)),
                ('pdescription', models.CharField(max_length=200)),
                ('pqty', models.IntegerField(default=10)),
                ('price', models.IntegerField(default=100)),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
