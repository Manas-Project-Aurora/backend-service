import factory
from factory.django import DjangoModelFactory

from board.models import Organization, OrganizationContact, Vacancy
from users.tests.factories import UserFactory


class OrganizationFactory(DjangoModelFactory):
    class Meta:
        model = Organization

    name = factory.Faker('company')
    description = factory.Faker('paragraph', nb_sentences=3)
    logo_url = factory.Faker(
        'image_url'
    )


class VacancyFactory(DjangoModelFactory):
    class Meta:
        model = Vacancy

    organization = factory.SubFactory(OrganizationFactory)
    user = factory.SubFactory(UserFactory)
    title = factory.Faker('job')
    description = factory.Faker('paragraph', nb_sentences=5)
    salary_from = factory.Faker('random_int', min=1000, max=3000)
    salary_to = factory.Faker('random_int', min=3001, max=7000)
    status = factory.Iterator(Vacancy.Status.values)
    type = factory.Iterator(Vacancy.Type.values)
    salary_type = factory.Iterator(Vacancy.SalaryType.values)


class OrganizationContactFactory(DjangoModelFactory):
    class Meta:
        model = OrganizationContact

    organization = factory.SubFactory(OrganizationFactory)
    type = factory.Iterator(OrganizationContact.Type.values)
    value = factory.LazyAttribute(
        lambda o: {
            OrganizationContact.Type.EMAIL: factory.Faker('email').generate(
                {}
            ),
            OrganizationContact.Type.PHONE_NUMBER: factory.Faker(
                'phone_number'
            ).generate({}),
            OrganizationContact.Type.TELEGRAM: f"@{factory.Faker('user_name').generate({})}",
            OrganizationContact.Type.WEBSITE: factory.Faker('url').generate({})
        }[o.type]
    )
