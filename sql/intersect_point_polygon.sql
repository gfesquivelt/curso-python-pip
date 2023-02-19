SELECT establecimientos_educativos.geom
FROM departamentos, establecimientos_educativos
WHERE departamentos.denombre = 'Cundinamarca'
AND ST_Intersects(departamentos.geom, establecimientos_educativos.geom)


/*
select departamentos.denombre, departamentos.geom, Count(*) as conteo from departamentos, point_table
where ST_Contains(departamentos.geom, point_table.geom)
GROUP BY denombre, departamentos.geom
ORDER BY conteo DESC
*/
--ORDER BY ST_AREA(geom)
--DESC

--look up and set the SRID
--SELECT Find_SRID('public', 'point_table', 'geom');
--SELECT UpdateGeometrySRID('municipios','geom',4326);