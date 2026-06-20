import os 
import json
import yaml
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import yaml
from openai import OpenAI
from dotenv import load_dotenv
from models import PromptConfig, ClassificationOutput

load_dotenv()
client = OpenAI()

def load_prompt(version: str = "v1") -> PromptConfig:
    with open(f"prompts/{version}.yaml") as f:
        data = yaml.safe_load(f)
    return PromptConfig(
        version=data["version"],
        system_prompt=data["system_prompt"]
    )

def classify_email(email_text: str, prompt: PromptConfig) -> ClassificationOutput:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt.system_prompt},
            {"role": "user", "content": email_text}
        ],
        temperature=0
    )
    raw = response.choices[0].message.content
    data = json.loads(raw)
    return ClassificationOutput(**data)