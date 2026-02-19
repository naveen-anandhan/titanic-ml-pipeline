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
            return result

        except Exception as e:
            traceback.print_exc()
            return "LLM service temporarily unavailable."


# 🔥 create single instance
llm_service = LLMService()

# # 🔥 expose function for FastAPI
# def explain_error(error_text):
#     return llm_service.explain_error(error_text)
