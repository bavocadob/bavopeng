from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.auth import get_user_model

import random
import datetime
from faker import Faker

from articles.models import Article, Comment


User = get_user_model()


class Command(BaseCommand):
    help = "게시글 더미 데이터를 만듭니다."

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

        users = User.objects.all()

        

        for _ in range(total):
            user = random.choice(users)
            title = fake.catch_phrase()
            content = fake.catch_phrase()
            article = Article.objects.create(
                user=user,
                title=title,
                content=f'<p>{content}</p>'
            )

            for i in range(random.randint(0, 13)):
                comment_content = fake.catch_phrase()
                comment = Comment.objects.create(
                    user=random.choice(users),
                    article=article,
                    parent_comment=None,
                    content=comment_content,
                )

        self.stdout.write(self.style.SUCCESS(f'{total}개의 게시글을 생성하였습니다.'))


        

