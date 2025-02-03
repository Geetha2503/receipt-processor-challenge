# Receipt Processor Service

This repository contains the solution to a task where a Receipt Processor Service is implemented. The application processes receipts and calculates points based on predefined rules.

## Features

- RESTful API built with Flask.
- Two endpoints:
  - **POST `/receipts/process`**: Processes a receipt and returns a unique receipt ID.
  - **GET `/receipts/{id}/points`**: Retrieves the points awarded for a specific receipt.
- In-memory storage for simplicity (no database required).
- Fully Dockerized for ease of setup and deployment.

---

## How to Run the Application

1. ### Run Locally (Python Installed):

   ```bash
      # Clone the repository (if applicable):
      git clone https://github.com/your-username/receipt-processor-service.git
      cd receipt-processor-service

      # Install dependencies:
      pip install -r requirements.txt

      # Start the server:
      python app.py
   ```

- The application will run on ```http://localhost:5000. ```

2. ### Run Using Docker:
   ```bash
      # Build the Docker image:
      docker build -t receipt-processor .
      # Run the Docker container:
      docker run -p 5000:5000 receipt-processor
   ```

- The application will run on ```http://localhost:5000. ```

3. ### API Endpoints: 

##### 1. POST `/receipts/process`

**Description**: Accepts a receipt JSON payload, calculates points, and returns a unique receipt ID.

**Example 1 Request**:
```json
{
    "retailer": "Target",
    "purchaseDate": "2022-01-01",
    "purchaseTime": "13:01",
    "items": [
        {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
        {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
        {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
        {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
        {"shortDescription": "Klarbrunn 12-PK 12 FL OZ", "price": "12.00"}
    ],
    "total": "35.35"
}

```

**Example 1 Response**:
```json
{
    "id": "0a8c8325-06e2-45d3-9884-5ab9e40f5222"
}
```
##### 2. GET `/receipts/{id}/points`

**Description**: Retrieves the points awarded for a specific receipt.

**Example Request**:
```json
     http://localhost:5000/receipts/0a8c8325-06e2-45d3-9884-5ab9e40f5222/points 
```

**Example Response**:
```bash
   {
    "points": 28
   }
```

**Example 2 Request**:
```json
{
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    }
  ],
  "total": "9.00"
}

```

**Example 2 Response**:
```json
{
    "id": "29d069f6-1c65-45ce-a162-87a4e03d29d0"
}
```
##### 2. GET `/receipts/{id}/points`

**Description**: Retrieves the points awarded for a specific receipt.

**Example Request**:
```json
     http://localhost:5000/receipts/29d069f6-1c65-45ce-a162-87a4e03d29d0/points 
```

**Example Response**:
```bash
   {
    "points": 109
}
```

4. ### Testing: 

Testing the Receipt Processor Service can be done effectively using any API development and testing software like Postman, a popular tool for testing API endpoints. Follow these steps to configure and use Postman for testing:

#### Using Postman

a. **Install Postman**:
   If you haven't already installed Postman, download and install it from [Postman's official site](https://www.postman.com/downloads/).

b. **Open Postman**:
   Launch Postman on your computer.

c. **Create a New Request**:
   - Click on the "New" button or the "+" tab to create a new request.
   - Set the request type to `POST` for submitting a receipt or `GET` for retrieving points.

d. **Set Up the Request for Submitting a Receipt**:
   - Enter the URL for the POST endpoint: `http://localhost:5000/receipts/process`
   - Set the method to `POST`.
   - In the Headers section, add a new header:
     - Key: `Content-Type`
     - Value: `application/json`
   - In the Body section, select `raw` and choose `JSON` from the dropdown menu that appears after selecting `raw`.
   - Paste the example JSON payload into the body area:

```json
{
    "retailer": "Target",
    "purchaseDate": "2022-01-01",
    "purchaseTime": "13:01",
    "items": [
        {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
        {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
        {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
        {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
        {"shortDescription": "Klarbrunn 12-PK 12 FL OZ", "price": "12.00"}
    ],
    "total": "35.35"
}
```
e. **Send the Request**:
   - Click the "Send" button to transmit your request to the Flask API.
   - View the response in the lower section of the Postman window. You should receive a JSON response with a unique ID.


f. **Create a New Request**:
   - Change the method to "GET".
   - Update the URL to include the ID of a processed receipt, e.g., http://localhost:5000/receipts/{id}/points, 
   replacing "{id}" with the actual receipt ID received from the POST request.
   - Send the request and you should receive the points associated with that receipt.

## Notes

- The application is designed to be stateless. Receipt data is stored in memory and will be cleared upon restarting the application.
- Ensure Docker or Python is installed before running the application.

---

## Assumptions

- Receipt validation follows the rules provided in the initial setup.
- All interactions assume JSON format for requests and responses.
