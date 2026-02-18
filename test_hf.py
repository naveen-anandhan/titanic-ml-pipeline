from gradio_client import Client

client = Client("Naveen-anandhan/titanic-error-llm")

result = client.predict(
    error_text="ValueError: index out of range",
    api_name="/explain_error"
)

print(result)
