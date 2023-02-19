import psycopg2

try:
    connection = psycopg2.connect(database="memoDB",
                        host="localhost",
                        user="postgres",
                        password="pablito_1",
                        port="5432")
    cursor = connection.cursor()

    lat = str(-1.4139788478845312)
    lon = str(-71.0593967818676)

    sql_query = "DROP TABLE IF EXISTS point_table; CREATE TABLE point_table (id serial primary key,nombre text,geom geometry(Point, 4326)); \
        INSERT INTO point_table (geom, nombre) VALUES (ST_SetSRID (ST_MakePoint (" + lon + "," + lat + "), 4326), 'abc'); \
            SELECT departamentos.* from departamentos,point_table \
            where ST_Intersects(departamentos.geom,point_table.geom)"

    cursor.execute(sql_query)
    municipios = cursor.fetchall()

    print("Print each row and columns data")
    #print(municipios)
    for row in municipios:
        print("Departamento = ", row[2], )
        #print("Name = ", row[1])
        #print("Price  = ", row[2], "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")