from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db import connection
from django.db import IntegrityError 
from django.db import transaction
from django.shortcuts import render
from .forms import PlayerForm, JuryForm, CoachForm, UpdateStadiumForm, DeleteSessionForm, NewSessionForm, RateSessionForm, SquadForm
import json

def index(request):
    return HttpResponse("view.index function is called")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        request.session['username'] = username  
        password = request.POST.get('password')

        with connection.cursor() as cursor:
            cursor.execute("SELECT username FROM DatabaseManagers WHERE DatabaseManagers.username = %s AND DatabaseManagers.password = %s", [username, password])
            dbmanager_exists = cursor.fetchone()

        # Check if the username exists in the Players table
        with connection.cursor() as cursor:
            cursor.execute("SELECT Users.username FROM Users INNER JOIN Players ON Users.username = Players.username WHERE Users.username= %s and Users.password= %s;", [username, password])
            player_exists = cursor.fetchone()

        # Check if the username exists in the Juries table
        with connection.cursor() as cursor:
            cursor.execute("SELECT Users.username FROM Users INNER JOIN Juries ON Users.username = Juries.username WHERE Users.username= %s and Users.password= %s;", [username, password])
            jury_exists = cursor.fetchone()

        # Check if the username exists in the Coaches table
        with connection.cursor() as cursor:
            cursor.execute("SELECT Users.username FROM Users INNER JOIN Coaches ON Users.username = Coaches.username WHERE Users.username= %s and Users.password= %s;", [username, password])
            coach_exists = cursor.fetchone()

        if player_exists:
            # Player exists, redirect to player page
            return redirect('player')
        elif jury_exists:
            # Jury exists, redirect to jury page
            return redirect('jury')
        elif coach_exists:
            # Coach exists, redirect to coach page
            return redirect('coach')
        elif dbmanager_exists:
            # Coach exists, redirect to coach page
            return redirect('dbmanager')
        else:
            # Username does not exist or incorrect password, render login page with error message
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
    else:
        # Render the login page
        return render(request, 'login.html')

def add_player_view(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            date_of_birth = form.cleaned_data['date_of_birth']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            player_position_id = form.cleaned_data['player_position_id']
            position_id = form.cleaned_data['position_id']
            player_teams_id = form.cleaned_data['player_teams_id']
            team_id = form.cleaned_data['team_id']
            with transaction.atomic():
                try:    
                    with connection.cursor() as cursor:
                        cursor.execute("INSERT INTO Users (username, password, name, surname) VALUES (%s, %s, %s, %s)", [username, password, name, surname])
                        cursor.execute("INSERT INTO Players (username, date_of_birth, height, weight) VALUES (%s, %s, %s, %s)", [username, date_of_birth, height, weight])
                        cursor.execute("INSERT INTO Have_Positions (player_position_id,username, position_id) VALUES (%s,%s, %s)", [player_position_id,username, position_id])
                        cursor.execute("INSERT INTO Player_Registered_Team (player_teams_id,username, team_id) VALUES (%s,%s, %s)", [player_teams_id,username, team_id])
                    
                    success_message = "Player is successfully added."
                    return render(request, 'dbmanager.html', {'message': 'hey manager!','success_message': success_message})
                except Exception as e:
                    error_message = "Error: {}".format(str(e))
                    transaction.set_rollback(True)
                    return render(request, 'dbmanager.html', {'message': 'hey manager!','error_message': error_message})
    else:
        form = PlayerForm()
    return render(request, 'add_player.html', {'form': form})
    
def add_jury_view(request):
    if request.method == 'POST':
        form = JuryForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            nationality = form.cleaned_data['nationality']
            with transaction.atomic():
                try:    
                    with connection.cursor() as cursor:
                        cursor.execute("INSERT INTO Users (username, password, name, surname) VALUES (%s, %s, %s, %s)", [username, password, name, surname])
                        cursor.execute("INSERT INTO Juries (username, nationality) VALUES (%s, %s)", [username, nationality])
                    success_message = "Jury is successfully added."
                    return render(request, 'dbmanager.html', {'message': 'hey manager!','success_message': success_message})
                except Exception as e:
                    error_message = "Error: {}".format(str(e))
                    transaction.set_rollback(True)
                    return render(request, 'dbmanager.html', {'message': 'hey manager!','error_message': error_message})
    else:
        form = JuryForm()
    return render(request, 'add_jury.html', {'form': form})

def add_coach_view(request):
    if request.method == 'POST':
        form = CoachForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            nationality = form.cleaned_data['nationality']
            with transaction.atomic():
                try:    
                    with connection.cursor() as cursor:
                        cursor.execute("INSERT INTO Users (username, password, name, surname) VALUES (%s, %s, %s, %s)", [username, password, name, surname])
                        cursor.execute("INSERT INTO Coaches (username, nationality) VALUES (%s, %s)", [username, nationality])
                    success_message = "Coach is successfully added."
                    return render(request, 'dbmanager.html', {'message': 'hey manager!','success_message': success_message})
                except Exception as e:
                    error_message = "Error: {}".format(str(e))
                    transaction.set_rollback(True)
                    return render(request, 'dbmanager.html', {'message': 'hey manager!','error_message': error_message})
    else:
        form = CoachForm()
    return render(request, 'add_coach.html', {'form': form})

def update_stadium_view(request):
    if request.method == 'POST':
        form = UpdateStadiumForm(request.POST)
        if form.is_valid():
            stadium_id = form.cleaned_data['stadium_id']
            new_stadium_name = form.cleaned_data['new_stadium_name']
            with transaction.atomic():
                try:    
                    with connection.cursor() as cursor:
                        cursor.execute("UPDATE Stadiums SET stadium_name = %s WHERE stadium_id = %s", [new_stadium_name, stadium_id])
                    success_message = "Stadium name is successfully updated."
                    return render(request, 'dbmanager.html', {'message': 'hey manager!','success_message': success_message})
                except Exception as e:
                    error_message = "Error: {}".format(str(e))
                    transaction.set_rollback(True)
                    return render(request, 'dbmanager.html', {'message': 'hey manager!','error_message': error_message})
    else:
        form = UpdateStadiumForm()
    return render(request, 'update_stadium.html', {'form': form})

def delete_session_view(request):
    if request.method == 'POST':
        form = DeleteSessionForm(request.POST)
        if form.is_valid():
            session_id = form.cleaned_data['session_id']

            # Check if the session exists
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM Match_Event WHERE session_id = %s", [session_id])
                session_exists = cursor.fetchone()

            if session_exists:
                try:
                    with transaction.atomic():
                        with connection.cursor() as cursor:
                            cursor.execute("DELETE FROM Players_PlayIn_Matches WHERE session_id = %s", [session_id])
                            cursor.execute("DELETE FROM Match_PlayedBy_Team WHERE session_id = %s", [session_id])
                            cursor.execute("DELETE FROM Match_Event WHERE session_id = %s", [session_id])                    
                    success_message = "Match Session is successfully deleted."
                    return render(request, 'coach.html', {'success_message': success_message})
                except Exception as e:
                    error_message = "Error: {}".format(str(e))
                    transaction.set_rollback(True)
                    return render(request, 'coach.html', {'error_message': error_message})
            else:
                error_message = "Error: Session {} does not exist.".format(session_id)
                return render(request, 'coach.html', {'error_message': error_message})
    else:
        form = DeleteSessionForm()
    return render(request, 'delete_session.html', {'form': form})

def list_stadium_view(request):
    with transaction.atomic():
        try:    
            with connection.cursor() as cursor:
                cursor.execute("SELECT stadium_name, stadium_country FROM Stadiums")   
                rows = cursor.fetchall()             
            # success_message = "Match Session is successfully deleted."
            return render(request, 'list_stadium.html', {'message': 'Stadiums:','query_result': rows})
        except Exception as e:
            error_message = "Error: {}".format(str(e))
            transaction.set_rollback(True)
            return render(request, 'list_stadium.html', {'message': 'Stadiums:','error_message': error_message})

def average_rating_view(request):
    username = request.session.get('username')
    with transaction.atomic():
        try:    
            with connection.cursor() as cursor:
                cursor.execute("SELECT AVG(rating) AS average_rating, COUNT(*) AS total_rated_sessions FROM Match_Event WHERE assigned_jury_username = %s;", [username])   
                rows = cursor.fetchall()             
            # success_message = "Match Session is successfully deleted."
            return render(request, 'average_rating.html', {'message': 'Average Ratings','query_result': rows})
        except Exception as e:
            error_message = "Error: {}".format(str(e))
            transaction.set_rollback(True)
            return render(request, 'average_rating.html', {'message': 'Average Rating:','error_message': error_message})

def list_player_view(request):
    username = request.session.get('username')
    with transaction.atomic():
        try:    
            with connection.cursor() as cursor:
                cursor.execute("SELECT DISTINCT u.name, u.surname FROM users u JOIN players_playin_matches ppm ON u.username = ppm.username WHERE ppm.session_id IN ( SELECT session_id FROM players_playin_matches WHERE username =  %s) AND u.username !=  %s ",[username,username])   
                rows = cursor.fetchall()             
            # success_message = "Match Session is successfully deleted."
            return render(request, 'list_player.html', {'message': 'Players that Played Within a Session Once:','query_result': rows})
        except Exception as e:
            error_message = "Error: {}".format(str(e))
            transaction.set_rollback(True)
            return render(request, 'list_player.html', {'message': 'Players that Played Within a Session Once:','error_message': error_message})

def average_height_view(request):
    username = request.session.get('username')
    with transaction.atomic():
        try:    
            with connection.cursor() as cursor:
                cursor.execute("""
                   SELECT
    CASE
        WHEN COUNT(DISTINCT ppm2.username) > 1 THEN AVG(p.height)
        ELSE MAX(p.height)
    END AS height
FROM
    Players_PlayIn_Matches ppm
JOIN
    Match_Event me ON ppm.session_id = me.session_id
JOIN
    Players_PlayIn_Matches ppm2 ON me.session_id = ppm2.session_id
JOIN
    Users u ON ppm2.username = u.username
JOIN
    Players p ON u.username = p.username
WHERE
    ppm.username = %s
    AND u.username != %s
GROUP BY
    ppm.username;
                    """,[username,username])   
                rows = cursor.fetchall()             
            return render(request, 'average_height.html', {'message': '(Average) Height of the Most Played Player:','query_result': rows})
        except Exception as e:
            error_message = "Error: {}".format(str(e))
            transaction.set_rollback(True)
            return render(request, 'average_height.html', {'message': '(Average) Height of the Most Played Player:','error_message': error_message})

def add_new_session_view(request):
    username = request.session.get('username')
    if request.method == 'POST':
        form = NewSessionForm(request.POST)
        if form.is_valid():
            session_id = form.cleaned_data['session_id']
            jury_name = form.cleaned_data['jury_name']
            jury_surname = form.cleaned_data['jury_surname']
            date = form.cleaned_data['date']
            rating = form.cleaned_data['rating']
            time_slot = form.cleaned_data['time_slot']
            stadium_id = form.cleaned_data['stadium_id']

            with transaction.atomic():
                try:
                    # Retrieve the latest team_id from Leads
                    with connection.cursor() as cursor:
                        cursor.execute("""SELECT team_id FROM Leads WHERE coach_username = %s ORDER BY STR_TO_DATE(contract_end_time,'%%d.%%m.%%Y') DESC LIMIT 1;""", [username])
                        row = cursor.fetchone()
                        if row:
                            team_id = row[0]
                        else:
                            # Handle the case where no team_id is found
                            raise Exception("No team_id found in Leads table")
                        
                    with connection.cursor() as cursor:
                        cursor.execute("SELECT Juries.username FROM Juries JOIN Users ON Users.username = Juries.username WHERE Users.name = %s AND Users.surname = %s", [jury_name, jury_surname])
                        row2 = cursor.fetchone()
                        if row2:
                            assigned_jury_username = row2[0]
                        else:
                            # Handle the case where no team_id is found
                            raise Exception("No jury found in juries")
                    # Insert the new session into Match_Event table
                    with connection.cursor() as cursor:
                        cursor.execute("""
                            INSERT INTO Match_Event (session_id, team_id, assigned_jury_username, date, rating, time_slot, stadium_id)
                            values (%s, %s, %s, %s, %s, %s, %s)
                            
                        """,[session_id, team_id, assigned_jury_username, date, rating, time_slot, stadium_id])
                        cursor.execute(""" INSERT INTO Match_PlayedBy_Team(session_id, team_id)
                                           VALUES(%s, %s)""", [session_id, team_id])
                    with connection.cursor() as cursor:
                        cursor.execute("""SELECT * FROM Leads WHERE team_id = %s AND STR_TO_DATE(contract_start_time,'%%d.%%m.%%Y') <= STR_TO_DATE(%s,'%%d.%%m.%%Y') AND STR_TO_DATE(contract_end_time,'%%d.%%m.%%Y') >= STR_TO_DATE(%s,'%%d.%%m.%%Y');""",[team_id,date,date])

                        #cursor.execute("""SELECT * FROM Leads WHERE team_id = %s AND STR_TO_DATE(contract_start_time,'"""+'%'+"""d-%m-%Y') <= STR_TO_DATE(%s,'"""+'%'+"""d-%m-%Y') AND STR_TO_DATE(contract_end_time,'"""+'%'+"""d-%m-%Y') >= STR_TO_DATE(%s,'"""+'%'+"""d-%m-%Y');""",[team_id,date,date])
                    success_message = "Session is successfully added."
                    return render(request, 'coach.html', {'success_message': success_message})
                except Exception as e:
                    error_message = "Error: {}".format(str(e))
                    transaction.set_rollback(True)
                    
                    return render(request, 'coach.html', {'error_message': error_message, 'form': form})

    else:
        form = NewSessionForm()
        return render(request, 'add_new_session.html', {'form': form})
    
def rate_session_view(request):
    results = []
    username = request.session.get('username')
    if request.method == 'POST':
        form = RateSessionForm(request.POST)
        if form.is_valid():
            # session_id = form.cleaned_data['session_id']
            rate = form.cleaned_data['rate']
            date = form.cleaned_data['date']
            session_id = form.cleaned_data['session_id']
            with transaction.atomic():
                try:    
                    with connection.cursor() as cursor:
                        cursor.execute("""SELECT session_id
                        FROM Match_Event
                        WHERE assigned_jury_username = %s AND rating IS NULL 
                        AND STR_TO_DATE(%s, '%%d-%%m-%%Y') >= STR_TO_DATE(date, '%%d-%%m-%%Y')""",
                        [username, date])
                        rows = cursor.fetchall()
                        for row in rows:
                            results.append(row[0])
                        if session_id in (results):
                            cursor.execute("UPDATE Match_Event SET rating = %s WHERE session_id = %s ;", [rate, session_id])
                            success_message = "Session is rated."
                            return render(request, 'jury.html', {'message': 'hey jury!','success_message': success_message})
                        else:
                            transaction.set_rollback(True)
                            return render(request, 'jury.html', {'message': 'hey jury!','error_message': 'Enter a valid session_id'})
                except Exception as e:
                    error_message = "Error: {}".format(str(e))
                    transaction.set_rollback(True)
                    return render(request, 'jury.html', {'message': 'hey jury!','error_message': error_message})
    else:
        form = RateSessionForm()
    return render(request, 'rate_session.html', {'form': form})
def squad_view(request):
    username = request.session.get('username')
    names = []
    players = []
    if request.method == 'POST':
        form = SquadForm(request.POST)
        if form.is_valid():
            session_id = form.cleaned_data['session_id']
            player1 = form.cleaned_data['player1']
            player2 = form.cleaned_data['player2']
            player3 = form.cleaned_data['player3']
            player4 = form.cleaned_data['player4']
            player5 = form.cleaned_data['player5']
            player6 = form.cleaned_data['player6']
            players = [player1, player2, player3, player4, player5, player6]
            position1 = form.cleaned_data['position1']
            position2 = form.cleaned_data['position2']
            position3 = form.cleaned_data['position3']
            position4 = form.cleaned_data['position4']
            position5 = form.cleaned_data['position5']
            position6 = form.cleaned_data['position6']
            with transaction.atomic():
                try:    
                    with connection.cursor() as cursor:
                        cursor.execute("""SELECT team_id FROM Leads WHERE coach_username = %s ORDER BY STR_TO_DATE(contract_end_time,'%%d.%%m.%%Y') DESC LIMIT 1;""", [username])
                        row = cursor.fetchone()
                        if row:
                            team_id = row[0]
                        else:
                            # Handle the case where no team_id is found
                            raise Exception("No team_id found")
                        cursor.execute("""SELECT name
                                    FROM Users
                                    JOIN Player_Registered_Team ON Player_Registered_Team.username = Users.username
                                    WHERE team_id = %s;
                                    """, [team_id])
                        rows = cursor.fetchall()
                        for row in rows:
                            names.append(row[0])
                        all_names_present = all(name in names for name in players)
                        if all_names_present:

                            cursor.execute("""
SELECT Users.username FROM Users JOIN Players ON Players.username = Users.username WHERE Users.name = %s""", [player1])
                            username1 = cursor.fetchall()
                            cursor.execute("""
SELECT Users.username FROM Users JOIN Players ON Players.username = Users.username WHERE Users.name = %s""", [player2])
                            username2 = cursor.fetchall()
                            cursor.execute("""
SELECT Users.username FROM Users JOIN Players ON Players.username = Users.username WHERE Users.name = %s""", [player3])
                            username3 = cursor.fetchall()
                            cursor.execute("""
SELECT Users.username FROM Users JOIN Players ON Players.username = Users.username WHERE Users.name = %s""", [player4])
                            username4 = cursor.fetchall()
                            cursor.execute("""
SELECT Users.username FROM Users JOIN Players ON Players.username = Users.username WHERE Users.name = %s""", [player5])
                            username5 = cursor.fetchall()
                            cursor.execute("""
SELECT Users.username FROM Users JOIN Players ON Players.username = Users.username WHERE Users.name = %s""", [player6])
                            username6 = cursor.fetchall()
                            cursor.execute("""INSERT INTO Players_PlayIn_Matches (squad_id, username, session_id, position_id)
                            VALUES  (150,%s, %s, %s),
                            (151,%s, %s, %s),
                            (152,%s, %s, %s),
                            (153,%s, %s, %s),
                            (154,%s, %s, %s),
                            (155,%s, %s, %s)""",[username1,session_id,position1,username2,session_id,position2,username3,session_id,position3,username4,session_id,position4,username5,session_id,position5,username6,session_id,position6])


                        else:
                            transaction.set_rollback(True)
                            return render(request, 'coach.html', {'message': 'hey coach!','error_message': 'Enter valid player names'})

                    success_message = "Squad is successfully added."
                    return render(request, 'coach.html', {'message': 'hey coach!','success_message': success_message})
                except Exception as e:
                    error_message = "Error: {}".format(str(e))
                    transaction.set_rollback(True)
                    return render(request, 'coach.html', {'message': 'hey coach!','error_message': error_message})
    else:
        form = SquadForm()
    return render(request, 'squad.html', {'form': form})


def dashboard_view(request):
    return render(request, 'dashboard.html', {'message': 'Welcome!'})

def player_view(request):
    return render(request, 'player.html', {'message': 'hey player!'})

def jury_view(request):
    return render(request, 'jury.html', {'message': 'hey jury!'})

def coach_view(request):
    return render(request, 'coach.html', {'message': 'hey coach!'})

def dbmanager_view(request):
    return render(request, 'dbmanager.html', {'message': 'hey manager!'})

