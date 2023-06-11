import numpy as np
x = np.array ([1.5, 2.2, 1.56, 1.78, 1.82, 1.90, 1.66, 1.91, 1.76, 1.88])
print (x)

#Calcular la media/desviacion estandar 
import numpy as np 

data = [1.5, 2.2, 1.56, 1.78, 1.82, 1.90, 1.66, 1.91, 1.76, 1.88]

print("Media: ", np.mean(data))
print("Media de los 10 datos: ", np.median(data))
print("Desviación Estándar: ", np.std(data))

#Dataset
dataset = [0.56744433976086, 0.6871979493457484, 0.8463706897561651, 0.31110389619407564, 0.23511891089708503, 0.6577102252485975, 0.6648803069356928, 0.49989209380778477, 0.023793000481246773, 0.8777416618364761, 0.45262683262543646, 0.6430419554811486, 0.06347145550399458, 0.10628535246898096, 0.13551828266629173, 0.7030802149078524, 0.8656176079542628, 0.3939640454664668, 0.5144582885753547, 0.6255032779041944]

print("Total de datos: ", np.size(dataset))
print("Media: ", np.mean(dataset))
print("Mediana: ", np.median(dataset))
print("Desviación Estándar: ", np.std(dataset))

# Reorganizar el arreglo
x = np.reshape(dataset, (5, 4))
print (x)

print("Media para la segunda columna: ", np.mean(x))
print("Mediana para la tercera fila de datos: ", np.median(x))
print("Desviación estándar para los datos de la fila 3 a 5 y las columnas 1 a 3: ", np.std(x))

