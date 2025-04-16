import datetime
from dataclasses import dataclass

from django.db.models import Count, QuerySet

from board.exceptions import OrganizationNotFoundError, OrganizationAccessDenied
from board.models import Organization, Vacancy
from board.services.common import Pagination
from users.models import User


@dataclass(frozen=True, slots=True, kw_only=True)
class OrganizationContact:
    type: str
    value: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


@dataclass(frozen=True, slots=True, kw_only=True)
class OrganizationListPageItem:
    id: int
    name: str
    description: str | None
    logo_url: str | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    contacts: list[OrganizationContact]
    vacancy_count: int
    event_count: int
    video_count: int


@dataclass(frozen=True, slots=True, kw_only=True)
class OrganizationListPage:
    organizations: list
    pagination: Pagination


def get_organizations_page(
        *,
        take: int,
        skip: int,
) -> OrganizationListPage:
    organizations_total_count = Organization.objects.count()
    organizations: QuerySet[Organization] = (
        Organization.objects
        .prefetch_related('contacts')
        .order_by('-created_at')
        [skip: skip + take]
    )

    organization_ids = [organization.id for organization in organizations]
    vacancy_count_by_organization = (
        Vacancy.objects
        .filter(
            organization_id__in=organization_ids,
            status=Vacancy.Status.ACTIVE,
        )
        .annotate(count=Count('id'))
        .values('organization_id', 'count')
    )
    organization_id_to_vacancy_count = {
        vacancy['organization_id']: vacancy['count']
        for vacancy in vacancy_count_by_organization
    }

    result: list[OrganizationListPageItem] = []
    for organization in organizations:
        contacts = [
            OrganizationContact(
                type=contact.type,
                value=contact.value,
                created_at=contact.created_at,
                updated_at=contact.updated_at,
            )
            for contact in organization.contacts.all()
        ]
        vacancy_count = organization_id_to_vacancy_count.get(
            organization.id, 0
        )
        result.append(
            OrganizationListPageItem(
                id=organization.id,
                name=organization.name,
                description=organization.description,
                logo_url=organization.logo_url,
                created_at=organization.created_at,
                updated_at=organization.updated_at,
                contacts=contacts,
                vacancy_count=vacancy_count,
                event_count=0,
                video_count=0,
            )
        )

    return OrganizationListPage(
        organizations=result,
        pagination=Pagination(
            total_count=organizations_total_count,
            taken_count=len(organizations),
            skipped_count=skip,
        )
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class OrganizationRetrieveItem:
    id: int
    name: str
    description: str | None
    logo_url: str | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    contacts: list[OrganizationContact]
    vacancy_count: int
    event_count: int
    video_count: int


def get_organization_details(organization_id: int) -> OrganizationRetrieveItem:
    try:
        organization = Organization.objects.prefetch_related('contacts').get(id=organization_id)
    except Organization.DoesNotExist:
        raise OrganizationNotFoundError

    vacancy_count = Vacancy.objects.filter(
        organization_id=organization_id,
        status=Vacancy.Status.ACTIVE,
    ).count()

    event_count = 0
    video_count = 0

    contacts = [
        OrganizationContact(
            type=contact.type,
            value=contact.value,
            created_at=contact.created_at,
            updated_at=contact.updated_at,
        )
        for contact in organization.contacts.all()
    ]

    return OrganizationRetrieveItem(
        id=organization.id,
        name=organization.name,
        description=organization.description,
        logo_url=organization.logo_url,
        created_at=organization.created_at,
        updated_at=organization.updated_at,
        contacts=contacts,
        vacancy_count=vacancy_count,
        event_count=event_count,
        video_count=video_count,
    )

def delete_organization(organization_id: int, user: User) -> None:
    try:
        organization = Organization.objects.get(id=organization_id)
    except Organization.DoesNotExist:
        raise OrganizationNotFoundError

    if not user.is_admin:
        raise OrganizationAccessDenied

    organization.delete()