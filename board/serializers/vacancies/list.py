from rest_framework import serializers

from board.models import Vacancy
from board.serializers.common import PaginationSerializer


class VacancyListInputSerializer(serializers.Serializer):
    take = serializers.IntegerField(
        min_value=1,
        max_value=100,
        default=50,
    )
    skip = serializers.IntegerField(default=0, min_value=0)
    statuses = serializers.ListField(
        child=serializers.ChoiceField(choices=Vacancy.Status.choices),
        default=[Vacancy.Status.ACTIVE],
    )
    types = serializers.ListField(
        child=serializers.ChoiceField(choices=Vacancy.Type.choices),
        default=None,
    )
    salary_from = serializers.IntegerField(
        min_value=1,
        default=None,
    )
    salary_to = serializers.IntegerField(
        min_value=1,
        default=None,
    )
    salary_types = serializers.ListField(
        child=serializers.ChoiceField(choices=Vacancy.SalaryType.choices),
        default=None,
    )


class VacancyListItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    organization_id = serializers.IntegerField()
    organization_name = serializers.CharField()
    salary_from = serializers.IntegerField(allow_null=True)
    salary_to = serializers.IntegerField(allow_null=True)
    status = serializers.ChoiceField(choices=Vacancy.Status.choices)
    type = serializers.ChoiceField(choices=Vacancy.Type.choices)
    salary_type = serializers.ChoiceField(choices=Vacancy.SalaryType.choices)
    user_id = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class VacancyListOutputSerializer(serializers.Serializer):
    vacancies = VacancyListItemSerializer(many=True)
    pagination = PaginationSerializer()
