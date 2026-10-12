def check_incidents(anomlaies:dict)->dict:
    anomaly_count=0
    affected_metrics=[]
    for metric,data in anomlaies.items():
        if data["is_anomaly"]:
            anomaly_count+=1
            affected_metrics.append(metric)
    MIN_INDEPENDENT_METRICS = 2
    DERIVED_METRICS = {"revenue"}

    independent = [m for m in affected_metrics if m not in DERIVED_METRICS]
    is_incident = len(independent) >= MIN_INDEPENDENT_METRICS
    return {
        "is_incident":is_incident,
        "anomaly_count":anomaly_count,
        "affected_metrics":affected_metrics
    }
