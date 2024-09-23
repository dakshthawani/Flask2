## Weather Data API

This is a user-friendly RESTful API that provides access to temperature data for a given weather station and date. Leverage this API to integrate weather information into your applications or projects.

## Features

* Retrieve temperature data for a specific station and date with ease.
* Streamline access to weather data through a clear and well-defined API endpoint.

## API Endpoints

The API currently offers one endpoint to retrieve temperature data:

* `/api/v1/<station>/<date>`:

    * **station**: Name of the weather station (replace with the desired station).
    * **date**: Date for which to retrieve temperature data (format: YYYY-MM-DD).

The endpoint returns a JSON object with the following keys:

* **station**: The name of the weather station.
* **date**: The date for which the temperature data was retrieved.
* **temp**: The temperature reading for the given station and date.

## Installation and Setup

To get started with the Weather Data API, follow these simple steps:

1. **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/weather-data-api.git](https://github.com/your-username/weather-data-api.git)
    ```
    Replace `your-username` with your actual GitHub username.

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    This command will install all the necessary libraries required for the API to function.

3. **Run the Application:**
    ```bash
    python app.py
    ```
    This will launch the API and make it accessible on your local machine.

## Usage

Once the API is running, you can use any HTTP client like `curl` or Postman to send GET requests to the API endpoint. Here's an example:
curl https://127.0.0.1:5001/api/v1/New_York/2024-09-24
This request will retrieve the temperature data for the New York station on September 24, 2024. The response will be a JSON object containing the station name, date, and temperature.

## License

This project is licensed under the MIT License. Please refer to the `LICENSE` file for details regarding the terms and conditions of use.
