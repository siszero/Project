# -*- coding: utf8 -*-
# vi:set sw=4 ts=4 expandtab:
import paho.mqtt.client as mqtt
import RPi.GPIO as gpio
import sys
import time
import unittest
sys.path.insert(0, "../")

from sdk.api.message import Message
from sdk.api.group_message import GroupMessage
from sdk.api.sender_id import SenderID
from sdk.api.image import Image
from sdk.coolsms import Coolsms 
from sdk.exceptions import CoolsmsException

import sys,json

def makeSuite(testcase,tests):
    return unittest.TestSuite(map(testcase,tests)) #testcase를 이용해서 testsuite생성


class CoolsmsUnitTest(unittest.TestCase):

    api_key = "NCSDFXNVHJIIRFX4"               #자신의 api_key, api_secret 입력
    api_secret = "9UFVMLSVWMCNWVJ10IQSJTIBUNGWMGHC"

    def setUp(self):
        pass

    def test_message(self):
        cool = Message(self.api_key, self.api_secret)

        ## send 
        params = {
            'type':'sms',
            'to':'01056686785',         #실제 사용시 119로 바꿈
            'from':'01055329063',        #    사용자의 번호
            'text':'한국기술교육대학교 2공학관 화재 발생'     #주소가 담길 부분
        }
        try:
            cool.send(params)
        except CoolsmsException as e:
            # 402는 잔액부족이기 때문에 테스트 실패사유가 안됨
            if e.code == 402:
                pass
            
        ## status : response 가 None값이 아니라면 성공
        response = cool.status()
        self.assertIsNotNone(response['registdate'])

        ## sent
        try:
            cool.sent()
        except CoolsmsException as e:
            # 404는 메시지 내역이 없는 것이기 때문에 테스트 실패사유가 안됨
            if e.code == 404:
                pass

        ## balane
        response = cool.balance()
        self.assertIsNotNone(response['deferred_payment'])

        ## cancel
        params = {
            'message_id':'TESTMESSAGEID',
        }
        
        

    
buzzer = 26

gpio.setmode(gpio.BCM)
gpio.setup(buzzer, gpio.OUT)


def on_connect(client, userdata, flags, rc):    
    print("connected with result code " + str(rc))
    client.subscribe("sensor/gas")   
        
def on_message(client, userdata, msg):
    print("Topic: " + msg.topic + " Message: " + msg.payload.decode())
    gasValue = int(msg.payload.decode())
    if gasValue >= 1000:            #가스 센서 값이 1000이상일 때
                                    #부저를 울리고 메세지 전송 실행
        gpio.output(buzzer,True)                                   
        if __name__ == "__main__":
            suite = makeSuite(CoolsmsUnitTest,['test_message'])
            unittest.TextTestRunner(verbosity=2).run(suite)
            sys.exit()            
          
    else :
        gpio.output(buzzer,False)
    
        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect("localhost")

try:
    client.loop_forever()
except KeyboardInterrupt:
    gpio.cleanup()
    print("Finished!")
    client.unsubscribe(["sensor/gas"])
    client.disconnect()
