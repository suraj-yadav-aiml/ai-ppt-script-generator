import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    Configuration settings for the project.
    """
    VERBOSE: bool = True  
    MODEL_NAME: str = os.getenv("MODEL_NAME", "gpt-4o-mini") 
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", 0.8))