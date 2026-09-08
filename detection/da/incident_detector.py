def check_incidents(anomlaies:dict)->dict:
    anomaly_count=0
    affected_metrics=[]
    for metric,data in anomlaies.items():
        if data["is_anomaly"]:
            anomaly_count+=1
            affected_metrics.append(metric)
    is_incident=anomaly_count>=3 and len("affected_metrics")>=2
    return {
        "is_incident":is_incident,
        "anomaly_count":anomaly_count,
        "affected_metrics":affected_metrics
    }