import google.generativeai as genai

# Put your actual Gemini API key here
genai.configure(api_key="AIzaSyBgqmmkNZB2-caq5qCJVJMU0_ymX_ilD4w")

models = genai.list_models()

for m in models:
    print("Model:", m.name)
    print("Supported methods:", m.supported_generation_methods)
    print("-" * 40)