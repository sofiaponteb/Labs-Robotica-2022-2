# Lab 3 - Robotica industrial 2 - Entradas y Salidas

### Contenido

1. [Código en RAPID](#código-en-rapid-computer)
2. [Descripción de la Solución Planteada](#descripción-de-la-solución-planteada)
3. [Conclusiones](#autores-blacknib)
5. [Referencias](#referencias-openbook)

6. [Autores](#autores-blacknib)

>Nota: Los documentos referentes a este laboratorio se encuentran en la carpeta del repositorio denominada "Lab3"

## Código en RAPID :computer:

> MODULE Module1
> 
>    !!!!!!! Para ver el código completo diríjase a la carpeta Lab3AJ de este repositorio
>    
>    !!Definicion de contantes...
>    
>    VAR intnum Mantenimiento;
>    
>    PROC main()
>    
>        !Añada aquí su código
>        
>        IEnable;
>        
>        CONNECT Mantenimiento WITH OpMantenimiento;
>        
>        ISignalDI EntDI_2,1, Mantenimiento ;
>        
>        WHILE TRUE DO 
>        
>            SetDO SalDO_1,0;
>            
>            WaitDI EntDI_1,1;
>            
>            SetDO SalDO_1,1;
>            
>            GoGoHome ;
>            
>            GoMiddle ;
>            
>            A1 ;
>            
>            A2 ;
>            
>            J ;
>            
>            GoMiddle ;
>            
>            GoGoHome ;
>            
>            !IDelete Mantenimiento;
>            
>        ENDWHILE
>        
>    ENDPROC
>
>
>    PROC A1()
>    
>        !!Movimiento Trayectoria A1...
>        
>    ENDPROC
>
>
>    PROC A2()
>    
>        !!Movimiento Trayectoria A2...        
>        
>    ENDPROC
>
>
>    PROC J()
>    
>        !!Movimiento Trayectoria J...         
>        
>    ENDPROC
>
>
>    PROC GoGoHome()
>    
>        MoveAbsJ GoHome,v1000,z100,tool_lab1\WObj:=tabla_AJ;
>        
>    ENDPROC
>
>
>    PROC GoMiddle()
>    
>        MoveAbsJ Middle,v1000,z100,tool_lab1\WObj:=tabla_AJ;
>        
>    ENDPROC
>
>
>    PROC GoMantenimiento()
>    
>        GoMiddle;
>        
>        MoveAbsJ Path_mantenimiento,v200,z100,tool_lab1\WObj:=tabla_AJ;
>        
>    ENDPROC
>
>
>    TRAP OpMantenimiento
>    
>        VAR robtarget parada;
>        
>        SetDO SalDO_1,0;
>        
>        SetDO SalDO_2,1;
>        
>        StopMove;
>        
>        StorePath;
>        
>        parada:=crobt(\Tool:=tool_lab1\WObj:=tabla_AJ);
>        
>        GoMantenimiento;
>        
>        WaitDI EntDI_1,1;
>        
>        GoMiddle;
>        
>        MoveL parada,v200,z100,tool_lab1\WObj:=tabla_AJ;
>        
>        SetDO SalDO_2,0;
>        
>        SetDO SalDO_1,1;
>        
>        RestoPath;
>        
>       StartMove;
>       
>    ENDTRAP
>    
> ENDMODULE    

Para la manipulacion de las entradas digitales se uso el pulsador "EntDI_1" para el inicio de la rutina de escritura y el pulsador "EntDI_2" como la interrupcion para iniciar la rutina de mantenimiento, estó con el objetivo de hacer un proceso mas dinamico y que el mantenimiento se pueda realizar en cualquier instante de la rutina de escritura. 
A continuacion se realiza una breve descripcion de los principales comandos usados:
- ```VAR intnum Mantenimiento``` nos permite definir una rutina de interupcion con nombre "Mantenimiento".
- ```IEnable```  habilita las interrupciones
-  ```CONNECT Mantenimiento WITH OpMantenimiento```  conecta la rutina "Mantenimiento" con la operacion "OpMantenimiento"
-  ```ISignalDI EntDI_2,1, Mantenimiento ``` se define una interrupcion por flanco de subida proveniente de "EntDI_2" que realiza la rutina "Mantenimiento"
-   ```SetDO SalDO_1,0 ``` la impone a la salida digital "SalDO_1" el valor de "0"
-   ``` WaitDI EntDI_1,1``` realiza una pausa del codigo hasta que "EntDI_1" sea 1
-   ```VAR robtarget parada``` crea una variable de tipo robtarget con nombre "parada"
-   ```StopMove``` frena el movimiento del manipulador
-   ```StorePath``` almacena el path actual
-    ```parada:=crobt(\Tool:=tool_lab1\WObj:=tabla_AJ)``` almacena el robtarget actual en "parada"
-     ```StorePath``` restaura el path
-      ```StartMove``` reinicia el movimiento.
Los ultimos 5 comando son los que permiten al dispositivo pausar el movimiento y retormarlo en donde se presento la interrupcion.

![5](/Lab3/mediaLab3/5turtleTeleport.png)


<p align="center"><img width="700" src="https://github.com/sofiaponteb/Labs-Robotica-2022-2/blob/main/Lab2/mediaLab2/tortugabonita.gif"></p>

## Descripción de la Solución Planteada
Lo primero que se realizo fue definir las entradas y salidas en el codigo RAPPID, posterior 

## Conclusiones :page_facing_up:



## Referencias :open_book:
- Laboratorio 3 - Robotica Industrial 2 - Entradas y Salidas.


## Autores :black_nib:
Ana Sofía Aponte Barriga

José Alejandro Peñaranda Chía

Universidad Nacional de Colombia - Sede Bogotá

Ingeniería Mecatrónica
