# rasp-machine-driver
英特尔杯-树莓派电机驱动程序

## 串口协议
### description
- 树莓派作为接收端\TX2作为发送端
- 单向传输
- 格式为JSON ASCII编码 以ASCII 0作为结束符
### template
```json
{
"type":"string",
"data":0
}
```
| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |