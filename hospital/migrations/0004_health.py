

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_alter_employee_employee_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center', models.CharField(max_length=200)),
                ('state', models.CharField(blank=True, choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh')], max_length=200, null=True)),
                ('city', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=50)),
            ],
        ),
    ]
