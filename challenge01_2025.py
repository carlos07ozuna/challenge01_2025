import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos desde las URLs
url1 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda1 = pd.read_csv(url1)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

# Calcular el ingreso total por cada tienda
ingreso_tienda_1 = tienda1['Precio'].sum()
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

print("\nIngresos Totales por Tienda:")
print(ingresos_totales)

# Calcular la cantidad de productos vendidos por categoría en cada tienda
ventas_por_categoria_tienda_1 = tienda1.groupby('Categoría del Producto')['Producto'].count().sort_values(ascending=False)
ventas_por_categoria_tienda_2 = tienda2.groupby('Categoría del Producto')['Producto'].count().sort_values(ascending=False)
ventas_por_categoria_tienda_3 = tienda3.groupby('Categoría del Producto')['Producto'].count().sort_values(ascending=False)
ventas_por_categoria_tienda_4 = tienda4.groupby('Categoría del Producto')['Producto'].count().sort_values(ascending=False)

# Mostrar las ventas por categoría para cada tienda
ventas_por_categoria = {
    "Tienda 1": ventas_por_categoria_tienda_1,
    "Tienda 2": ventas_por_categoria_tienda_2,
    "Tienda 3": ventas_por_categoria_tienda_3,
    "Tienda 4": ventas_por_categoria_tienda_4
}

print("\nVentas por Categoría por Tienda:")
print(ventas_por_categoria)

# Calcular la valoración media por tienda
valoracion_media_tienda_1 = tienda1['Calificación'].mean()
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

print("\nValoración Media por Tienda:")
print(valoracion_media)

# Calcular los productos más vendidos y menos vendidos por tienda
# Tienda 1
productos_vendidos_tienda_1 = tienda1.groupby('Producto')['Cantidad de cuotas'].sum()
productos_mas_vendidos_tienda_1 = productos_vendidos_tienda_1.sort_values(ascending=False).head(10)
productos_menos_vendidos_tienda_1 = productos_vendidos_tienda_1.sort_values(ascending=True).head(10)

# Tienda 2
productos_vendidos_tienda_2 = tienda2.groupby('Producto')['Cantidad de cuotas'].sum()
productos_mas_vendidos_tienda_2 = productos_vendidos_tienda_2.sort_values(ascending=False).head(10)
productos_menos_vendidos_tienda_2 = productos_vendidos_tienda_2.sort_values(ascending=True).head(10)

# Tienda 3
productos_vendidos_tienda_3 = tienda3.groupby('Producto')['Cantidad de cuotas'].sum()
productos_mas_vendidos_tienda_3 = productos_vendidos_tienda_3.sort_values(ascending=False).head(10)
productos_menos_vendidos_tienda_3 = productos_vendidos_tienda_3.sort_values(ascending=True).head(10)

# Tienda 4
productos_vendidos_tienda_4 = tienda4.groupby('Producto')['Cantidad de cuotas'].sum()
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

print("\nProductos Más y Menos Vendidos por Tienda:")
print(productos_vendidos)

# Calcular el valor de envío promedio por tienda
envio_promedio_tienda_1 = tienda1['Costo de envío'].mean()
envio_promedio_tienda_2 = tienda2['Costo de envío'].mean()
envio_promedio_tienda_3 = tienda3['Costo de envío'].mean()
envio_promedio_tienda_4 = tienda4['Costo de envío'].mean()

# Mostrar el costo de envío promedio por tienda
costo_envio_promedio = {
    "Tienda 1": envio_promedio_tienda_1,
    "Tienda 2": envio_promedio_tienda_2,
    "Tienda 3": envio_promedio_tienda_3,
    "Tienda 4": envio_promedio_tienda_4
}

print("\nCosto de Envío Promedio por Tienda:")
print(costo_envio_promedio)

# --- Visualizaciones ---

# Ingresos Totales por Tienda - Gráfico de Barras
tiendas = list(ingresos_totales.keys())
ingresos = list(ingresos_totales.values())

plt.figure(figsize=(10, 6))
plt.bar(tiendas, ingresos, color='skyblue')
plt.xlabel('Tiendas')
plt.ylabel('Ingresos Totales')
plt.title('Ingresos Totales por Tienda')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Ventas por Categoría - Gráfico de Barras Apiladas
categorias = tienda1['Categoría del Producto'].unique()
tiendas = ["Tienda 1", "Tienda 2", "Tienda 3", "Tienda 4"]
ventas_por_tienda = {}

for tienda_nombre, tienda_data in zip(tiendas, [tienda1, tienda2, tienda3, tienda4]):
    ventas_por_tienda[tienda_nombre] = tienda_data.groupby('Categoría del Producto')['Producto'].count()

plt.figure(figsize=(12, 8))
for categoria in categorias:
    ventas = [ventas_por_tienda[tienda].get(categoria, 0) for tienda in tiendas]
    plt.bar(tiendas, ventas, label=categoria)

plt.xlabel('Tiendas')
plt.ylabel('Cantidad de Productos Vendidos')
plt.title('Ventas por Categoría en Cada Tienda')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Valoración Media por Tienda - Gráfico de Barras
tiendas = list(valoracion_media.keys())
valoraciones = list(valoracion_media.values())

plt.figure(figsize=(8, 6))
plt.bar(tiendas, valoraciones, color='lightcoral')
plt.xlabel('Tiendas')
plt.ylabel('Valoración Media')
plt.title('Valoración Media por Tienda')
plt.xticks(rotation=45)
plt.ylim(0, 5)  # Escala de 0 a 5 estrellas
plt.tight_layout()
plt.show()

# Costo de Envío Promedio - Gráfico de Barras
tiendas = list(costo_envio_promedio.keys())
costos_envio = list(costo_envio_promedio.values())

plt.figure(figsize=(8, 6))
plt.bar(tiendas, costos_envio, color='lightgreen')
plt.xlabel('Tiendas')
plt.ylabel('Costo de Envío Promedio')
plt.title('Costo de Envío Promedio por Tienda')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Productos Más Vendidos por Tienda - Gráfico de Barras Horizontales
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
axes = axes.flatten()

tiendas = ["Tienda 1", "Tienda 2", "Tienda 3", "Tienda 4"]
productos_mas_vendidos_lista = [productos_mas_vendidos_tienda_1, productos_mas_vendidos_tienda_2, productos_mas_vendidos_tienda_3, productos_mas_vendidos_tienda_4]

for i, (tienda, productos_vendidos) in enumerate(zip(tiendas, productos_mas_vendidos_lista)):
    sns.barplot(x=productos_vendidos.values, y=productos_vendidos.index, ax=axes[i], color='skyblue')
    axes[i].set_title(f'Productos Más Vendidos en {tienda}')
    axes[i].set_xlabel('Cantidad de Cuotas')
    axes[i].set_ylabel('Producto')
    axes[i].tick_params(axis='y', labelsize=8)

plt.tight_layout()
plt.show()

#mejorar el codigo para obtener mejores graficos y paletas de colores; y mejorar los comentarios en forma camelcase