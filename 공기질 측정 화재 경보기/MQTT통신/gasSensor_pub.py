import spidev
import paho.mqtt.client as mqtt
import time

spi=spidev.SpiDev()

spi.open(0,0)

spi.max_speed_hz=500000

def read_spi_adc(adcChannel):           #센서의 아날로그 값을 반환해주는 함
    adcValue=0
    buff =spi.xfer2([1,(8+adcChannel)<<4,0])
    adcValue = ((buff[1]&3)<<8)+buff[2]
    return adcValue


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_publish(client, userdata, mid):
    msg_id = mid
    

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

mqttc.connect("localhost")
mqttc.loop_start()

try:
    while True:
        MQ2adcChannel=0                 #유해가스 센서
        MQ2adcValue=read_spi_adc(MQ2adcChannel)
        
        print(" gas %d"%MQ2adcValue)
        (result, m_id) = mqttc.publish("sensor/gas", MQ2adcValue)
        
        
        MQ135adcChannel=1               #공기질 센서
        MQ135adcValue=read_spi_adc(MQ135adcChannel)
        
        print(" air_quality : %d" %MQ135adcValue + " ppm")
        (result, m_id) = mqttc.publish("sensor/air_quality", MQ135adcValue)
        time.sleep(1.0)
        

except KeyboardInterrupt:
    print("Finished!")
    mqttc.loop_stop()
    mqttc.disconnect()
    spi.close() 
