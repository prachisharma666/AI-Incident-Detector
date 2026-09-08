import pandas as pd
from simulations.simulation import generate_data
from detection.da.anomaly_detection import detect_anomalies
from detection.da.incident_detector import check_incidents
def test_normal_scenario():
    df=generate_data("normal")
    anomalies=detect_anomalies(df)
    incident=check_incidents(anomalies)
    assert incident["is_incident"]==False
    assert incident["anomaly_count"]==0
def test_payment_failure_scenario():
    df=generate_data("payment_failure")
    anomalies=detect_anomalies(df)
    incident=check_incidents(anomalies)
    assert incident["is_incident"]==True
    assert incident["anomaly_count"]>=3
    assert "payment_failure" in incident["affected_metrics"]