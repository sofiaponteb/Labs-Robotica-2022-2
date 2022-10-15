# Lab 3 - Robotica industrial 2 - Entradas y Salidas

### Contenido

1. [Código en RAPID](#código-en-rapid-computer)
2. [Descripción de la Solución Planteada](#descripción-de-la-solución-planteada)
3. [Conclusiones](#autores-blacknib)
5. [Referencias](#referencias-openbook)

6. [Autores](#autores-blacknib)

>Nota: Los documentos referentes a este laboratorio se encuentran en la carpeta del repositorio denominada "Lab3"

## Código en RAPID :computer:

>    MODULE Module1
> 
>     !!!!!!! Para ver el código completo diríjase a la carpeta Lab3AJ de este repositorio   
>     !!Definicion de constantes...  
>     VAR intnum Mantenimiento;  
>     PROC main()   
>        !Añada aquí su código      
>        IEnable;
>        CONNECT Mantenimiento WITH OpMantenimiento;
>        ISignalDI EntDI_2,1, Mantenimiento ;
>        WHILE TRUE DO    
>            SetDO SalDO_1,0;    
>            WaitDI EntDI_1,1;  
>            SetDO SalDO_1,1;  
>            GoGoHome ;  
>            GoMiddle ;  
>            A1 ;
>            A2 ;
>            J ; 
>            GoMiddle ;
>            GoGoHome ;
>        ENDWHILE
>     ENDPROC
>
>     PROC A1()
>        !!Movimiento Trayectoria A1...
>     ENDPROC
>
>     PROC A2()
>        !!Movimiento Trayectoria A2...         
>     ENDPROC
>
>     PROC J()
>        !!Movimiento Trayectoria J...           
>     ENDPROC
>
>     PROC GoGoHome()
>        MoveAbsJ GoHome,v1000,z100,tool_lab1\WObj:=tabla_AJ;  
>     ENDPROC
>
>     PROC GoMiddle()
>        MoveAbsJ Middle,v1000,z100,tool_lab1\WObj:=tabla_AJ;
>     ENDPROC
>
>     PROC GoMantenimiento()
>        GoMiddle; 
>        MoveAbsJ Path_mantenimiento,v200,z100,tool_lab1\WObj:=tabla_AJ;  
>     ENDPROC
>
>     TRAP OpMantenimiento
>        VAR robtarget parada;
>        SetDO SalDO_1,0;
>        SetDO SalDO_2,1;
>        StopMove;
>        StorePath;
>        parada:=crobt(\Tool:=tool_lab1\WObj:=tabla_AJ);
>        GoMantenimiento;
>        WaitDI EntDI_1,1;
>        GoMiddle;
>        MoveL parada,v200,z100,tool_lab1\WObj:=tabla_AJ;
>        SetDO SalDO_2,0;
>        SetDO SalDO_1,1;
>        RestoPath;
>       StartMove;
>     ENDTRAP
>    
>   ENDMODULE    

Para la manipulacion de las entradas digitales se uso el pulsador "EntDI_1" para el inicio de la rutina de escritura y el pulsador "EntDI_2" como la interrupcion para iniciar la rutina de mantenimiento, estó con el objetivo de hacer un proceso mas dinamico y que el mantenimiento se pueda realizar en cualquier instante de la rutina de escritura. 
A continuacion se realiza una breve descripcion de los principales comandos usados:
- ```VAR intnum Mantenimiento``` nos permite definir una rutina de interupcion con nombre "Mantenimiento".
- ```IEnable```  habilita las interrupciones
-  ```CONNECT Mantenimiento WITH OpMantenimiento```  conecta la rutina "Mantenimiento" con la operacion "OpMantenimiento"
-  ```ISignalDI EntDI_2,1, Mantenimiento ``` se define una interrupcion por flanco de subida proveniente de "EntDI_2" que realiza la rutina "Mantenimiento"
-   ```SetDO SalDO_1,0 ``` la impone a la salida digital "SalDO_1" el valor de "0"
-   ``` WaitDI EntDI_1,1``` realiza una pausa del codigo hasta que "EntDI_1" sea 1
-   ```VAR robtarget parada``` crea una variable de tipo robtarget con nombre "parada"
-   ```StopMove``` frena el movimiento del manipulador.
-   ```StorePath``` almacena el path actual.
-  ```parada:=crobt(\Tool:=tool_lab1\WObj:=tabla_AJ)``` almacena el robtarget actual en "parada".
-  ```StorePath``` restaura el path.
-  ```StartMove``` reinicia el movimiento.

Los ultimos 5 comando son los que permiten al programa pausar el movimiento y retormarlo en donde se presento la interrupcion.

En el siguiente gif se puede observar la simulacion del Programa en RobotStudio: 

<p align="center"><img width="700" src="https://github.com/sofiaponteb/Labs-Robotica-2022-2/blob/main/Lab3/mediaLab3/Video_simulacion_vfinal2.gif"></p>

En el siguiente enlace se puede observar la implementacion de la practica con los robots del laboratorio sin realizar la ubicacion del WorkObject:
https://youtu.be/raot1BQLAMo


## Descripción de la Solución Planteada
Partiendo de la programacion realizada en la practica 1, lo primero que se realiza es definir las entradas y salidas (E/S) en RobotStudio, posterior a esto se define la secuencia de mantenimiento, teniendo definidas la secuencia de operacion y la secuencia de mantenimiento, procedemos a definir el ciclo de operacion de nuestro programa, el cual incluye comandos dependientes de las Entradas y que modifican el valor de las Salidas, para esta labor nuestro codigo usa los siguientes comandos ```SetDO```,```ISignalDI``` y ``` WaitDI```, en donde cabe resaltar que nuestra secuencia principal sera la de operacion y la secuencia mantenimiento se ejecutara como una interrupcion si se activa la entrada "EntDI_2". Por ultimo se carga el programa en el controlador del laboratorio, se cambia el nombre de las E/S para que correspondan con las del controlador y se ejecuta el programa.

En los siguientes enlaces se puede observar la implementacion de la practica con los robots del laboratorio realizando la ubicacion del WorkObject:
- https://youtu.be/nLM2jwPQpeQ
- https://youtu.be/LfaXL3PrBfE


## Conclusiones :page_facing_up:

- Las Entradas digitales permiten el adquisicion y manipulacion de informacion de forma sencilla, existen diferentes comandos que se pueden usan dependiendo de las necesidad del programador, siendo estas ideales para aquellas funciones en la cuales solo se desee saber 2 estados en una variable de interes.
- Las Salidas digitales permiten la manipulacion de elementos cuya funcionalidad sea digital, por ejemplo luces o electroactuadores, en los cuales solo se tengan 2 estados de interes, en programas mas robuztos estas salidas pueden permitir el control en procesos industriales de a gran escala.
- Las interrupcione son ideales en procesos donde se tenga prioridad una accion sobre la otras, ya que nuestro caso es didactico no son necesarias, pero al realizar el programa con esta funcionalidad se puede tener un apredizaje mas profundo sobre el uso de E/S digitales.



## Referencias :open_book:
- Laboratorio 3 - Robotica Industrial 2 - Entradas y Salidas.
- Manual de referencia técnica. Instrucciones, funciones y tipos de datos de RAPID. Software de controlador para IRC5. RobotWare 5.13.
- Diseño, programación y simulación de estaciones robotizadas industriales con Robotstudio. Agustín Ramos Hurtado.



## Autores :black_nib:
Ana Sofía Aponte Barriga

José Alejandro Peñaranda Chía

Universidad Nacional de Colombia - Sede Bogotá

Ingeniería Mecatrónica
