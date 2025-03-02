from django.contrib.auth import get_user_model
from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=4096, null=True, blank=True)
    logo_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrganizationContact(models.Model):
    class Type(models.TextChoices):
        EMAIL = 'email', 'Email'
        PHONE_NUMBER = 'phone_number', 'Phone'
        TELEGRAM = 'telegram', 'Telegram'
        WEBSITE = 'website', 'Website'

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, choices=Type.choices)
    value = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Vacancy(models.Model):
    class Type(models.TextChoices):
        FULL_TIME = 'full_time', 'Full time'
        PART_TIME = 'part_time', 'Part time'
        INTERNSHIP = 'internship', 'Internship'
        REMOTE = 'remote', 'Remote'
        PROJECT_BASED = 'project_based', 'Project based'

    class SalaryType(models.TextChoices):
        MONTHLY = 'monthly', 'Monthly'
        HOURLY = 'hourly', 'Hourly'
        PROJECT_BASED = 'project_based', 'Project based'

    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        ACTIVE = 'active', 'Active'
        SUSPENDED = 'suspended', 'Suspended'

    organization = models.ForeignKey(
        to=Organization,
        on_delete=models.CASCADE,
        related_name='vacancies',
    )
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name='vacancies',
    )
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=4096)
    salary_from = models.PositiveIntegerField(null=True, blank=True)
    salary_to = models.PositiveIntegerField(null=True, blank=True)
    status = models.CharField(max_length=255, choices=Status.choices)
    type = models.CharField(max_length=255, choices=Type.choices)
    salary_type = models.CharField(max_length=255, choices=SalaryType.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
