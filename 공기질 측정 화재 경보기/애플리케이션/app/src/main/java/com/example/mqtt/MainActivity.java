package com.example.mqtt;

import androidx.appcompat.app.AppCompatActivity;


import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import org.eclipse.paho.android.service.MqttAndroidClient;
import org.eclipse.paho.client.mqttv3.IMqttActionListener;
import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.IMqttToken;
import org.eclipse.paho.client.mqttv3.MqttCallback;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;

public class MainActivity extends AppCompatActivity {
    // MQTT 통신을 위한 변수
    static String MQTTHOST = "tcp://192.168.43.80:1883";
    static String USERNAME = "ddd";
    static String PASSWORD = "dd";
    static String message = "0";

    // MQ2, MQ135 토픽을 저장하는 변수
    String topicMQ2 = "sensor/gas";
    String topicMQ135 = "sensor/air_quality";

    // MQ2, MQ135로부터 전달받을 값을 저장하는 변수
    private String mq2Data;
    private String mq135Data;

    // MQTT 통신을 위한 client 객체 생성
    MqttAndroidClient client;

    // 레이아웃에 표현하기 위해 사용되는 변수
    TextView subText;
    TextView subText2;
    private TextView mq135Text;
    private TextView mq2Text;
    private int mq135;
    private Button button;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // id와 변수 연결
        subText = (TextView) findViewById(R.id.mq2Data);
        subText2 = (TextView) findViewById(R.id.mq135Data);

        mq135Text = (TextView)findViewById(R.id.inf1);
        mq2Text = (TextView)findViewById(R.id.inf2);
        button = (Button)findViewById(R.id.button);

        // client 객체 초기화
        String clientId = MqttClient.generateClientId();
        client =
                new MqttAndroidClient(this.getApplicationContext(), MQTTHOST,
                        clientId);
        MqttConnectOptions options = new MqttConnectOptions();
        options.setUserName(USERNAME);
        options.setPassword(PASSWORD.toCharArray());

        // 버튼 이벤트 리스너 등록
        button.setOnClickListener(new View.OnClickListener() {
            // 버튼 클릭시 등록된 IP와 통신을 시작하며 MQ2, MQ135에 해닫하는 토픽을 구독한다.
            @Override
            public void onClick(View v) {
                try {
                    IMqttToken token = client.connect(options);
                    token.setActionCallback(new IMqttActionListener() {
                        @Override
                        public void onSuccess(IMqttToken asyncActionToken) {
                            Toast.makeText(MainActivity.this, "connected!", Toast.LENGTH_LONG).show();
                            setSubcription();
                        }

                        @Override
                        public void onFailure(IMqttToken asyncActionToken, Throwable exception) {
                            Toast.makeText(MainActivity.this, "connection failed", Toast.LENGTH_LONG).show();

                        }
                    });
                } catch (MqttException e) {
                    e.printStackTrace();
                }
                client.setCallback(new MqttCallback() {
                    @Override
                    public void connectionLost(Throwable cause) {

                    }
                    // 구독하는 토픽으로부터 메시지 도착 시 콜백되는 함수
                    @Override
                    public void messageArrived(String topic, MqttMessage message) throws Exception {
                        Log.i("mq2Topic", topic);
                        // 토픽에 따라 해당 TextView에 그 값을 출력하고 조건에 따라 출력하는 내용을 다르게 한다.
                        if(topic.equals(topicMQ2)) {
                            mq2Data = new String(message.getPayload());
                            Log.i("mq2Topic", "mq2 Topic success arrived");
                            subText.setText(mq2Data);
                            // 값이 1023 이상일 시 "화재 경보!" 메시지를 출력한다.
                            if(Integer.parseInt(mq2Data) >= 1023){
                                mq2Text.setVisibility(View.VISIBLE);
                            }
                            else{
                                mq2Text.setVisibility(View.INVISIBLE);
                            }
                        }
                        else if(topic.equals(topicMQ135)) {
                            mq135Data = new String(message.getPayload());
                            mq135 = Integer.parseInt(mq135Data);
                            Log.i("mq135Topic", "mq135 Topic success arrived");
                            subText2.setText(mq135Data);
                            // 값에 따라 미세먼지 상태를 나타낸다.
                            if(mq135 >= 1000){
                                mq135Text.setText("미세먼지 매우 나쁨");
                                mq135Text.setTextColor(0xFFFF0000);
                            }
                            else if(mq135 >= 800){
                                mq135Text.setText("미세먼지 나쁨");
                                mq135Text.setTextColor(0xFFFF9800);
                            }
                            else if(mq135 >= 600){
                                mq135Text.setText("미세먼지 보통");
                                mq135Text.setTextColor(0xFFFBE200);
                            }
                            else if(mq135 >= 450){
                                mq135Text.setText("미세먼지 좋음");
                                mq135Text.setTextColor(0xFF0005FF);
                            }
                            else {
                                mq135Text.setText("미세먼지 아주 좋음");
                                mq135Text.setTextColor(0xFF29A52E);
                            }
                        }

                    }

                    @Override
                    public void deliveryComplete(IMqttDeliveryToken token) {

                    }
                });
            }
        });

    }
    // 토픽을 구독하는 함수
    private void setSubcription() {
        try {
            client.subscribe(topicMQ2, 0);
            client.subscribe(topicMQ135, 0);

        } catch (MqttException e) {
            e.printStackTrace();
        }

    }

}