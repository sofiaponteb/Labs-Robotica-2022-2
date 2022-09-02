# Lab 1 - Robótica industrial #1

### Contenido

1. [Diseño de la herramienta](#diseño-de-la-herramienta-wrench)

2. [Código en RAPID del módulo utilizado para el desarrollo de la práctica](#código-en-rapid-del-módulo-utilizado-para-el-desarrollo-de-la-práctica-computer)

3. [Simulación en *RobotStudio* - implementación de la práctica con los robots reales](#simulación-en-robotstudio---implementación-de-la-práctica-con-los-robots-reales-moviecamera)

4. [Descripción de la solución planteada](#descripción-de-la-solución-planteada-pagefacingup)

5. [Referencias](#referencias-openbook)

6. [Autores](#autores-blacknib)


## Diseño de la herramienta :wrench:
Para el diseño de la herramienta se uso como base el modelo disponible en el repositorio de Robotstudio y las recomendaciones dadas por el profesor, de está forma se modelo la herramienta a usar en el software de INVENTOR, la cual consta de 3 partes:
- Estructura base para la fijacion al plato.

- PortaHerramienta para sostener el marcador.

- Tapa de fijacion.
Se utiliza una herramienta con una inclinacion de 30° para disminuir la aparicion de singularidades en el modelo.
Las partes anteriormente nombradas se materializaron usando impresion 3D y se ensamblaron entre si para asi obtener el montaje final de la herramienta, las uniones se hicieron mediante tornillos o usando pegantes.


Acatando las recomendacioens del profesor debido al desconocimiento de las dimensiones finales del modelo se decidio realizar calibracion usando el robot real obteniendo lo siguiente:

En conjunto con la calibracion y el montaje final de la herramienta se realizo el diseño de está en Robotstudio, para asi tener el modelo mas aproximado a la realidad y poder realizar la programacion de la rutina a desarrollar.

![marcador](/mediaLab1/herramienta.jfif)

## Código en RAPID del módulo utilizado para el desarrollo de la práctica :computer:




## Simulación en *RobotStudio* - implementación de la práctica con los robots reales :movie_camera:




## Descripción de la solución planteada :page_facing_up:
Para poder realizar la rutina propuesta fue necesario en primer lugar crear la herramienta en Robotstudio, posterior a esto fue necesario importar la geometria la cual va a seguir la rutina, habiendo implementado todo nuestro montaje procedemos a definir las rutinas para esto usamos la funcion de autodefinir trayectos seleccionando een orden lños trayectos a recorres, ademas, definimos las posiciones articulares de interes para nuestra rutina estas son home y punto medio entre el trayecto. Despues, ingresamos estos trayectos al codigo de RAPID y lo ejecutamos para ver su buen funcionamiento. Por ultimo, subimos el programa al flex expendant y lo ejecutamps usando el controlador y el manipulador del laboratorio.



## Referencias :open_book:
- Laboratorio 1 - Robotica Industrial No. 1 UNAL.
- 


## Autores :black_nib:
Ana Sofía Aponte Barriga

José Alejandro Peñaranda Chía

Universidad Nacional de Colombia - Sede Bogotá

Ingeniería Mecatrónica