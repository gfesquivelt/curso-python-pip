ALTER TABLE barrios 
  ALTER COLUMN geom 
  TYPE Geometry(Multipolygon, 4326) 
  USING ST_Transform(geom, 4326);