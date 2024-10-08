# # Create your models here.
# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models


# class Channels(models.Model):
#     channel_id = models.IntegerField(primary_key=True)
#     channel_name = models.CharField(unique=True, max_length=150, blank=True, null=True)

#     class Meta:
#         #managed = False
#         db_table = 'Channels'


# class Coaches(models.Model):
#     username = models.OneToOneField('Users', models.DO_NOTHING, db_column='username', primary_key=True)
#     nationality = models.CharField(max_length=125)

#     class Meta:
#         #managed = False
#         db_table = 'Coaches'


# class Databasemanagers(models.Model):
#     username = models.CharField(primary_key=True, max_length=125)
#     password = models.CharField(max_length=250, blank=True, null=True)

#     class Meta:
#         #managed = False
#         db_table = 'DatabaseManagers'


# class HavePositions(models.Model):
#     player_position_id = models.IntegerField(primary_key=True)
#     username = models.ForeignKey('Players', models.DO_NOTHING, db_column='username', blank=True, null=True)
#     position = models.ForeignKey('Positions', models.DO_NOTHING)

#     class Meta:
#         #managed = False
#         db_table = 'Have_Positions'


# class Juries(models.Model):
#     username = models.OneToOneField('Users', models.DO_NOTHING, db_column='username', primary_key=True)
#     nationality = models.CharField(max_length=125)

#     class Meta:
#         #managed = False
#         db_table = 'Juries'


# class Leads(models.Model):
#     lead_id = models.IntegerField(primary_key=True)
#     coach_username = models.ForeignKey(Coaches, models.DO_NOTHING, db_column='coach_username', blank=True, null=True)
#     contract_start_time = models.CharField(max_length=125, blank=True, null=True)
#     contract_end_time = models.CharField(max_length=125, blank=True, null=True)
#     team = models.ForeignKey('Teams', models.DO_NOTHING)

#     class Meta:
#         #managed = False
#         db_table = 'Leads'


# class MatchEvent(models.Model):
#     session_id = models.IntegerField(primary_key=True)
#     team = models.ForeignKey('Teams', models.DO_NOTHING)
#     assigned_jury_username = models.ForeignKey(Juries, models.DO_NOTHING, db_column='assigned_jury_username')
#     date = models.CharField(max_length=125, blank=True, null=True)
#     rating = models.FloatField(blank=True, null=True)
#     time_slot = models.IntegerField(blank=True, null=True)
#     stadium = models.ForeignKey('Stadiums', models.DO_NOTHING)

#     class Meta:
#         #managed = False
#         db_table = 'Match_Event'


# class MatchPlayedbyTeam(models.Model):
#     session = models.OneToOneField(MatchEvent, models.DO_NOTHING, primary_key=True)
#     team = models.ForeignKey('Teams', models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         #managed = False
#         db_table = 'Match_PlayedBy_Team'


# class PlayerRegisteredTeam(models.Model):
#     player_teams_id = models.IntegerField(primary_key=True)
#     username = models.ForeignKey('Players', models.DO_NOTHING, db_column='username', blank=True, null=True)
#     team = models.ForeignKey('Teams', models.DO_NOTHING)

#     class Meta:
#         #managed = False
#         db_table = 'Player_Registered_Team'


# class Players(models.Model):
#     username = models.OneToOneField('Users', models.DO_NOTHING, db_column='username', primary_key=True)
#     date_of_birth = models.CharField(max_length=125, blank=True, null=True)
#     height = models.IntegerField(blank=True, null=True)
#     weight = models.IntegerField(blank=True, null=True)

#     class Meta:
#         #managed = False
#         db_table = 'Players'


# class PlayersPlayinMatches(models.Model):
#     squad_id = models.IntegerField(primary_key=True)
#     username = models.ForeignKey(Players, models.DO_NOTHING, db_column='username', blank=True, null=True)
#     session = models.ForeignKey(MatchEvent, models.DO_NOTHING, blank=True, null=True)
#     position = models.ForeignKey('Positions', models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         #managed = False
#         db_table = 'Players_PlayIn_Matches'


# class Positions(models.Model):
#     position_id = models.IntegerField(primary_key=True)
#     position_name = models.CharField(max_length=120, blank=True, null=True)

#     class Meta:
#         #managed = False
#         db_table = 'Positions'


# class Stadiums(models.Model):
#     stadium_id = models.IntegerField(primary_key=True)
#     stadium_name = models.CharField(max_length=150, blank=True, null=True)
#     stadium_country = models.CharField(max_length=150, blank=True, null=True)

#     class Meta:
#         #managed = False
#         db_table = 'Stadiums'


# class Teams(models.Model):
#     team_id = models.IntegerField(primary_key=True)
#     team_name = models.CharField(max_length=150, blank=True, null=True)
#     channel = models.ForeignKey(Channels, models.DO_NOTHING)

#     class Meta:
#         #managed = False
#         db_table = 'Teams'


# class Users(models.Model):
#     username = models.CharField(primary_key=True, max_length=125)
#     password = models.CharField(max_length=125, blank=True, null=True)
#     name = models.CharField(max_length=125, blank=True, null=True)
#     surname = models.CharField(max_length=125, blank=True, null=True)

#     class Meta:
#         #managed = False
#         db_table = 'Users'


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'
