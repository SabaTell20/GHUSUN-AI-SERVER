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
    try:
        print(f"📥 INSIGHTS REQUEST received: {req.input}")
        
        # Load prompt
        try:
            system_prompt = load_prompt("insights.txt")
            print("✓ Prompt loaded successfully")
        except Exception as e:
            print(f"❌ ERROR loading prompt: {type(e).__name__}: {str(e)}")
            raise
        
        # Call LLM
        try:
            llm_output = call_llm(system_prompt, req.input)
            print("✓ LLM call successful")
        except Exception as e:
            print(f"❌ ERROR calling LLM: {type(e).__name__}: {str(e)}")
            raise
        
        # Parse JSON
        try:
            result = json.loads(llm_output)
            print("✓ JSON parsed successfully")
            return result
        except Exception as e:
            print(f"❌ JSON PARSE ERROR: {type(e).__name__}: {str(e)}")
            print(f"RAW LLM OUTPUT: {llm_output}")
            return {
                "error": "Invalid JSON from AI",
                "raw": llm_output,
                "parse_error": str(e)
            }
    except Exception as e:
        print(f"❌ UNHANDLED ERROR in /insights: {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
        raise
