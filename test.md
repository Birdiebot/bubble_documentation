坐标系定义参考[REP103](https://www.ros.org/reps/rep-0103.html)，使用右手坐标系  

底盘坐标系$O_{chassis\ xyz}$，其中，前方为${x}$正方向，右方为${y}$正方向，上侧为${z}$正方向  

云台坐标系通过$yaw$轴与$pitch$轴连接在底盘上，初始坐标系$O_{gimbal\ xyz}$其中，前方为${x}$正方向，右方为${y}$正方向，上侧为${z}$正方向  

在$O_{chassis\ xyz}$中:  
$O_{gimbal\ xyz}$中空间目标点$P_0{[x_0, y_0, z_0]^\top}$和$\vec{v}_0 = [v_{x_0}, v_{y_0}, v_{z_0}]^\top$在变换矩阵$^{chassis}_{gimbal}T$作用下，变换为$P{(p_x, p_y, p_z)}$、$\vec{v} = [vx, vy, vz]^\top$，则空间向量$\overrightarrow{O_{gimbal}P}=[p_x, p_y, p_z]^\top$,一般地$||\vec{v}|| = ||\vec{v}_0|| = 30m/s$，$\alpha_{yaw}$和$\alpha_{pitch}$为云台偏转角度在底盘坐标系下的偏转角度，弹丸在空中飞行时间为$t$，底盘速度$\vec{v}_{chassis} = （v_{chassis}, 0 ,0）$    

其中：  
$^{chassis}_{gimbal}T = \left[\begin{array}{ccc}
    ^{chassis}_{gimbal}R & ^{chassis}_{gimbal}p \\
    0 & 1
\end{array}\right]$

根据几何关系，有：   
$g$ down  
$\overrightarrow{O_{gimbal}P} = \left[\begin{array}{ccc}
    p_x \\ p_y \\ p_z
\end{array}\right] = 
\left[\begin{array}{ccc}
    ||\vec{v}||t\cos \alpha_{pitch}  \cos \alpha_{yaw} \\
    ||\vec{v}||t\cos \alpha_{pitch}\sin \alpha_{yaw} + v_{chassis}t \\
    -||\vec{v}||t\sin \alpha_{pitch} - \frac{1}{2} gt^2 \\
\end{array}\right]
\Longrightarrow \\
\frac{1}{4}g^2 t^4+(v_{chassis}^2-gp_z-||\vec{v}||^2)t^2 - 2p_y v_{chassis}t + ||\overrightarrow{O_{gimbal}P}||^2 = 0
$

则:  
$\alpha_{pitch} = \arcsin \frac{-p_z-\frac{1}{2}gt^2}{||\vec{v}||t}$  
$\alpha_{yaw} = \arcsin \frac{p_y-v_{chassis}t}{||\vec{v}||t \cos \alpha_{pitch}}$
