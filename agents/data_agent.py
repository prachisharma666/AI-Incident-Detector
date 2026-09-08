from google import genai
def analyze_data(anomalies:dict)->str:
    client=genai.Client()
    abnormal_metrics={metric:details for metric,details in anomalies.items() if details["is_anomaly"]}
    if not abnormal_metrics:
        return "No anomalies detected in the provided data."
    prompt=f"""
You are an expert Data Analyst Agent. Anallyze the following metrics anomalies and keep your analysis concise (3-4 sentences maximum).
Focus on the Business annd the Technical impact of the anomalies. Provide actionable insights and recommendations for each affected metric.
Anomalies:{abnormal_metrics}"""
    response=client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    return response.text