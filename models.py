from pydantic import BaseModel
from typing import Literal

class PromptConfig(BaseModel):
    version : str
    system_prompt : str 

class EmailInput(BaseModel):
    email_text : str

class ClassificationOutput(BaseModel):
    category : Literal["billing", "technical", "account", "general"]
    summary : str