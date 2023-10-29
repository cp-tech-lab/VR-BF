# VR-BF

***Baldini Andrea***
Information Engineering Department, University of Pisa.

***Paper*** 

## Description
Heart rate variability biofeedback (HRV-BF) treatments have recently aroused great interest from the scientific community due to their possible effectiveness in treating many medical disorders (e.g., stress, anxiety) alongside the almost total absence of side effects. Virtual reality (VR) may provide advantages for BF treatments regarding motivation, attentional focus, and engagement. However, BF outcomes are often contrasting and variable, probably due to the complex physiological nature of the heart dynamics governed by both branches of the autonomic nervous system. On the other hand, a more direct, manageable and controllable BF parameter (e.g., the electrodermal activity; EDA) could enhance BF effectiveness.
In this study, we propose an innovative VR-BF mapping algorithm based on EDA to teach subjects how to reduce physiological arousal. To assess the validity of the proposed mapping algorithm, we compared it with a VR-BF based on HRV in terms of physiological and psychological outcomes, as well as ease of learning. For this purpose, we developed a VR architecture to manage EDA-BF and HRV-BF, and we designed a randomized experimental timeline exposing 20 subjects to both BF modalities. Statistical analyses revealed the non-inferiority of the EDA-BF in terms of physiological outcomes and better performance regarding the psychological response and ease of learning, proposing a novel method to guide BF treatment.

![demo](img/vr_bf_demo.png)


## Executing the application
To launch the app application:

#### Configuration
Set up your shimmer device to stream the acquired data over a selected Bluetooth port. You must be sure to update the [config.json](./python/config.json) file to input such port modifying the *port* key. Afterwards, you can select your custom configuration in terms of mapping function (scl_d or hfnu), sampling frequency (fs) and scenario's updating frequency (fu).

#### Python
Once you have completed the configuration phase, you can lauch the python application by running the [main.py](./python/main.py) file.

#### Unity
A [UnityClient.cs](./unity/UnityClient.cs) file is provided to connect the python application to your Unity scenario. You are free to graphically replicate the virtual environment described in the paper or create another from scratch. In both cases, to make the application work, you should follow the paper in designing the objects proportion because the constants of the algorithm are tuned to work with a maximum height of thirty meters. 
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


