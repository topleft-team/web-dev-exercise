# Generated by Django 5.0.3 on 2024-03-09 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0002_alter_category_options_alter_priority_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='rank',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]