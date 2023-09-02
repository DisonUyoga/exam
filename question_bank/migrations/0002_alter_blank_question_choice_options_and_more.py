# Generated by Django 4.2.3 on 2023-09-01 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("question_bank", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blank_question_choice",
            options={
                "verbose_name": "Blank Question Choice",
                "verbose_name_plural": "Blank Question Choices",
            },
        ),
        migrations.AlterModelOptions(
            name="judgement_question_choice",
            options={
                "verbose_name": "Judgement Question Choice",
                "verbose_name_plural": "Judgement Question Choices",
            },
        ),
        migrations.AlterModelOptions(
            name="multi_choice_choice",
            options={
                "verbose_name": "Multi Choices",
                "verbose_name_plural": "Multi Choices",
            },
        ),
        migrations.AlterModelOptions(
            name="short_answer_choice",
            options={
                "verbose_name": "Short Answer Choice",
                "verbose_name_plural": "Short Answer Choices",
            },
        ),
        migrations.AlterField(
            model_name="blank_question_choice",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="question_bank.blank_question",
            ),
        ),
        migrations.AlterField(
            model_name="judgement_question_choice",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="question_bank.judgement_question",
            ),
        ),
        migrations.AlterField(
            model_name="short_answer_choice",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="question_bank.short_answer_question",
            ),
        ),
    ]
