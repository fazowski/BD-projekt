from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class RefereeDetails(models.Model):
    """
        Class representing referee details model object
    """
    user = models.OneToOneField(
        User,
        related_name='ref_user',
        on_delete=models.CASCADE
    )

    REFEREE_LEVEL = [
        (1, 'Zwiazkowy'),
        (2, 'Okregowy')
    ]
    referee_level = models.IntegerField(
        default=1,
        verbose_name='Poziom sędziego',
        choices=REFEREE_LEVEL,
    )
    city = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Miasto'
    )
    telephone = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        verbose_name='Numer telefonu'
    )

    class Meta:
        verbose_name = 'Sędzia szczegóły'
        verbose_name_plural = 'Sedziowie szczegóły'


class Team(models.Model):
    """
        Class representing Team model object
    """
    name = models.CharField(
        max_length=100,
        verbose_name='Nazwa drużyny'
    )
    city = models.CharField(
        max_length=50,
        verbose_name='Miasto'
    )
    telephone = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        verbose_name='Numer kontaktowy'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular team instance."""
        return reverse('team_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Drużyna'
        verbose_name_plural = 'Druzyny'


class MatchCategory(models.Model):
    """
        Class representing MatchCategory model object
    """
    name = models.CharField(
        max_length=50,
        verbose_name='Kateogria meczu'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'


class MatchStatus(models.Model):
    """
        Class representing Match Status model object
    """
    name = models.CharField(
        max_length=100,
        verbose_name='Nazwa'
    )
    next_status = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Nastepny status'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Status meczu'
        verbose_name_plural = 'Statusy meczy'


class Match(models.Model):
    """
        Class representing Match model object
    """
    match_number = models.CharField(
        max_length=10,
        verbose_name='Numer meczu'
    )
    home_team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        related_name='home_team',
        verbose_name='Gospodarz'
    )
    away_team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        related_name='away_team',
        verbose_name='Gosc'
    )
    match_category = models.ForeignKey(
        MatchCategory,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Kategoria'
    )
    date_time = models.DateTimeField(
        default=timezone.now,
        verbose_name='Data i godzina'
    )
    referee_a = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='referee_a',
        verbose_name='Sędzia A'
    )
    referee_b = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='referee_b',
        verbose_name='Sędzia B'
    )
    match_status = models.ForeignKey(
        MatchStatus,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Status meczu'
    )

    def __str__(self):
        return '{0} {1} - {2}'.format(self.match_number, self.home_team, self.away_team)

    class Meta:
        verbose_name = 'Mecz'
        verbose_name_plural = 'Mecze'
        ordering = ('date_time',)




class MatchResult(models.Model):
    match = models.ForeignKey(
        Match,
        on_delete=models.CASCADE,
        verbose_name='Mecz'
    )
    home_team_goals = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Bramki Gospodarze'
    )
    away_team_goals = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Bramki Goscie'
    )

    winner = models.CharField(
        max_length=1,
        verbose_name='Zwyciezca',
        blank=True,
        null=True
    )