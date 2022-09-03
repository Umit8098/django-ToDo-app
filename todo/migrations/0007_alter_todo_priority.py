# Generated by Django 4.1 on 2022-08-29 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_alter_todo_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('1', '1️⃣'), ('2', '2️⃣'), ('3', '3️⃣'), ('4', '4️⃣'), ('5', '5️⃣')], max_length=2),
        ),
    ]
