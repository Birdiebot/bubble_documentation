
通过预构建的Docker容器使用
============================================

概述
----------------
Bubble提供了一个预构建Docker容器，快速完成环境的搭建。
您可以在容器中运行Bubble。Bubble的docker镜像托管在 `docker hub <https://hub.docker.com/repository/docker/birdiebot/bubble-aarch64v8>`__ 中。

Bubble的Docker镜像基于 `dustynv的galactic-ros-base-l4t-r34.1.1 <https://github.com/dusty-nv/jetson-containers>`__ 构建。镜像提供了：

* Ros Galactic环境
* l4t rootfs 的包子集（Multimedia、Gstreamer、Camera、Core、3D Core、Vulkan、Weston）
* CUDA、CuDNN和TensorRT
* hikrobot工业相机驱动
* Bubble运行时所需要的环境依赖

运行Bubble的容器
--------------------------

先决条件
^^^^^^^^^^^^^^^^^^^^^^^^^^
Bubble容器在Jetson在使用，请确保Jetson上的NVIDIA Container Runtime已经安装。

运行容器
^^^^^^^^^^^^^^^^^^^^^^^^^^

* 允许外部应用程序连接到主机的显示器：
    
.. code-block:: console

    xhost +

* 使用 docker 命令运行 docker 容器

.. code-block:: console

    docker run -it --rm --net=host --runtime nvidia \
        -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix \
        --device=/dev/bus/usb/ --device=/dev/ttyTHS0 \
        -v /home/nvidia/Desktop/bubble:/home/bubble \
        birdiebot/bubble-aarch64v8:v1.0-l4t-r32.7.1 /bin/bash

- 参数说明：

    - -it表示以交互模式运行
    - --rm完成后将删除容器
    - --runtime nvidia将在运行Bubble容器时使用NVIDIA容器运行时
    - -v是挂载目录，用于挂载主机的 X11 显示在容器文件系统中以渲染输出视频
    - --device是共享主机中的usb设备（主要是工业相机）和串口设备
    - 1.0是bubble版本对应的镜像标签，l4t-r32.7.1是对应的Linux for Tegra版本

运行Bubble
^^^^^^^^^^^^^^^^^^^^^^^^^^
根据之前设置的源码路径，运行Bubble。

.. code-block:: console

    ros2 launch bubble_bringup sentry_launch.py
