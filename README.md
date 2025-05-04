# challenge01_2025
import pandas as pd

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda = pd.read_csv(url)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

tienda.head()
Ingreso total por cada tienda
en la lista 
Backlog

Descripción
En este primer análisis, debes calcular el ingreso total de cada tienda. Sumando los valores de la columna Precio de cada conjunto de datos de la tienda para estimar los ingresos.
2025-04-23 23:22:42
GPT-4o mini

Para calcular el ingreso total por cada tienda, puedes realizar lo siguiente:

    Leer los archivos CSV de cada tienda.
    Sumar los valores de la columna "Precio" de cada conjunto de datos.
    Mostrar el resultado de los ingresos totales por tienda.

Aquí te dejo el código que puedes usar:

python

# Calcular el ingreso total por cada tienda
ingreso_tienda_1 = tienda['Precio'].sum()
ingreso_tienda_2 = tienda2['Precio'].sum()
ingreso_tienda_3 = tienda3['Precio'].sum()
ingreso_tienda_4 = tienda4['Precio'].sum()

# Mostrar los ingresos totales
ingresos_totales = {
    "Tienda 1": ingreso_tienda_1,
    "Tienda 2": ingreso_tienda_2,
    "Tienda 3": ingreso_tienda_3,
    "Tienda 4": ingreso_tienda_4
}

ingresos_totales

Este código sumará los valores de la columna "Precio" para cada tienda y te dará el ingreso total por tienda. Si ya tienes los datos cargados, simplemente ejecútalo para obtener los resultados.
2025-04-23 23:22:42
You


Ventas por categoría
en la lista 
Backlog

Descripción
En este debes calcular la cantidad de productos vendidos por categoría en cada tienda. La idea es agrupar los datos por categoría y contar el número de ventas de cada tipo, mostrando las categorías más populares de cada tienda.
2025-04-23 23:25:36
GPT-4o mini

Para calcular la cantidad de productos vendidos por categoría en cada tienda, puedes agrupar los datos por la columna de "Categoría" y contar el número de ventas (es decir, el número de productos) en cada categoría. Aquí tienes el código que te permitirá hacer esto para cada tienda:

python

# Calcular la cantidad de productos vendidos por categoría en cada tienda
ventas_por_categoria_tienda_1 = tienda.groupby('Categoría')['Producto'].count().sort_values(ascending=False)
ventas_por_categoria_tienda_2 = tienda2.groupby('Categoría')['Producto'].count().sort_values(ascending=False)
ventas_por_categoria_tienda_3 = tienda3.groupby('Categoría')['Producto'].count().sort_values(ascending=False)
ventas_por_categoria_tienda_4 = tienda4.groupby('Categoría')['Producto'].count().sort_values(ascending=False)

# Mostrar las ventas por categoría para cada tienda
ventas_por_categoria = {
    "Tienda 1": ventas_por_categoria_tienda_1,
    "Tienda 2": ventas_por_categoria_tienda_2,
    "Tienda 3": ventas_por_categoria_tienda_3,
    "Tienda 4": ventas_por_categoria_tienda_4
}

ventas_por_categoria

Explicación:

    Agrupación por Categoría: Se agrupan los datos de cada tienda por la columna "Categoría".
    Contar productos vendidos: Luego, se cuenta el número de productos en cada categoría usando .count() en la columna "Producto".
    Ordenar: Los resultados se ordenan de mayor a menor para ver las categorías más populares.

Este código te dará la cantidad de productos vendidos por categoría en cada tienda. Asegúrate de que las columnas "Categoría" y "Producto" estén correctamente nombradas en los datos cargados.
2025-04-23 23:25:36
You


Valoración media por tienda
en la lista 
Backlog

Descripción
En este paso, debes calcular las calificaciones promedio de los clientes para cada tienda. El objetivo es conocer la satisfacción del cliente con los productos vendidos.
2025-04-23 23:28:08
GPT-4o mini

Para calcular la valoración media por tienda, es necesario calcular el promedio de las calificaciones de los clientes para cada tienda. Para hacerlo, puedes usar la columna que contiene las calificaciones de los productos (por ejemplo, "Calificación" o similar) y calcular la media para cada conjunto de datos de la tienda. Aquí te dejo el código:

python

# Calcular la valoración media por tienda
valoracion_media_tienda_1 = tienda['Calificación'].mean()
valoracion_media_tienda_2 = tienda2['Calificación'].mean()
valoracion_media_tienda_3 = tienda3['Calificación'].mean()
valoracion_media_tienda_4 = tienda4['Calificación'].mean()

# Mostrar la valoración media por tienda
valoracion_media = {
    "Tienda 1": valoracion_media_tienda_1,
    "Tienda 2": valoracion_media_tienda_2,
    "Tienda 3": valoracion_media_tienda_3,
    "Tienda 4": valoracion_media_tienda_4
}

valoracion_media

Explicación:

    Calcular la media: Se utiliza el método .mean() para calcular el promedio de las calificaciones de la columna "Calificación" de cada tienda.
    Mostrar los resultados: Al final, se crea un diccionario con las valoraciones medias de cada tienda.

Este código te dará la valoración promedio por tienda, lo que te permitirá tener una idea sobre la satisfacción de los clientes con los productos vendidos. Asegúrate de que la columna de calificación esté correctamente nombrada (puede ser "Calificación", "Puntuación", etc.).
2025-04-23 23:28:08
You


Productos más vendidos y menos vendidos
en la lista 
Backlog

Descripción
En este paso, debes identificar qué productos fueron los más vendidos y los menos vendidos en cada tienda. Visualiza los resultados para que quede claro qué productos destacaron en ventas en cada tienda.
2025-04-23 23:29:21
GPT-4o mini

Para identificar los productos más vendidos y los menos vendidos en cada tienda, se puede agrupar por el nombre del producto y contar la cantidad de veces que se vendió cada uno. Luego, puedes ordenar los productos de mayor a menor para los más vendidos, y de menor a mayor para los menos vendidos.

Aquí tienes el código que puedes usar para este análisis:

python

# Calcular los productos más vendidos y menos vendidos por tienda

# Tienda 1
productos_vendidos_tienda_1 = tienda.groupby('Producto')['Cantidad'].sum()
productos_mas_vendidos_tienda_1 = productos_vendidos_tienda_1.sort_values(ascending=False).head(10)
productos_menos_vendidos_tienda_1 = productos_vendidos_tienda_1.sort_values(ascending=True).head(10)

# Tienda 2
productos_vendidos_tienda_2 = tienda2.groupby('Producto')['Cantidad'].sum()
productos_mas_vendidos_tienda_2 = productos_vendidos_tienda_2.sort_values(ascending=False).head(10)
productos_menos_vendidos_tienda_2 = productos_vendidos_tienda_2.sort_values(ascending=True).head(10)

# Tienda 3
productos_vendidos_tienda_3 = tienda3.groupby('Producto')['Cantidad'].sum()
productos_mas_vendidos_tienda_3 = productos_vendidos_tienda_3.sort_values(ascending=False).head(10)
productos_menos_vendidos_tienda_3 = productos_vendidos_tienda_3.sort_values(ascending=True).head(10)

# Tienda 4
productos_vendidos_tienda_4 = tienda4.groupby('Producto')['Cantidad'].sum()
productos_mas_vendidos_tienda_4 = productos_vendidos_tienda_4.sort_values(ascending=False).head(10)
productos_menos_vendidos_tienda_4 = productos_vendidos_tienda_4.sort_values(ascending=True).head(10)

# Mostrar los resultados
productos_vendidos = {
    "Tienda 1 - Más vendidos": productos_mas_vendidos_tienda_1,
    "Tienda 1 - Menos vendidos": productos_menos_vendidos_tienda_1,
    "Tienda 2 - Más vendidos": productos_mas_vendidos_tienda_2,
    "Tienda 2 - Menos vendidos": productos_menos_vendidos_tienda_2,
    "Tienda 3 - Más vendidos": productos_mas_vendidos_tienda_3,
    "Tienda 3 - Menos vendidos": productos_menos_vendidos_tienda_3,
    "Tienda 4 - Más vendidos": productos_mas_vendidos_tienda_4,
    "Tienda 4 - Menos vendidos": productos_menos_vendidos_tienda_4
}

productos_vendidos

Explicación:

    Agrupar por Producto: Se agrupan los datos por "Producto" y luego se suma la cantidad de cada producto vendido.
    Ordenar: Los productos se ordenan para encontrar los más vendidos (ordenados de mayor a menor) y los menos vendidos (ordenados de menor a mayor).
    Top 10: Se muestran los 10 productos más vendidos y los 10 productos menos vendidos, pero puedes ajustar la cantidad según lo necesites.

Este código te permitirá ver qué productos fueron los más populares y cuáles tuvieron menos ventas en cada tienda. Si quieres visualizar más o menos productos, puedes modificar la cantidad de resultados que se muestran (head(10) para los 10 más vendidos, por ejemplo).
2025-04-23 23:29:21
You


Valor del envío promedio por tienda
en la lista 
Backlog

Descripción
En este paso, debes calcular el costo de envío promedio para cada tienda. El objetivo es comprender cuánto se gasta, en promedio, en el envío de cada tienda.
2025-04-23 23:30:34
GPT-4o mini

Para calcular el costo de envío promedio por tienda, debes calcular el promedio de los valores en la columna que contiene los costos de envío (por ejemplo, "Costo_Envío" o algo similar) para cada tienda. Aquí te dejo el código que puedes usar para calcular el costo de envío promedio por tienda:

python

# Calcular el valor de envío promedio por tienda
envio_promedio_tienda_1 = tienda['Costo_Envío'].mean()
envio_promedio_tienda_2 = tienda2['Costo_Envío'].mean()
envio_promedio_tienda_3 = tienda3['Costo_Envío'].mean()
envio_promedio_tienda_4 = tienda4['Costo_Envío'].mean()

# Mostrar el costo de envío promedio por tienda
costo_envio_promedio = {
    "Tienda 1": envio_promedio_tienda_1,
    "Tienda 2": envio_promedio_tienda_2,
    "Tienda 3": envio_promedio_tienda_3,
    "Tienda 4": envio_promedio_tienda_4
}

costo_envio_promedio

Explicación:

    Calcular el promedio: Se utiliza el método .mean() para calcular el promedio del costo de envío en la columna "Costo_Envío" de cada tienda.
    Mostrar los resultados: Al final, se crea un diccionario con el costo de envío promedio para cada tienda.

# challenge01_2025
