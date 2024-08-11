INSERT INTO DatabaseManagers(username, password)
VALUES 
    ('Kevin', 'Kevin'),
    ('Bob', 'Bob'),
    ('sorunlubirarkadas', 'muvaffakiyetsizleştiricileştiriveremeyebileceklerimizdenmişsinizcesine');
    
    
INSERT INTO Users (username, password, name, surname)
VALUES 
    ('g_orge', 'Go.1993', 'Gizem', 'Örge'),
    ('c_ozbay', 'Co.1996', 'Cansu', 'Özbay'),
    ('m_vargas', 'Mv.1999', 'Melissa', 'Vargas'),
    ('h_baladin', 'Hb.2007', 'Hande', 'Baladın'),
    ('a_kalac', 'Ak.1995', 'Aslı', 'Kalaç'),
    ('ee_dundar', 'Eed.2008', 'Eda Erdem', 'Dündar'),
    ('z_gunes', 'Zg.2008', 'Zehra', 'Güneş'),
    ('i_aydin', 'Ia.2007', 'İlkin', 'Aydın'),
    ('e_sahin', 'Es.2001', 'Elif', 'Şahin'),
    ('e_karakurt', 'Ek.2006', 'Ebrar', 'Karakurt'),
    ('s_akoz', 'Sa.1991', 'Simge', 'Aköz'),
    ('k_akman', 'Ka.2006', 'Kübra', 'Akman'),
    ('d_cebecioglu', 'Dc.2007', 'Derya', 'Cebecioğlu'),
    ('a_aykac', 'Aa.1996', 'Ayşe', 'Aykaç'),
    ('user_2826', 'P.45825', 'Brenda', 'Schulz'),
    ('user_9501', 'P.99695', 'Erika', 'Foley'),
    ('user_3556', 'P.49595', 'Andrea', 'Campbell'),
    ('user_7934', 'P.24374', 'Beatrice', 'Bradley'),
    ('user_4163', 'P.31812', 'Betsey', 'Lenoir'),
    ('user_2835', 'P.51875', 'Martha', 'Lazo'),
    ('user_8142', 'P.58665', 'Wanda', 'Ramirez'),
    ('user_2092', 'P.16070', 'Eileen', 'Ryen'),
    ('user_3000', 'P.73005', 'Stephanie', 'White'),
    ('user_8323', 'P.33562', 'Daenerys', 'Targaryen');
    
INSERT INTO Users (username, password, name, surname)
VALUES 
    ('d_santarelli', 'santa.really1', 'Daniele', 'Santarelli'),
    ('g_guidetti', 'guidgio.90', 'Giovanni', 'Guidetti'),
    ('f_akbas', 'a.fatih55', 'Ferhat', 'Akbaş'),
    ('m_hebert', 'm.hebert45', 'Mike', 'Hebert'),
    ('o_deriviere', 'oliviere_147', 'Oliviere', 'Deriviere'),
    ('a_derune', 'aderune_147', 'Amicia', 'Derune');
    
INSERT INTO Users (username, password, name, surname)
VALUES 
    ('o_ozcelik', 'ozlem.0347', 'Özlem', 'Özçelik'),
    ('m_sevinc', 'mehmet.0457', 'Mehmet', 'Sevinç'),
    ('e_sener', 'ertem.4587', 'Ertem', 'Şener'),
    ('s_engin', 'sinan.6893', 'Sinan', 'Engin');

INSERT INTO Players (username, date_of_birth, height, weight)
VALUES 
    ('g_orge', '26-04-1993', 170, 59),
    ('c_ozbay', '17-10-1996', 182, 78),
    ('m_vargas', '16-10-1999', 194, 76),
    ('h_baladin', '01-09-2007', 190, 81),
    ('a_kalac', '13-12-1995', 185, 73),
    ('ee_dundar', '22-06-2008', 188, 74),
    ('z_gunes', '07-07-2008', 197, 88),
    ('i_aydin', '05-01-2007', 183, 67),
    ('e_sahin', '19-01-2001', 190, 68),
    ('e_karakurt', '17-01-2006', 196, 73),
    ('s_akoz', '23-04-1991', 168, 55),
    ('k_akman', '13-10-2006', 200, 88),
    ('d_cebecioglu', '24-10-2007', 187, 68),
    ('a_aykac', '27-02-1996', 176, 57),
    ('user_2826', '13-12-2002', 193, 80),
    ('user_9501', '21-12-1995', 164, 62),
    ('user_3556', '26-04-1996', 185, 100),
    ('user_7934', '28-05-1997', 150, 57),
    ('user_4163', '07-05-1993', 156, 48),
    ('user_2835', '20-05-2001', 173, 71),
    ('user_8142', '03-01-1994', 183, 94),
    ('user_2092', '21-06-2004', 188, 60),
    ('user_3000', '19-05-2002', 193, 74),
    ('user_8323', '16-09-2006', 222, 74);
    
INSERT INTO Positions (position_id, position_name)
VALUES 
    (0, 'Libero'),
    (1, 'Setter'),
    (2, 'Opposite hitter'),
    (3, 'Outside hitter'),
    (4, 'Middle blocker');
    
INSERT INTO Have_Positions (player_position_id, username, position_id)
VALUES 
    (1, 'g_orge', 0),
    (2, 'g_orge', 3),
    (3, 'c_ozbay', 1),
    (4, 'm_vargas', 2),
    (5, 'h_baladin', 3),
    (6, 'a_kalac', 4),
    (7, 'ee_dundar', 4),
    (8, 'z_gunes', 4),
    (9, 'i_aydin', 1),
    (10, 'i_aydin', 3),
    (11, 'e_sahin', 1),
    (12, 'e_sahin', 3),
    (13, 'e_karakurt', 2),
    (14, 'e_karakurt', 3),
    (15, 's_akoz', 0),
    (16, 'k_akman', 0),
    (17, 'k_akman', 4),
    (18, 'd_cebecioglu', 3),
    (19, 'd_cebecioglu', 4),
    (20, 'a_aykac', 0),
    (21, 'user_2826', 2),
    (22, 'user_2826', 1),
    (23, 'user_9501', 0),
    (24, 'user_9501', 4),
    (25, 'user_3556', 1),
    (26, 'user_3556', 0),
    (27, 'user_7934', 4),
    (28, 'user_7934', 2),
    (29, 'user_4163', 3),
    (30, 'user_4163', 0),
    (31, 'user_2835', 2),
    (32, 'user_2835', 3),
    (33, 'user_8142', 1),
    (34, 'user_8142', 3),
    (35, 'user_2092', 4),
    (36, 'user_2092', 2),
    (37, 'user_3000', 1),
    (38, 'user_3000', 4),
    (39, 'user_8323', 3),
    (40, 'user_8323', 2);
    
INSERT INTO Coaches (username, nationality)
VALUES 
    ('d_santarelli', 'ITA'),
    ('g_guidetti', 'ITA'),
    ('f_akbas', 'TR'),
    ('m_hebert', 'US'),
    ('o_deriviere', 'FR'),
    ('a_derune', 'FR');

INSERT INTO Channels (channel_ID, channel_name)
VALUES 
    (0, 'BeIN Sports'),
    (1, 'Digiturk'),
    (2, 'TRT');
    
INSERT INTO Teams (team_ID, team_name, channel_ID)
VALUES 
    (0, 'Women A', 0),
    (1, 'Women B', 1),
    (2, 'U19', 0),
    (3, 'Women B', 1),
    (4, 'Women C', 1),
    (5, 'U19', 2),
    (6, 'U19', 2);

INSERT INTO Player_Registered_Team (player_teams_id, username, team_id)
VALUES 
    (1, 'g_orge', 0),
    (2, 'c_ozbay', 0),
    (3, 'c_ozbay', 1),
    (4, 'm_vargas', 0),
    (5, 'm_vargas', 1),
    (6, 'h_baladin', 0),
    (7, 'h_baladin', 2),
    (8, 'a_kalac', 0),
    (9, 'a_kalac', 1),
    (10, 'ee_dundar', 0),
    (11, 'ee_dundar', 2),
    (12, 'z_gunes', 0),
    (13, 'z_gunes', 2),
    (14, 'i_aydin', 1),
    (15, 'i_aydin', 2),
    (16, 'e_sahin', 0),
    (17, 'e_karakurt', 0),
    (18, 'e_karakurt', 2),
    (19, 's_akoz', 0),
    (20, 's_akoz', 1),
    (21, 'k_akman', 0),
    (22, 'k_akman', 2),
    (23, 'd_cebecioglu', 0),
    (24, 'd_cebecioglu', 1),
    (25, 'a_aykac', 0),
    (26, 'user_2826', 2),
    (27, 'user_2826', 3),
    (28, 'user_9501', 0),
    (29, 'user_9501', 3),
    (30, 'user_3556', 2),
    (31, 'user_3556', 3),
    (32, 'user_7934', 0),
    (33, 'user_7934', 3),
    (34, 'user_4163', 1),
    (35, 'user_4163', 3),
    (36, 'user_2835', 2),
    (37, 'user_2835', 3),
    (38, 'user_8142', 0),
    (39, 'user_8142', 3),
    (40, 'user_2092', 2),
    (41, 'user_2092', 3),
    (42, 'user_3000', 2),
    (43, 'user_3000', 3),
    (44, 'user_8323', 0),
    (45, 'user_8323', 3);

INSERT INTO Juries (username, nationality)
VALUES 
    ('o_ozcelik', 'TR'),
    ('m_sevinc', 'TR'),
    ('e_sener', 'TR'),
    ('s_engin', 'TR');
    
INSERT INTO Leads (lead_id, coach_username, contract_start_time, contract_end_time, team_id)
VALUES 
    (1, 'd_santarelli', '25-12-2021', '12-12-2025', 0),
    (2, 'g_guidetti', '11-09-2021', '11-09-2026', 1),
    (3, 'f_akbas', '10-08-2021', '10-08-2026', 2),
    (4, 'f_akbas', '10-08-2000', '10-08-2015', 3),
    (5, 'm_hebert', '01-04-2024', '21-07-2026', 4),
    (6, 'o_deriviere', '10-08-2015', '09-08-2020', 5),
    (7, 'a_derune', '10-08-2005', '10-08-2010', 6);
    
INSERT INTO Stadiums (stadium_id, stadium_name, stadium_country)
VALUES 
    (0, 'Burhan Felek Voleybol Salonu', 'TR'),
    (1, 'GD Voleybol Arena', 'TR'),
    (2, 'Copper Box Arena', 'UK');
    
INSERT INTO Match_Event (session_id, team_id, assigned_jury_username, date, rating, time_slot, stadium_id)
VALUES 
    (0, 0, 'o_ozcelik', '10-03-2024', '4.5', 1, 0),
    (1, 1, 'o_ozcelik', '03-04-2024', '4.9', 1, 1),
    (2, 0, 'o_ozcelik', '03-04-2024', '4.4', 3, 1),
    (3, 2, 'm_sevinc', '03-04-2024', '4.9', 2, 2),
    (4, 3, 'e_sener', '03-04-2023', '4.5', 2, 2),
    (5, 3, 's_engin', '27-05-2023', '4.4', 1, 1),
    (6, 0, 'm_sevinc', '01-09-2022', '4.6', 1, 1),
    (7, 0, 'o_ozcelik', '02-05-2023', '4.7', 3, 2),
    (8, 1, 'o_ozcelik', '10-02-2024', '4.5', 1, 0);
    
INSERT INTO Match_PlayedBy_Team (session_id, team_id)
VALUES 
    (0, 0),
    (1, 1),
    (2, 0),
    (3, 2),
    (4, 3),
    (5, 3),
    (6, 0),
    (7, 0),
    (8, 1);

INSERT INTO Players_PlayIn_Matches(squad_id,username, session_id, position_id)
VALUES 
    (1, 'g_orge', 0, 0),
    (2, 'c_ozbay', 0, 1),
    (3, 'm_vargas', 0, 2),
    (4, 'h_baladin', 0, 3),
    (5, 'a_kalac', 0, 4),
    (6, 'ee_dundar', 0, 4),
    (7, 'c_ozbay', 1, 1),
    (8, 'm_vargas', 1, 2),
    (9, 'i_aydin', 1, 1),
    (10, 'a_kalac', 1, 4),
    (11, 's_akoz', 1, 0),
    (12, 'd_cebecioglu', 1, 3),
    (13, 'g_orge', 2, 3),
    (14, 'm_vargas', 2, 2),
    (15, 'c_ozbay', 2, 1),
    (16, 'a_kalac', 2, 4),
    (17, 's_akoz', 2, 0),
    (18, 'a_aykac', 2, 0),
    (19, 'ee_dundar', 3, 4),
    (20, 'h_baladin', 3, 3),
    (21, 'z_gunes', 3, 4),
    (22, 'i_aydin', 3, 3),
    (23, 'e_karakurt', 3, 2),
    (24, 'k_akman', 3, 0),
    (25, 'user_2826', 4, 2),
    (26, 'user_9501', 4, 0),
    (27, 'user_3556', 4, 1),
    (28, 'user_7934', 4, 4),
    (29, 'user_4163', 4, 3),
    (30, 'user_2835', 4, 2),
    (31, 'user_2826', 5, 1),
    (32, 'user_9501', 5, 4),
    (33, 'user_3556', 5, 0),
    (34, 'user_7934', 5, 2),
    (35, 'user_4163', 5, 0),
    (36, 'user_2835', 5, 3),
    (37, 'g_orge', 6, 0),
    (38, 'm_vargas', 6, 2),
    (39, 'c_ozbay', 6, 1),
    (40, 'a_kalac', 6, 4),
    (41, 'e_karakurt', 6, 3),
    (42, 'a_aykac', 6, 0),
    (43, 'g_orge', 7, 3),
    (44, 'm_vargas', 7, 2),
    (45, 'c_ozbay', 7, 1),
    (46, 'a_kalac', 7, 4),
    (47, 'e_karakurt', 7, 2),
    (48, 'a_aykac', 7, 0);
