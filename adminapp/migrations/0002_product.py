# Generated by Django 5.0.1 on 2024-02-04 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Bird', 'Bird'), ('Fish', 'Fish'), ('Rabbit', 'Rabbit'), ('Gunniepig', 'Gunniepig')], max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('image', models.FileField(upload_to='productimages')),
                ('secure_key', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'product_table',
            },
        ),
    ]
