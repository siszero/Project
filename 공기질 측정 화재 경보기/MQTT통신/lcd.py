import paho.mqtt.client as mqtt
import lcddriver

display = lcddriver.lcd()

def on_connect(client, userdata, flags, rc):
    print("connected with result code " + str(rc))
    client.subscribe("sensor/air_quality")               
    
def on_message(client, userdata, msg):
    control_lcd = int(msg.payload.decode())
    print(str(msg.payload.decode()))
    display.lcd_display_string("air_quality:" + str(control_lcd), 1)
    #공기질 센서 값을 lcd 첫번째 줄에 출력
    if(control_lcd >=1000):             #공기질 센서값에 따라 상태를  5단계로 나눔
        airQ_state = "Very Bad "
    elif(control_lcd >= 800):
        airQ_state = "Bad      "
    elif(control_lcd >= 600):
        airQ_state = "Normally "
    elif(control_lcd >= 450):
        airQ_state = "Good     "
    else:
        airQ_state = "Very Good"
    print(airQ_state);
    
    display.lcd_display_string(airQ_state, 2)
    #공기질의 상태를 lcd 두번째 줄에 출력 
    
client = mqtt.Client("lcdController")
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost")

try:
    client.loop_forever()
    
except KeyboardInterrupt:
    print("lcd Controller END")
    client.unsubscribe("sensor/air_quality")
    display.lcd_clear()
    client.disconnect()
