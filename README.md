# MCOC2020-P0
Primer repositorio Métodos Computacionales en Obras Civiles
# Mi Computador
  - Procesador CPU Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
  - Numero de nucleos: 6
  - Procesadores logicos (hilos): 12
  - Memoria RAM : 16 Gb DDR4 2667 MHz
  - Disco SSHD (hibrido) 1tb disco duro y 0.8 gb disco solido
  - Tarjeta de video NVIDIA GeForce GTX 1050
  
  - Marca/modelo: TUF Gaming FX505GD

  - Tipo: Notebook

  - Año adquisición: 2019

  - Procesador:

	- Marca/Modelo: CPU Intel(R) Core(TM) i7-8750H
	- Velocidad Base: 2.21 GHz
	- Velocidad Máxima: 2.21 GHz
	- Numero de núcleos: 6
	- Humero de hilos: 12
	- Arquitectura: x86_64
	- Set de instrucciones: Intel SSE4.1, Intel SSE4.2, Intel AVX2
- Tamaño de las cachés del procesador:


	- L1: 384KB
	- L2: 1500KB
	- L3: 9000KB
- Memoria:

	- Total: 16 GB
	- Tipo memoria: DDR4
	- Velocidad 2667 MHz
	- Numero de (SO)DIMM: 4
- Tarjeta Gráfica:

	- Marca / Modelo: Nvidia GeForce GTX 1050
	- Memoria total: 12136 MB
	- Memoria compartida: 8117 MB
	- Memoria dedicada: 4000 MB
	- Resolución: 1920 x 1080
- Discos: 1, 3 particiones:
	- Disco 1, particion #0:

		- Modelo: ST1000LX015-1U7172
		- Tipo: HDD
		- Tamaño: 1TB
		- Sistema de archivos: NTFS

	- Disco 1, particion #1:

		- Marca: ?
		- Tipo: SSD
		- Tamaño: 0.8 GB
		- Sistema de archivos: ? ocupacion para arranque me imagino

	- Disco 1, particion #2:

		- Marca: ?
		- Tipo: SSD
		- Tamaño: 0.26 GB
		- Sistema de archivos: ? ocupacion para arranque me imagino

- Dirección MAC de la tarjeta wifi: 18:56:80:F7:68:C2

- Dirección IP (Interna, del router): 192.168.1.93

- Dirección IP (Externa, del ISP): 201.189.181.251

- Proveedor internet: Movistar Banda Ancha S.A.

# Desempeño MATMUL
- Grafico resultado: 
	- ![image](https://user-images.githubusercontent.com/43451947/89659909-91c10580-d89e-11ea-921f-61ccb9b4b83b.png)
- ¿Como difiere del gráfico del profesor/ayudante?
	- El grafico difiere principalmente en los tiempos que toma al programa/computador realizar la multiplicación de las matrices de distinto tamaño, donde en este caso se puede ver que no difiere tanto con respecto al del profesor, por lo que probablemente tengan caracteristicas similares mi computador con el de el. Con respecto a la memoria RAM, esta no difiere, ya que esta es especifica en cuanto a la cantidad de datos de la matriz, en lo unico que difiere es que mi limite de memoria son 16 GB y el del profesor 32 GB, donde se puede apreciar que mi linea discontinua esta ligeramente mas abajo.
- ¿A qué se pueden deber las diferencias?
	- Las diferencias se pueden deber a distintos factores, principalmente los componentes del computador, como el procesador y la memoria RAM, ya que a medida que aumentan las dimensiones de la matriz, la multiplicacion de estas se hace mas dificil, lo que necesita mas rendimiento del computador.
	- Otros factores que podrian afectar es la cantidad de programas que tenemos abiertos en el computador, ya que utilizan mas memoria, lo que podria afectar el rendimiento.
- El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
	- Esto se debe a que a medida que aumenta el tamaño de la matriz, aumentan los datos dentro de ella, y siendo que 1 dato pesa 8 bytes, a medida que aumentan, aumentan la cantidad de bytes con respecto a la formula: 3x(N^2)x8, siendo N el tamaño de la matriz, por lo que aumenta linealmente. Siendo el caso contrario para el tiempo transcurrido, ya que esto al depender del rendimiento del computador, no hay certeza del tiempo que se demore en realizar la operacion de multiplicar las matrices, por lo que no se puede suponer que tendra un crecimiento lineal.
- ¿Qué versión de python está usando?
	- Actualmente estoy utilizando Python 3.8
- ¿Qué versión de numpy está usando?
	- Actualmente estoy utilizando Numpy 1.18.5
- Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar.
	- ![image](https://user-images.githubusercontent.com/43451947/89662339-f0d44980-d8a1-11ea-849a-a8fcbb0778e5.png)
	- Como se puede ver en la imagen, no se alcanza a ocupar mas de un procesador, sino que ocupa al rededor del 80% de este cuando se realiza una corrida.

# Desempeño MIMATMUL
- Grafico resultado:
	- ![image](https://user-images.githubusercontent.com/43451947/89808347-03e85300-db08-11ea-80c3-768346d72e56.png)
- ¿Como difiere del gráfico del profesor/ayudante?
	- Para este grafico, nuevamente no difiere en mayor parte con el grafico propuesto por el ayudante en el foro de preguntas del proyecto, lo que quiere decir que las caracteristicas de rendimiento de los computadores deberian ser parecidas ya que les toma mas menos el mismo tiempo en realizar las operaciones para la multiplicacion de las matrices.
- ¿A qué se pueden deber las diferencias?
	- Las pequeñas diferencias que pueden haber son principalmente por el procesador de cada computador y la memoria RAM, que son los principales motivos que afectan al rendimiento de las operaciones, luego estan los procesos secundarios que tienen que ver con las tareas apartes que esta ejecutanco el computador, vale decir, si por ejemplo justo cuando corri el programa me encontraba viendo una pelicula, o realizando un streaming, afectara en el rendimiento y lo mas probable es que haga que el proceso del codigo se demore mas tiempo.
	- Hablando de las diferencias con respecto a la entrega 2, se puede ver claramente que la funcion mimatmul demora mucho tiempo mas, esto se debe a que esta funcion lo que hace es recorrer y ademas multiplicar cada fila por cada columna de las matrices, al contrario del operador @, que es casi instantaneo, es por eso que cerca del tamaño de matriz N = 1000 se demoraba alrededor de 15 minutos, lo que es un tiempo aceptable para tomar en cuenta como limite, ya que si lo hubiera hecho para un N = 10000, lo mas probable es que se habria demorado horas en una sola corrida, siendo que eran 10 corridas.
- El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
	- Para esta entrega con respecto a la entrega 2, se puede ver que independientemente que no sea exactamente lineal el grafico del tiempo transcurrido, se acerca mucho mas a serlo, debido a que los procesos que tiene que realizar el programa son bastante sencillos, pero a medida que aumentaba el tamaño de la matriz, eran mas datos, y al ser mas datos tomaba mas tiempo, y las irregularidades que se podrian haber generado tendrian directa relacion con las tareas secundarias que se estaban desarrollando en el computador. Esto lo pude verificar debido a que en una corrida, estaba viendo una pelicula y pude recalcar que el proceso tomo mas tiempo de lo esperado, donde claramente se pudo concluir que para un optimo rendimiento, hay que tratar de solo tener como tarea la ejecucion del codigo.

- Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar.
	- ![image](https://user-images.githubusercontent.com/43451947/89808453-28dcc600-db08-11ea-90d9-837262503234.png)
	- Como se puede ver en la imagen se estan utilizando los 12 procesadores logicos del computador, pero a diferencia de la entrega 2 el porcentaje de uso es aproximadamente un 20% (60% menor que la entrega 2), y esto se debe a que la funcion mimatmul, es larga pero sencilla, es decir al ser un proceso de bajo nivel no necesita tanto rendimiento del computador, sino mas bien tiempo.












