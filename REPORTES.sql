/* Creacion de los indices*/
CREATE INDEX index_usuarios ON usuarios(usuario);
CREATE INDEX index_pelicula ON peliculas(id_pelicula);


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