

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='employee_profile_pic',
            field=models.ImageField(default='', upload_to='image/download/uploads/employee_profile_pic/'),
        ),
    ]