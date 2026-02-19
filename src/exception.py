import sys
import traceback
import logging
import threading
from src.llm_service import LLMService

llm = LLMService()


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    error_message = (
        f"Error occurred in script: [{file_name}] "
        f"at line: [{line_number}] "
        f"message: [{str(error)}]"
    )

    return error_message


def async_llm_analysis(error_text: str):
    try:
        explanation = llm.explain_error(error_text)

        logging.info("🤖 LLM Suggested Fix:")
        logging.info("=" * 60)
        logging.info(explanation)
        logging.info("=" * 60)

    except Exception as e:
        logging.error("LLM analysis failed")
        logging.error(str(e))


class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        super().__init__(str(error))

        # Your original structured message
        self.error_message = error_message_detail(error, error_detail)

        # Log original message
        logging.error("🔥 Exception Captured:")
        logging.error(self.error_message)

        # Get full traceback for LLM
        full_trace = traceback.format_exc()

        # Run LLM in background thread (non-blocking)
        threading.Thread(
            target=async_llm_analysis,
            args=(full_trace,),
            daemon=True
        ).start()

    def __str__(self):
        return self.error_message
