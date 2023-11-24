from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

import random
from faker import Faker

from accounts.models import Profile

User = get_user_model()


class Command(BaseCommand):
    help = 'Creates random users'

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            default=2,
            type=int,
            help="Indicates the number of users to be created"
        )

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker('ko-KR')

        users = []
        for i in range(total):
            username = f'test{i + 1}'
            user = User.objects.create(
                username=username,
                is_staff=False,
                is_superuser=False,
                is_active=True,
                email=fake.email(),
            )
            user.set_password('qwer1234')
            user.save() 
            users.append(user)
            profile = Profile.objects.get(pk=user.pk)

            nickname = f'{fake.name()}{i}'
            introduce = fake.catch_phrase()
            profile.nickname=nickname
            profile.introduce=introduce
            profile.save()
            

        for user in users:
            other_users = [u for u in users if u != user]
            for follower in random.choices(other_users, k=random.randint(0, 8)):
                user.followings.add(follower)

        self.stdout.write(self.style.SUCCESS(f'{total} users were created successfully.'))
