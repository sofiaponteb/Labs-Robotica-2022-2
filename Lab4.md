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


<p align="center"><img width="400" src="https://github.com/sofiaponteb/Labs-Robotica-2022-2/blob/main/Lab4/pincher1.gif"></p>

<p align="center"><img width="400" src="https://github.com/sofiaponteb/Labs-Robotica-2022-2/blob/main/Lab4/pincher2.gif"></p>

## Script en MATLAB :computer:
Se desarrolla un corto Script en MATLAB para crear una imagen virtual de las posiciones del robot y así poder contrastarlas con las obtenidas en el robot real.

>      l = [0, 10.2, 10.2, 7.8];
>      q = [-90, 45, -55, 45]*pi/180;
>      offset = [0, pi/2, 0, 0];
>      % Orden parametros funcion link [THETA D A ALPHA SIGMA(0R,1P) OFFSET]
>      DHparameters = [q(1) 5.4 l(1) pi/2 0 offset(1);
>                      q(2) 0   l(2) 0    0 offset(2);
>                      q(3) 0   l(3) 0    0 offset(3);
>                      q(3) 0   l(4) pi/2 0 offset(4)                ];
>      L21(1) = Link(DHparameters(1,:));
>      L21(2) = Link(DHparameters(2,:));
>      L21(3) = Link(DHparameters(3,:));
>      L21(4) = Link(DHparameters(4,:));
>      Robot_punto21 = SerialLink(L21,'name','Punto2.1');
>      ws2_2 = [-10 10 -10 10 -4.5 40];
>      Robot_punto21.plot(q,'workspace',ws2_2);
>      xlim([-12.0 39.5])
>      ylim([-16.8 34.7])
>      zlim([-41.0 73.7])

Se cambia el vector ```q``` para hallar la representación de cada una de las 5 posiciones requeridas:

Se realiza la verificación de poses. La ubicación de la cámara de MATLAB se mantuvo constante, mientras que la cámara real se ubicó en las posiciones donde se apreciaba mejor la ubicación de cada articulación.

- 0, 0, 0, 0, 0.
![1](/Lab4/img/1.png)

- -20, 20, -20, 20, 0.
![2](/Lab4/img/2.png)

- 30,-30, 30, -30, 0.
![3](/Lab4/img/3.png)

- -90, 15, -55, 17, 0.
![4](/Lab4/img/4.png)

- -90, 45, -55, 45, 10.
![5](/Lab4/img/5.png)


## Conclusiones :page_facing_up:

- El uso de frameworks como ROS permite facilitar en gran medida el uso de robots pequeños como el Pincher utilizado en este laboratorio.
- En casos en los cuales no se tenga un buen agarre superficial ni el torque suficiente en las articulaciones, una menor velocidad de trabajo mejora la estabilidad del robot.
- El trabajo en equipo permite adquirir un mayor aprendizaje en el desarrollo de los ejercicios, ya que se genera discusión acerca de lo que se está realizando y cuál es la mejor manera de hacerlo.

## Referencias :open_book:
- Laboratorio 4 - Cinemática Directa - Phantom X - ROS UNAL.
- https://github.com/fegonzalez7/rob_unal_clase4
- Apuntes de clase, Robótica 2022-2


## Autores :black_nib:
Ana Sofía Aponte Barriga

José Alejandro Peñaranda Chía

Universidad Nacional de Colombia - Sede Bogotá

Ingeniería Mecatrónica
