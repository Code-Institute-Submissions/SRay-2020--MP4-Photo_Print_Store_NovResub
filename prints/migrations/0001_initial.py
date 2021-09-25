# Generated by Django 3.2.7 on 2021-09-24 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoPrint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('has_sizes', models.BooleanField(blank=True, default=False, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]