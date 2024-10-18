from datetime import datetime, timedelta
import pandas as pd
import random

# Generar fechas al azar
start_date = datetime(2023, 11, 17, 0, 0, 0)
end_date = datetime(2023, 11, 29, 23, 59, 59)

date_list = [start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds()))) for _ in range(50)]

# Ordenar las fechas
date_list.sort()

# Crear un DataFrame con las fechas
df = pd.DataFrame(date_list, columns=['Fecha'])

# Formatear las fechas en el formato deseado
df['Fecha'] = df['Fecha'].dt.strftime('%d/%m/%Y %H:%M:%S')

# Exportar a Excel
df.to_excel('fechas_ordenadas.xlsx', index=False)
