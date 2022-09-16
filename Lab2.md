# Lab 2 - Robotica de desarrollo - Intro a ROS #2

### Contenido

1. [Script en MATLAB](#script-en-matlab-computer)
2. [Script en Python](#script-en-python-snake)
3. [Conclusiones](#autores-blacknib)
5. [Referencias](#referencias-openbook)

6. [Autores](#autores-blacknib)


## Script en MATLAB :computer:
Lo primero que se nos pide es abrir 2 terminales en Ubuntu para esto se da click izquierdo en el simbolo de terminal de la barra de tareas 2 veces, posterior a esto se escribe en la primera terminal el comando de "roscore" para iniciar el nodo maestro.  
![1](/Lab2/mediaLab2/1roscore.png)
Una vez iniciado el nodo maestro se escribe en la segunda terminal el comando "rosrun turtlesim turtlesim_node" el cual se introduce para correr turtlesim
![2](/Lab2/mediaLab2/2rosrun.png)
Una vez abierta una instacia de matlab para linux se introduce el codigo propuesto por la guia con el cual se busca realizar un conexion con el nodo maestro, definir un publicador y posteriormente manipular este publicador para poder enviar un comando a TurtleSim.
**falta un pantallazo de matlab y el codigo el de la guia **
Lo primero que se realiza es la suscripcion al nodo de TurtleSim para poder recibir datos, esto se hace mediante la funcion "rossubscriber" cuyos argumentos son los datos que se desean recibir, que en este caso son los provenientes de turtle1 acerca de la posicion "/turtle1/pose", y el segundo argumento es el tipo de mensaje que se va a recibir, de forma general tendra la estructura de la posicion proveniente de TurtleSim "/TurtleSim/pose". 
![3](/Lab2/mediaLab2/3turtlePos.png)

![4](/Lab2/mediaLab2/4turtleTeleport.png)

![5](/Lab2/mediaLab2/5turtleTeleport.png)

## Script en Python :snake:



<p align="center"><img width="700" src="https://github.com/sofiaponteb/Labs-Robotica-2022-2/blob/main/mediaLab1/AJescribiendo.gif"></p>


## Conclusiones :page_facing_up:



## Referencias :open_book:
- Laboratorio 2 - Robotica de desarrollo - Intro a ROS UNAL.


## Autores :black_nib:
Ana Sofía Aponte Barriga

José Alejandro Peñaranda Chía

Universidad Nacional de Colombia - Sede Bogotá

Ingeniería Mecatrónica
