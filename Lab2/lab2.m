%% INICIAL
rosinit; %Conexion con nodo maestro
%%
velPub = rospublisher('/turtle1/cmd_vel','geometry_msgs/Twist'); %Creacion publicador
velMsg = rosmessage(velPub); %Creacion de mensaje
%%
velMsg.Linear.X = 1; %Valor del mensaje
send(velPub,velMsg); %Envio
pause(1)
%% SUBSCRIBER
TurtlePose = rossubscriber("/turtle1/pose", "turtlesim/Pose")
scanMsg = TurtlePose.LatestMessage
%% POSE
TurtleTeleport = rossvcclient("/turtle1/teleport_absolute")
waitForServer(TurtleTeleport);

TurtleMsg = rosmessage(TurtleTeleport)
TurtleMsg.X = 5;
TurtleMsg.Y = 3;
TurtleMsg.Theta = 2*pi/3 ;

call(TurtleTeleport,TurtleMsg)

%% FINALIZAR NODO MAESTRO
rosshutdown