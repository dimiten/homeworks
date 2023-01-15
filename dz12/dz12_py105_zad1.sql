-- DROP DATABASE IF EXISTS prodaja;
CREATE DATABASE IF NOT EXISTS prodaja;
USE prodaja;

CREATE TABLE IF NOT EXISTS kupac(
ime VARCHAR(100) NOT NULL,
prezime VARCHAR(100) NOT NULL,
jmbg VARCHAR(13) NOT NULL UNIQUE,
adresa VARCHAR(100) NOT NULL,
tel VARCHAR(15)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

CREATE TABLE IF NOT EXISTS mesto(
naziv VARCHAR(100) NOT NULL,
zip VARCHAR(5) NOT NULL,
zemlja VARCHAR(100) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

CREATE TABLE IF NOT EXISTS materijal(
naziv VARCHAR(100) NOT NULL,
opis VARCHAR(100) NOT NULL,
slika BLOB NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

CREATE TABLE IF NOT EXISTS proizvod(
naziv VARCHAR(100) NOT NULL,
opis VARCHAR(100) NOT NULL,
slika BLOB NOT NULL,
cena FLOAT NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

CREATE TABLE IF NOT EXISTS sastavnica(
kolicina INTEGER NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

CREATE TABLE IF NOT EXISTS kupovina_proizvoda(
kolicina INTEGER NOT NULL,
ukupna_cena FLOAT NOT NULL,
datum DATETIME
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

ALTER TABLE kupac
ADD COLUMN id_kupac INT PRIMARY KEY AUTO_INCREMENT;

ALTER TABLE mesto
ADD PRIMARY KEY (zip);

ALTER TABLE materijal
ADD PRIMARY KEY (naziv);

ALTER TABLE proizvod
ADD PRIMARY KEY (naziv);

ALTER TABLE sastavnica
ADD COLUMN proizvod_naziv VARCHAR (100);

ALTER TABLE sastavnica
ADD CONSTRAINT fk_proizvod FOREIGN KEY (proizvod_naziv) REFERENCES proizvod (naziv);

ALTER TABLE sastavnica
ADD COLUMN materijal_naziv VARCHAR (100);

ALTER TABLE kupac
ADD COLUMN mesto_zip VARCHAR (5);

ALTER TABLE kupac
ADD CONSTRAINT fk_mesto_kupac FOREIGN KEY (mesto_zip) REFERENCES mesto (zip);

ALTER TABLE sastavnica
ADD CONSTRAINT fk_materijal FOREIGN KEY (materijal_naziv) REFERENCES materijal (naziv);

ALTER TABLE kupovina_proizvoda
ADD COLUMN proizvod_naziv VARCHAR (100);

ALTER TABLE kupovina_proizvoda
ADD COLUMN mesto_zip VARCHAR (5);

ALTER TABLE kupovina_proizvoda
ADD COLUMN id_kupac INT;

ALTER TABLE kupovina_proizvoda
ADD CONSTRAINT fk_proizvod_kupovina FOREIGN KEY (proizvod_naziv) REFERENCES proizvod (naziv);

ALTER TABLE kupovina_proizvoda
ADD CONSTRAINT fk_mesto_zip FOREIGN KEY (mesto_zip) REFERENCES mesto (zip);

ALTER TABLE kupovina_proizvoda
ADD CONSTRAINT fk_kupac_id FOREIGN KEY (id_kupac) REFERENCES kupac (id_kupac);

ALTER TABLE materijal DROP COLUMN slika;
ALTER TABLE proizvod DROP COLUMN slika;

ALTER TABLE kupac RENAME COLUMN tel TO telefon;

CREATE TABLE IF NOT EXISTS nova_tabela(
mesto_zip VARCHAR(5),
proizvod_naziv VARCHAR (100),
FOREIGN KEY (mesto_zip) REFERENCES kupac (mesto_zip),
FOREIGN KEY (proizvod_naziv) REFERENCES sastavnica (proizvod_naziv)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

INSERT INTO mesto (naziv, zip, zemlja)
VALUES ('naziv 1', '12345', 'zemlja 1'), ('naziv 2', '21341', 'zemlja 2'), ('naziv 3', '39359', 'zemlja 3');

INSERT INTO materijal (naziv, opis)
VALUES ('naziv 1', 'opis 1'), ('naziv 2', 'opis 2'), ('naziv 3', 'opis 3');

INSERT INTO proizvod (naziv, opis, cena)
VALUES ('naziv 1', 'opis 1', 3348), ('naziv 2', 'opis 2', 9104), ('naziv 3', 'opis 3', 8324);

INSERT INTO kupac (ime, prezime, jmbg, adresa, telefon, mesto_zip)
VALUES ('ime 1', 'prezime 1', '1235492958234', 'adresa 1', 'telefon 1', '12345'),
	   ('ime 2', 'prezime 2', '5925819584432', 'adresa 2', 'telefon 2', '21341'),
	   ('ime 3', 'prezime 3', '6583865382068', 'adresa 3', 'telefon 3', '39359');

INSERT INTO sastavnica (kolicina, proizvod_naziv, materijal_naziv)
VALUES (12, 'naziv 1', 'naziv 1'), (21, 'naziv 2', 'naziv 2'), (4, 'naziv 3', 'naziv 3');

INSERT INTO kupovina_proizvoda (kolicina, ukupna_cena, datum, proizvod_naziv, mesto_zip, id_kupac)
VALUES (56, 34356, '2018-10-23', 'naziv 1', '12345', 1),
	   (32, 45241, '2018-11-13', 'naziv 2', '21341', 2),
	   (12, 53563, '2019-11-13', 'naziv 3', '39359', 3);
       
INSERT INTO nova_tabela (mesto_zip, proizvod_naziv)
VALUES ('39359', 'naziv 1'), ('12345', 'naziv 2'), ('21341', 'naziv 3');
       
DELETE FROM nova_tabela;
DELETE FROM kupovina_proizvoda;
DELETE FROM sastavnica;
DELETE FROM kupac;
DELETE FROM proizvod;
DELETE FROM materijal;
DELETE FROM mesto;

DROP TABLE  nova_tabela;
DROP TABLE kupovina_proizvoda;
DROP TABLE sastavnica;
DROP TABLE kupac;
DROP TABLE proizvod;
DROP TABLE materijal;
DROP TABLE mesto;

DROP DATABASE prodaja;



