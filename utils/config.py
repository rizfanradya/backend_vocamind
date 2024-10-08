from dotenv import load_dotenv
import os


load_dotenv()

ELEVENLABS_API_KEY = os.environ.get('ELEVENLABS_API_KEY')
ASSEMBLYAI_API_KEY = os.environ.get('ASSEMBLYAI_API_KEY')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
HUGGING_FACE_API_KEY = os.environ.get('HUGGING_FACE_API_KEY')
GEMINIAI_API_KEY = os.environ.get('GEMINIAI_API_KEY')

print(f'ELEVENLABS_API_KEY : {ELEVENLABS_API_KEY}')
print(f'ASSEMBLYAI_API_KEY : {ASSEMBLYAI_API_KEY}')
print(f'OPENAI_API_KEY : {OPENAI_API_KEY}')
print(f'HUGGING_FACE_API_KEY : {HUGGING_FACE_API_KEY}')
print(f'GEMINIAI_API_KEY : {GEMINIAI_API_KEY}')
