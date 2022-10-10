# MMM-PIR-motion-poweron

This program switch the RaspberryPi on, if a motion on the PIR-Sensor is detectet and switches the RasspberryPi of after a specific time. 
<img src="https://user-images.githubusercontent.com/60329834/194888681-0f4a8c82-b71c-4adb-b94d-ca8867e6edd9.png" alt="drawing" width="500"/>

## Requirements

Connect your PIR-Sensor to the Pin 3 of Your RaspberryPI. An BD137 Transistor inverts the Signal for the Interrupt to start the RP.
Raspberry Pi try reading the output from the PIR motion sensor. The sensor outputs a digital HIGH (5V) signal when it detects a person. 

### What you will need
Example PIR-Sensor: https://www.amazon.de/dp/B07V6BY66P/

### Wireing
Connecting PIR-Sensor: 

<img src="https://user-images.githubusercontent.com/60329834/194886593-2a06cc30-faa7-409b-8a29-b5f6a4dc3f78.png" alt="drawing" width="500"/>
<img src="https://user-images.githubusercontent.com/60329834/194887463-1ff34bbf-9036-4240-b954-f8260f2437b8.jpg" alt="drawing" width="500"/>

Mor infos to the Wake up funktion of the RaspberryPI: 
https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi

## Installation

Just clone the files into a new directory Powermanagement .
```
mkdir Powermanagement
git clone https://github.com/ChrisBaehrig/MM-PIR-motion-poweron.git
```

### Integrate Powermanagement to System
1. Give permissions for run: 
    ```
    chmod +x time-shutdown.py
    ```
2. Crete Batch for PM2 command:
    ```
    cd ~
    nano timeshut.sh
    ```
3. Write into file following command: 
    ``` 
    sudo pm2 start time-shutdown.py
    ```
4. Save with crtl + o and close crtl + x 
5. Give permissions for run: 
    ```
    chmod +x time-shut.sh
    ```

###  Add to PM2 for autostart
1. Start PM2: 
    ```
    pm2 start time-shut.sh
    ```
2. Save to PM2: 
    ```
    pm2 save
    ```
3. Check PM2 tasks: 
    ```
    pm2 monit
    ```
    and
    ```
    sudo pm2 monit
    ```
### Stop autostart: 
    ```
    pm2 stop time-shut
    sudo pm2 stop time-shutdown.py
    ```

## Changelog
### [1.0.0] - 2022-10-10

- Initial release

## Acknowledgements

Many thanks to

- [MichMich](https://github.com/MichMich/MagicMirror) for the MagicMirror development

