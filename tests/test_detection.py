import pandas as pd
from simulations.simulation import generate_data
from detection.da.anomaly_detection import detect_anomalies
from detection.da.incident_detector import check_incidents

def test_normal_scenario():
    df = generate_data("normal")
    anomalies = detect_anomalies(df)
    incident = check_incidents(anomalies)
    assert incident["is_incident"] == False
    assert incident["anomaly_count"] == 0

def test_payment_failure_scenario():
    df = generate_data("payment_failure")
    anomalies = detect_anomalies(df)
    incident = check_incidents(anomalies)
    assert incident["is_incident"] == True
    assert incident["anomaly_count"] >= 3
    assert "payment_failure" in incident["affected_metrics"]

def test_database_slowdown_scenario():
    df = generate_data("database_slowdown")
    anomalies = detect_anomalies(df)
    incident = check_incidents(anomalies)
    assert incident["is_incident"] == True
    assert incident["anomaly_count"] >= 3
    # Database slowdown affects latency and errors
    assert "api_latency" in incident["affected_metrics"] or "api_errors" in incident["affected_metrics"]

def test_traffic_spike_scenario():
    df = generate_data("traffic_spike")
    anomalies = detect_anomalies(df)
    incident = check_incidents(anomalies)
    assert incident["is_incident"] == True
    assert incident["anomaly_count"] >= 3
    # Traffic spike heavily impacts order volume and latency
    assert "orders" in incident["affected_metrics"]