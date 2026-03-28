import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyDz6kkRCI35djLzms40GDGMiJZuwOiV8Lo")  # Replace with your real API key

# Load model
model = genai.GenerativeModel("gemini-1.5-flash-latest")


def generate_proposal_content(prompt):
    system_prompt = """You are a professional business proposal writer. Given a short description or project title, 
    generate a structured proposal including: 
    1. Project Introduction 
    2. Objectives 
    3. Timeline 
    4. Deliverables 
    5. Technology Stack 
    6. Benefits to the Client 
    7. Conclusion.
    Format in clear, formal language for a consulting proposal."""
    
    response = model.generate_content(f"{system_prompt}\n\nUser input: {prompt}")
    return response.text
