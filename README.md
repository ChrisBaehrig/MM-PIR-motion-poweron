# MMM-PIR-motion-poweron

This program switch the RaspberryPi on, if a motion on the PIR-Sensor is detectet and switches the RasspberryPi of after a specific time. 

## Requirements

Connect your PIR-Sensor to the Pin 3 of Your RaspberryPI. 
Raspberry Pi try reading the output from the PIR motion sensor. The sensor outputs a digital HIGH (5V) signal when it detects a person. 

### What you will need
Example PIR-Sensor: https://www.amazon.de/dp/B07V6BY66P/

### Wireing
Connecting PIR-Sensor: 
<img src="https://user-images.githubusercontent.com/60329834/194863175-1e79b0cd-cc10-4a34-b3be-07cfd544f147.jpg" alt="drawing" width="500"/>

Connection to the RaspberryPI 4b: 
<img src="https://user-images.githubusercontent.com/60329834/194863175-1e79b0cd-cc10-4a34-b3be-07cfd544f147.jpg" alt="drawing" width="500"/>

Mor infos to the Wake up funktion of the RaspberryPI: https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi

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

- [alexyak](https://github.com/alexyak/motiondetector) for the original module code
- [lonekorean](https://github.com/lonekorean/diff-cam-engine/) for the diffcam engine code.
