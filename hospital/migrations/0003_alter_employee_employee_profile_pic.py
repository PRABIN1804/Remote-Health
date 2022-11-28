

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_employee_employee_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_profile_pic',
            field=models.ImageField(upload_to='image/download/uploads/employee_profile_pic/'),
        ),
    ]
