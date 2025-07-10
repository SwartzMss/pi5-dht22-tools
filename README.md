# pi5-dht22-tools

使用树莓派 Pi5 读取 DHT22 温湿度传感器数据的示例脚本。

## 环境准备
1. 安装依赖（需要在系统中安装 `pip`）：
   ```bash
   pip install Adafruit_DHT
   ```
2. 将 DHT22 数据引脚连接到 GPIO4（可在 `main.py` 中指定），并连接电源与地线。

## 运行脚本
运行脚本（持续读取）：
```bash
python3 main.py
```

可通过 `--interval` 指定读取间隔（秒），`--pin` 指定传感器连接的 GPIO 引脚。
