# Generated by Django 3.2.25 on 2024-04-24 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sonu1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='catagory',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CP', 'Cappuccino'), ('LT', 'Latte'), ('FC', 'Frappuccino'), ('M', 'Mocha '), ('AM', 'Americano'), ('IC', 'Irish Coffee'), ('LB', 'Long Black'), ('DP', 'Doppio'), ('FW', 'Flat White'), ('MT', 'Macchiato')], default=0, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='composition',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='prodapp',
            field=models.TextField(default=''),
        ),
    ]