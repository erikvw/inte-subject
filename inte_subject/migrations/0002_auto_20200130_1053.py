# Generated by Django 2.2.9 on 2020-01-30 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inte_subject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalassessment',
            name='diabetes_informed',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], help_text='Diabetes', max_length=15, null=True, verbose_name='Were you told you have diabetes?'),
        ),
        migrations.AddField(
            model_name='generalassessment',
            name='hiv_informed',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], help_text='HIV', max_length=15, null=True, verbose_name='Were you told you are HIV positive?'),
        ),
        migrations.AddField(
            model_name='generalassessment',
            name='hypertension_informed',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], help_text='Hypertension', max_length=15, null=True, verbose_name='Were you told you have high blood pressure?'),
        ),
        migrations.AddField(
            model_name='historicalgeneralassessment',
            name='diabetes_informed',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], help_text='Diabetes', max_length=15, null=True, verbose_name='Were you told you have diabetes?'),
        ),
        migrations.AddField(
            model_name='historicalgeneralassessment',
            name='hiv_informed',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], help_text='HIV', max_length=15, null=True, verbose_name='Were you told you are HIV positive?'),
        ),
        migrations.AddField(
            model_name='historicalgeneralassessment',
            name='hypertension_informed',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], help_text='Hypertension', max_length=15, null=True, verbose_name='Were you told you have high blood pressure?'),
        ),
        migrations.AlterField(
            model_name='generalassessment',
            name='conditions',
            field=models.ManyToManyField(to='inte_lists.Conditions', verbose_name='On what basis was the patient enrolled?'),
        ),
        migrations.AlterField(
            model_name='generalassessment',
            name='diabetes_screening',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], help_text='Diabetes', max_length=15, null=True, verbose_name='Besides the tests done today, have you been tested for diabetes (high blood sugar)'),
        ),
        migrations.AlterField(
            model_name='generalassessment',
            name='diabetes_screening_ago',
            field=models.CharField(blank=True, help_text='Diabetes', max_length=15, null=True, verbose_name='How long ago was this?'),
        ),
        migrations.AlterField(
            model_name='generalassessment',
            name='hiv_screening',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], help_text='HIV', max_length=15, null=True, verbose_name='Besides the tests done today, have you been tested for HIV?'),
        ),
        migrations.AlterField(
            model_name='generalassessment',
            name='hiv_screening_ago',
            field=models.CharField(blank=True, help_text='HIV', max_length=15, null=True, verbose_name='How long ago was this'),
        ),
        migrations.AlterField(
            model_name='generalassessment',
            name='hypertension_screening',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], help_text='Hypertension', max_length=15, null=True, verbose_name='Besides the tests done today, have you been tested for high blood pressure?'),
        ),
        migrations.AlterField(
            model_name='generalassessment',
            name='hypertension_screening_ago',
            field=models.CharField(blank=True, help_text='Hypertension', max_length=15, null=True, verbose_name='How long ago was this?'),
        ),
        migrations.AlterField(
            model_name='historicalgeneralassessment',
            name='diabetes_screening',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], help_text='Diabetes', max_length=15, null=True, verbose_name='Besides the tests done today, have you been tested for diabetes (high blood sugar)'),
        ),
        migrations.AlterField(
            model_name='historicalgeneralassessment',
            name='diabetes_screening_ago',
            field=models.CharField(blank=True, help_text='Diabetes', max_length=15, null=True, verbose_name='How long ago was this?'),
        ),
        migrations.AlterField(
            model_name='historicalgeneralassessment',
            name='hiv_screening',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], help_text='HIV', max_length=15, null=True, verbose_name='Besides the tests done today, have you been tested for HIV?'),
        ),
        migrations.AlterField(
            model_name='historicalgeneralassessment',
            name='hiv_screening_ago',
            field=models.CharField(blank=True, help_text='HIV', max_length=15, null=True, verbose_name='How long ago was this'),
        ),
        migrations.AlterField(
            model_name='historicalgeneralassessment',
            name='hypertension_screening',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], help_text='Hypertension', max_length=15, null=True, verbose_name='Besides the tests done today, have you been tested for high blood pressure?'),
        ),
        migrations.AlterField(
            model_name='historicalgeneralassessment',
            name='hypertension_screening_ago',
            field=models.CharField(blank=True, help_text='Hypertension', max_length=15, null=True, verbose_name='How long ago was this?'),
        ),
    ]
