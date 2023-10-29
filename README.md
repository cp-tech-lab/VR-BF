# Novel VR-based Biofeedback systems: a comparison between heart rate variability- and electrodermal activity-driven approaches


***Paper*** Baldini, A., Patron, E., Gentili, C., Scilingo, E. P., & Greco, A. Novel VR-based Biofeedback systems: a comparison between heart rate variability- and electrodermal activity-driven approaches

## Description
Anxiety symptoms are important contributors to the global health-related burden. Low-intensity interventions have been proposed to reduce anxiety symptoms in the population. Among these, biofeedback (BF) offers an effective approach to reducing anxiety. In the present study, BF was integrated into a novel virtual reality (VR) architecture to enhance BF’s effectiveness to i) evaluate the feasibility of a VR-based single-session BF in teaching participants to self-regulate; ii) compare the BF aiming at reducing sympathetic (measured though the tonic level of skin conductance, SCL) versus increasing cardiac vagal (i.e., normalized high frequency of heart rate variability, HFnu-HRV) activation, and iii) evaluate which of the two VR-BF single-sessions was most effective in reducing perceived state anxiety.
20 healthy participants underwent both SCL- and HFnu-based in a single session VR-BF. Results showed the feasibility of a short single-session VR-BF and the effectiveness of both VR-BF sessions in reducing perceived state anxiety. Moreover, SCL-based VR-BF determined a significant reduction in sympathetic activation and in sympathovagal balance as well as a greater reduction in perceived state anxiety compared to HFnu-based VR-BF. SCL-based VR-BF represents a safe and effective intervention in reducing anxiety while enhancing adaptive psychophysiological activation.

## Video Demonstration
[![Alt text](./img/vr_bf_demo.png)](https://drive.google.com/drive/folders/1I6p-QJtqOD4YljUHDc__V_r54W-R86yq?usp=sharing)


## Executing the application
To launch the app application:

#### 1. Configuration
Set up your shimmer device to stream the acquired data over a selected Bluetooth port. You must be sure to update the [config.json](./python/config.json) file to input such port modifying the *port* key. Afterwards, you can select your custom configuration in terms of mapping function (scl_d or hfnu), sampling frequency (fs) and scenario's updating frequency (fu).

#### 2. Python
Once you have completed the configuration phase, you can lauch the python application by running the [main.py](./python/main.py) file.

#### 3. Unity
A [UnityClient.cs](./unity/UnityClient.cs) file is provided to connect the python application to your Unity scenario. You are free to graphically replicate the virtual environment described in the paper or create another one from scratch. In both cases, to make the application work, you should follow the paper in designing the objects proportion because the constants of the algorithm are tuned to work with a maximum height of thirty meters. 
To launch the application, you just need to attach the provided .cs file to the objects you want to move and start the Unity project.

## Reference
If you use this code or data, please cite the paper:
```
@inproceedings{baldini2019vrbf,
author="Baldini, Andrea"
}
```

## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Acknowledgment


