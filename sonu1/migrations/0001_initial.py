# Generated by Django 3.2.25 on 2024-04-11 09:12

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
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('discription', models.TextField()),
                ('composition', models.TextField()),
                ('prodapp', models.TextField()),
                ('catagory', models.CharField(choices=[('ml', 'milk coffee'), ('Cf', 'coffee'), ('C', 'coff')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]
