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
