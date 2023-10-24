# Monitor de Preços com Python

Este projeto é um simples script em Python que permite monitorar o preço de um produto em um site de comércio eletrônico (por exemplo, Amazon) e receber notificações quando o preço cai abaixo de um limite definido.

## Requisitos

- Python 3.x
- Bibliotecas Python: `requests`, `beautifulsoup4`

Você pode instalar as bibliotecas necessárias com o seguinte comando:

```bash
pip install requests beautifulsoup4
```

## Uso

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/monitor-de-precos.git
```

2. Edite o arquivo `monitor_de_precos.py` e configure as seguintes variáveis:
   - `url` - A URL do produto que você deseja monitorar.
   - `classe_preco` - A classe HTML que contém o preço do produto na página.
   - `preco_maximo` - O preço máximo que você está disposto a pagar.

3. Execute o script:

```bash
python monitor_de_precos.py
```

O script fará uma requisição à página, extrairá o preço do produto e verificará se está abaixo do preço máximo configurado. Você receberá uma mensagem indicando se vale a pena comprar o produto ou não.

## Notas

Lembre-se de que é importante verificar os termos de serviço do site que você está monitorando para garantir que você está em conformidade com suas políticas de scraping.

## Licença

Este projeto é licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.
