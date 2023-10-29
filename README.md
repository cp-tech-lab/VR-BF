# Novel VR-based Biofeedback systems: a comparison between heart rate variability- and electrodermal activity-driven approaches


***Paper*** Baldini, A., Patron, E., Gentili, C., Scilingo, E. P., & Greco, A. Novel VR-based Biofeedback systems: a comparison between heart rate variability- and electrodermal activity-driven approaches

## Description
Anxiety symptoms are important contributors to the global health-related burden. Low-intensity interventions have been proposed to reduce anxiety symptoms in the population. Among these, biofeedback (BF) offers an effective approach to reducing anxiety. In the present study, BF was integrated into a novel virtual reality (VR) architecture to enhance BF’s effectiveness to i) evaluate the feasibility of a VR-based single-session BF in teaching participants to self-regulate; ii) compare the BF aiming at reducing sympathetic (measured though the tonic level of skin conductance, SCL) versus increasing cardiac vagal (i.e., normalized high frequency of heart rate variability, HFnu-HRV) activation, and iii) evaluate which of the two VR-BF single-sessions was most effective in reducing perceived state anxiety.
20 healthy participants underwent both SCL- and HFnu-based in a single session VR-BF. Results showed the feasibility of a short single-session VR-BF and the effectiveness of both VR-BF sessions in reducing perceived state anxiety. Moreover, SCL-based VR-BF determined a significant reduction in sympathetic activation and in sympathovagal balance as well as a greater reduction in perceived state anxiety compared to HFnu-based VR-BF. SCL-based VR-BF represents a safe and effective intervention in reducing anxiety while enhancing adaptive psychophysiological activation.

## Video Demonstration
[![Alt text](./img/vr_bf_demo.png)](https://drive.google.com/drive/folders/1I6p-QJtqOD4YljUHDc__V_r54W-R86yq?usp=sharing)


## Executing the application
To launch the application:

#### 1. Configuration
Set up your shimmer device to real-time stream physiological signals over a selected Bluetooth port. You must be sure to update the [config.json](./python/config.json) file to let the application know the configured port. Additionally, you can customize other parameters such as the mapping function (scl_d or hfnu), the sampling frequency (fs) and the virtual scenario's updating frequency (fu).

#### 2. Python
Once you have completed the configuration phase, you can launch the python application by running the [main.py](./python/main.py) file.

#### 3. Unity
To correctly run the source code, you must design a virtual scenario by starting a [Unity project](https://unity.com/pages/unity-pro-buy-now?utm_source=google&utm_medium=cpc&utm_campaign=cc_dd_upr_emea_emea-t2_en_pu_sem-gg_acq_br-pr_2023-01_brand-et2_cc3022_ev-br_id:71700000105990829&utm_content=cc_dd_upr_emea_pu_sem_gg_ev-br_pros_x_npd_cpc_kw_sd_all_x_x_brand_id:58700008262875240&utm_term=unity&&&&&gad_source=1&gclid=EAIaIQobChMI0fTLwOibggMVDtF3Ch04NgWVEAAYASAAEgIsc_D_BwE&gclsrc=aw.ds).
You are free to graphically replicate the virtual environment described in the paper or create another one from scratch. The unique constraint to be taken into consideration throughout the designing process is related to the virtual objects dimensions that should follow those described in the paper. In facts, bearing in mind that the maximum reachable height by our virtual element was set to thirty meter, the objects must be scaled to reasonable dimensions.
Then, to let the python application communicate with your Unity objects and make them fly, you must attach the provided [*C#*](./unity/UnityClient.cs) to them. Now, you can run your Unity project.


## Reference
If you use this code or data, please cite the paper.
```
```

## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.



