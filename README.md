# Exibidor de Níveis Coloridos

Script em Python (`app.py`) que exibe no terminal um dos cinco níveis (de "Muito Baixo" a "Muito Alto"), cada um com uma cor diferente, usando a biblioteca [colorama](https://pypi.org/project/colorama/).

## Como funciona

A função `exibir_nivel(nivel)` recebe um número inteiro de 1 a 5 e imprime a descrição correspondente, toda na cor do nível. Se o valor estiver fora desse intervalo, mostra uma mensagem de erro.

| Nível | Descrição                    | Cor      |
|-------|------------------------------|----------|
| 1     | Muito Baixo                  | Vermelho |
| 2     | Baixo                        | Amarelo  |
| 3     | Médio                        | Verde    |
| 4     | Alto                         | Ciano    |
| 5     | Muito Alto (alerta)          | Azul     |

Ao final de cada impressão é aplicado `Style.RESET_ALL`, para que a cor não "vaze" para o restante do terminal.

## Requisitos

- Python 3.x
- colorama

## Instalação

```bash
pip install colorama
```

## Como executar

```bash
python app.py
```

Por padrão, o final do arquivo chama `exibir_nivel(1)`, então a execução exibe o Nível 1 em vermelho. Para ver outro nível, altere o número na chamada.

## Exemplo de uso

```python
exibir_nivel(3)   # imprime "Nível 3: Médio" em verde
exibir_nivel(9)   # imprime "Nível inválido. Por favor, insira um nível entre 1 e 5."
```

## Estrutura do código

- `exibir_nivel(nivel)`: importa o `colorama`, define a lista de níveis coloridos e imprime o texto correspondente ao nível informado.
- Chamada de demonstração no final do arquivo: `exibir_nivel(1)`.