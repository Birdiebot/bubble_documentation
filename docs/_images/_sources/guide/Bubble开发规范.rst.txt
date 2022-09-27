Bubble开发规范
======================================
:Authors: Ligcox
:Maintainers:
    Ligcox,
    HarryWen
:Contact: 
    ligcox@birdiebot.top,
    858601365@qq.com
:Last edit date: 2022/08/14
:Copyright: This document has been placed in the public domain.

开发者参与Bubble开发时，遵循的规范在该文档中阐述。

.. contents:: 目录
   :depth: 2
   :local:

1 代码风格规范
-----------------------

1.1 代码规范
^^^^^^^^^^^^^^^^^^^
Bubble代码风格原则上使用 `ROS2的代码风格和语言版本 <https://docs.ros.org/en/foxy/The-ROS2-Project/Contributing/Code-Style-Language-Versions.html>`__

* 对于实现逻辑的函数、回调函数使用蛇形命名法（snake_case）命名。例如： ``send_data()`` 、 ``data_callback()``
* 对于实现具体功能的函数，使用小驼峰命名法（dromedary case）命名。例如： ``algImplement``
* 对于类名、结构体名，采用大驼峰命名法（Pascal case）命名。例如：  ``class MyClass`` 、 ``struct DataType``

1.2 文件注释模板
^^^^^^^^^^^^^^^^^^^
Bubble项目中使用的 `koroFileHeader <https://marketplace.visualstudio.com/items?itemName=OBKoro1.korofileheader>`__ 自动生成代码文件模板。
配置字段具体功能介绍可参考 `配置文档 <https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE>`__

代码模板配置为：

.. code-block:: js

    {
        "fileheader.customMade": {
        "custom_string_obkoro1": "Copyright (c) 2022 Birdiebot R&D Department\nShanghai University Of Engineering Science. All Rights Reserved",
        "custom_string_obkoro2": "License: GNU General Public License v3.0.\nSee LICENSE file in root directory.",
        "custom_string_obkoro3": "",
        "Author": "your name your email",
        "Date": "Do not edit",
        "FilePath": "Do not edit",
        "LastEditors": "your name your email",
        "LastEditTime": "Do not edit",
        },
        "fileheader.cursorMode": {
            "Description": "\n\t",

            "Parameters": "",
            "------------": "",
            "param": "",
            "":"",

            "Returns": "",
            "-----------": "",

        },
        "fileheader.configObj": {
            "autoAdd": true,
            "wideSame": false,
            "writeLog": false,
            "useWorker": false,
            "moveCursor": true,
            "headDesign": false,
            "autoAlready": true,
            "createHeader": false,
            "designAddHead": false,
            "CheckFileChange": false,
            "showErrorMessage": true,
            "openFunctionParamsCheck": true,

            "wideNum": 13,
            "functionWideNum": 0,
            "autoAddLine": 10000,
            "throttleTime": 60000,

            "prohibitAutoAdd": [
                "json",
                "md",
                "yaml"
            ],
            "prohibitItemAutoAdd": [
                "项目的全称禁止项目自动添加头部注释, 使用快捷键自行添加"
            ],
            "folderBlacklist": [
                "launch"
            ],
            "headInsertLine": {
                "php": 2,
                "py": 0,
            },

            "switch": {
                "newlineAddAnnotation": true
            },
            "atSymbol": [
                "@",
                "@"
            ],

            "colon": [
                ": ",
                ""
            ],

            "filePathColon": "/",
            "functionTypeSymbol": "*",
            "typeParamOrder": "param",
            "headDesignName": "random",
            "functionParamAddStr": ": ",
            "NoMatchParams": "no show param",
            "dateFormat": "YYYY-MM-DD HH:mm:ss",

            "colonObj": {},
            "atSymbolObj": {},
            "afterAnnotation": {},
            "customHasHeadEnd": {},
            "beforeAnnotation": {},
            "functionBlankSpaceAll": {"python":4},
            "cursorModeInternalAll": {"python":true,"c11":true},
            "supportAutoLanguage": [],
            "functionParamsShape": ["",": "],
            "language": {
                "h/hpp/cpp": {
                    "head": "/*** ",
                    "middle": " * @",
                    "end": " */"
                },
                "py": {
                    "head": "\"\"\"",
                    "middle": "",
                    "end": "\"\"\"",

                },
            }
        },
        "annotationStr": {
            "head": "/*",
            "middle": " * @",
            "end": " */",
            "use": false
        },
    }

文件头模板为：

.. tabs::
    .. group-tab:: Python

        .. code-block:: python

            '''
            Author: your name
            Date: YYYY-MM-DD HH:MM:SS
            FilePath: your code path
            LastEditors: your name
            LastEditTime: YYYY-MM-DD HH:MM:SS
            License: GNU General Public License v3.0. See LICENSE file in root directory.
            Copyright (c) 2022 Birdiebot R&D Department
            Shanghai University Of Engineering Science. All Rights Reserved
            '''
    .. group-tab:: C++

        .. code-block:: C++

            /*
            * @Author: your name
            * @Date: YYYY-MM-DD HH:MM:SS
            * @FilePath: your code path
            * @LastEditors: your name
            * @LastEditTime: YYYY-MM-DD HH:MM:SS
            * License: GNU General Public License v3.0. See LICENSE file in root directory.
            * Copyright (c) 2022 Birdiebot R&D Department
            * Shanghai University Of Engineering Science. All Rights Reserved
            */

函数模板为：

.. tabs::
    .. group-tab:: Python

        .. code-block:: python

            """
            Description

            Parameters
            ------------

            Returns
            -----------
            """

    .. group-tab:: C++

        .. code-block:: C++

            /*
            TODO
            */

2 坐标系定义
------------------------
Bubble中的坐标系定义原则上使用 `REP105 移动平台的坐标系 <https://www.ros.org/reps/rep-0105.html>`__ 定义的规范，
坐标系中出现的单位，使用 `REP103 标准测量单位和坐标约定 <https://www.ros.org/reps/rep-0103.html>`__ 定义的标准单位。

特殊地，对于除RMUA及全自动步兵机器人外的绝大部分机器人，实际对移动关系不敏感，做以下额外地约定：

* 不设置 ``earth`` 坐标系
* 对于考虑相对位置的机器人 ``map frame`` 原点设置在机器人初始位置
* 对于不考虑相对位置的机器人不设置 ``map`` 、 ``odom`` 坐标系
* ``base_link`` 坐标系原点与底盘坐标系 ``chassis`` 重合
* 认为相机关节坐标系 ``camara frame`` 、相机坐标系 ``camara_optical frame`` 、云台坐标系 ``gimbal frame`` 为同一个坐标系 ``gimbal frame`` ，原点位于摩擦轮两点连线中点（即弹丸发射的初始位置）处
* 使用rpy形式的欧拉角（euler angle）进行旋转表述，而不是四元数（quaternion）

3 文件结构
------------------------

3.1 功能包结构
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Bubble中的功能包以 ``bubble_`` 前缀命名，结构原则上使用 `ROS2功能包layout <https://docs.ros.org/en/galactic/The-ROS2-Project/Contributing/Developer-Guide.html#package-layout>`__ 定义的规范。

.. tabs::
    .. group-tab:: Python

        .. code-block:: console
        
            bubble_python_pkg
                ├─bubble_python_pkg # 源码目录
                ├─launch            # launch文件目录
                ├─script            # 脚本文件路径
                ├─setup.py
                ├─setup.cfg
                ├─package.xml
                ├─LICENSE
                └─README.md

    .. group-tab:: C/C++

        .. code-block:: console

            bubble_c_pkg
                ├─config     # 配置文件目录
                ├─include    # 头文件目录
                ├─launch     # launch文件目录
                ├─script     # 脚本文件路径
                ├─src        # 源码目录
                ├─CMakeLists.txt
                ├─package.xml
                ├─LICENSE
                └─README.md

3.2 代码仓库
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
不同的功能包应当放置在相应的代码仓库下，当一个代码仓库仅有一个功能包时，它可以选择位于仓库的根目录中。

4 文档及注释
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
考虑到代码的可读性和维护

Bubble的文档使用sphinx进行书写，各功能模块应保留必要的注释，配置模板头后，直接使用koroFileHeader生成，并导出到文档中。

Bubble的文档及注释做以下约定：

.. csv-table::
    :header: 内容，推荐类型，语言，备注
    :align: center
    :widths: auto

    文档, ReStructuredText/rst, 中文, 为便于文档维护，文档主要使用中文进行维护
    API文档, ReStructuredText/rst, 英语, API文档使用Sphinx生成，内容与源码保持一致
    主项目自述文件, MarkDown/md, 英语、中文, 提供中文和英语的自述文件，在必要部分使用html语法调整格式
    模块自述文件, MarkDown/md, 英语, 各模块自述文件仅使用英文书写，在必要部分使用html语法调整格式
    代码注释, Python/C/C++, 英语, 代码中使用英文解释必要的函数、模块和功能逻辑