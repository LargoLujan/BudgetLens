from src.utils.gpt_recommender import generate_gpt_recommendation
from src.utils.prepare_context import prepare_recommendation_context
from src.utils.user_utils import get_user_type

class RecommendationService:
    def __init__(self, user_id):
        self.user_id = user_id
        self.user_type = get_user_type(user_id)
    
    def get_recommendation(self, plot_data):
        if self.user_type == "premium":
            # Generar recomendación con GPT
            return generate_gpt_recommendation(plot_data)
        else:
            # Devolver URL de recomendación de compra
            return {
                "recommendation": None,
                "redirect_url": "https://tuwebsite.com/comprar-recomendacion"
            }

