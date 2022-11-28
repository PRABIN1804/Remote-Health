

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_auto_20221126_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
                ('service', models.CharField(max_length=200)),
                ('doctor', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
            ],
        ),
    ]
