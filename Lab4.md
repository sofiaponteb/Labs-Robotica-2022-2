# Lab 4 - Cinemática Directa - Phantom X - ROS

### Contenido

1. [Script en Python](#script-en-python-snake)
1. [Script en MATLAB](#script-en-matlab-computer)
3. [Conclusiones](#autores-blacknib)
5. [Referencias](#referencias-openbook)

6. [Autores](#autores-blacknib)

>Nota: Los documentos referentes a este laboratorio se encuentran en la carpeta del respositorio denominada "Lab4"



## Script en Python :snake:

A continuación se muestra el script realizado en Python para ubicar el robot Pincher en las 5 posiciones especificadas:
- 0, 0, 0, 0, 0.
- -20, 20, -20, 20, 0.
- 30,-30, 30, -30, 0.
- -90, 15, -55, 17, 0.
- -90, 45, -55, 45, 10.

Este script se encuentra en la ruta ```catkin_ws\src\dynamixel_one_motor\scripts\jointPub.py```:

El código desarrollado para operar una tortuga del paquete turtlesim con el teclado es el siguiente:

>      import rospy
>      from std_msgs.msg import String
>      from sensor_msgs.msg import JointState
>      from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
>      
>      def joint_publisher():
>          pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
>          rospy.init_node('joint_publisher', anonymous=False)
>          
>          while not rospy.is_shutdown():
>              state = JointTrajectory()
>              state.header.stamp = rospy.Time.now()
>              state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
>              point = JointTrajectoryPoint()
>              point.positions = [0, 0, 0, 0, 0]    
>              point.time_from_start = rospy.Duration(1)
>              state.points.append(point)
>              pub.publish(state)
>              print('published command')
>              rospy.sleep(5)
>              state = JointTrajectory()
>              state.header.stamp = rospy.Time.now()
>              state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
>              point = JointTrajectoryPoint()
>              point.positions = [-0.34, 0.34, -0.34, 0.34, 0]    
>              point.time_from_start = rospy.Duration(1)
>              state.points.append(point)
>              pub.publish(state)
>              print('published command')
>              rospy.sleep(5)
>              state = JointTrajectory()
>              state.header.stamp = rospy.Time.now()
>              state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
>              point = JointTrajectoryPoint()
>              point.positions = [0.52, -0.52, 0.52, -0.52, 0]    
>              point.time_from_start = rospy.Duration(1)
>              state.points.append(point)
>              pub.publish(state)
>              print('published command')
>              rospy.sleep(5)
>              state = JointTrajectory()
>              state.header.stamp = rospy.Time.now()
>              state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
>              point = JointTrajectoryPoint()
>              point.positions = [-1.57, 0.26, -0.95, 0.29, 0]    
>              point.time_from_start = rospy.Duration(1)
>              state.points.append(point)
>              pub.publish(state)
>              print('published command')
>              rospy.sleep(5)
>              state = JointTrajectory()
>              state.header.stamp = rospy.Time.now()
>              state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
>              point = JointTrajectoryPoint()
>              point.positions = [-1.57, 0.78, -0.95, 0.78, 0.17]    
>              point.time_from_start = rospy.Duration(1)
>              state.points.append(point)
>              pub.publish(state)
>              print('published command')
>              rospy.sleep(5)
>      
>      
>      if __name__ == '__main__':
>          try:
>              joint_publisher()
>          except rospy.ROSInterruptException:
>              pass

Este script de python inicia importando las librerías necesarias para ser ejecutado en el robot. Posteriormente, se definen las variables y se inicia el nodo de ROS. Finalmente, se repite el siguiente fragmento de código para alcanzar cada posición requerida:

>        state = JointTrajectory()
>        state.header.stamp = rospy.Time.now()
>        state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
>        point = JointTrajectoryPoint()
>        point.positions = [0, 0, 0, 0, 0]    
>        point.time_from_start = rospy.Duration(1)
>        state.points.append(point)
>        pub.publish(state)
>        print('published command')
>        rospy.sleep(5)

Este fragmento de código asigna los nombres a los eslabones del robot, para posteriormente asignarle una posición a cada uno con la variable ```point.positions```. Finalmente se configuran parámetros como el tiempo de duración del movimiento y el tiempo de inactividad luego de alcanzar la posición deseada.

Para ejecutar este código se utilizaron los siguientes comandos en una terminal de Linux, con el robot Pincher conectado a un puerto USB del computador:

En la ruta ```/catkin_ws/src```

```
sudo chmod 777 /dev/ttyUSB0
```

En la ruta ```/catkin_ws```
```
catkin build dynamixel_one_motor
```
![1](/Lab4/img/catkin-build.png)


```
source devel/setup.bash
```

```
roslaunch dynamixel_one_motor one_controller.launch
```
![1](/Lab4/img/roslaunch.png)

Luego de esto, se ejecuta el script de python e inicia el movimiento del robot. Cada que se ejecuta un movimiento en la terminal se observa el estado de este:

![1](/Lab4/img/succeeded.png)


<p align="center"><img width="700" src="https://github.com/sofiaponteb/Labs-Robotica-2022-2/blob/main/Lab2/mediaLab2/tortugabonita.gif"></p>

## Script en MATLAB :computer:
Lo primero que se nos pide es abrir 2 terminales en Ubuntu para esto se da click izquierdo en el simbolo de terminal de la barra de tareas 2 veces, posterior a esto se escribe en la primera terminal el comando de ```roscore``` para iniciar el nodo maestro.  
![1](/Lab2/mediaLab2/1roscore.png)
Una vez iniciado el nodo maestro se escribe en la segunda terminal el comando ```rosrun turtlesim turtlesim_node``` el cual se introduce para correr turtlesim
![2](/Lab2/mediaLab2/2rosrun.png)
Una vez abierta una instacia de matlab para linux se introduce el codigo propuesto por la guia con el cual se busca realizar un conexion con el nodo maestro, definir un publicador y posteriormente manipular este publicador para poder enviar un comando a TurtleSim. Como se muestra acontinuacion:

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


Para recibir un mensaje de turtlesim lo primero que se realiza es la suscripcion al nodo de TurtleSim para poder recibir datos, esto se hace mediante la funcion ```rossubscriber``` cuyos argumentos son los datos que se desean recibir, que en este caso son los provenientes de turtle1 acerca de la posicion ```/turtle1/pose```, y el segundo argumento es el tipo de mensaje que se va a recibir, de forma general tendra la estructura de la posicion proveniente de TurtleSim ```/TurtleSim/pose```. 
![3](/Lab2/mediaLab2/3turtlePos.png)

A continuación se utiliza la función ```TurtleTeleport``` para asignar posiciones arbitrarias a la tortuga por medio de los atributos ```TurtleMsg.X``` y ```TurtleMsg.Y```. Posteriormente se realiza el llamado a la función Teleport enviándole como argumento los atributos asignados en TurtleMsg.

![4](/Lab2/mediaLab2/4turtleTeleport.png)

Al anterior procedimiento se le agrega el atributo de rotación, para evidenciar cómo sería un cambio de posición no solo con respecto a los ejes sino también de la orientación angular de la tortuga:

![5](/Lab2/mediaLab2/5turtleTeleport.png)

A continuación se muestra un animación del movimiento de la tortuga al usar la función ``TurtleTeleport``:

<p align="center"><img width="700" src="https://github.com/sofiaponteb/Labs-Robotica-2022-2/blob/main/Lab2/mediaLab2/tortugabonita.gif"></p>

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
