"""
Gemini Service for handling text generation using Google's Gemini API.
"""
import google.generativeai as genai
from typing import Optional
from ..config.settings import settings
import asyncio


class GeminiService:
    def __init__(self):
        """
        Initialize the Gemini client using the API key from settings.
        """
        genai.configure(api_key=settings.gemini_api_key)
        self.client = genai.GenerativeModel(settings.gemini_model)

    async def generate_text(self, prompt: str) -> str:
        """
        Generate text using the Gemini API.

        Args:
            prompt (str): The input prompt for text generation

        Returns:
            str: The generated text response

        Raises:
            Exception: If there's an error during text generation
        """
        try:
            # For async generation, we need to run the sync method in a thread pool
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(None, lambda: self.client.generate_content(prompt))

            # Extract and return the text content
            if response.candidates and len(response.candidates) > 0:
                candidate = response.candidates[0]
                if candidate.content.parts and len(candidate.content.parts) > 0:
                    # Extract text from the parts and ensure proper encoding
                    text_parts = []
                    for part in candidate.content.parts:
                        if hasattr(part, 'text') and part.text:
                            # Handle potential encoding issues by ensuring UTF-8
                            text_part = part.text.encode('utf-8', errors='ignore').decode('utf-8')
                            text_parts.append(text_part)
                    return ''.join(text_parts)
                else:
                    raise Exception("No text content returned from Gemini API")
            else:
                raise Exception("No candidates returned from Gemini API")

        except Exception as e:
            # Handle any errors that occur during generation
            # Convert error to string safely to avoid encoding issues
            error_msg = str(e).encode('utf-8', errors='ignore').decode('utf-8')
            raise Exception(f"Gemini API error: {error_msg}")