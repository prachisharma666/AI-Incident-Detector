import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Incident Detector", layout="wide")
st.title("🚨 AI Incident Detector")
st.markdown("Multi-Agent Root Cause Analysis System using Gemini")

st.sidebar.header("Control Panel")
st.sidebar.markdown("Trigger system scenarios to see how the multi-agent AI responds.")

scenario = st.sidebar.radio(
    "Select Scenario",
    ["normal", "payment_failure", "database_slowdown", "traffic_spike"]
)

if st.sidebar.button("Run Diagnostics"):
    with st.spinner("Running system analysis..."):
        try:
            response = requests.post(f"{API_URL}/investigate", json={"scenario": scenario})
            data = response.json()
            
            st.header("System Metrics Status")
            
            # Display metrics as cards
            cols = st.columns(3)
            metrics_list = list(data["metrics"].items())
            
            for i, (metric_name, metric_data) in enumerate(metrics_list):
                col = cols[i % 3]
                color = "red" if metric_data["is_anomaly"] else "normal"
                delta = f"{metric_data['percentage_change']}%"
                col.metric(
                    label=metric_name.replace("_", " ").title(),
                    value=metric_data["current_value"],
                    delta=delta,
                    delta_color="inverse" if "error" in metric_name or "fail" in metric_name or "complaint" in metric_name else "normal"
                )
            
            st.divider()
            
            # Display AI Incident Report if triggered
            if data["incident_detected"]:
                report = data["report"]
                
                st.error(f"## 🚨 {report['severity']} SEVERITY INCIDENT DETECTED")
                st.subheader(f"Root Cause: {report['root_cause']}")
                st.info(f"**Confidence:** {report['confidence']}%")
                st.write(report['summary'])
                
                with st.expander("View Multi-Agent Audit Trail"):
                    st.markdown("### 📊 Data Agent Analysis")
                    st.write(data["evidence"]["data_agent"])
                    
                    st.markdown("### 📝 Log Agent Analysis")
                    st.write(data["evidence"]["log_agent"])
                    
                    st.markdown("### 💻 Raw System Logs")
                    st.code(data["evidence"]["raw_logs"])
            else:
                st.success("✅ System Operating Normally. No incidents detected.")
                
        except Exception as e:
            st.error(f"Failed to connect to backend. Is FastAPI running? Error: {str(e)}")