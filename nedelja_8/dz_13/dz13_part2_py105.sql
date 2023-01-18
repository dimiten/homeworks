-- 1
SELECT AirportName, NumTerminals
FROM airport
WHERE NumTerminals > 2;

-- 2
SELECT COUNT(*) AS NumFlightsHighestDistance
FROM flight
WHERE flight.RouteID = 
	(SELECT route.RouteID
    FROM route
    WHERE Distance = 
		(SELECT MAX(Distance) 
		 FROM route));
         
-- 3
SELECT AircraftName, COUNT(AircraftID) AS NumAircrafts
FROM aircrafttype
LEFT JOIN aircraft
ON aircrafttype.AircraftTypeID = aircraft.AircraftTypeID
GROUP BY AircraftName
ORDER BY NumAircrafts DESC;

-- 4
SELECT AircraftName, COUNT(AircraftID) AS NumAircrafts
FROM aircraft
RIGHT JOIN aircrafttype
ON aircrafttype.AircraftTypeID = aircraft.AircraftTypeID
GROUP BY AircraftName
ORDER BY NumAircrafts DESC;

-- 5
SELECT DepDay, NumFlights
FROM (
	SELECT DepDay, COUNT(*) AS NumFlights
	FROM flightdep
	GROUP BY DepDay) AS derived_table1
WHERE NumFlights > (SELECT AVG(NumFlights) FROM (
	SELECT DepDay, COUNT(*) AS NumFlights
	FROM flightdep
	GROUP BY DepDay) AS derived_table2);

-- 6
SELECT flightid
FROM flight
WHERE flight.RouteID IN (SELECT RouteID FROM route WHERE (FromAirport = (SELECT AirportID FROM airport WHERE AirportName LIKE "Heathrow%")
OR ToAirport = (SELECT AirportID FROM airport WHERE AirportName LIKE "Heathrow%")))
ORDER BY FlightID DESC;

