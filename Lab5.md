# Lab 5 - Cinemática Inversa - Robot Phantom X - ROS

### Contenido

1. [Modelo de cinemática inversa](#modelo-de-cinemática-inversa)
1. [Script en Python](#script-en-python-snake)
1. [Resultados](#resultados)
3. [Conclusiones](#conclusiones-page_facing_up)
5. [Referencias](#referencias-openbook)

6. [Autores](#autores-blacknib)

>Nota: Los documentos referentes a este laboratorio se encuentran en la carpeta del respositorio denominada "Lab5"


## Modelo de cinemática inversa

Inicialmente se realizó el trazo manual de los dos semicírculos que delimitan el alcance del robot, con la ayuda del software dynamyxel. Posteriormente se realizó un modelo en AutoCAD de los trazos a realizar del robot pincher, para así poder tomar las coordenadas de cada dibujo y tener un punto de partida para la cinemática inversa. Las coordenadas tomadas se encuentran en el archivo de excel ```Puntos_XYZ_AJ.xlsx```

![1](/Lab5/img/circulo.png)

Se realizó un modelo de cinemática inversa en MATLAB, para así poder encontrar los ángulos correspondientes a cada eslabón del robot según la posición que se deseara alcanzar.

>     l = [0, 10.6, 10.6, 7.6];
>     qini = [0,0,0,0];
>     offset = [0, pi/2, 0, 0];
>     % Orden parametros funcion link [THETA D A ALPHA SIGMA(0R,1P) OFFSET]
>     DHparameters = [qini(1) 4.8 l(1) pi/2 0 offset(1);
>                     qini(2) 0   l(2) 0    0 offset(2);
>                     qini(3) 0   l(3) 0    0 offset(3);
>                     qini(4) 0   l(4) pi/2    0 offset(4)];
>     L(1) = Link(DHparameters(1,:));
>     L(2) = Link(DHparameters(2,:));
>     L(3) = Link(DHparameters(3,:));
>     L(4) = Link(DHparameters(4,:));
>     Robot_pincher = SerialLink(L,'name','Pincher');
>     ws = [-30 30 -30 30 -10 50];

En la variable ```l``` se almacenan las longitudes de los eslabones del robot pincher utilizado para el ejercicio. Posteriormente se realiza la matriz de parámetros DH teniendo en cuenta ```theta, d, a, alpha```. Finalmente, usando el toolbox de peter corke se construye el modelo de los eslabones utilizando la función ```link``` y posteriormente se genera el modelo del robot con la función ```SerialLink```.

Para cada conjunto de coordenadas, se hallan los valores de los ángulos con los que debe cumplir cada eslabón:

>     y=0.01
>     x=30
>     z=7.7
>     q=double(round(ikine(x,y,z),3))
>     qfin=[q(1), pi/2-q(2),-q(3),-q(4)]
>     view([4 30]);
>     Robot_pincher.plot(qfin,'workspace',ws);

Estos ángulos se hallan gracias a la función de cinemática inversa ```ikine```, que se presenta a continuación:

>     function q = ikine(x,y,z)
>        syms theta2 theta3;
>        l1=9.2;
>        l2=4.8; 
>        l3=10.6;
>        l4=10.6; 
>        l5=10.5;
>        theta1=double(vpa(atan(y/x)));
>        eqn1 = z == l1+l2+sin(theta2)*l3+sin(theta2+theta3)*l4;
>        eqn3 = y == sin(theta1)*(cos(theta2)*l3+cos(theta2+theta3)*l4+l5);
>        S = solve([eqn1 eqn3],[theta2 theta3],'Real',true);
>        theta4=-(vpa(S.theta2(1))+vpa(S.theta3(1)));
>        q=[theta1 vpa(S.theta2(1)) vpa(S.theta3(1)) theta4];
>     end

## Script en Python :snake:

Por comodidad en la lectura no se incluye el script en este readme, sin embargo, se encuentra disponible en la carpeta del repositorio que lleva como nombre ```Lab4```.

A lo largo del script se ejecutan los siguientes ítems:
- importación de paquetes necesarios para el desarrollo del ejercicio
- definición del archivo fuente en excel
- parametrización de las alturas del marcador y valores de apertura y cierre del último eslabón
- funciones para cada uno de los trazos a realizar: ```Arco interno, arco externo, nombres, triangulo, circulo, lineas, puntos, figura```
- funciones para movimientos del robot: ```tomar herramienta, dejar herramienta```
- condicional que asocia cada una de las funciones anteriores a una tecla, logrando así que al presionarla se realice dicho movimiento. (al inicio y al final de cada trazo se agrega un movimiento hasta home, para así evitar posibles choques o movimientos indeseados)



Para ejecutar este código se utilizaron los siguientes comandos en una terminal de Linux, con el robot Pincher conectado a un puerto USB del computador:

En la ruta ```/catkin_ws/src```

```
sudo chmod 777 /dev/ttyUSB0
```

En la ruta ```/catkin_ws```
```
catkin build dynamixel_one_motor
```

```
source devel/setup.bash
```

```
roslaunch dynamixel_one_motor one_controller.launch
```

Luego de esto, se ejecuta el script de python y con las teclas pre definidas se controla la rutina de escritura del robot.


<p align="center"><img width="400" src="https://"></p>



## Resultados

A continuación se presentan los resultados obtenidos en el ejercicio:

<p align="center"><img width="400" src="https://www.fotosdememes.com/wp-content/uploads/2022/04/aqui-colocaria-mi-trofeo-si-tuviera-uno-sin-texto.jpg"></p>

## Conclusiones :page_facing_up:

- Se debe tener en cuenta la cantidad de puntos a enviar al robot pincher, ya que si se enviaban muchos puntos a la vez se saturaba la salida y el robot dejaba de responder. Adicionalmente, se presentaba un desfase en el eje Z, que aumentaba conforme se ponían más puntos en un mismo trazo, esto provocaba que al final de un dibujo el marcador ya no estuviera sobre la superficie.

- Cuando hay poca disponibilidad de recursos se vuelve fundamental el trabajo en equipo, no solo dentro de los grupos de trabajo para cada laboratorio sino también entre varios, ya que esto brinda un beneficio común y se mitigan los riesgos de que alguien no pueda realizar el ejercicio.

- Se hace necesaria la verificación del robot al inicio de cada práctica, ya que existe la posibilidad de que se haya generado algún desfase en algún eslabón, haciendo parecer que hay un script incorrecto cuando esto se puede corregir simplemente sumando un ángulo al eslabón correcto.



## Referencias :open_book:
- Laboratorio 5 - Cinemática Inversa - Robot Phantom X - ROS
- Apuntes de clase, Robótica 2022-2


## Autores :black_nib:
Ana Sofía Aponte Barriga

José Alejandro Peñaranda Chía

Universidad Nacional de Colombia - Sede Bogotá

Ingeniería Mecatrónica
