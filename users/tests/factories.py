import factory
from factory.django import DjangoModelFactory
from django.contrib.auth import get_user_model
import uuid


User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('email',)

    username = factory.LazyFunction(lambda: uuid.uuid4().hex)
    email = factory.Sequence(lambda n: f'user{n}@example.com')
    password = factory.PostGenerationMethodCall(
        'set_password', 'defaultpassword'
    )
    telegram_id = factory.Faker('random_number', digits=9, fix_len=True)
    is_admin = False
