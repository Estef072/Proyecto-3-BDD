select * 
from bitacora

select*
From  perfiles

select *
from usuarios

select *
from sponsor, anuncios, favoritos

ALTER TABLE reproduccion
ADD COLUMN hora_fecha DATE


DELETE FROM usuarios
WHERE usuario = '2342'

select * 
FROM reproduccion

SELECT* FROM usuarios WHERE usuario='prisci' and tipo_usuarios='administrador'

select *
From usuarios

CREATE TABLE bitacora(
    fecha_hora timestamp default current_timestamp,
    tipo_cambio VARCHAR(200),
    id_user_admin VARCHAR(200),
    lugar_cambio VARCHAR(200),
    dato_cambio VARCHAR(200),
    PRIMARY KEY(fecha_hora, tipo_cambio, id_user_admin),
    FOREIGN KEY(id_user_admin) REFERENCES usuarios(usuario));

CREATE FUNCTION CREATEUSER(usuarioAdmin)
RETURNS TRIGGER AS $$
DECLARE	userAdmin VARCHAR

BEGIN
	SELECT	usuario INTO userAdmin
	FROM	usuarios
	WHERE	tipo_usuario ILIKE 'administrador' AND usuario = usuarioAdmin
	INSERT INTO bitacora VALUES(current_timestamp, 'SELECT', userAdmin, 'usuarios', NEW.dato_cambio);
END;
$$
LANGUAGE 'plpgsql'

CREATE TRIGGER 
	createUser
BEFORE INSERT ON
	bitacora
FOR EACH ROW
EXECUTE PROCEDURE
	CREATEUSER()


INSERT INTO actores VALUES(1,'Kang-ho Song','1967-01-17','South-Corea');
INSERT INTO actores VALUES(2,'Choi Woo-sik','1990-05-26','South-Corea');
INSERT INTO actores VALUES(3,'So-dam Park','1991-09-08','South-Corea');
INSERT INTO actores VALUES(4,'Sun-kyun Lee','1975-03-02','South-Corea');
INSERT INTO actores VALUES(5,'Yeo-jeong Cho','1981-02-10','South-Corea');
INSERT INTO actores VALUES(6,'Andrew Garfield','1983-08-20','USA');
INSERT INTO actores VALUES(7,'Robbert Pattinson','1986-05-13','UK');
INSERT INTO actores VALUES(8,'Keanu Reeves','1964-09-02','Lebanon');
INSERT INTO actores VALUES(9,'Daniel Radclief','1989-07-23','UK');
INSERT INTO actores VALUES(10,'Emma Watson','1990-04-15','France');
INSERT INTO actores VALUES(11,'Jim Carrey','1962-01-17','USA');
INSERT INTO actores VALUES(12,'Leonardo Dicaprio','1974-11-11','USA');
INSERT INTO actores VALUES(13,'Matthew McConaughey','1969-11-04','USA');
INSERT INTO actores VALUES(14,'Anne Hathaway','1982-11-12','USA');
INSERT INTO actores VALUES(15,'Rupert Grint','1988-08-24','UK');
INSERT INTO actores VALUES(16,'Kristen Stewart','1990-04-09','USA');
INSERT INTO actores VALUES(17,'Sarah Clarke','1972-02-16','USA');

INSERT INTO director VALUES(1,'Bong Joon Ho','1969-09-14','South-Corea');
INSERT INTO director VALUES(2,'Christopher Nolan','1970-06-30','UK');
INSERT INTO director VALUES(3,'Matt Reeves' ,'1966-04-27','USA');
INSERT INTO director VALUES(4,'Chris Columbus','1958-11-10','USA');
INSERT INTO director VALUES(5,'Catherine Hardwicke','1965-10-11','USA');
INSERT INTO director VALUES(6,'Seong-Hu Park',null,'South-Corea');
INSERT INTO director VALUES(7,'Makoto Shinkai','1973-02-09','Japan');

INSERT INTO productora VALUES('Warner Bros. Pictures, Inc.','USA',1300000000);
INSERT INTO productora VALUES('Paramount','USA',1300000000);
INSERT INTO productora VALUES('Disney','USA',1300000000);
INSERT INTO productora VALUES('Century-Fox','USA',1300000000);
INSERT INTO productora VALUES('NBCUniversal','USA',1300000000);
INSERT INTO productora VALUES('Sony Pictures','USA',1300000000);
INSERT INTO productora VALUES('Toho Co','Japon',1300000000);
INSERT INTO productora VALUES('Cj Entreteinment','Corea del sur',1300000000);
INSERT INTO productora VALUES('Netflix','USA',1300000000);

INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('snoopy-grey-vulture', '2022-07-06', '"El planeta de tesoro"');
INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('skinny-brown-beetle', '2022-07-06', '"Godzilla"');
INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('hasty-beige-octopus', '2022-07-06', '"tick, tick... boom"');
INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('nerdy-pink-shrew', '2022-07-06', 'Andrew Garfield');
INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('wheezy-olivine-chinchilla', '2022-07-06', '"Godzilla"');
INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('skimpy-red-dolphin', '2022-07-06', 'Andrew Garfield');
INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('freaky-peach-coral', '2022-07-06', '"tick, tick... boom"');
INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('chummy-denim-bison', '2022-07-06', 'Daniel Radclief');
INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('ready-jade-wolf', '2022-07-06', '"tick, tick... boom"');
INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('scummy-teal-gar', '2022-07-06', 'Anne Hathaway');
INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('wheezy-olivine-chinchilla', '2022-07-06', 'Anne Hathaway');
INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('clammy-sapphire-bombay', '2022-07-06', 'Anne Hathaway');
INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('wheezy-ecru-caracal', '2022-07-06', 'Anne Hathaway');
INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('bluesy-platinum-buffalo', '2022-07-06', 'Robbert Pattinson');
INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('woozy-cobalt-wallaby', '2022-07-06', 'Robbert Pattinson');
INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('lanky-smalt-hedgehog', '2022-07-06', 'Robbert Pattinson');
INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('scummy-teal-gar', '2022-07-06', 'Robbert Pattinson');
INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('ugly-magnolia-jellyfish', '2022-07-06', 'Robbert Pattinson');
INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('cranky-tan-cow', '2022-07-06', '"Warner Bros. Pictures, Inc."');
INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('tasty-heliotrope-binturong', '2022-07-06', '"Sony Pictures"');
INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('jumpy-amethyst-gorilla', '2022-07-06', 'Matt Reeves');
INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('skanky-tangerine-falcon', '2022-07-06', 'Netflix');
INSERT INTO busqueda (usuario, fecha_hora, termino)
VALUES		('skanky-tangerine-falcon', '2022-07-06', 'Disney');