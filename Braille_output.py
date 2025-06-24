const int solenoidPins[] = {2, 3, 4, 5, 6, 7};

void setup() {
  Serial.begin(9600);
  delay(2000);

  for (int i = 0; i < 6; i++) {
    pinMode(solenoidPins[i], OUTPUT);
  }
}

void loop() {
  if (Serial.available() > 0) {
    delay(500);
    char inputChar = Serial.read();
    Serial.print("Received: ");
    Serial.println(inputChar);
    delay(500);
    
    switch (inputChar) {
      case 'a':
        activateSolenoids(1, 0);
        break;
      case 'b':
        activateSolenoids(2, 0, 2);
        break;
      case 'c':
        activateSolenoids(2, 0, 1);
        break;
      case 'd':
        activateSolenoids(3, 0, 1, 3);
        break;
      case 'e':
        activateSolenoids(2, 0, 3);
        break;
      case 'f':
        activateSolenoids(3, 0, 1, 2);
        break;
      case 'g':
        activateSolenoids(4, 0, 1, 2, 3);
        break;
      case 'h':
        activateSolenoids(3, 0, 2, 3);
        break;
      case 'i':
        activateSolenoids(2, 1, 2);
        break;
      case 'j':
        activateSolenoids(3, 1, 2, 3);
        break;
      case 'k':
        activateSolenoids(2, 0, 4);
        break;
      case 'l':
        activateSolenoids(3, 0, 2, 4);
        break;
      case 'm':
        activateSolenoids(3, 0, 1, 4);
        break;
      case 'n':
        activateSolenoids(4, 0, 1, 3, 4);
        break;
      case 'o':
        activateSolenoids(3, 0, 3, 4);
        break;
      case 'p':
        activateSolenoids(4, 0, 1, 2, 4);
        break;
      case 'q':
        activateSolenoids(5, 0, 1, 2, 3, 4);
        break;
      case 'r':
        activateSolenoids(4, 0, 2, 3, 4);
        break;
      case 's':
        activateSolenoids(3, 1, 2, 4);
        break;
      case 't':
        activateSolenoids(4, 1, 2, 3, 4);
        break;
      case 'u':
        activateSolenoids(3, 0, 4, 5);
        break;
      case 'v':
        activateSolenoids(4, 0, 2, 4, 5);
        break;
      case 'w':
        activateSolenoids(4, 1, 2, 3, 5);
        break;
      case 'x':
        activateSolenoids(4, 0, 1, 4, 5);
        break;
      case 'y':
        activateSolenoids(5, 0, 1, 3, 4, 5);
        break;
      case 'z':
        activateSolenoids(4, 0, 3, 4, 5);
        break;

      default:
        deactivateSolenoids();
        break;
    }
  }
}

void activateSolenoids(int pinCount, ...) {
  Serial.print("Activating pins: ");
    
  va_list pins;
  va_start(pins, pinCount);

  for (int i = 0; i < pinCount; i++) {
    int pin = va_arg(pins, int);
    Serial.print(pin);
    Serial.print(" ");
    digitalWrite(solenoidPins[pin], HIGH);
  }
  Serial.println();
  delay(500);

  for (int i = 0; i < pinCount; i++) {
    int pin = va_arg(pins, int);
    digitalWrite(solenoidPins[pin], LOW);
  }
  va_end(pins);
}

void deactivateSolenoids() {
  for (int i = 0; i < 6; i++) {
    digitalWrite(solenoidPins[i], LOW);
  }
}
