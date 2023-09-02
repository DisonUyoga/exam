# Generated by Django 4.2.3 on 2023-09-02 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("question_bank", "0003_alter_judgement_question_choice_answer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blank_question_choice",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="b_choices",
                to="question_bank.blank_question",
            ),
        ),
        migrations.AlterField(
            model_name="judgement_question_choice",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="j_choices",
                to="question_bank.judgement_question",
            ),
        ),
        migrations.AlterField(
            model_name="multi_choice_choice",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="m_choices",
                to="question_bank.multi_choice_question",
            ),
        ),
        migrations.AlterField(
            model_name="short_answer_choice",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="s_choices",
                to="question_bank.short_answer_question",
            ),
        ),
    ]
