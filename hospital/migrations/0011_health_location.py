

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0010_alter_appointment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='health',
            name='location',
            field=models.CharField(default='', max_length=200),
        ),
    ]
