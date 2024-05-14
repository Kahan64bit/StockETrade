# ❖ StockETrade
AIO CLI stock trading applicaiton linked with Alpaca API and GPT to buy stocks.

## How to use?
Follow the steps below to get started.
  
1. Create an account on [Alpaca](https://alpaca.markets/) and [OpenAI](https://openai.com/)

2. Run the `authenticate.py` file in the terminal and follow the prompts. Make sure to enter each API key seperately.

3. Run the ui.py file in the terminal, and check to see if all commands are working.

4. Enable paper trading in Alpaca to test if commands work properly.

## Commands and Syntax
StockeETrade uses typer for all CLI commands. Reference the page [here](https://typer.tiangolo.com/) to learn more.

1. To run scripts in terminal type `python ui.py`


## ❖ Smoke Detection iRobot

The Following Program demonstrates a fully autonomous iRobot that can traverse a finite space until a gas particulate is detected. 

## ❖ Requirements
1. Software Requirements
   - iRobot edu sdk. The link provided has the library. [iRobot® Education Python® SDK](https://github.com/iRobotEducation/irobot-edu-python-sdk?tab=readme-ov-file#iroboteducation-python-sdk)
   - Bluetooth Library (BLE): [bleak](https://bleak.readthedocs.io/en/latest/)
   - pySerial(Serialized Input to iRobot & RPi 3B+): `pip install pyserial`

2. Hardware Requirements
   - [Raspberry PI Ver. 3B+](https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/) or equil
   - [Arduino Uno R1](https://store-usa.arduino.cc/products/arduino-uno-rev3) or equil
   - [iRobot Create3](https://edu.irobot.com/shop/coding-robots/create?variant=269697) or equil

## ❖ 3B+ Integration with irobot

Follow the tutorial on the [create3](https://edu.irobot.com/learning-library/connect-create-3-to-raspberry-pi) website to connect the PI to the robot.
**
WIP
**

## ❖ BLE Connectivity
To run any .py script on the iRobot it must be connected by either **Bluetooth**, **WI-Fi**, or **Serial**. Setting up bluetooth is the easiest. Here is the way to connect to iRobot via Bluetooth using BLE.
1. Identify the iRobot's 
   - `Bluetooth(address="#irobot BLE MAC address")`
   - If issues persists read the issues page on [iRobot's github page](https://github.com/iRobotEducation/irobot-edu-python-sdk/issues)
  
## ❖ 3D Modeling Gas Sensor Mounting
1. Onshape Software
      - *Version 1.0*
         - Base platform for gas sensor (35mm x 24mm x 1mm).
         - Vertical beam perpendicular to the platform on the left edge (1mm x 24mm) extruded upward (9.532mm).
         - Horizontal beam perpendicular to vertical beam, and parallel with platform, on top of the vertical beam (2mm x 24mm x 1mm).
         - On the bottom of the base platform circle centered at (17.5mm x 12mm) with radius (1.375mm), extruded downward (20mm).
      - *Version 2.0*
         - Base platform for gas sensor (35mm x 24mm x 1mm).
         - Vertical beam perpendicular to the platform on the left edge (1mm x 24mm) extruded upward (9.532mm).
         - Horizontal beam perpendicular to vertical beam, and parallel with platform, on top of the vertical beam (2mm x 24mm x 1mm).
         - On the bottom of the base platform circle centered at (17.5mm x 12mm) with radius 1.375mm, extruded downward (20mm).
         - Front and back edges of base platform have perpendicularly joined walls (leveled with the base) measuring (35mm x 2mm) extruding outward (1mm)

## ❖  Development Stages
All files besides `main.py ` show development files before the final script. Read below to learn more about each file

1. bases.py
   - Commands iRobot to navigate to set points in a finite plane. Use this script to familiarize yourself with multithreaded python.  

