# Generated by Django 4.0.1 on 2022-01-05 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('ItemID', models.AutoField(primary_key=True, serialize=False)),
                ('ItemName', models.CharField(max_length=30)),
                ('ItemDescription', models.TextField(blank=True, null=True)),
                ('ItemPrice', models.IntegerField(default=0)),
                ('ItemQuantity', models.IntegerField(default=0)),
            ],
        ),
    ]
