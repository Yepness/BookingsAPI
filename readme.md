# Business Scheduling with Microsoft Graph API

This Flask application enables the creation, listing, and retrieval of appointments for businesses using **Microsoft Bookings** via the **Microsoft Graph API**. The goal is to integrate scheduling functionalities into a system using MSAL authentication and interactions with the Microsoft Graph API.

## Features

* **List Businesses** (`GET /businesses`): Retrieves a list of all businesses configured in Microsoft Bookings.
* **List Appointments** (`GET /appointments/{business_id}`): Retrieves all appointments for a specific business identified by `business_id`.
* **Create Appointment** (`POST /appointments/{business_id}`): Creates a new appointment for a specific business. Appointment data is provided in the request body.

## Prerequisites

* **Python 3.x** installed on your system.
* **Microsoft Azure App Registration** with permissions to access the Microsoft Graph API (using `CLIENT_ID`, `CLIENT_SECRET`, and `TENANT_ID` credentials).
* **Microsoft Graph API** configured to manage Booking Businesses and Appointments.

### Dependencies

Dependencies can be installed using the following command:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should include the following dependencies:

```
Flask
requests
msal
flask-cors
python-dotenv
```

## Environment Variables

The application requires Azure credentials to be configured in the `.env` file at the project root. The `.env` file should contain the following variables:

```env
CLIENT_ID=<your_client_id>
CLIENT_SECRET=<your_client_secret>
TENANT_ID=<your_tenant_id>
```

These variables are used for authentication and authorization with the **Microsoft Graph API**.

## Running the Application

To run the application, execute the following command:

```bash
python app.py
```

The Flask server will start at `http://127.0.0.1:5000/`.

## Endpoints

### 1. **List Businesses**

* **Method**: `GET`
* **URL**: `/businesses`
* **Description**: Returns a list of businesses configured in Microsoft Bookings.
* **Example Response**:

```json
{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#solutions/bookingBusinesses",
    "value": [
        {
            "displayName": "Test",
            "id": "Test@systemautomationgroup.onmicrosoft.com"
        }
    ]
}
```

### 2. **List Appointments**

* **Method**: `GET`
* **URL**: `/appointments/{business_id}`
* **Parameter**: `business_id` (Business ID)
* **Description**: Returns all appointments for a specific business.
* **Example Response**:

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
                "emailAddress": "customer@example.com",
                "name": "Customer Name",
                "phone": "11987654321"
            },
            "staffMemberIds": ["6d8cbee8-8456-40bb-9828-5bf4d30a9aec"]
        }
    ]
}
```

### 3. **Create Appointment**

* **Method**: `POST`
* **URL**: `/appointments/{business_id}`
* **Parameter**: `business_id` (Business ID)
* **Request Body**:
  The request body must include the following data to create an appointment:

```json
{
    "start_time": "2025-01-15T10:00:00",
    "end_time": "2025-01-15T10:30:00",
    "service_id": "c2be51d6-2b2e-4709-87b2-5ce3335f1136",
    "customer_email": "customer@example.com",
    "customer_name": "Customer Name",
    "customer_phone": "11987654321",
    "staff_member_id": "6d8cbee8-8456-40bb-9828-5bf4d30a9aec"
}
```

* **Example Response**:

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
        "emailAddress": "customer@example.com",
        "name": "Customer Name",
        "phone": "11987654321"
    },
    "staffMemberIds": ["6d8cbee8-8456-40bb-9828-5bf4d30a9aec"]
}
```

## Common Errors

* **401 Unauthorized**: Verify that `CLIENT_ID`, `CLIENT_SECRET`, and `TENANT_ID` are correct and that the app has the appropriate permissions in Azure.
* **400 Bad Request**: The format of the data provided for creating an appointment may be incorrect. Check the JSON fields in the request.

## Contributions

If you want to contribute to this project, feel free to fork the repository and submit pull requests.

## License

This project is licensed under the [MIT License]
```
