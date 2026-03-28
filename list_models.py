import google.generativeai as genai

# Replace with your actual API key from https://makersuite.google.com/app/apikey
genai.configure(api_key="AIzaSyCcTREiXY1HVnAhIpbcGilw_dqlb4duuT8")

models = genai.list_models()
for m in models:
    print(m.name)
