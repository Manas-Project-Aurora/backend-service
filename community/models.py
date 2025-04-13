from django.db import models
from django.db.models.constraints import UniqueConstraint


class CommunityResourceGroup(models.Model):
    name = models.CharField(max_length=255, unique=True)
    priority = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CommunityResource(models.Model):
    class Color(models.TextChoices):
        BLUE = 'blue', 'Blue'
        LIGHT_BLUE = 'light-blue', 'Light blue'
        GREEN = 'green', 'Green'
        VIOLET = 'violet', 'Violet'
        RED = 'red', 'Red'
        CONTRAST = 'contrast', 'Contrast'

    name = models.CharField(max_length=255)
    priority = models.PositiveIntegerField(default=0)
    group = models.ForeignKey(
        to=CommunityResourceGroup,
        on_delete=models.CASCADE,
        related_name='resources',
    )
    url = models.URLField()
    color = models.CharField(max_length=100, choices=Color.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = (
            UniqueConstraint(
                fields=('name', 'group'),
                name='unique_community_resource_name_group',
            ),
        )

    def __str__(self):
        return self.name