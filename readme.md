
# Agendamento de Negócios com Microsoft Graph API

Esta aplicação Flask permite criar, listar e obter agendamentos para negócios que utilizam o **Microsoft Bookings** através da  **Microsoft Graph API** . O objetivo é integrar funcionalidades de agendamento em um sistema utilizando autenticação via MSAL e interações com a API do Microsoft Graph.

## Funcionalidades

* **Listar Negócios** (`GET /businesses`): Recupera uma lista de todos os negócios configurados no Microsoft Bookings.
* **Listar Agendamentos** (`GET /appointments/{business_id}`): Recupera todos os agendamentos de um negócio específico, identificado pelo `business_id`.
* **Criar Agendamento** (`POST /appointments/{business_id}`): Cria um novo agendamento para um negócio específico. Os dados do agendamento são fornecidos no corpo da requisição.

## Pré-requisitos

* **Python 3.x** instalado no seu sistema.
* **Microsoft Azure App Registration** com permissão para acessar a API do Microsoft Graph (usando as credenciais `CLIENT_ID`, `CLIENT_SECRET` e `TENANT_ID`).
* **Microsoft Graph API** configurada para manipular Booking Businesses e Agendamentos.

### Dependências

As dependências podem ser instaladas com o seguinte comando:

```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` deve conter as seguintes dependências:

```
Flask
requests
msal
flask-cors
python-dotenv
```

## Variáveis de Ambiente

A aplicação requer que as credenciais do Azure sejam configuradas no arquivo `.env` na raiz do projeto. O arquivo `.env` deve conter as seguintes variáveis:

```env
CLIENT_ID=<seu_client_id>
CLIENT_SECRET=<seu_client_secret>
TENANT_ID=<seu_tenant_id>
```

Essas variáveis são usadas para autenticação e autorização com a  **Microsoft Graph API** .

## Executando a Aplicação

Para rodar a aplicação, execute o seguinte comando:

```bash
python app.py
```

O servidor Flask será iniciado no endereço `http://127.0.0.1:5000/`.

## Endpoints

### 1. **Listar Negócios**

* **Método** : `GET`
* **URL** : `/businesses`
* **Descrição** : Retorna uma lista de negócios configurados no Microsoft Bookings.
* **Resposta Exemplo** :

```json
  {
      "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#solutions/bookingBusinesses",
      "value": [
          {
              "displayName": "Teste",
              "id": "Teste@systemautomationgroup.onmicrosoft.com"
          }
      ]
  }
```

### 2. **Listar Agendamentos**

* **Método** : `GET`
* **URL** : `/appointments/{business_id}`
* **Parâmetro** : `business_id` (ID do negócio)
* **Descrição** : Retorna todos os agendamentos para um negócio específico.
* **Resposta Exemplo** :

```json
  {
      "value": [
          {
              "id": "a6b5b8f8-81a1-4d71-b722-4d3d6e88889b",
              "startDateTime": {
                  "dateTime": "2025-01-15T10:00:00",
                  "timeZone": "UTC"
              },
              "endDateTime": {
                  "dateTime": "2025-01-15T10:30:00",
                  "timeZone": "UTC"
              },
              "serviceId": "c2be51d6-2b2e-4709-87b2-5ce3335f1136",
              "customer": {
                  "emailAddress": "cliente@example.com",
                  "name": "Nome do Cliente",
                  "phone": "11987654321"
              },
              "staffMemberIds": ["6d8cbee8-8456-40bb-9828-5bf4d30a9aec"]
          }
      ]
  }
```

### 3. **Criar Agendamento**

* **Método** : `POST`
* **URL** : `/appointments/{business_id}`
* **Parâmetro** : `business_id` (ID do negócio)
* **Corpo da Requisição** :
  O corpo da requisição deve conter os seguintes dados para criar um agendamento:

```json
  {
      "start_time": "2025-01-15T10:00:00",
      "end_time": "2025-01-15T10:30:00",
      "service_id": "c2be51d6-2b2e-4709-87b2-5ce3335f1136",
      "customer_email": "cliente@example.com",
      "customer_name": "Nome do Cliente",
      "customer_phone": "11987654321",
      "staff_member_id": "6d8cbee8-8456-40bb-9828-5bf4d30a9aec"
  }
```

* **Resposta Exemplo** :

```json
  {
      "id": "a6b5b8f8-81a1-4d71-b722-4d3d6e88889b",
      "startDateTime": {
          "dateTime": "2025-01-15T10:00:00",
          "timeZone": "UTC"
      },
      "endDateTime": {
          "dateTime": "2025-01-15T10:30:00",
          "timeZone": "UTC"
      },
      "serviceId": "c2be51d6-2b2e-4709-87b2-5ce3335f1136",
      "customer": {
          "emailAddress": "cliente@example.com",
          "name": "Nome do Cliente",
          "phone": "11987654321"
      },
      "staffMemberIds": ["6d8cbee8-8456-40bb-9828-5bf4d30a9aec"]
  }
```

## Erros Comuns

* **401 Unauthorized** : Verifique se o `CLIENT_ID`, `CLIENT_SECRET` e `TENANT_ID` estão corretos e se o aplicativo possui permissões adequadas no Azure.
* **400 Bad Request** : O formato dos dados fornecidos para a criação de um agendamento pode estar incorreto. Verifique os campos do JSON enviado.

## Contribuições

Se você quiser contribuir para este projeto, sinta-se à vontade para fazer um fork e enviar pull requests.

## Licença

Este projeto é licenciado sob a [MIT License](https://chatgpt.com/c/LICENSE).
