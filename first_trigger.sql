DELIMITER //

DROP TRIGGER if exists before_insert_match_event //

CREATE TRIGGER before_insert_match_event
BEFORE INSERT ON Match_Event
FOR EACH ROW
BEGIN
    DECLARE conflicting_matches INT;
    DECLARE match_duration INT;
    DECLARE existing_match_in_slot3 INT;
    DECLARE team_matches_at_date INT;
    DECLARE team_match_slot1_count INT;
    DECLARE team_match_slot2_count INT;
   
    -- Check for conflicting matches
    SELECT COUNT(*)
    INTO conflicting_matches
    FROM Match_Event
    WHERE date = NEW.date
    AND time_slot = NEW.time_slot
    AND stadium_id = NEW.stadium_id;

    IF conflicting_matches > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Conflicting matches exist for the given date, time slot, and stadium.';
    END IF;

    -- Check for match duration
    SELECT COUNT(*)
    INTO match_duration
    FROM Match_Event
    WHERE date = NEW.date
    AND stadium_id = NEW.stadium_id
    AND time_slot IN (1, 3);

    IF match_duration >= 2 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Match duration constraint violated. Only 2 matches allowed for the same date and stadium, starting at time slot 1 or 3.';
    END IF;

    -- Check for new entry with same date and stadium_id if existing match time_slot is 2 or 3
    IF EXISTS (
        SELECT 1
        FROM Match_Event
        WHERE date = NEW.date
        AND stadium_id = NEW.stadium_id
        AND time_slot = 2
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot insert a new entry with the same date and stadium_id if the existing match time slot is 2 or 3.';
    END IF;
    
    -- Check if there exists a match in time_slot 3 for the same date and stadium_id
    SELECT COUNT(*)
    INTO existing_match_in_slot3
    FROM Match_Event
    WHERE date = NEW.date
    AND stadium_id = NEW.stadium_id
    AND time_slot = 3;

    IF existing_match_in_slot3 > 0 AND NEW.time_slot = 2 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot insert a match with time_slot 2 when there is a match with time_slot 3 for the same date and stadium_id.';
    END IF;
     -- Check the number of matches for the same team_id at the same date
    SELECT COUNT(*)
    INTO team_matches_at_date
    FROM Match_Event
    WHERE date = NEW.date
    AND team_id = NEW.team_id;

    IF team_matches_at_date >= 2 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'The same team cannot have more than 2 matches at the same date.';
    END IF;

    -- Check if the same team_id already has a match in time_slot 1 for the same date
    SELECT COUNT(*)
    INTO team_match_slot1_count
    FROM Match_Event
    WHERE date = NEW.date
    AND team_id = NEW.team_id
    AND time_slot = 1;

    IF team_match_slot1_count > 0 AND NEW.time_slot = 2 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'The same team cannot have a match in time_slot 2 if it already has a match in time_slot 1 for the same date.';
    END IF;

    -- Check if the same team_id already has a match in time_slot 2 for the same date
    SELECT COUNT(*)
    INTO team_match_slot2_count
    FROM Match_Event
    WHERE date = NEW.date
    AND team_id = NEW.team_id
    AND time_slot = 2;

    IF team_match_slot2_count > 0 AND NEW.time_slot = 3 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'The same team cannot have a match in time_slot 3 if it already has a match in time_slot 2 for the same date.';
    END IF;
    
     IF EXISTS (
        SELECT 1
        FROM Match_Event
        WHERE date = NEW.date
        AND team_id = NEW.team_id
        AND time_slot = NEW.time_slot
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'The same team cannot have a match in the same time_slot for the same date.';
    END IF;
    
END //

DELIMITER ;

