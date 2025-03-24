from litellm import completion
import os

os.environ['GROQ_API_KEY'] = "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"
response = completion(
    model="groq/llama3-8b-8192", 
    messages=[
       {"role": "user", "content": "hello from litellm"}
   ],
)
print(response)