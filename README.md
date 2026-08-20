# Pinkyup ✋

A small project that uses a webcam to count raised fingers and display the count on three LEDs connected to an Arduino Uno.

## How it works

```text
Webcam → Hand Tracking → Finger Count → Serial → Arduino → LEDs
````

Python uses **cvzone**, and **MediaPipe** to detect the hand and count raised fingers. The count is sent to the Arduino using **PySerial**.

The Arduino displays the count as a 3-bit binary number:

| Fingers | Binary | LEDs (4 2 1) |
| ------: | :----: | :----------: |
|       0 |  `000` |  OFF OFF OFF |
|       1 |  `001` |  OFF OFF ON  |
|       2 |  `010` |  OFF ON OFF  |
|       3 |  `011` |   OFF ON ON  |
|       4 |  `100` |  ON OFF OFF  |
|       5 |  `101` |   ON OFF ON  |

## Hardware

* Arduino Uno
* 3 LEDs
* 3 resistors
* Breadboard
* Jumper wires
* Webcam

### Connections

| Arduino Pin | LED   | Value |
| ----------- | ----- | ----: |
| D13         | LED 1 |     1 |
| D12         | LED 2 |     2 |
| D11         | LED 3 |     4 |


