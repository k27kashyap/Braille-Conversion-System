const int solenoidPins[] = {2, 3, 4, 5, 6, 7};

bool brailleDisplayStarted = false;

void setup() {
  Serial.begin(9600);

  Serial.println("Arduino initialized");
  
  for (int i = 0; i < 6; i++) {
    pinMode(solenoidPins[i], OUTPUT);
  }
  
  while (!brailleDisplayStarted) {
    if (Serial.available() > 0) {
      char command = Serial.read();
      if (command == 'S') {
        brailleDisplayStarted = true;
      }
    }
  }

  Serial.println("Received 'START' command from Python");
}

void loop() {
  if (Serial.available() > 0) {
    char character = Serial.read();
    
    Serial.print("Received character: ");
    Serial.println(character);
    
    displayBraille(character);
  }
}

void displayBraille(char character) {
  const char* brailleCharacters[] = {
    "100000", // A
    "101000", // B
    "110000", // C
    "110100", // D
    "100100", // E
    "111000", // F
    "111100", // G
    "101100", // H
    "011000", // I
    "011100", // J
    "100010", // K
    "101010", // L
    "110010", // M
    "110110", // N
    "100110", // O
    "111010", // P
    "111110", // Q
    "101110", // R
    "011010", // S
    "011110", // T
    "100011", // U
    "101011", // V
    "011101", // W
    "110011", // X
    "110111", // Y
    "100111", // Z
    "000000", // (Space)
    "011011", // , (Comma)
    "010010", // . (Full-stop)
    "000011", // 0
    "100000", // 1
    "101000", // 2
    "110000", // 3
    "110100", // 4
    "100100", // 5
    "111000", // 6
    "111100", // 7
    "101100", // 8
    "011000"  // 9
  };

  // Find the index of the character in the mapping
  int index = -1;
  if ((character >= 'A' && character <= 'Z')) {
    index = character - 'A';
  } else if (character >= 'a' && character <= 'z') {
    index = character - 'a';
  } else if (character >= '0' && character <= '9') {
    index = 26 + (character - '0');
  } else if (character == ' ') {
    index = 36;
  } else if (character == ',') {
    index = 37;
  } else if (character == '.') {
    index = 38;
  }

  if (index >= 0 && index < 39) {
    for (int i = 0; i < 6; i++) {
      digitalWrite(solenoidPins[i], brailleCharacters[index][i] == '1' ? HIGH : LOW);
    }
    
    Serial.println("Displaying Braille for character: " + String(character));
    
    delay(1000);
    
    for (int i = 0; i < 6; i++) {
      digitalWrite(solenoidPins[i], LOW);
    }
  }
}
