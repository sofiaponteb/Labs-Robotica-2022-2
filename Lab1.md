# Lab 1 - Robótica industrial #1

### Contenido

1. [Diseño de la herramienta](#diseño-de-la-herramienta-wrench)

2. [Código en RAPID del módulo utilizado para el desarrollo de la práctica](#código-en-rapid-del-módulo-utilizado-para-el-desarrollo-de-la-práctica-computer)

3. [Simulación en *RobotStudio* - implementación de la práctica con los robots reales](#simulación-en-robotstudio---implementación-de-la-práctica-con-los-robots-reales-moviecamera)

4. [Descripción de la solución planteada](#descripción-de-la-solución-planteada-pagefacingup)

5. [Referencias](#referencias-openbook)

6. [Autores](#autores-blacknib)


## Diseño de la herramienta :wrench:
Para el diseño de la herramienta se usó como base el modelo disponible en el repositorio de Robotstudio y las recomendaciones dadas por el profesor, de esta forma se modeló la herramienta a usar en el software de INVENTOR, la cual consta de 3 partes:
- Estructura base para la fijación al plato.

- PortaHerramienta para sostener el marcador.

- Tapa de fijación.

Se utiliza una herramienta con una inclinación de 30° para disminuir la aparición de singularidades en el modelo.

Las partes anteriormente nombradas se materializaron usando impresión 3D y se ensamblaron entre sí para así obtener el montaje final de la herramienta, las uniones se hicieron mediante tornillos o usando pegantes.

![marcador](/mediaLab1/herramienta.jfif)
![montaje](/mediaLab1/marcadormontado.jfif)

Acatando las recomendacioens del profesor debido al desconocimiento de las dimensiones finales del modelo se decidió realizar calibración usando el robot real obteniendo lo siguiente:

![calibracion](/mediaLab1/calibracion.jfif)
![calibracion](/mediaLab1/marcadorcalibrado.jfif)

En conjunto con la calibración y el montaje final de la herramienta se realizó el diseño de esta en Robotstudio, para así tener el modelo más aproximado a la realidad y poder realizar la programación de la rutina a desarrollar.



## Código en RAPID del módulo utilizado para el desarrollo de la práctica :computer:

El código en RAPID usado para el desarrollo de la práctica se encuentra en la carpeta ```AJ_Lab1```.

Para realizar este código incialmente se creó un modelo del tablero en inventor, donde se incluyeron las iniciales de los integrantes del grupo. Esta pieza se importó a RobotStudio y se ubicó en el espacio de trabajo con una inclinación de 45°, posteriormente se parametrizaron los targets y la orientación de la herramienta en cada punto para así poder generar 3 paths, correspondientes a las partes interna y externa de la A y el trazo de la J. Finalmente, se creó un target de orientación de joints para crear un path a home y un target en un punto medio arbitrario para mayor seguridad al momento de ejecutar el programa. 

Los parámetros generados se llevaron a la interfaz de RAPID, donde se creó la sección main del código, donde se iniciaba en home, se pasaba por la posición intermedia, se trazaban las letras y finalmente se volvía a home pasando por la posición media. 

A continuación se muestra el código utilizado:

> MODULE Module1
>         !!!!!!! sección de targets eliminada para mejor visualización del código. Para ver el código completo diríjase a la carpeta AJ_Lab1 de este repositorio
> !***********************************************************
>     !
>     ! Module:  Module1
>     !
>     ! Description:
>     !   <Insert description here>
>     !
>     ! Author: Usuario
>     !
>     ! Version: 1.0
>     !
>     !***********************************************************
>     
>    
>     !***********************************************************
>     !
>     ! Procedure main
>     !
>     !   This is the entry point of your program
>     !
>     !***********************************************************
>     PROC main()
>     GoHome ;
>     GoMedio ;
>     A1 ;
>     A2 ;
>     J ;
>     GoMedio ;
>     GoHome ;
>     ENDPROC
>     PROC Path_10()
>         MoveL Target_10,v200,z10,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_20,v200,z10,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_30,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_40,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_50,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_60,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_70,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_80,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_90,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_100,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_110,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_120,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_130,v200,z100,tool_lab1\WObj:=tabla_AJ;
>     ENDPROC
>     PROC Path_20()
>         MoveL Target_140,v200,z10,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_150,v200,z10,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_160,v200,z10,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_170,v200,z10,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_180,v200,z10,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_190,v200,z10,tool_lab1\WObj:=tabla_AJ;
>    ENDPROC
>     PROC Path_30()
>         MoveL Target_200,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_210,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_220,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_230,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_240,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_250,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_260,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_270,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_280,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_290,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_300,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_310,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_320,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_330,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_340,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_350,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_360,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_370,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_380,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_390,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_400,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_410,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_420,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_430,v200,z100,tool_lab1\WObj:=tabla_AJ;
>     ENDPROC
>     PROC A1()
>         MoveL Target_10,v200,z10,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_20,v200,z10,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_30,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_40,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_50,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_60,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_70,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_80,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_90,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_100,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_110,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_120,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_130,v200,z100,tool_lab1\WObj:=tabla_AJ;
>     ENDPROC
>     PROC A2()
>         MoveL Target_140,v200,z10,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_150,v200,z10,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_160,v200,z10,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_170,v200,z10,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_180,v200,z10,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_190,v200,z10,tool_lab1\WObj:=tabla_AJ;
>     ENDPROC
>     PROC J()
>         MoveL Target_200,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_210,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_220,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_230,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_240,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_250,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_260,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_270,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_280,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_290,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_300,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_310,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_320,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_330,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_340,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_350,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_360,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_370,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_380,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_390,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_400,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_410,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_420,v200,z100,tool_lab1\WObj:=tabla_AJ;
>         MoveL Target_430,v200,z100,tool_lab1\WObj:=tabla_AJ;
>     ENDPROC
>     PROC GoHome()
>         MoveAbsJ Home,v1000,z100,tool_lab1\WObj:=tabla_AJ;
>     ENDPROC
>     PROC GoMedio()
>         MoveAbsJ Medio,v1000,z100,tool_lab1\WObj:=tabla_AJ;
>     ENDPROC
> ENDMODULE


## Simulación en *RobotStudio* - implementación de la práctica con los robots reales :movie_camera:
Ya con el código de RAPID se procede a ubicar el main y con esto se realiza la simulación del trazado de las letras, para así poder verificar el correcto funcionamiento del mismo antes de realizarlo en el robot del laboratorio, a continuación se muestran las dos simulaciones realizadas:
<p align="center"><img width="700" src="https://github.com/sofiaponteb/Labs-Robotica-2022-2/blob/main/mediaLab1/simulacion1.gif"></p>

<p align="center"><img width="700" src="https://github.com/sofiaponteb/Labs-Robotica-2022-2/blob/main/mediaLab1/simulacion2.gif"></p>

Cabe notar que para mayor seguridad al momento de realizar el trazado en el robot real, se realizó una configuración de velocidad en 200 y punto de aproximación en Z de 100. Esto quiere decir que a 100mm del plano de trazado el robot disminuirá su velocidad a 200 para así poder tener una mejor observabilidad de lo que sucede y en una eventualidad poder oprimir el botón de parada antes de cualquier daño que pudiera causarse.

Finalmente, se presenta un video del resultado final obtenido en la práctica de laboratorio:

<p align="center"><img width="700" src="https://github.com/sofiaponteb/Labs-Robotica-2022-2/blob/main/mediaLab1/AJescribiendo.gif"></p>

![letras](/mediaLab1/AJtablero.jfif)

## Descripción de la solución planteada :page_facing_up:
Para poder realizar la rutina propuesta fue necesario en primer lugar crear la herramienta en Robotstudio, posterior a esto fue necesario importar la geometría, la cual va a seguir la rutina. Habiendo implementado todo nuestro montaje procedemos a definir las rutinas para esto usamos la función de autodefinir trayectos seleccionando en orden los trayectos a recorrer. Además, definimos las posiciones articulares de interés para nuestra rutina estas son home y punto medio entre el trayecto. Después, ingresamos estos trayectos al código de RAPID y lo ejecutamos para ver su buen funcionamiento. Por último, subimos el programa al flex pendant y lo ejecutamos usando el controlador y el manipulador del laboratorio.

Se obtuvo un programa que es capaz de trazar el dibujo seleccionado en cualquier plano seeccionable dentro del espacio de trabajo del robot, esto gracias a la configuración flexible del workobject, que sólo requiere de la ubicación de los puntos: superior izquierdo, superior derecho e inferior derecho para poder ajustar las coordenadas y realizar el trazado en la superficie indicada.



## Referencias :open_book:
- Laboratorio 1 - Robotica Industrial No. 1 UNAL.


## Autores :black_nib:
Ana Sofía Aponte Barriga

José Alejandro Peñaranda Chía

Universidad Nacional de Colombia - Sede Bogotá

Ingeniería Mecatrónica