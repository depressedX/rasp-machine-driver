# rasp-machine-driver
英特尔杯-树莓派电机驱动程序

## 串口协议
### description
- 树莓派作为接收端\TX2作为发送端
- 单向传输
- 格式为JSON ASCII编码 以ASCII 0作为结束符
### template
|参数|是否必选|类型|说明|
|---|---|---|---|
|type|是|string|发送信号类型|
|payload|否|任意|payload|

## 所有请求格式参考
- 启动发球机
    ```json
    {
    "type":"start"
    }
    ```
- 终止发球机
    ```json
    {
    "type":"shutdown"
    }
    ```
--------------------------
- 装载模式
    ```json
    {
    "type":"load",
    "payload":"load"
    }
    ```
- 卸载模式
    ```json
    {
    "type":"load",
    "payload":"unload"
    }
    ```
- 暂停装载/卸载
    ```json
    {
    "type":"load",
    "payload":"pause"
    }
    ```
-------------------------------------
- 改变击球位置  
    **payload**

    |type|value|description|
    |----|-----|-----------|
    |number|0-9|9个落点 调整角度和力度改变落点|

    ```json
    {
    "type":"move",
    "payload":0
    }
    ```

## TX2控制乒乓球机
package : *serialTransmitter.py*
### 开始
**一段简短的example**
```python
# coding:utf-8
import serialTransmitter as serial

# 初始化  必须调用
serial.init()

try:
    # 启动电机
    serial.start()
    
    # 在这里通过内置函数控制乒乓球机的行为
    serial.loadBalls()
    # serial.***()
    # ... ...
    
    # 关闭电机
    serial.shutdown()
    
finally:
    # 程序结束必须调用
    serial.destroy()
```
### 可操作的电机行为
- serial.start()  
启动电机
- serial.shutdown()  
关闭电机
- serial.loadBalls()  
开始装载球
- serial.unloadBalls()  
开始卸载球
- serial.stopLoadMotor()  
关闭装/卸载电机
- serial.move(pos)  
改变转速和角度实现定点发球

    |parameter|type|description|
    |:------:|:---:|:-------:|
    |pos|int|落点位置 0-9|
