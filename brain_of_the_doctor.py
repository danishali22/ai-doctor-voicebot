# Step 1: Setup GROQ Api Key 
import os
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Step 2: Convert image to required format 
import base64    # convert bits or bytes data to string
image_path = "acne.jpg"
image_file = open(image_path, "rb")
encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

# Step 3: Setup Multimodel LLM 
from groq import Groq

client = Groq()
model = "llama-3.2-90b-vision-preview"
query = "Is there something wrong with my face?"
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": query,
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{encoded_image}"
                }
            },
        ],
    }]
chat_completion=client.chat.completions.create(
    messages = messages,
    model = model
)
print(chat_completion.choices[0].message.content)
