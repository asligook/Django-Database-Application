DELIMITER //

DROP TRIGGER IF EXISTS before_insert_squad_event //

CREATE TRIGGER before_insert_squad_event
BEFORE INSERT ON Players_PlayIn_Matches
FOR EACH ROW
BEGIN
    DECLARE session_count INT;
    DECLARE position_exists INT;
    DECLARE player_exists INT;
    DECLARE max_squad_id INT;

    -- Check if the combination of username and position_id exists in Have_Positions table
    SELECT COUNT(*)
    INTO position_exists
    FROM Have_Positions
    WHERE username = NEW.username AND position_id = NEW.position_id;

    IF position_exists = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot insert entry for a player who does not have the specified position.';
    END IF;

    -- Check if there are already 6 rows for the same session_id
    SELECT COUNT(*)
    INTO session_count
    FROM Players_PlayIn_Matches
    WHERE session_id = NEW.session_id;

    IF session_count >= 6 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot insert more than 6 rows for the same session_id.';
    END IF;
    
    -- Check if the combination of session_id and username is unique
    SELECT COUNT(*)
    INTO player_exists
    FROM Players_PlayIn_Matches
    WHERE session_id = NEW.session_id AND username = NEW.username;

    IF player_exists > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot insert entry with the same username for the same session_id.';
    END IF;
    
     -- Get the maximum squad_id and increment by 1
    SELECT IFNULL(MAX(squad_id), 0) + 1
    INTO max_squad_id
    FROM Players_PlayIn_Matches;

    -- Set the new squad_id for the inserted row
    SET NEW.squad_id = max_squad_id;
END //

DELIMITER ;


