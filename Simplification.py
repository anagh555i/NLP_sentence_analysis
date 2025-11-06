import pandas as pd
from openai import OpenAI
import asyncio
import aiohttp
from typing import List

# Config
INPUT_FILE = 'complexSrs.csv'  
OUTPUT_FILE = 'output.csv'
LM_STUDIO_URL = 'http://localhost:1234/v1'  # Default LM Studio server
MODEL_NAME = 'local-model'  # LM Studio uses this; doesn't matter
BATCH_SIZE = 5  # Adjust based on VRAM (1-10 typical)
PROMPT_TEMPLATE = """You are a text-simplifier.  
Rewrite the following sentence in the simplest possible English.  
Return **only** the simplified sentence – no quotes, no labels, no extra words.

Sentence: {input_text}

Simplified:"""
# Initialize OpenAI-compatible client
client = OpenAI(base_url=LM_STUDIO_URL, api_key='not-needed')  # LM Studio ignores API key


async def async_completion(prompts: List[str], session: aiohttp.ClientSession) -> List[str]:
    """Async batch completion via OpenAI API."""
    tasks = []
    for prompt in prompts:
        task = asyncio.create_task(
            session.post(
                f"{LM_STUDIO_URL}/chat/completions",
                json={
                    "model": MODEL_NAME,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.1,
                    "max_tokens": 512,
                }
            )
        )
        tasks.append(task)

    responses = await asyncio.gather(*tasks)
    outputs = []
    for resp in responses:
        if resp.status == 200:
            data = await resp.json()
            outputs.append(data['choices'][0]['message']['content'].strip())
        else:
            outputs.append(f"Error: {resp.status}")
    return outputs


def process_csv():
    df = pd.read_csv(INPUT_FILE)
    results = []

    # Process in batches
    for i in range(0, len(df), BATCH_SIZE):
        batch_df = df.iloc[i:i + BATCH_SIZE]
        prompts = [PROMPT_TEMPLATE.format(input_text=row['sentence']) for _, row in
                   batch_df.iterrows()]  # Adjust column name if needed

        # Run async batch
        async def run_batch():
            async with aiohttp.ClientSession() as session:
                return await async_completion(prompts, session)

        batch_outputs = asyncio.run(run_batch())

        # Append to results
        for j, output in enumerate(batch_outputs):
            row = batch_df.iloc[j].copy()
            row['model_output'] = output
            results.append(row)

        print(f"Processed batch {i // BATCH_SIZE + 1}/{(len(df) - 1) // BATCH_SIZE + 1} ({len(results)} rows done)")

    # Save output CSV
    output_df = pd.DataFrame(results)
    output_df.to_csv(OUTPUT_FILE, index=False)
    print(f"Done! Output saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    process_csv()