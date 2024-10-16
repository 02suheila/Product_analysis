# Generated by Django 5.0.7 on 2024-10-09 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platform_analytics', '0004_alter_flipkartdata_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmazonData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, verbose_name='Email of the customer')),
                ('platform', models.CharField(max_length=50, verbose_name='Platform')),
                ('orders', models.IntegerField()),
                ('returns', models.IntegerField()),
                ('deliveries', models.IntegerField()),
            ],
            options={
                'db_table': 'amazon_data',
            },
        ),
    ]
