import json
from google import genai
def deteremine_root_cause(data_analysis:str,log_analysis:str)->dict:
    client=genai.Client()
    prompt=f"""
You are the incident root cause analysis agent.Based on the independent findings of the Data Agent
and Log Agent, determine the root cause of the incidnet.
Data Agent Findings:{data_analysis}
Log Agent Findings:{log_analysis}
Respond only with a JSON object containing the following keys:
{{
"severity":"HIGH,MEDIUM or LOW",
"root_cause":"A concise description of the root cause of the incident",
"confidence":"Percentage as Integer (e.g., 90),
"summary":"A concise summary of the incident and its impact on the system or business operations",
}}
"""
    response=client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    raw_text=response.text.replace("```json","").replace('```',"").strip()
    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
            return {
                "severity":"UNKNOWN",
                "root_cause":"Failed to parse AI response",
                "confidence":0,
                "summary":raw_text
            }