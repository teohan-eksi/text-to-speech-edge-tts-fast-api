


# Text to Speech with Edge TTS and FastAPI

A clean and lightweight Python app built with FastAPI that accepts text, voice and file parameters and converts the text into an audio file with a given name and the voice.

## Features
* **Text-to-Speech Conversion:** Converts raw text string into high-quality audio file.
* **FastAPI Powered:** Fully asynchronous, fast, and with an automatic Swagger documentation.

## Tech Stack
* **Language:** Python 3.10+
* **Framework:** FastAPI
* **ASGI Server:** Uvicorn
* **TTS Library:** edge-tts (Microsoft Edge's text to speech service)

## Getting Started

### Prerequisites

Make sure you have Python 3.10 or higher installed.

### Installation

1. Clone the repository: <br>
   **Bash** <br>

   ```
   git clone https://github.com/teohan-eksi/text-to-speech-edge-tts-fast-api.git
   ```
   ```
   cd text-to-speech-edge-tts-fast-api
   ```
   
3. Create and activate a virtual environment: <br>
   **Bash** <br>

   ```
   python3 -m venv .
   ```
   ```
   source ./bin/activate
   ```
   ```
   python -V # to see the current Python version
   ```

4. Install the dependencies <br>
   **Bash** <br>

   ```
   pip install -r requirements.txt
   ```

### Running the Application
Start the local development server using: <br>
   **Bash** <br>
   
   ```
   fastapi dev
   ```

The server will start spinning at http://127.0.0.1:8000.

## API Documentation
Once the server is running, you can view the interactive API documentation at:

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

### Endpoint:
* Method: POST
* URL: /audio-files
* Content-Type: application/json

### Request Body Example

**JSON** <br>

```
{
    "text": "Hello world! This is a text to speech conversion test.",
    "voice": "en-US-BrianNeural",
    "audio_file_name": "output",
    "audio_file_type": "mp3"
}
```

### Response
Returns a string response as in the form of "'audio_file_name' was created."
And saves the file to the root.
