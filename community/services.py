import datetime
from dataclasses import dataclass

from community.models import CommunityResource


@dataclass(frozen=True, slots=True, kw_only=True)
class CommunityResourceListItem:
    id: int
    name: str
    group_id: int
    group_name: str
    url: str
    color: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


def get_community_resources() -> list[CommunityResourceListItem]:
    resources = (
        CommunityResource.objects
        .select_related('group')
        .order_by('-group__priority', '-priority')
    )
    return [
        CommunityResourceListItem(
            id=resource.id,
            name=resource.name,
            group_id=resource.group.id,
            group_name=resource.group.name,
            url=resource.url,
            color=resource.color,
            created_at=resource.created_at,
            updated_at=resource.updated_at,
        )
        for resource in resources
    ]
