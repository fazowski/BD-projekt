from django.contrib import admin
from .models import RefereeDetails, Team, MatchCategory, Match, MatchStatus, MatchResult

# Register your models here.
@admin.register(RefereeDetails)
class RefereeDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'referee_level'
    )

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'city'
    )

@admin.register(MatchCategory)
class MatchCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = (
        'match_number',
        'home_team',
        'away_team',
        'match_category',
        'date_time',
        'referee_a',
        'referee_b'
    )


@admin.register(MatchStatus)
class MatchStatusAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(MatchResult)
class MatchResultAdmin(admin.ModelAdmin):
    list_display = (
        'match',
        'home_team_goals',
        'away_team_goals',
        'winner'
    )