import pandas as pd
import numpy as np
def detect_anomalies(df:pd.DataFrame,threshold=3.0)->dict:
    anomalies={}
    baseline=df.iloc[::-1]
    current=df.iloc[-1]
    for i in df.columns:
        mean=baseline[i].mean()
        std=baseline[i].std()
        if std==0:
            std=0.001
        z_score=(current[i]-mean)/std
        is_anomaly=abs(z_score)>threshold
        percentage_change=((current[i]-mean)/mean)*100
        anomalies[i]={
            "current_value":round(float(current[i]),2),
            "baseline_mean":round(float(mean),2),
            "z_score":round(float(z_score),2),
            "is_anomaly":bool(is_anomaly),
            "percentage_change":round(float(percentage_change),2)
        }
    return anomalies