
import requests


def generate_reply(message: str) -> str:

    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "llama3.2:latest",
        "prompt": (
            "You are Institute360's helpful chatbot. "
            "Answer users politely, clearly, and concisely. "
            "Help with admissions, courses, fees, contact details, "
            "timings, and general questions. "
            "Do not invent institute-specific information. "
            "If you do not know an official detail, ask the user "
            "to contact the institute administration.\n\n"
            f"User: {message}\n"
            "Assistant:"
        ),
        "stream": False
    }

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        result = response.json()

        return result.get(
            "response",
            "Sorry, I couldn't generate a response."
        ).strip()

    except requests.exceptions.ConnectionError:
        return (
            "Unable to connect to Ollama. "
            "Please make sure Ollama is running."
        )

    except requests.exceptions.Timeout:
        return (
            "The AI is taking too long to respond. "
            "Please try again."
        )

    except requests.exceptions.RequestException as e:
        return f"An error occurred while generating the response: {e}"
