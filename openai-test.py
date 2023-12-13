from openai import OpenAI

api_base = "https://openai.phate.dev/v1"
api_key = "sk-template"
openai = OpenAI(base_url=api_base, api_key=api_key)
res = openai.completions.create(model="starling", prompt="This is a test", max_tokens=5)
print(res)
