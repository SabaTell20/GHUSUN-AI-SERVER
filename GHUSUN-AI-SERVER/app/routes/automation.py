import json
from fastapi import APIRouter
from pydantic import BaseModel

from app.services.llm_service import call_llm
from app.services.prompt_loader import load_prompt

router = APIRouter()


class AutomationRequest(BaseModel):
    input: str


@router.post("/automation")
def automation(req: AutomationRequest):
    system_prompt = load_prompt("automation.txt")
    llm_output = call_llm(system_prompt, req.input)
    return json.loads(llm_output)