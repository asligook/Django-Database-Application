from django import forms

class PlayerForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    date_of_birth = forms.CharField(max_length=100)
    height = forms.IntegerField()
    weight = forms.IntegerField()
    player_position_id = forms.IntegerField()
    position_id = forms.IntegerField()
    player_teams_id = forms.IntegerField()
    team_id = forms.IntegerField()

class JuryForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    nationality = forms.CharField(max_length=100)

class CoachForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    nationality = forms.CharField(max_length=100)

class UpdateStadiumForm(forms.Form):
    stadium_id = forms.IntegerField()
    new_stadium_name = forms.CharField(max_length=100)

class DeleteSessionForm(forms.Form):
    session_id = forms.IntegerField()

class NewSessionForm(forms.Form):
    session_id = forms.IntegerField()
    jury_name = forms.CharField(max_length=100)
    jury_surname = forms.CharField(max_length=100)
    date = forms.CharField(max_length=100)
    rating = forms.FloatField(required=False)
    time_slot = forms.IntegerField()
    stadium_id = forms.IntegerField()

class RateSessionForm(forms.Form):
    rate = forms.FloatField()
    date = forms.CharField(max_length=100)
    session_id = forms.IntegerField()

class SquadForm(forms.Form):
    session_id = forms.IntegerField()
    player1 = forms.CharField(max_length=100)
    player2 = forms.CharField(max_length=100)
    player3 = forms.CharField(max_length=100)
    player4 = forms.CharField(max_length=100)
    player5 = forms.CharField(max_length=100)
    player6 = forms.CharField(max_length=100)
    position1 = forms.IntegerField()
    position2 = forms.IntegerField()
    position3 = forms.IntegerField()
    position4 = forms.IntegerField()
    position5 = forms.IntegerField()
    position6 = forms.IntegerField()