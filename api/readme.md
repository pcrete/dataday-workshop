
#### Example Usage

- **GET Request:**
    ```
    GET /calculate?ratio=16:9&value=1920
    ```

- **POST Request:**
    ```
    POST /calculate
    ```
    **Request Body:**
    ```json
    {
        "ratio": "16:9",
        "value": 1920
    }
    ```

- **Response (Success):**
    ```
    200 OK
    ```
    **Response Body:**
    ```json
    {
        "result": 1080
    }
    ```

This API allows clients to calculate the missing dimension of an image based on a desired aspect ratio and a known width or height value. It supports both GET and POST requests for flexibility.
