-- 1
INSERT INTO class (ClassName) VALUES ("Regular");
UPDATE pax SET ClassID = 5;

-- 2
UPDATE aircraft, aircrafttype
SET aircraft.AircraftTypeID = (SELECT aircrafttype.AircraftTypeID 
FROM aircrafttype
WHERE aircrafttype.AircraftName LIKE "%330%")
WHERE aircrafttype.AircraftName LIKE "Boeing%" OR aircrafttype.AircraftName LIKE "M" OR aircrafttype.AircraftName LIKE "W";

-- 3
SELECT RouteID, Distance
FROM route
WHERE Distance > (SELECT AVG (Distance) FROM route)
ORDER BY Distance DESC;

-- 4
SELECT flightid
FROM flight
WHERE flight.RouteID IN (SELECT RouteID FROM route WHERE (FromAirport = (SELECT AirportID FROM airport WHERE AirportName LIKE "Heathrow%")
OR ToAirport = (SELECT AirportID FROM airport WHERE AirportName LIKE "Heathrow%")))
ORDER BY FlightID DESC;

-- 5
SELECT *
FROM route
WHERE Distance > (SELECT AVG (Distance) FROM route);

-- 6
SELECT *
FROM flight
WHERE AircraftID IN (
	SELECT AircraftID
	FROM aircraft
    WHERE AircraftTypeID IN (
		SELECT AircraftTypeID
        FROM aircrafttype
        WHERE AircraftName LIKE "%SW%"));













