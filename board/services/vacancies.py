import datetime
from dataclasses import dataclass

from board.models import Vacancy
from board.services.common import Pagination


@dataclass(frozen=True, slots=True, kw_only=True)
class VacancyListPageItem:
    id: int
    title: str
    description: str
    organization_id: int
    organization_name: str
    salary_from: int
    salary_to: int
    status: str
    type: str
    salary_type: str
    user_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime


@dataclass(frozen=True, slots=True, kw_only=True)
class VacancyListPage:
    vacancies: list[VacancyListPageItem]
    pagination: Pagination


def get_vacancies_page(
        take: int,
        skip: int,
        statuses: list[Vacancy.Status],
        types: list[Vacancy.Type] | None,
        salary_from: int | None,
        salary_to: int | None,
        salary_types: list[Vacancy.SalaryType] | None,
        user_ids: list[int] | None,
) -> VacancyListPage:
    vacancies = (
        Vacancy.objects
        .select_related('organization')
        .filter(status__in=statuses)
        .order_by('-created_at')
    )
    if types is not None:
        vacancies = vacancies.filter(type__in=types)
    if salary_from is not None:
        vacancies = vacancies.filter(salary_from__gte=salary_from)
    if salary_to is not None:
        vacancies = vacancies.filter(salary_to__lte=salary_to)
    if salary_types is not None:
        vacancies = vacancies.filter(salary_type__in=salary_types)
    if user_ids is not None:
        vacancies = vacancies.filter(user_id__in=user_ids)

    total_count = vacancies.count()
    vacancies = vacancies[skip: skip + take]

    return VacancyListPage(
        vacancies=[
            VacancyListPageItem(
                id=vacancy.id,
                title=vacancy.title,
                description=vacancy.description,
                organization_id=vacancy.organization.id,
                organization_name=vacancy.organization.name,
                salary_from=vacancy.salary_from,
                salary_to=vacancy.salary_to,
                status=vacancy.status,
                type=vacancy.type,
                user_id=vacancy.user_id,
                salary_type=vacancy.salary_type,
                created_at=vacancy.created_at,
                updated_at=vacancy.updated_at,
            )
            for vacancy in vacancies
        ],
        pagination=Pagination(
            total_count=total_count,
            taken_count=len(vacancies),
            skipped_count=skip,
        ),
    )


def create_vacancy(
        *,
        user_id: int,
        title: str,
        description: str,
        organization_id: int,
        salary_from: int | None,
        salary_to: int | None,
        type: str,
        salary_type: str,
) -> None:
    vacancy = Vacancy(
        user_id=user_id,
        title=title,
        description=description,
        organization_id=organization_id,
        salary_from=salary_from,
        salary_to=salary_to,
        type=type,
        salary_type=salary_type,
        status=Vacancy.Status.PENDING,
    )
    vacancy.full_clean()
    vacancy.save()
