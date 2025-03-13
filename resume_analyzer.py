import openai  

openai.api_key = "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"

def analyze_resume(resume_text):
    """Analyzes resume text and suggests improvements using GPT-4."""
    prompt = f"Analyze this resume and suggest improvements:\n{resume_text}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]
def improve_bullet_points(resume_text):
    """Enhances resume bullet points for clarity and impact."""
    prompt = f"Improve the following resume bullet points for clarity and impact:\n{resume_text}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]
