# Lab 2 - Robotica de desarrollo - Intro a ROS #2

### Contenido

1. [Script en MATLAB](#script-en-matlab-computer)
2. [Script en Python](#script-en-python-snake)
3. [Conclusiones](#autores-blacknib)
5. [Referencias](#referencias-openbook)

6. [Autores](#autores-blacknib)

>Nota: Los documentos referentes a este laboratorio se encuentran en la carpeta del respositorio denominada "Lab2"

## Script en MATLAB :computer:
Lo primero que se nos pide es abrir 2 terminales en Ubuntu para esto se da click izquierdo en el simbolo de terminal de la barra de tareas 2 veces, posterior a esto se escribe en la primera terminal el comando de ```roscore``` para iniciar el nodo maestro.  
![1](/Lab2/mediaLab2/1roscore.png)
Una vez iniciado el nodo maestro se escribe en la segunda terminal el comando ```rosrun turtlesim turtlesim_node``` el cual se introduce para correr turtlesim
![2](/Lab2/mediaLab2/2rosrun.png)
Una vez abierta una instacia de matlab para linux se introduce el codigo propuesto por la guia con el cual se busca realizar un conexion con el nodo maestro, definir un publicador y posteriormente manipular este publicador para poder enviar un comando a TurtleSim.

>      
>          %% INICIAL
>    
>          rosinit; %Conexion con nodo maestro
>    
>          %%
>    
>          velPub = rospublisher('/turtle1/cmd_vel','geometry_msgs/Twist'); %Creacion publicador
>    
>          velMsg = rosmessage(velPub); %Creacion de mensaje
>    
>          %%
>    
>          velMsg.Linear.X = 1; %Valor del mensaje
>    
>          send(velPub,velMsg); %Envio
>    
>          pause(1)
>    
>          %% SUBSCRIBER
>    
>          TurtlePose = rossubscriber("/turtle1/pose", "turtlesim/Pose")
>    
>          scanMsg = TurtlePose.LatestMessage
>    
>          %% POSE
>    
>          TurtleTeleport = rossvcclient("/turtle1/teleport_absolute")
>    
>          waitForServer(TurtleTeleport);
>    
>          TurtleMsg = rosmessage(TurtleTeleport)
>    
>          TurtleMsg.X = 5;
>    
>          TurtleMsg.Y = 3;
>    
>          TurtleMsg.Theta = 2*pi/3 ;
>    
>          call(TurtleTeleport,TurtleMsg)
>    
>          %% FINALIZAR NODO MAESTRO
>          rosshutdown


Lo primero que se realiza es la suscripcion al nodo de TurtleSim para poder recibir datos, esto se hace mediante la funcion ```rossubscriber``` cuyos argumentos son los datos que se desean recibir, que en este caso son los provenientes de turtle1 acerca de la posicion ```/turtle1/pose```, y el segundo argumento es el tipo de mensaje que se va a recibir, de forma general tendra la estructura de la posicion proveniente de TurtleSim ```/TurtleSim/pose```. 
![3](/Lab2/mediaLab2/3turtlePos.png)

A continuación se utiliza la función ```TurtleTeleport``` para asignar posiciones arbitrarias a la tortuga por medio de los atributos ```TurtleMsg.X``` y ```TurtleMsg.Y```. Posteriormente se realiza el llamado a la función Teleport enviándole como argumento los atributos asignados en TurtleMsg.

![4](/Lab2/mediaLab2/4turtleTeleport.png)

Al anterior procedimiento se le agrega el atributo de rotación, para evidenciar cómo sería un cambio de posición no solo con respecto a los ejes sino también de la orientación angular de la tortuga:

![5](/Lab2/mediaLab2/5turtleTeleport.png)

A continuación se muestra un animación del movimiento de la tortuga al usar la función ``TurtleTeleport``:

<p align="center"><img width="700" src="https://github.com/sofiaponteb/Labs-Robotica-2022-2/blob/main/Lab2/mediaLab2/tortugabonita.gif"></p>

## Script en Python :snake:

El codigo desarrollado para operar una tortuga del paquete turtlesim con el teclado es el siguiente:

>    
>       from pynput import keyboard
>       
>       import rospy
>       
>       import roslaunch
>       
>       from geometry_msgs.msg import Twist
>    
>       from turtlesim.srv import TeleportAbsolute, TeleportRelative
>    
>       import termios, sys, os
>    
>       from numpy import pi
>    
>       from std_srvs.srv import Empty
>    
>       rospy.init_node('TeleopKey', anonymous=True)
>    
>       def pubVel(speed, angspeed, t):
>       
>           velpub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
>        
>           velmsg = Twist()
>        
>           velmsg.linear.x = speed
>        
>           velmsg.angular.z = angspeed
>        
>           velpub.publish(velmsg)
>        
>           endTime = rospy.Time.now() + rospy.Duration(t)
>        
>           while rospy.Time.now() < endTime:
>        
>               velpub.publish(velmsg)
>    
>       def on_press(key):
>    
>           return
>    
>       def on_release(key):
>    
>           if key == keyboard.KeyCode.from_char('w'):
>        
>               pubVel(1, 0, 0.5)
>            
>           if key == keyboard.KeyCode.from_char('s'):
>        
>               pubVel(-1, 0, 0.5)
>            
>           if key == keyboard.KeyCode.from_char('a'):
>        
>               pubVel(0, -1, 0.5)
>            
>           if key == keyboard.KeyCode.from_char('d'):
>        
>               pubVel(0, 1, 0.5)
>            
>           if key == keyboard.Key.space:
>        
>                try:
>                       # Wait for the service to be available
>                    
>                       rospy.wait_for_service('/turtle1/teleport_relative')
>                    
>                       # Create handle to call the service
>                    
>                       giro = rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative)
>                    
>                       giro(0, pi)
>                    
>                       rospy.loginfo('Turtle rotated')
>                    
>                except rospy.ServiceException as e:  # If the service is not available, print a warning
>             
>                       rospy.logwarn("Service teleport_relative call failed")
>                    
>           if key == keyboard.KeyCode.from_char('r'):
>        
>                try:
>                       rospy.wait_for_service('/turtle1/teleport_absolute')
>                    
>                       teleportOrigen = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
>                    
>                       Reset=teleportOrigen(5.5, 5.5, 0)
>    
>                       rospy.wait_for_service('/clear')  # Clear the trajectory
>                    
>                       clearTrajec = rospy.ServiceProxy('/clear', Empty)
>                    
>                       Reset = clearTrajec()
>    
>                       rospy.loginfo('Turtle reset')
>                    
>                except rospy.ServiceException as e:
>             
>                           rospy.logwarn("Service teleport_absolute call failed")
>    
>       with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
>    
>           listener.join()
>    
En la parte inicial del codigo se importan las librerias y funciones que usaremos a lo largo del programa, en esta seccion se destaca la siguiente instruccion ``from turtlesim.srv import TeleportAbsolute, TeleportRelative`` los cuales incluyen los comandos de movimiento relativo y absoluto de la tortuga.
Usando la funcion ``keyboard.Listener`` nuestro porgrama queda atento en caso de relizarse una accion en el teclado el program ejecutara la funcion ``on_release`` y dependiendo de cual sea la tecla ingresada realizara su respectivo movimiento, para las teclas A,S,W, y D se envia una instruccion de movimiento dependiendo de cual haya sido presionada usando la funcion ``rospy.Publisher``, por otro lado, para R y ESPACIO se utiliza la funcion ``rospy.ServiceProxy`` con el respectivo moviento a realizar, ya sea absoluto o relativo, cabe resaltar que se usa la funcion ``rospy.ServiceProxy('/clear', Empty)`` para limpiar Turtle1 cuando se presione R.


<p align="center"><img width="700" src="https://github.com/sofiaponteb/Labs-Robotica-2022-2/blob/main/Lab2/mediaLab2/python.gif"></p>

## Conclusiones :page_facing_up:

- Es importante conocer diversas formas de realizar código para robótica, de esta forma se puede facilitar en gran medida la ejecución de diferentes aplicaciones dependiendo de la necesidad que se tenga.
- El framework ROS permite realizar diversas operaciones de una manera rápida y sencilla, por ello es importante reconocer su funcionamiento y herramientas disponibles.
- El trabajo en equipo permite adquirir un mayor aprendizaje en el desarrollo de los ejercicios, ya que se genera discusión acerca de lo que se está realizando y cuál es la mejor manera de hacerlo.

## Referencias :open_book:
- Laboratorio 2 - Robotica de desarrollo - Intro a ROS UNAL.


## Autores :black_nib:
Ana Sofía Aponte Barriga

José Alejandro Peñaranda Chía

Universidad Nacional de Colombia - Sede Bogotá

Ingeniería Mecatrónica
