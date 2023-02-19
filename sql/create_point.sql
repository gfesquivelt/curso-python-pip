DROP TABLE IF EXISTS point_table;

CREATE TABLE point_table (
    id serial primary key,
	nombre text,
    geom geometry(Point, 4326)
);

INSERT INTO point_table (geom, nombre)
VALUES (ST_SetSRID(ST_MakePoint(-75.51714521995629,5.0674047987635635), 4326), 'abc');

select * from point_table
