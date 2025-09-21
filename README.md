# 🧪 IA Test Agent

Este projeto implementa um **agente de IA** em Python que gera automaticamente **testes unitários** usando `pytest`.  
O agente recebe um arquivo Python como entrada e retorna um arquivo `test_<nome>.py` com os testes correspondentes.

---

## ⚙️ Tecnologias usadas
- Python 3.10+ (testado até 3.13)  
- [LangChain](https://www.langchain.com/)  
- [Azure OpenAI](https://learn.microsoft.com/azure/cognitive-services/openai/overview)  
- [pytest](https://docs.pytest.org/)  

---

## 📥 Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/SEU_USUARIO/ia-test-agent.git
   cd ia-test-agent
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔑 Configuração do Azure OpenAI
Antes de rodar o agente, configure as variáveis de ambiente no terminal:

```bash
setx AZURE_OPENAI_ENDPOINT "https://SEU_ENDPOINT.openai.azure.com/"
setx AZURE_OPENAI_KEY "SUA_CHAVE_API"
```

No Linux/Mac:
```bash
export AZURE_OPENAI_ENDPOINT="https://SEU_ENDPOINT.openai.azure.com/"
export AZURE_OPENAI_KEY="SUA_CHAVE_API"
```

---

## ▶️ Como usar

1. Crie uma função de exemplo em `examples/funcoes.py`, como:

```python
def soma(a, b):
    return a + b

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não permitida")
    return a / b
```

2. Rode o agente para gerar os testes:

```bash
python agent.py examples/funcoes.py
```

3. Será criado um arquivo `test_funcoes.py` na raiz do projeto.

---

## 🧪 Rodando os testes
Depois de gerar os testes:

```bash
pytest -v
```

Saída esperada (exemplo):
```
============================= test session starts =============================
collected 2 items

test_funcoes.py::test_soma_sucesso PASSED
test_funcoes.py::test_divisao_erro PASSED
```

---

## 📂 Estrutura do projeto
```
ia-test-agent/
│── agent.py
│── requirements.txt
│── README.md
│── .gitignore
│── examples/
│   └── funcoes.py
```

---

## 📌 Próximos passos
- Gerar testes para funções mais complexas  
- Integrar com GitHub Actions para rodar `pytest` automaticamente a cada push  
