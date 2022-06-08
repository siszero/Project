#include "mbed.h"
DigitalOut L_motor_A(PA_0);
DigitalOut L_motor_B(PA_1);
DigitalOut L_motor_C(PA_4);
DigitalOut L_motor_D(PB_0);

DigitalOut R_motor_A(PA_5);
DigitalOut R_motor_B(PA_6);
DigitalOut R_motor_C(PA_7);
DigitalOut R_motor_D(PC_5);

AnalogIn sensor1(PB_1);
AnalogIn sensor2(PC_4);
AnalogIn sensor3(PC_2);

Ticker flipper1;
Ticker flipper2;

int state = 0;

void run_Lmotor(){
    if(state == 0){
        L_motor_A = 1;
        L_motor_B = 0;
        L_motor_C = 0;
        L_motor_D = 1;
        state += 1;        
    }
    
    else if(state == 1){
        L_motor_A = 0;
        L_motor_B = 0;
        L_motor_C = 0;
        L_motor_D = 1;
        state += 1;
    }
    
    else if(state == 2){        
        L_motor_A = 0;
        L_motor_B = 0;
        L_motor_C = 1;
        L_motor_D = 1;
        state += 1;
    }
    
    else if(state == 3){       
        L_motor_A = 0;
        L_motor_B = 0;
        L_motor_C = 1;
        L_motor_D = 0;
        state += 1;
    }
    
    else if(state == 4){
        L_motor_A = 0;
        L_motor_B = 1;
        L_motor_C = 1;
        L_motor_D = 0;
        state += 1;
    }
    
    else if(state ==5){        
        L_motor_A = 0;
        L_motor_B = 1;
        L_motor_C = 0;
        L_motor_D = 0;
        state += 1;
    }

    else if(state == 6){
        L_motor_A = 1;
        L_motor_B = 1;
        L_motor_C = 0;
        L_motor_D = 0;
        state += 1;
    }
    
    else if(state == 7){
        L_motor_A = 1;
        L_motor_B = 0;
        L_motor_C = 0;
        L_motor_D = 0;
        state = 0;
    }              
}

void run_Rmotor(){
    if(state == 0){
        R_motor_A = 1;
        R_motor_B = 0;
        R_motor_C = 0;
        R_motor_D = 0;     
        state += 1;        
    }
    
    else if(state == 1){
        R_motor_A = 1;
        R_motor_B = 1;
        R_motor_C = 0;
        R_motor_D = 0;
        state += 1;
    }
    
    else if(state == 2){        
        R_motor_A = 0;
        R_motor_B = 1;
        R_motor_C = 0;
        R_motor_D = 0;
        state += 1;
    }
    
    else if(state == 3){       
        R_motor_A = 0;
        R_motor_B = 1;
        R_motor_C = 1;
        R_motor_D = 0;
        state += 1;
    }
    
    else if(state == 4){
        R_motor_A = 0;
        R_motor_B = 0;
        R_motor_C = 1;
        R_motor_D = 0;
        state += 1;
    }
    
    else if(state ==5){        
        R_motor_A = 0;
        R_motor_B = 0;
        R_motor_C = 1;
        R_motor_D = 1;        
        state += 1;
    }

    else if(state == 6){
        R_motor_A = 0;
        R_motor_B = 0;
        R_motor_C = 0;
        R_motor_D = 1;
        state += 1;
    }
    
    else if(state == 7){
        R_motor_A = 1;
        R_motor_B = 0;
        R_motor_C = 0;
        R_motor_D = 1;
        state = 0;
    }              
}

void turn_right(){
    flipper1.attach(&run_Lmotor, 0.003);
    flipper2.attach(&run_Rmotor, 10);
}

void turn_left(){
    flipper1.attach(&run_Lmotor, 10);
    flipper2.attach(&run_Rmotor, 0.003);
}
 

void run(){
    flipper1.attach(&run_Lmotor, 0.003);
    flipper2.attach(&run_Rmotor, 0.003);
}

int main() {
     
    run();
    while(1) {
        if(sensor1.read()>0.6 && sensor2.read() < 0.5 && sensor3.read()>0.6){
            run();
        }
    
        else if(sensor1.read() < 0.5 && sensor2.read() < 0.5 && sensor3.read()>0.6){
            turn_right();
        }
    
        else if(sensor3.read() < 0.5 && sensor2.read() < 0.5 && sensor1.read()>0.6){
            turn_left();
        }
        else if(sensor1.read() < 0.5 && sensor2.read() > 0.6 && sensor3.read() > 0.6){
            turn_right();
        }
        else if(sensor3.read() < 0.5 && sensor2.read() > 0.6 && sensor1.read() > 0.6){
            turn_left();
        }
       wait_ms(10);
    }
}