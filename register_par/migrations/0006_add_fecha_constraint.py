from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('register_par', '0005_logical_changes'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='encuentros',
            constraint=models.CheckConstraint(
                condition=models.Q(('ffinEnc__isnull', True)) | models.Q(('ffinEnc__gt', models.F('finiEnc'))),
                name='check_fechas_encuentro',
            ),
        ),
    ]