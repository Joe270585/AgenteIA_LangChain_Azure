import os
from langchain_openai import AzureChatOpenAI

# Configurar credenciais do Azure OpenAI
# export AZURE_OPENAI_API_KEY="sua_chave"
# export AZURE_OPENAI_ENDPOINT="seu_endpoint"

llm = AzureChatOpenAI(
    openai_api_version="2024-05-01-preview",
    deployment_name="gpt-4o-mini",  # ou o modelo configurado no Azure
    temperature=0
)

def gerar_testes(codigo: str, nome_arquivo: str = "funcoes") -> str:
    """Gera um arquivo de testes pytest a partir de um código Python."""

    prompt = f"""
    Você é um agente de IA que gera testes unitários em Python usando pytest.
    Receberá um código Python e deve retornar um arquivo de testes chamado test_{nome_arquivo}.py.

    Regras:
    - A primeira linha do arquivo deve ser: import pytest
    - Crie funções def test_* para casos de sucesso e falha
    - Não invente funções, só use as que estão no código dado

    Código fornecido:
    {codigo}
    """

    resposta = llm.invoke(prompt)
    conteudo_teste = resposta.content

    # Salvar em arquivo
    nome_saida = f"examples/test_{nome_arquivo}.py"
    with open(nome_saida, "w", encoding="utf-8") as f:
        f.write(conteudo_teste)

    return nome_saida


if __name__ == "__main__":
    # Exemplo de uso
    with open("examples/funcoes.py", "r", encoding="utf-8") as f:
        codigo = f.read()

    arquivo_teste = gerar_testes(codigo, "funcoes")
    print(f"Arquivo de testes gerado: {arquivo_teste}")
