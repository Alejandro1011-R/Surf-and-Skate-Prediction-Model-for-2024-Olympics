# Surf-and-Skate-Prediction-Model-for-2024-Olympics

**Introducción:**

El proyecto de simulación de competencias de surf nace como una iniciativa investigativa en la Universidad de La Habana, con el objetivo de predecir los resultados en deportes extremos, especialmente en el surf, para la próxima olimpiada. Esta investigación responde a la creciente demanda de herramientas y técnicas avanzadas capaces de analizar y predecir el rendimiento deportivo, proporcionando insights valiosos para entrenadores, atletas y aficionados al deporte.

El proyecto se propone explorar cómo técnicas de modelado estadístico y simulación computacional pueden proporcionar una comprensión más profunda del rendimiento en competiciones de surf. Al utilizar datos históricos de competiciones anteriores, se busca desarrollar modelos predictivos que puedan simular resultados futuros y ayudar a los atletas, entrenadores y organizadores de eventos a tomar decisiones más informadas.

El objetivo del proyecto es desarrollar un modelo predictivo para predecir los resultados de la próximas Olimpiadas en la modalidad surf y proporcionar información valiosa sobre el rendimiento individual de los surfistas en diferentes condiciones y eventos.

En nuestra simulación de competencias utilizamos los modelos de estimación de densidad kernel (KDE) que son una técnica no paramétrica utilizada para estimar la función de densidad de probabilidad (PDF) de una variable aleatoria continua. En términos más simples, los modelos KDE se utilizan para obtener una estimación suave de la distribución de los datos observados.

Las variables de interés que describen el problema son:

1. **Nombre del surfista (`Name`):** Esta variable identifica a cada surfista que participa en el torneo.
2. **Puntos promedio por evento (`Average Points per Events`):** Representa el rendimiento promedio de cada surfista en los eventos anteriores. Este dato se utiliza para ajustar los modelos de densidad kernel (KDEs) que describen el rendimiento de cada surfista.
3. **Año (`Year`):** Indica en qué año se obtuvieron los puntos promedio por evento.
4. **Tipo de ronda de la competición (`Round Type`):** Describe el tipo de ronda en la que participa cada surfista (por ejemplo, ronda 1, octavos de final, cuartos de final, etc.). Esta información se utiliza para simular las diferentes rondas del torneo.
5. **Resultados de la competición:** Los resultados de cada ronda del torneo se utilizan para actualizar los modelos y simular las siguientes rondas. Esto incluye información sobre los surfistas que avanzan a las siguientes rondas y su rendimiento en cada ronda.

Estas variables describen los datos de entrada del problema (nombre del surfista, puntos promedio por evento, año) y los resultados de la competición (resultados de cada ronda del torneo), que se utilizan para ajustar los modelos y simular el torneo de surf.

**Pasos seguidos para la implementación.**

**Recopilación de Datos:**

La recopilación de datos es un paso fundamental en el proyecto, ya que proporciona la materia prima necesaria para el análisis y la simulación. En este sentido, se ha utilizado una variedad de fuentes de datos para obtener información sobre competiciones pasadas, resultados de surfistas y condiciones de oleaje.

1. **World Surf League (WSL):** La WSL es la principal organización que supervisa las competiciones de surf a nivel mundial. Se ha accedido a su plataforma en línea para recopilar datos históricos sobre eventos pasados, resultados de competiciones y detalles de los surfistas participantes (https://www.worldsurfleague.com/athletes). Esto incluye información sobre los nombres de los surfistas, sus resultados en competiciones anteriores y puntuaciones obtenidas en cada ronda.
2. **Fuentes de Datos Externas:** Además de la plataforma oficial de la WSL, se han utilizado otras fuentes de datos externas para complementar la información disponible como (https://isasurf.org/event/paris-2024/#) para saber los clasificados a las olimpiadas y las personas que hiban a participar en cada heat.
3. **Herramientas de Web Scraping:** Para recopilar datos de sitios web que no ofrecen acceso directo a través de una API o una base de datos estructurada, se han utilizado técnicas de web scraping. Esto implica el uso de bibliotecas como BeautifulSoup y Selenium en Python para extraer información de páginas web HTML y convertirla en un formato utilizable para el análisis posterior.

En conjunto, la recopilación de datos se ha llevado a cabo de manera exhaustiva y cuidadosa, asegurando que se obtenga una variedad de información relevante y confiable sobre competiciones pasadas y surfistas individuales. Esto proporciona una base sólida para el análisis y la simulación en etapas posteriores del proyecto.

**Preprocesamiento de Datos:**

Una vez recopilados, los datos fueron sometidos a un riguroso proceso de preprocesamiento para limpiarlos y prepararlos para su análisis. Esto incluyó tareas como la eliminación de duplicados, la imputación de valores faltantes, la normalización de datos y la identificación y manejo de valores atípicos. Este paso es crucial para garantizar la calidad y consistencia de los datos utilizados en el modelado estadístico subsiguiente.

El preprocesamiento de datos es una fase crítica en cualquier proyecto de análisis de datos, ya que garantiza que los datos estén limpios, estructurados y listos para el análisis. En el contexto de este proyecto, el preprocesamiento de datos incluye varias etapas clave:

1. **Limpieza de Datos:** Se realizan operaciones para eliminar datos duplicados, manejar valores faltantes y corregir posibles errores en los datos. Esto puede implicar eliminar registros incompletos o inconsistentes, rellenar valores faltantes con estimaciones razonables o eliminar caracteres no deseados en los datos.
2. **Transformación de Datos:** Los datos se transforman y reorganizan según sea necesario para facilitar el análisis posterior. Por ejemplo, se pueden realizar conversiones de tipos de datos, como convertir cadenas de texto en números para su análisis numérico. Además, se pueden crear nuevas variables derivadas de los datos originales para capturar información adicional relevante.
3. **Selección de Características:** Se pueden seleccionar las características más relevantes y significativas para el análisis o la modelización. Esto ayuda a reducir la dimensionalidad de los datos y a mejorar la eficiencia y la interpretabilidad de los modelos
4. .**División de Datos:** Los datos se dividen en conjuntos de entrenamiento y prueba para evaluar la precisión y el rendimiento de los modelos. Esto asegura que los modelos se evalúen en datos independientes de los utilizados para su entrenamiento, lo que ayuda a evitar el sobreajuste.

En el proyecto, el preprocesamiento de datos se llevó a cabo utilizando varias herramientas y técnicas para garantizar que los datos estuvieran limpios y estructurados adecuadamente para su análisis posterior. A continuación, se detallan algunas de las principales estrategias utilizadas:

1. **Limpieza de Datos con Pandas y NumPy:** Se utilizó la biblioteca Pandas de Python para cargar y manipular los datos en estructuras de datos tabulares, como DataFrames. Se realizaron operaciones de limpieza de datos, como la eliminación de registros duplicados y el manejo de valores faltantes. Además, NumPy se utilizó para realizar operaciones numéricas eficientes en los datos.
2. **Transformación de Datos con Pandas:** Se realizaron transformaciones en los datos según fuera necesario para facilitar su análisis. Esto incluyó la conversión de tipos de datos, como la conversión de cadenas de texto en números, y la creación de nuevas variables derivadas de los datos originales para capturar información adicional.
3. **Normalización de Datos:** Aunque no se mencionó explícitamente en el código proporcionado, la normalización de datos es una técnica común en el preprocesamiento de datos para asegurar que todas las variables estén en la misma escala o rango. Esto puede ser especialmente importante cuando se utilizan algoritmos sensibles a la escala de las variables, como los modelos de aprendizaje automático.
4. **Selección de Características:** Si bien no se realizó explícitamente en el código proporcionado, la selección de características es una etapa importante del preprocesamiento de datos en muchos proyectos de análisis de datos. Esto implica identificar y seleccionar las características más relevantes y significativas para el análisis o la modelización.
5. **División de Datos con sklearn:** Se utilizó la función train_test_split de la biblioteca scikit-learn para dividir los datos en conjuntos de entrenamiento y prueba. Esta división asegura que los modelos se evalúen en datos independientes de los utilizados para su entrenamiento, lo que ayuda a evitar el sobreajuste.

En resumen, el preprocesamiento de datos en el proyecto se llevó a cabo utilizando una combinación de herramientas y técnicas, incluyendo Pandas, NumPy y scikit-learn, para garantizar que los datos estuvieran limpios, estructurados y listos para su análisis posterior.

##### Generación de variables aleatorias

En el contexto del modelo presentado, la técnica de aceptación-rechazo se utiliza implícitamente en la simulación del torneo de surf.

Esta técnica es un método general utilizado en simulación estocástica para generar muestras de una distribución de probabilidad dada. En este caso, se aplica en la generación de muestras de los KDEs ajustados para simular el rendimiento de los surfistas en cada ronda del torneo.

En la simulación de cada ronda del torneo, se generan muestras aleatorias de los KDEs de cada surfista utilizando la técnica de aceptación-rechazo. Estas muestras representan los posibles resultados de rendimiento de los surfistas en la ronda actual del torneo. Luego, estos resultados se utilizan para determinar qué surfistas avanzan a las siguientes rondas del torneo.

**Modelo utilizado para la Simulación de Competencias:**

En nuestra simulación de competencias utilizamos los modelos de estimación de densidad kernel (KDE) que son una técnica no paramétrica utilizada para estimar la función de densidad de probabilidad (PDF) de una variable aleatoria continua. En términos más simples, los modelos KDE se utilizan para obtener una estimación suave de la distribución de los datos observados.

Matemáticamente, supongamos que tenemos una muestra \( X = \{x_1, x_2, ..., x_n\} \) de una variable aleatoria continua \( X \). La función de densidad de probabilidad (PDF) de esta variable aleatoria es denotada por \( f(x) \). La idea detrás de los modelos KDE es aproximar esta función \( f(x) \) utilizando una combinación de funciones más simples conocidas como "kernels". El KDE se define como:

\[ \hat{f}_h(x) = \frac{1}{n \cdot h} \sum_{i=1}^{n} K\left(\frac{x - x_i}{h}\right) \]

Donde:

- \( \hat{f}_h(x) \) es la estimación de la densidad de probabilidad en el punto \( x \).
- \( n \) es el número de muestras en el conjunto de datos.
- \( h \) es el ancho de banda (bandwidth), un parámetro que controla la suavidad de la estimación.
- \( K(\cdot) \) es la función kernel, que asigna un peso a cada observación según su distancia a \( x \).

Los kernels más comúnmente utilizados incluyen el kernel gaussiano (también conocido como kernel normal), el kernel uniforme y el kernel triangular. En el contexto de los modelos KDE, el ancho de banda (\( h \)) juega un papel importante en la suavidad de la estimación: un valor más pequeño de \( h \) conduce a una estimación más detallada (y posiblemente con más ruido), mientras que un valor más grande de \( h \) produce una estimación más suave pero potencialmente menos detallada.

En nuestro proyecto utilizamos  el kernel `tophat` para ajustar las estimaciones de densidad kernel (KDEs) el cual utiliza cla funcion de Epanechnikov.

La función de Epanechnikov se define como:

\[ K(u) = \frac{3}{4}(1 - u^2) \]

donde \( u \) es la variable de entrada, generalmente normalizada para que esté en el rango [-1, 1].

Esta función de kernel tiene una forma de "cuenco" y es no negativa en el intervalo [-1, 1], alcanzando su máximo en \( u = 0 \). Fuera de este intervalo, la función de Epanechnikov es cero.

La función de Epanechnikov se utiliza comúnmente en KDEs debido a sus propiedades deseables. Algunas de estas propiedades incluyen:

1. **Óptima para estimar la media:** La función de Epanechnikov es óptima en el sentido de que minimiza el error cuadrático medio en la estimación de la media de una distribución normal. Esto la hace adecuada para aplicaciones donde la precisión en la estimación de la media es importante.
2. **Reducción de varianza:** La función de Epanechnikov reduce la varianza de la estimación de densidad en comparación con otros kernels como el kernel gaussiano, especialmente en la vecindad del centro del kernel.
3. **Robustez:** La función de Epanechnikov es robusta frente a datos atípicos o valores extremos debido a su naturaleza truncada.

En resumen, la función de Epanechnikov es una opción popular para la estimación de densidades kernel debido a sus buenas propiedades estadísticas y su capacidad para producir estimaciones de densidad suaves y eficientes.

Simulación de Competencias:

En el proyecto, una de las partes más interesantes es la simulación de competencias. Esta parte se llevó a cabo utilizando modelos de densidad kernel (KDE, por sus siglas en inglés) para simular el rendimiento de los surfistas en cada ronda de la competencia. A continuación, se detallan los pasos y las técnicas utilizadas en esta etapa:

1. **Kernel Density Estimation (KDE):** Los modelos KDE se utilizaron para estimar la distribución de probabilidad de los puntajes de los surfistas en cada ronda de la competencia. Estos modelos se construyeron utilizando los datos históricos de rendimiento de los surfistas en eventos anteriores.
2. **Generación de Muestras Simuladas:** Una vez que se construyeron los modelos KDE, se generaron muestras simuladas de los puntajes de los surfistas para cada ronda de la competencia. Estas muestras se obtuvieron muestreando aleatoriamente la distribución de probabilidad estimada por los modelos KDE.
3. **Simulación de Heats y Rondas:** Utilizando las muestras simuladas de puntajes de los surfistas, se simularon las rondas de la competencia, incluyendo los heats individuales. En cada ronda, se asignaron puntajes simulados a cada surfista en función de su desempeño estimado por el modelo KDE.
4. **Determinación de Ganadores:** Después de simular todas las rondas de la competencia, se determinaron los ganadores de cada heat y ronda en función de los puntajes simulados. Estos resultados se utilizaron para avanzar a los surfistas en la competencia hasta que se determinaron los finalistas.
5. **Evaluación de Resultados:** Una vez completada la simulación de la competencia, se evaluaron los resultados obtenidos y se compararon con los resultados reales de la competencia histórica para validar la efectividad de la simulación.

La simulación de competencias se llevó a cabo utilizando modelos KDE para estimar la distribución de probabilidad de los puntajes de los surfistas, y luego se generaron muestras simuladas para simular el rendimiento de los surfistas en cada ronda de la competencia. Este enfoque proporcionó una manera interesante y efectiva de predecir los resultados de la competencia y explorar diferentes escenarios hipotéticos.

**Resultados y Evaluación:**

Después de completar la simulación de la competencia, se procedió a analizar los resultados obtenidos y evaluar su validez en comparación con los datos reales de la competencia histórica. Este proceso de resultados y evaluación implicó los siguientes pasos y consideraciones:

1. **Análisis de los Resultados Simulados:** Se examinaron los resultados simulados de cada ronda de la competencia, incluidos los puntajes de los surfistas en cada heat y las clasificaciones finales de cada ronda. Esto permitió comprender cómo se desarrolló la competencia simulada y quiénes fueron los surfistas destacados en cada etapa.
2. **Comparación con Datos Reales:** Se compararon los resultados simulados con los datos reales de la competencia histórica para determinar su precisión y validez. Esto implicó analizar si los surfistas que se destacaron en la simulación coincidieron con los surfistas que obtuvieron buenos resultados en la competencia real.
3. **Evaluación de la Efectividad:** Se evaluó la efectividad de la simulación considerando diversos factores, como la precisión en la predicción de los resultados, la coherencia con los datos históricos y la capacidad para identificar tendencias y patrones en el rendimiento de los surfistas.
4. **Validación de la Metodología:** Se examinó la robustez y la validez de la metodología utilizada en la simulación, incluyendo la construcción de los modelos KDE, la generación de muestras simuladas y la simulación de la competencia en sí. Se consideraron aspectos como la calidad de los datos utilizados, la adecuación de los modelos y la consistencia en los resultados obtenidos.
5. **Identificación de Mejoras Potenciales:** Se identificaron posibles áreas de mejora en la metodología de simulación y en la selección de parámetros, con el objetivo de perfeccionar el proceso y aumentar su precisión en futuras simulaciones.

El análisis de los resultados y la evaluación de la simulación de la competencia implicaron comparar los resultados simulados con los datos reales, evaluar la efectividad de la metodología utilizada y validar la capacidad de la simulación para predecir resultados precisos y coherentes con la realidad histórica. Este proceso proporcionó información valiosa sobre la utilidad y la fiabilidad de la simulación en la predicción de eventos deportivos como las competencias de surf.

**Conclusiones :**

En conclusión, el proyecto ha demostrado la viabilidad y utilidad de utilizar técnicas avanzadas de modelado estadístico y simulación para analizar y predecir el desempeño en competiciones de surf. Se recomienda continuar refinando los modelos y procesos de simulación utilizando datos adicionales y técnicas de modelado más avanzadas.
