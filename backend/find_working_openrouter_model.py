#!/usr/bin/env python3
"""
Script to find and set a working OpenRouter free model automatically.
Tests multiple candidate models and updates the environment when a working one is found.
"""

import asyncio
import os
import json
from pathlib import Path
from openai import AsyncOpenAI
from dotenv import load_dotenv


async def test_openrouter_model(client: AsyncOpenAI, model_name: str) -> bool:
    """
    Test if a specific OpenRouter model is working by making a simple chat completion call.

    Args:
        client: AsyncOpenAI client configured for OpenRouter
        model_name: Name of the model to test

    Returns:
        True if the model works (returns 200), False otherwise
    """
    try:
        print(f"Testing model: {model_name}")

        # Make a simple test call to the model
        response = await client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "user", "content": "Say 'test' in one word."}
            ],
            max_tokens=10,
            temperature=0
        )

        # If we get here without exception, the model is working
        print(f"  SUCCESS: Model {model_name} is working!")
        return True

    except Exception as e:
        print(f"  ERROR: Model {model_name} failed: {str(e)}")
        return False


def update_env_file(env_path: str, new_model: str):
    """
    Update the MODEL_NAME in an environment file.

    Args:
        env_path: Path to the environment file
        new_model: New model name to set
    """
    # Read the file
    with open(env_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Update the MODEL_NAME line
    updated_lines = []
    model_found = False

    for line in lines:
        if line.strip().startswith('MODEL_NAME='):
            updated_lines.append(f'MODEL_NAME="{new_model}"\n')
            model_found = True
        else:
            updated_lines.append(line)

    # If MODEL_NAME wasn't found, add it
    if not model_found:
        updated_lines.append(f'\nMODEL_NAME="{new_model}"\n')

    # Write the updated file
    with open(env_path, 'w', encoding='utf-8') as f:
        f.writelines(updated_lines)

    print(f"  Updated {env_path} with MODEL_NAME={new_model}")


async def find_working_model():
    """
    Find a working OpenRouter free model from a list of candidates.

    Returns:
        Name of working model or None if none found
    """
    # Load environment variables
    backend_dir = Path(__file__).parent
    load_dotenv(backend_dir / ".env", override=True)

    # Get the OpenRouter API key
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
    if not openrouter_api_key:
        print("ERROR: OPENROUTER_API_KEY not found in environment!")
        return None

    # List of candidate free models to test
    # Based on OpenRouter's current free models (as of Jan 2026)
    candidate_models = [
        "google/gemma-2-9b-it:free",  # Gemma 2 9B IT (free tier)
        "microsoft/phi-3-medium-128k-instruct:free",  # Phi-3 Medium (free tier)
        "nousresearch/nous-hermes-2-mixtral-8x7b-dpo:free",  # Nous Hermes Mixtral (free tier)
        "mistralai/mistral-7b-instruct:free",  # Mistral 7B (free tier)
        "openchat/openchat-7b:free",  # OpenChat 7B (free tier)
        "microsoft/phi-3-mini-4k-instruct:free",  # Phi-3 Mini (free tier)
        "google/gemma-7b-it:free"  # Original Gemma 7B (may be deprecated)
    ]

    print("Starting OpenRouter model testing...")
    print(f"Using API key: {'*' * (len(openrouter_api_key) - 4) + openrouter_api_key[-4:]}")
    print(f"Testing {len(candidate_models)} candidate models:\n")

    # Initialize OpenRouter client
    client = AsyncOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=openrouter_api_key
    )

    # Test each model
    for model in candidate_models:
        is_working = await test_openrouter_model(client, model)
        if is_working:
            print(f"\nFOUND: Found working model: {model}")
            return model

    print("\nERROR: No working models found from the candidate list.")
    return None


async def main():
    """
    Main function to run the model finder and update environment.
    """
    print("=" * 60)
    print("OpenRouter Model Finder")
    print("=" * 60)

    # Find a working model
    working_model = await find_working_model()

    if working_model:
        # Update environment files
        backend_dir = Path(__file__).parent

        # Update main .env file
        env_path = backend_dir / ".env"
        if env_path.exists():
            update_env_file(str(env_path), working_model)
        else:
            print(f"  Warning: {env_path} does not exist")

        # Update .env.example file
        env_example_path = backend_dir / ".env.example"
        if env_example_path.exists():
            update_env_file(str(env_example_path), working_model)
        else:
            print(f"  Warning: {env_example_path} does not exist")

        print(f"\nSUCCESS: Successfully set working model: {working_model}")

        # Run the debug script to verify
        print(f"\nNow running debug_openrouter_call.py to verify the new model...")
        import subprocess
        try:
            result = subprocess.run([
                "python", "debug_openrouter_call.py"
            ], cwd=backend_dir, capture_output=True, text=True, timeout=60)

            print(f"Debug script exit code: {result.returncode}")
            print("STDOUT:", result.stdout)
            if result.stderr:
                print("STDERR:", result.stderr)

            # Save verification results
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            # Save to backend history
            backend_history_dir = backend_dir / "history" / "003-agent-retrieval"
            backend_history_dir.mkdir(parents=True, exist_ok=True)
            backend_log_path = backend_history_dir / f"model_verification_{timestamp}.log"
            with open(backend_log_path, 'w') as f:
                f.write(f"Model: {working_model}\n")
                f.write(f"Timestamp: {datetime.now()}\n")
                f.write(f"Exit code: {result.returncode}\n")
                f.write(f"STDOUT:\n{result.stdout}\n")
                if result.stderr:
                    f.write(f"STDERR:\n{result.stderr}\n")

            # Save to main history
            main_history_dir = backend_dir.parent / "history" / "003-agent-retrieval"
            main_history_dir.mkdir(parents=True, exist_ok=True)
            main_log_path = main_history_dir / f"model_verification_{timestamp}.log"
            with open(main_log_path, 'w') as f:
                f.write(f"Model: {working_model}\n")
                f.write(f"Timestamp: {datetime.now()}\n")
                f.write(f"Exit code: {result.returncode}\n")
                f.write(f"STDOUT:\n{result.stdout}\n")
                if result.stderr:
                    f.write(f"STDERR:\n{result.stderr}\n")

            print(f"Verification log saved to: {backend_log_path}")
            print(f"Verification log also saved to: {main_log_path}")

        except subprocess.TimeoutExpired:
            print("Debug script timed out after 60 seconds")
        except Exception as e:
            print(f"Error running debug script: {str(e)}")

        return True
    else:
        print("\nERROR: No working model found. Please check your OpenRouter API key or try again later.")
        return False


if __name__ == "__main__":
    success = asyncio.run(main())
    if success:
        print("\nSUCCESS: Model finding and verification completed successfully!")
    else:
        print("\nERROR: Model finding and verification failed!")
        exit(1)