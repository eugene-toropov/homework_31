from django.db import models
from django.db.models import TextChoices


class UserRoles(TextChoices):
    MEMBER = 'member', 'Пользователь'
    ADMIN = 'admin', 'Администратор'
    MODERATOR = 'moderator', 'Модератор'


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField()
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)
    locations = models.ManyToManyField('Location')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.author.last_name,
            'username': self.username,
            'age': self.age,
            'role': self.role,
            'locations': [loc.name for loc in self.locations.all()],
        }


class Location(models.Model):
    name = models.CharField(max_length=200, unique=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name
