-- DROP DATABASE IF EXISTS zdravstvena_ustanova;
CREATE DATABASE IF NOT EXISTS zdravstvena_ustanova;
USE zdravstvena_ustanova;

CREATE TABLE IF NOT EXISTS pacijent(
ime VARCHAR(100) NOT NULL,
prezime VARCHAR(100) NOT NULL,
jmbg VARCHAR(13) NOT NULL UNIQUE,
adresa VARCHAR(100) NOT NULL,
telefon VARCHAR(15)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

CREATE TABLE IF NOT EXISTS doktor(
ime VARCHAR(100) NOT NULL,
prezime VARCHAR(100) NOT NULL,
jmbg VARCHAR(13) NOT NULL UNIQUE,
specijalizacija VARCHAR(100) NOT NULL,
br_licence VARCHAR(20) NOT NULL UNIQUE
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

CREATE TABLE IF NOT EXISTS medikament(
naziv VARCHAR(50) NOT NULL,
sifra VARCHAR(50) NOT NULL UNIQUE
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

CREATE TABLE IF NOT EXISTS bolest(
naziv VARCHAR(50) NOT NULL,
opis VARCHAR(50) NOT NULL,
slika BLOB NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

CREATE TABLE IF NOT EXISTS proizvodjac(
naziv VARCHAR(50) NOT NULL,
adresa VARCHAR(50) NOT NULL,
tel VARCHAR(15) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

CREATE TABLE IF NOT EXISTS boluje_od(
datum_dijagnoze DATETIME NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

ALTER TABLE pacijent ADD COLUMN id_pacijent INT PRIMARY KEY AUTO_INCREMENT;

ALTER TABLE doktor ADD PRIMARY KEY (br_licence);

ALTER TABLE medikament ADD PRIMARY KEY (sifra);

ALTER TABLE bolest ADD PRIMARY KEY (naziv);

ALTER TABLE proizvodjac ADD PRIMARY KEY (naziv);

ALTER TABLE pacijent ADD COLUMN doktor_br_licence VARCHAR(20);

ALTER TABLE pacijent
ADD CONSTRAINT fk_pacijent_doktor_br_licence FOREIGN KEY (doktor_br_licence) REFERENCES doktor (br_licence);

ALTER TABLE medikament ADD COLUMN proizvodjac_naziv VARCHAR (50);

ALTER TABLE medikament 
ADD CONSTRAINT fk_proizvodjac_naziv FOREIGN KEY (proizvodjac_naziv) REFERENCES proizvodjac (naziv);

ALTER TABLE boluje_od ADD COLUMN (id_pacijent INT, doktor_br_licence VARCHAR (20), bolest_naziv VARCHAR(50));

ALTER TABLE boluje_od
ADD CONSTRAINT fk_id_pacijent FOREIGN KEY (id_pacijent) REFERENCES pacijent (id_pacijent),
ADD CONSTRAINT fk_boluje_od_doktor_br_licence FOREIGN KEY (doktor_br_licence) REFERENCES doktor (br_licence),
ADD CONSTRAINT fk_bolest_naziv FOREIGN KEY (bolest_naziv) REFERENCES bolest (naziv);

ALTER TABLE bolest DROP COLUMN slika;

ALTER TABLE proizvodjac RENAME COLUMN tel TO telefon;

CREATE TABLE IF NOT EXISTS nova_tabela(
doktor_br_licence VARCHAR(20),
proizvodjac_naziv VARCHAR (50),
FOREIGN KEY (doktor_br_licence) REFERENCES pacijent (doktor_br_licence),
FOREIGN KEY (proizvodjac_naziv) REFERENCES medikament (proizvodjac_naziv)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

INSERT INTO doktor (ime, prezime, jmbg, specijalizacija, br_licence)
VALUES ('ime 1', 'prezime 1', '9438581939542', 'specijalizacija 1', '9348341'),
	   ('ime 2', 'prezime 2', '3734187431478', 'specijalizacija 2', '3474317'),
       ('ime 3', 'prezime 3', '318943179y431', 'specijalizacija 3', '4894431');
       
INSERT INTO bolest (naziv, opis)
VALUES ('ime bolesti 1', 'opis 1'),
	   ('ime bolesti 2', 'opis 2'),
       ('ime bolesti 3', 'opis 3');
       
INSERT INTO proizvodjac (naziv, adresa, telefon)
VALUES ('naziv proizvodjaca 1', 'adresa 1', '0114313481'),
	   ('naziv proizvodjaca 2', 'adresa 2', '0341843184'),
       ('naziv proizvodjaca 3', 'adresa 3', '0134942592');

INSERT INTO medikament (naziv, sifra, proizvodjac_naziv)
VALUES ('ime leka 1', '381348', 'naziv proizvodjaca 1'),
	   ('ime leka 2', '348481', 'naziv proizvodjaca 2'),
       ('ime leka 3', '134942', 'naziv proizvodjaca 3');

INSERT INTO pacijent (ime, prezime, jmbg, adresa, telefon, doktor_br_licence)
VALUES ('ime pacijenta 1', 'prezime pacijenta 1', '3943498314814', 'adresa 1', '063943491', '9348341'),
	   ('ime pacijenta 2', 'prezime pacijanta 2', '1349542094149', 'adresa 2', '064452552', '3474317'),
       ('ime pacijenta 3', 'prezime pacijenta 3', '4310549204134', 'adresa 3', '069349431', '4894431');
       
INSERT INTO boluje_od (datum_dijagnoze, id_pacijent, doktor_br_licence, bolest_naziv)
VALUES ('2022-12-21', 1, '9348341', 'ime bolesti 1'),
	   ('2021-12-21', 2, '3474317', 'ime bolesti 2'),
       ('2022-12-20', 3, '4894431', 'ime bolesti 3');
       
INSERT INTO nova_tabela (doktor_br_licence, proizvodjac_naziv)
VALUES ('9348341', 'naziv proizvodjaca 1'),
	   ('3474317', 'naziv proizvodjaca 2'),
       ('4894431', 'naziv proizvodjaca 3');
       
DELETE FROM nova_tabela;
DELETE FROM boluje_od;
DELETE FROM pacijent;
DELETE FROM medikament;
DELETE FROM proizvodjac;
DELETE FROM bolest;
DELETE FROM doktor;
       
DROP TABLE nova_tabela;
DROP TABLE boluje_od;
DROP TABLE pacijent;
DROP TABLE medikament;
DROP TABLE proizvodjac;
DROP TABLE bolest;
DROP TABLE doktor;

DROP DATABASE zdravstvena_ustanova;
