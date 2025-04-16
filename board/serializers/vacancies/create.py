from rest_framework import serializers

from board.models import Vacancy


class VacancyCreateInputSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=4096)
    organization_id = serializers.IntegerField()
    salary_from = serializers.IntegerField(allow_null=True)
    salary_to = serializers.IntegerField(allow_null=True)
    type = serializers.ChoiceField(choices=Vacancy.Type.choices)
    salary_type = serializers.ChoiceField(choices=Vacancy.SalaryType.choices)
