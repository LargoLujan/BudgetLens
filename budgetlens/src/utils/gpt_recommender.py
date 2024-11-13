import openai
from src.utils.config_loader import get_openai_api_key
from src.utils.prepare_context import prepare_recommendation_context


openai.api_key = get_openai_api_key()

def generate_gpt_recommendation(analysis_results):
    # Prepara el contexto específico para infoproductores
    context = prepare_recommendation_context(analysis_results)
    
    # Prompt detallado para guiar al modelo
    prompt = (
        f"{context}\n\n"
        "Los resultados anteriores muestran el análisis de ingresos y gastos de un infoproductor. "
        "Por favor, proporcione recomendaciones de mejora, si son necesarias, teniendo en cuenta que el usuario "
        "se enfoca en la creación y venta de infoproductos. "
        "Si los resultados ya son óptimos y no se requiere ninguna mejora, indique que el rendimiento actual es satisfactorio.\n\n"
        "¿Qué recomendaciones puede dar sobre estos resultados?"
    )
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    
    # Devuelve la recomendación formateada
    recommendation = response.choices[0].text.strip()
    return recommendation

