import os
import requests
import json
from flask import Flask, jsonify, request
from msal import ConfidentialClientApplication
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
TENANT_ID = os.getenv("TENANT_ID")
GRAPH_API_ENDPOINT = 'https://graph.microsoft.com/v1.0'

app = Flask(__name__)
app.secret_key = 'P1RR6654'
app.config['SESSION_COOKIE_SECURE'] = True

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
CORS(app)

# Função para gerar token de acesso usando MSAL
def generate_access_token(client_id, client_secret, tenant_id):
    authority = f"https://login.microsoftonline.com/{tenant_id}"
    app = ConfidentialClientApplication(client_id, authority=authority, client_credential=client_secret)
    scopes = ["https://graph.microsoft.com/.default"]
    result = app.acquire_token_for_client(scopes=scopes)

    if "access_token" in result:
        return result['access_token']
    else:
        raise Exception("Falha ao adquirir token.")

# Função para listar os negócios (bookingBusinesses)
def get_booking_businesses(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(f'{GRAPH_API_ENDPOINT}/solutions/bookingBusinesses', headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Falha ao obter os negócios do Bookings. Status: {response.status_code}, Resposta: {response.text}")

# Função para listar os agendamentos de um negócio específico
def get_bookings_appointments(access_token, business_id):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(f'{GRAPH_API_ENDPOINT}/solutions/bookingBusinesses/{business_id}/appointments', headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Falha ao obter agendamentos. Status: {response.status_code}, Resposta: {response.text}")

# Função para criar um agendamento
def create_appointment(access_token, business_id, appointment_data):
    url = f"{GRAPH_API_ENDPOINT}/solutions/bookingBusinesses/{business_id}/appointments"
    headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=appointment_data)
    
    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Falha ao criar agendamento. Status: {response.status_code}, Resposta: {response.text}")

# Rota para obter os negócios existentes (bookingBusinesses)
@app.route('/businesses', methods=['GET'])
def businesses():
    try:
        access_token = generate_access_token(CLIENT_ID, CLIENT_SECRET, TENANT_ID)
        businesses = get_booking_businesses(access_token)
        return jsonify(businesses), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Rota para obter agendamentos de um negócio específico
@app.route('/appointments/<business_id>', methods=['GET'])
def appointments(business_id):
    try:
        access_token = generate_access_token(CLIENT_ID, CLIENT_SECRET, TENANT_ID)
        appointments = get_bookings_appointments(access_token, business_id)
        return jsonify(appointments), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Rota para criar um agendamento
@app.route('/appointments/<business_id>', methods=['POST'])
def create_appointment_route(business_id):
    try:
        # Recupera e utiliza os dados do agendamento enviados no corpo da requisição
        appointment_data = request.json
        appointment_json = {
            "startDateTime": {
                "dateTime": appointment_data["start_time"],
                "timeZone": "UTC"
            },
            "endDateTime": {
                "dateTime": appointment_data["end_time"],
                "timeZone": "UTC"
            },
            "serviceId": appointment_data["service_id"],
            "customer": {
                "emailAddress": appointment_data["customer_email"],
                "name": appointment_data["customer_name"],
                "phone": appointment_data["customer_phone"]
            },
            "staffMemberIds": [appointment_data["staff_member_id"]]
        }

        # Gera o token de acesso e criar agendamento
        access_token = generate_access_token(CLIENT_ID, CLIENT_SECRET, TENANT_ID)
        new_appointment = create_appointment(access_token, business_id, json.dumps(appointment_json))
        
        return jsonify(new_appointment), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Executa a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)
