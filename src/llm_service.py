from gradio_client import Client
import traceback

class LLMService:
    def __init__(self):
        try:
            self.client = Client("Naveen-anandhan/titanic-error-llm")
            print("✅ Connected to HF Space successfully")
        except Exception as e:
            print("❌ Failed to initialize LLM client")
            print(str(e))
            self.client = None

    def explain_error(self, error_text):
        if not self.client:
            return "LLM client not initialized."

        try:
            result = self.client.predict(
                error_text=error_text,
                api_name="/explain_error"
            )

            print("✅ LLM response received")
            return result

        except Exception as e:
            print("❌ Error while calling LLM:")
            print(str(e))
            traceback.print_exc()

            return "LLM service temporarily unavailable."
