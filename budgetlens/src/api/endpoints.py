from fastapi import APIRouter, HTTPException
from src.models.recommendation import RecommendationService

router = APIRouter()

@router.get("/recommendation/{user_id}")
async def get_recommendation(user_id: int, plot_data: dict):
    try:
        recommendation_service = RecommendationService(user_id)
        result = recommendation_service.get_recommendation(plot_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
