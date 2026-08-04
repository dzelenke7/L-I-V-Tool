#define V0 0
#define V1 1
#define V2 2
const float R_f = 1000000.0;

void setup() 
{
  Serial.begin(9600);

}

void loop() 
{
  float V_0 = analogRead(V0) * (5.0 / 1023.0);
  float V_1 = analogRead(V1) * (5.0 / 1023.0);
  float V_amp = analogRead(V2) * (5.0 / 1023.0);

  float I_res = V_0 / 100;
  float V_led = V_0 - V_1;
  float I_photo = (V_amp / R_f);

  Serial.println(I_res * 1000.0);
  Serial.println(V_led);
  Serial.println(I_photo * 1000000.0);

  delay(100);
}
