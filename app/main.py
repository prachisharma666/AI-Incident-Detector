import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from simulations.simulation import generate_data, generate_logs
from detection.da.anomaly_detection import detect_anomalies
from detection.da.incident_detector import check_incidents
from agents.data_agent import analyze_data
from agents.log_agent import analyze_logs
from agents.root_cause_agent import deteremine_root_cause
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
app=FastAPI(title="AI Incident Detector")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to your frontend's domain in production
    allow_methods=["*"],
    allow_headers=["*"],
)
class Scenariorequest(BaseModel):
    scenario:str
@app.get("/health")
def health_check():
    return{"status":"operational","api_key_loaded":bool(os.getenv("GEMINI_API_KEY"))}
@app.post("/investigate")
def investigate_system(req:Scenariorequest):
    df=generate_data(req.scenario)
    logs=generate_logs(req.scenario)
    anomalies=detect_anomalies(df)
    incident_status=check_incidents(anomalies)
    result={
        "scenario":req.scenario,
        "incident_detected":incident_status["is_incident"],
        "metrics":anomalies
    }
    if incident_status["is_incident"]:
        data_insight=analyze_data(anomalies)
        log_insight=analyze_logs(logs)
        root_cause_report=deteremine_root_cause(data_insight,log_insight)
        result["report"]=root_cause_report
        result["evidence"]={
            "data_agent":data_insight,
            "log_agent":log_insight,
            "raw_logs":logs
        }
    return result
