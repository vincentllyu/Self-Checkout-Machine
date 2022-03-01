#include "../src/HX711.h"
#define DOUT 19
#define CLK 13

HX711 scale(DOUT, CLK);
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  scale.set_scale();
  scale.tare();
}

void loop() {
  // put your main code here, to run repeatedly:
  float current_weight=scale.get_units(20);
  float scale_factor=(current_weight/0.145);
  Serial.println(scale_factor);
}
