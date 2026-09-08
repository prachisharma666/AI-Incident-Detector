from google import genai
def analyze_logs(logs:str)->str:
    client=genai.Client()
    prompt = f"""You are an expert DevOps Log Analyst. Review the following system logs and identify 
    any technical failures.Keep your analysis concise (3-4 sentences max). Do not hallucinate; stick to the evidence provided.
    Logs:{logs}
    """
    response=client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    return response.text