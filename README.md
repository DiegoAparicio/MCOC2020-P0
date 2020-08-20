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


# Desempeño INV
- Tamaño de memoria de tipos de dato:
	- np.half : 16 bits (2 Bytes)
	- np.single : 32 bits (4 Bytes)
	- np.double : 64 bits (8 Bytes)
	- np.longdouble : 128 bits (16 Bytes)
- Desempeño de los distintos tipos de dato:
	- Para el dtype = np.half:
		- ![image](https://user-images.githubusercontent.com/43451947/90071478-a3057a00-dcc3-11ea-9d94-d3c4a7e6470b.png)
	- Para el dtype = np.single:	
		- ![image](https://user-images.githubusercontent.com/43451947/90071600-db0cbd00-dcc3-11ea-80a2-ea5b53de874d.png)
	- Para el dtype = np.double:
		- ![image](https://user-images.githubusercontent.com/43451947/90071851-58d0c880-dcc4-11ea-9e8a-44ba46709e3d.png)
	- Para el dtype = np.longdouble:
		- ![image](https://user-images.githubusercontent.com/43451947/90071929-7bfb7800-dcc4-11ea-8b5b-09526dc1cb7b.png)
	- Como se puede ver para los casos de np.half y np.longdouble, no aparece el desempeño de numpy.inv, debido a que la inversion de matrices con numpy no se puede realizar con tipos de datos float16 ni float64, donde el tipo de dato longdouble, se comporta como un float64, pero no quiere decir que ocupe memoria 64 bits.	
	- Hablando de la eficiencia de los distintos casos, se puede apreciar que la funcion numpy.inv, en un principio realiza la inversion de las matrices de manera mas rapida que las otras dos funciones pero a largo plazo, vale decir, con matrices de mayor tamaño la eficiencia de las otras dos funciones es mas rapida (al rededor de 10 segundos mas rapida para la matriz de 10000x10000), y frente a la comparacion entre scipy.inv False y True, en la mayoria de los casos con overwrite=False, toma ligeramente mas tiempo que con overwrite=True, es decir, que con overwrite=True seria la opcion mas eficiente para matrices de gran tamaño, supongo que por el hecho de que el overwrite reemplaza datos en vez de añadirlos (append).
- Monitoreo de uso de memoria y procesadores:
	- Analizando el desempeño mientras se corria el codigo, se puede concluir que en general el uso del procesador es de 20% para las matrices pequeñas (N=[2,4,...,5000]), pero cuando se enfrenta a la matriz de N=10000 el uso del procesador aumenta a un 80%.
	- Otra observacion fue que a medida que los tipos de datos iban haciendose mas grandes, es decir, de np.half hasta np.longdouble, el tiempo que tomaba analizar la matriz de N=10000 era mayor, vale decir, como esta era la matriz con mayor cantidad de datos, al incrementar el tipo de dato lo esperado fuera que tomase mas tiempo, ya que es un dato mas "pesado", lo que se pudo verificar mediante el rendimiento de los procesadores y los graficos presentados en la seccion Desempeño, donde se puede ver que realmente tomo mas tiempo pudiendo asi, verificar la hipotesis esperada.
- ¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)?
	- Para el caso de numpy.linalg.inv, se utiliza la inversion de matriz mediante la matriz identidad.
	- De la misma forma scipy.linalg.inv, utiliza la matriz identidad para invertir la matriz A.
	- En general scipy utiliza las mismas funciones que numpy, solo que scipy es siempre compilado por el soporte BLAS/LAPACK, el que hace que los calculos lineales algebraicos sean mucho mas rapido, cosa que para numpy es opcional.
	- Finalmente la funcion de "overwrite=True" lo que hace es ignorar valores que no aportan, lo que hace que los calculos sean mas eficientes y tomen menos tiempo.
- ¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso?
	- Por lo menos mi computador al momento de correr el codigo, aprovecha el paralelismo totalmente, es decir ocupa todos los procesadores logicos para asi no forzar tanto a unos pocos solamente, y a medida que se esta llegando al limite de memoria de los caché, por lo menos en el L1=384 kB, se generan ciertos "saltos" antes de llegar, y estos saltos no son justo en el limite sino que son antes debido a que como el computador esta corriendo varios programas a la vez incluyendo Python, se ocupa esta memoria antes y asi el "cambio" de caché genera estos pequeños "saltos".
	- Por otro lado, como numpy esta mas cerca al bajo nivel de escritura, como los procesos son mas basicos, toma mas tiempo de lo que le toma a scipy, ya que este al ser una escritura mas avanzada es mas "inteligente" por asi decirlo, lo que toma menos tiempo.

# Entrega6 - Desempeño de Ax = b (Parte 2)
- A partir de los solvers resultantes se pudo llegar al siguiente grafico de performance:
	- ![image](https://user-images.githubusercontent.com/43451947/90346188-001b6b80-dff5-11ea-95f8-ec3ff3dcc593.png)
	- Del cual se puede decir en primer lugar que se evaluaron matrices ascendentes laplaceanas desde tamaños N = 2, hasta N = 15000.
	- Luego segun lo esperado la solucion del sistema Ax=b que demoro mas fue el "A_invB_inv", la cual demora mas debido a que primeramente se tiene que invertir la matriz A, para solucionar el sistema de la siguiente forma x=(A^-1)b. Con lo que el hecho de invertir la matriz toma mas tiempo que el solver en si, llegando a una resolucion del sistema con N = 15000 en un tiempo de 58,6 segundos aprox.
	- Realizando la comparacion entre spSolve con spSolve_sym, se puede apreciar que al definir la matriz simetrica, esto optimiza de cierta forma los calculos haciendo que demore menos tiempo, ya que al definirla asi, el solver solo toma la parte triangular superior para realizar las operaciones matriciales, y al tomar la parte triangular significa que ocupa menos datos y con eso es esperable que tome menos tiempo, con una diferencia de aproximadamente 0,8 segundos para la matriz de tamaño N = 10000.
	- Finalmente la mejor opcion en esta caso fue la definida con overwrite = True, el resultado tambien fue esperado debido a que la funcion de "overwrite" lo que hace es permitir que se pueda sobreescribir informacion en este caso en la matriz A, lo que hace que la realizacion de los pasos algebraicos sean mas rapidos y asi se pueda optimizar el tiempo de resolucion del sistema.
 
# Matrices dispersas y complejidad computacional
## Complejidad algoritmica de MATMUL
	- Grafico matrices llenas:
		- ![image](https://user-images.githubusercontent.com/43451947/90794806-3dc11280-e2db-11ea-936a-25dcd7770789.png)
	- Grafico matrices dispersas:
		- ![image](https://user-images.githubusercontent.com/43451947/90794864-53ced300-e2db-11ea-8c35-e3b567f09231.png)
	- Comentarios y discusiones:
		-
## Complejidad algorítmica de SOLVE
	- Grafico matrices llenas:
		- ![image](https://user-images.githubusercontent.com/43451947/90794892-60532b80-e2db-11ea-8710-2c10334258fe.png)
	- Grafico matrices dispersas:
		- ![image](https://user-images.githubusercontent.com/43451947/90794916-6a752a00-e2db-11ea-8349-485e70ea7614.png)
	- Comentarios y discusiones:
		-
## Complejidad algorítmica de INV:
	- Grafico matrices llenas:
		- ![image](https://user-images.githubusercontent.com/43451947/90794942-7234ce80-e2db-11ea-91b1-79cbd6e2dd94.png)
	- Grafico matrices dispersas:
		- ![image](https://user-images.githubusercontent.com/43451947/90794963-7c56cd00-e2db-11ea-99da-3e0129f6b7a4.png)
	- Comentarios y discusiones:
		-





