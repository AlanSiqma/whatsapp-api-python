# Twilio SMS Sender 🐍

Este é um pequeno script Python que utiliza a biblioteca Twilio para enviar mensagens de texto (SMS) para um número de telefone específico. Ele carrega as credenciais necessárias do arquivo `.env` usando a biblioteca `dotenv`.

## Pré-requisitos

Antes de executar este script, você precisará de:

- Uma conta Twilio. Você pode criar uma gratuitamente em [twilio.com](https://www.twilio.com).
- Um número de telefone Twilio verificado para enviar mensagens.
- As credenciais da sua conta Twilio (Account SID e Auth Token).

## Configuração

1. Clone este repositório para o seu ambiente local.
2. Instale as dependências executando `pip install -r requirements.txt`.
3. Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis com suas respectivas informações:

account_sid=SUA_ACCOUNT_SID
auth_token=SEU_AUTH_TOKEN
to=NUMERO_DE_DESTINO
from_=NUMERO_DE_ORIGEM

Certifique-se de substituir `SUA_ACCOUNT_SID`, `SEU_AUTH_TOKEN`, `NUMERO_DE_DESTINO` e `NUMERO_DE_ORIGEM` pelos valores apropriados.

## Uso

Para enviar uma mensagem, execute o script 
```
py send_sms.py
```

Ele enviará uma mensagem de texto simples com o corpo "Cuidado!" para o número especificado como destino.
## Observações

- Este script foi projetado para fins educacionais ou de teste. Por favor, use-o com responsabilidade e de acordo com os termos de serviço do Twilio.
- Se você estiver enfrentando problemas, verifique suas credenciais e certifique-se de que seu número de telefone Twilio está verificado para enviar mensagens SMS.
- Certifique-se de não compartilhar suas credenciais do Twilio publicamente ou incluí-las em repositórios de código aberto sem precauções adequadas.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias ou correções.

