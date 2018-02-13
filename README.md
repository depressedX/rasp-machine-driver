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
|data|否|任意|payload|