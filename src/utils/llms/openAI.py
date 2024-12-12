from langchain_openai import ChatOpenAI as gpt

gpt4_mini = gpt(
    model="gpt-4o-mini",
    temperature=0.7,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    logprobs=True,
)

# Classe ou função para encapsular a lógica do nó LLM
class LLMNode:
    def __init__(self, model_name="gpt-4", temperature=0.6):
        # Configure o LLM (aqui usamos LangChain como exemplo)
        self.llm = gpt(model=model_name, temperature=temperature)
    
    def __call__(self, input_text):
        # Chame o LLM com o texto de entrada e retorne a resposta
        response = self.llm(input_text)
        return response