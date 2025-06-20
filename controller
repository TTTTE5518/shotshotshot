const int trigPin = 5;    // 超音波 Trig 腳
const int echoPin = 4;    // 超音波 Echo 腳

void setup() {
  Serial.begin(9600);     // 與電腦/TouchDesigner 串口同步
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  long duration;
  int distance;

  // 發送 10 微秒的高電位脈衝到 Trig
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // 讀取 Echo 回來的高電位持續時間（微秒）
  duration = pulseIn(echoPin, HIGH, 30000); // 30ms timeout

  // 計算距離（公分）：聲速約 340m/s
  // 距離 = (持續時間 / 2) * 0.0343
  distance = duration * 0.0343 / 2;

  // 如果量測到有效距離（通常 HC-SR04 0~400cm）
  if (distance > 0 && distance < 400) {
    Serial.println(distance);
  } else {
    Serial.println("Out of range");
  }

  delay(100); // 0.1 秒更新一次
}
