import json
from fastapi import APIRouter
from pydantic import BaseModel

from app.services.llm_service import call_llm
from app.services.prompt_loader import load_prompt

router = APIRouter()

class InsightsRequest(BaseModel):
    input: str

@router.post("/insights")
def insights(req: InsightsRequest):
    system_prompt = load_prompt("insights.txt")
    llm_output = call_llm(system_prompt, req.input)
    try:
        return json.loads(llm_output)
    except Exception as e:
        print("JSON ERROR:", str(e))
        print("RAW LLM OUTPUT:", llm_output)
        return {
            "error": "Invalid JSON from AI",
            "raw": llm_output
        }
