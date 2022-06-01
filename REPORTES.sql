/* Creacion de los indices*/
CREATE INDEX index_usuarios ON usuarios(usuario);
CREATE INDEX index_pelicula ON peliculas(id_pelicula);

/* TOP 10 TÉRMINOS QUE LOS USUARIOS BUSCAN */
SELECT	
	termino, COUNT(termino) AS recuento_termino_mas_buscado
FROM	
	busqueda
GROUP BY
	termino
ORDER BY
	COUNT(termino) DESC
LIMIT 
	10

/* TOP 5 ADMIN QUE MÁS HAN HECHO MODIFICACIONES */
SELECT
    usuario
FROM
    usuarios u INNER JOIN bitacora b ON (u.usuario = b.id_user_admin)
WHERE
    u.tipo_usuarios = 'Administrador' AND b.tipo_cambio = 'UPDATE'
GROUP BY
    usuario
ORDER BY
    COUNT(usuario) DESC
LIMIT 
    5

/* TOP 20 PELÍCULAS QUE LLEVAN MÁS DE 20 DÍAS SIN FINALIZARSE */

SELECT
    p.titulo, r.nombre_perfil
FROM
    reproduccion r LEFT JOIN peliculas p ON (r.id_pelicula = p.id_pelicula)
WHERE
    r.visualizacion = 1 OR r.hora_fecha = '2022-05-12' AND r.hora_fecha = '2022-06-01'
GROUP BY 
	p.titulo, r.nombre_perfil
ORDER BY
    COUNT (p.titulo) DESC 
LIMIT 
    20


/*CREACION DE FUNCIONES PARA LA BITACORA */
DECLARE  userAdmin VARCHAR(200);

BEGIN
    SELECT    usuario INTO userAdmin
    FROM    usuarios
    WHERE    tipo_usuarios ILIKE 'administrador' AND usuario = 'prisci';
    INSERT INTO bitacora VALUES(current_timestamp, 'INSERT', userAdmin, 'peliculas', NEW.titulo);

    RETURN NEW;
END;
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION UpdateMovieIntoBitacora()
RETURNS TRIGGER AS $$
DECLARE  userAdmin VARCHAR(200);

BEGIN
    SELECT    usuario INTO userAdmin
    FROM    usuarios
    WHERE    tipo_usuarios ILIKE 'administrador' AND usuario = 'prisci';
    INSERT INTO bitacora VALUES(current_timestamp, 'UPDATE', userAdmin, 'peliculas', NEW.titulo);

   RETURN NEW;
END;
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION DeletedMovieIntoBitacora()
RETURNS TRIGGER AS $$
DECLARE  userAdmin VARCHAR(200);

BEGIN
    SELECT    usuario INTO userAdmin
    FROM    usuarios
    WHERE    tipo_usuarios ILIKE 'administrador' AND usuario = 'prisci';
    INSERT INTO bitacora VALUES(current_timestamp, 'DELETE', userAdmin, 'pelicula', NEW.titulo);

   RETURN NEW;
END;
$$
LANGUAGE plpgsql;
SELECT*
FROM BITACORA


CREATE OR REPLACE FUNCTION NewActorIntoBitacora()
RETURNS TRIGGER AS $$
DECLARE  userAdmin VARCHAR(200);

BEGIN
    SELECT    usuario INTO userAdmin
    FROM    usuarios
    WHERE    tipo_usuarios ILIKE 'administrador' AND usuario = 'prisci';
    INSERT INTO bitacora VALUES(current_timestamp, 'INSERT', userAdmin, 'actores', NEW.nombre);

    RETURN NEW;
END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION UpdateActorIntoBitacora()
RETURNS TRIGGER AS $$
DECLARE  userAdmin VARCHAR(200);

BEGIN
    SELECT    usuario INTO userAdmin
    FROM    usuarios
    WHERE    tipo_usuarios ILIKE 'administrador' AND usuario = 'prisci';
    INSERT INTO bitacora VALUES(current_timestamp, 'UPDATE', userAdmin, 'actores', NEW.nombre);

    RETURN NEW;
END;
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION DeletedActorIntoBitacora()
RETURNS TRIGGER AS $$
DECLARE  userAdmin VARCHAR(200);

BEGIN
    SELECT    usuario INTO userAdmin
    FROM    usuarios
    WHERE    tipo_usuarios ILIKE 'administrador' AND usuario = 'prisci';
    INSERT INTO bitacora VALUES(current_timestamp, 'DELETE', userAdmin, 'actores', NEW.nombre);

    
	RETURN NEW;
END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION NewDirectorIntoBitacora()
RETURNS TRIGGER AS $$
DECLARE  userAdmin VARCHAR(200);

BEGIN
    SELECT    usuario INTO userAdmin
    FROM    usuarios
    WHERE    tipo_usuarios ILIKE 'administrador' AND usuario = 'prisci';
    INSERT INTO bitacora VALUES(current_timestamp, 'INSERT', userAdmin, 'director', NEW.nombre);

   RETURN NEW;
END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION UpdateDirectorIntoBitacora()
RETURNS TRIGGER AS $$
DECLARE  userAdmin VARCHAR(200);

BEGIN
    SELECT    usuario INTO userAdmin
    FROM    usuarios
    WHERE    tipo_usuarios ILIKE 'administrador' AND usuario = 'prisci';
    INSERT INTO bitacora VALUES(current_timestamp, 'UPDATE', userAdmin, 'director', NEW.nombre);

    RETURN NEW;
END;
$$
LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION DeletedDirectorIntoBitacora()
RETURNS TRIGGER AS $$
DECLARE  userAdmin VARCHAR(200);

BEGIN
    SELECT    usuario INTO userAdmin
    FROM    usuarios
    WHERE    tipo_usuarios ILIKE 'administrador' AND usuario = 'prisci';
    INSERT INTO bitacora VALUES(current_timestamp, 'DELETE', userAdmin, 'director', NEW.nombre);

   RETURN NEW;
END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION NewUsuarioIntoBitacora()
RETURNS TRIGGER AS $$
DECLARE  userAdmin VARCHAR(200);

BEGIN
    SELECT    usuario INTO userAdmin
    FROM    usuarios
    WHERE    tipo_usuarios ILIKE 'administrador' AND usuario = 'prisci';
    INSERT INTO bitacora VALUES(current_timestamp, 'INSERT', userAdmin, 'director', NEW.usuario);

    RETURN NEW;
END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION UpdateUsuarioIntoBitacora()
RETURNS TRIGGER AS $$
DECLARE  userAdmin VARCHAR(200);

BEGIN
    SELECT    usuario INTO userAdmin
    FROM    usuarios
    WHERE    tipo_usuarios ILIKE 'administrador' AND usuario = 'prisci';
    INSERT INTO bitacora VALUES(current_timestamp, 'UPDATE', userAdmin, 'director', NEW.usuario);

   RETURN NEW;
END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION DeletedUsuarioIntoBitacora()
RETURNS TRIGGER AS $$
DECLARE  userAdmin VARCHAR(200);

BEGIN
    SELECT    usuario INTO userAdmin
    FROM    usuarios
    WHERE    tipo_usuarios ILIKE 'administrador' AND usuario = 'prisci';
    INSERT INTO bitacora VALUES(current_timestamp, 'DELETE', userAdmin, 'director', NEW.usuario);

    RETURN NEW;
END;
$$
LANGUAGE plpgsql;

