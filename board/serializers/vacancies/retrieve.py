from rest_framework import serializers

from board.models import Vacancy


class VacancyRetrieveOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    organization_id = serializers.IntegerField(source='organization.id')
    organization_name = serializers.CharField(source='organization.name')
    salary_from = serializers.IntegerField(allow_null=True)
    salary_to = serializers.IntegerField(allow_null=True)
    status = serializers.ChoiceField(choices=Vacancy.Status.choices)
    type = serializers.ChoiceField(choices=Vacancy.Type.choices)
    salary_type = serializers.ChoiceField(choices=Vacancy.SalaryType.choices)
    user_id = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


