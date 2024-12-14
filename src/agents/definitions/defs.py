from crewai import Agent, Task, Crew
from crewai_tools import ScrapeWebsiteTool




receptor = Agent(
    role="Seletor de estágio",
    goal="Seu objetivo é entener o contexto da história e definir em que parte está: 1: explanação, 2: venda, 3: marcar reunião, ou 4: indefinido",
    backstory="Você tem especialistam no seu time capazes de desenvolver as melhores respostas, a mensagem recebida deve ser enviada para o melhor departamento escolher, sua função é definir para qual a ultima mensagem atual vai",
    vervbose="True"
)


receptor = Agent(
    role="Receptor",
    goal="Seu objetivo é entener o contexto da história e definir em que parte está",
    backstory="",
    vervbose="True"
)