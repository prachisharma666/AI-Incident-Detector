import pandas as pd
import numpy as np
Scenarios={
    "payment_failure":{
        "multipliers":{"orders":0.62}, # Drops orders by 38%
        "overrides":{"payment_failures":5.8,"api_errors":18.0,"complaints":45},
        "logs":"13:01:02 Payment API timeout\n13:01:05 Payment API timeout\n13:01:07 HTTP 500 error at /checkout\n13:01:08 Database connection warning\n13:01:10 Payment gateway unavailable"
    },
    "database_slowdown":{
        "multipliers":{"orders":0.75}, # Drops orders by 25%
        "overrides":{"api_latency":850,"api_errors":12.0},
        "logs":"13:01:02 Query timeout on table 'orders'\n13:01:05 Postgres high CPU warning\n13:01:07 HTTP 503 error at /inventory\n13:01:10 Connection pool exhausted"
    },
    "traffic_spike":{
        "multipliers":{"orders":2.5}, # Increases orders by 150%
        "overrides":{"api_latency": 400,"api_errors":4.0},
        "logs":"13:01:02 Rate limit warning exceeded\n13:01:05 Nginx queue full\n13:01:07 Auto-scaling triggered\n13:01:10 HTTP 429 Too Many Requests"
    }
}
def generate_data(scenario:str="normal")->pd.DataFrame:
    np.random.seed(60)
    base_orders=np.random.normal(1000,50,60)
    base_revenue=base_orders*850
    base_latency=np.random.normal(200,10,60)
    base_errors=np.random.normal(0.5,0.1,60)
    base_payment_fail=np.random.normal(1.0,0.2,60)
    base_complaints=np.random.normal(10,2,60)
    df=pd.DataFrame({
        "orders":base_orders,
        "revenue":base_revenue,
        "api_latency":base_latency,
        "api_errors":base_errors,
        "payment_failures":base_payment_fail,
        "complaints":base_complaints
    })
    current_state=df.iloc[-1].copy()
    if scenario in Scenarios:
        config=Scenarios[scenario]
        if "multipliers" in config:
            for metric,factor in config["multipliers"].items():
                current_state[metric]*=factor
        if "overrides" in config:
            for metric,val in config["overrides"].items():
                current_state[metric]=val
        current_state["revenue"]=current_state["orders"]*850
    df.loc[60]=current_state
    return df

def generate_logs(scenario:str="normal")->str:
    default_logs="13:01:02 All systems operational\n13:01:05 Health check OK"
    return Scenarios.get(scenario,{}).get("logs",default_logs)
