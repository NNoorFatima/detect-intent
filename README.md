# Intent Detection WordPress Project

A simple intent-detection service for conversational commerce, built around a small FastAPI app and a standalone intent extractor.

## Overview

This project detects user intents from chat messages and returns a normalized JSON response. It supports common ecommerce intents such as:
- `product_search`
- `product_query`
- `add_to_cart`
- `remove_from_cart`
- `clear_cart`
- `view_cart`
- `place_order`
- `greeting`
- `thank_you`
- `confirmation`
- `decline`
- `discount_request`
- `speak_to_person`
- `option_selected`
- `unknown_intent`

Fast-path logic handles numeric selection, greetings, thank-you messages, cart actions, and prompt-injection detection. When a message is not matched by the built-in rules, the service falls back to the Groq chat completion API.

## Files

- `server.py` - FastAPI application exposing the `/detect` endpoint.
- `detect_intent.py` - Core intent detection logic.
- `api.py` - Loads the `GROQ_API_KEY` from environment variables.
- `test_intent.py` - Manual test script for `detect_intent()` behavior.
- `requirements.txt` - Python package dependencies.

## Requirements

Recommended Python packages:
- `fastapi`
- `uvicorn`
- `python-dotenv`
- `requests`
- `groq`

The included `requirements.txt` also contains `flask`, `flask-cors`, and `openai`, but the current service implementation uses FastAPI.

## Setup

1. Create and activate a Python virtual environment.

```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies.

```bash
pip install -r requirements.txt
pip install fastapi uvicorn
```

3. Create a `.env` file at the project root with your Groq API key:

```env
GROQ_API_KEY=your_real_groq_api_key_here
```

## Run the API

Start the server with:

```bash
python server.py
```

The API will be available at `http://0.0.0.0:3000`.

## API Usage

Send a POST request to `/detect` with a JSON body containing `message`.

Example using `curl`:

```bash
curl -X POST http://127.0.0.1:3000/detect \
  -H "Content-Type: application/json" \
  -d '{"message": "Add an iPhone to my cart"}'
```

Example response:

```json
{
  "intent": "add_to_cart",
  "item": "iPhone",
  "quantity": 1
}
```

## Testing

Run the manual test script:

```bash
python test_intent.py
```

This script exercises the built-in intent rules and reports pass/fail status for each case.

## Notes

- The fallback Groq API call uses `llama-3.3-70b-versatile` and returns a JSON object.
- If `GROQ_API_KEY` is missing or the request fails, the service returns `{"intent": "unknown_intent"}`.
- The project is focused on intent extraction for ecommerce-style conversations and can be extended to integrate with WordPress or other bot frameworks.
