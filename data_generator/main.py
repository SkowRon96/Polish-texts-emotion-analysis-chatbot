import os
import openai
import random
from csv import writer

openai.api_key = os.getenv('CHATGPT_TOKEN')

EMOTIONS = {
    "NEUTRAL":{
        "label": 0,
        "text": ["neutralną", "bez emocji"] 
    },
    "HAPPINES":{
        "label": 1,
        "text": ["wesołą", "radosną", "szczęśliwą"] 
    },
    "SADNESS":{
        "label": 2,
        "text": ["smutną", "przygnębioną", "nieszczęśliwą"] 
    },
    "FEAR":{
        "label": 3,
        "text": ["pełną strachu", "pełną obaw", "strachliwą"] 
    },
    "ANGER":{
        "label": 4,
        "text": ["gniewną", "wściekłą", "poirytowaną"] 
    },
    "DISGUST":{
        "label": 5,
        "text": ["wstrętną", "obrzydliwą", "odrażającą"] 
    },
    "SURPRISE":{
        "label": 6,
        "text": ["zaskoczoną", "osłupiałą", "zdumioną"] 
    }
}

def generate_gpt3_response(user_text, print_output=False):
    """
    Query OpenAI GPT-3 for the specific key and get back a response
    :type user_text: str the user's text to query for
    :type print_output: boolean whether or not to print the raw output JSON
    """
    completions = openai.Completion.create(
        engine='text-davinci-003',  # Determines the quality, speed, and cost.
        temperature=0.5,            # Level of creativity in the response
        prompt=user_text,           # What the user typed in
        max_tokens=300,             # Maximum tokens in the prompt AND response
        n=1,                        # The number of completions to generate
        stop=None,                  # An optional setting to control response generation
    )

    # Displaying the output can be helpful if things go wrong
    if print_output:
        print(completions)

    # Return the first choice's text
    return completions.choices[0].text

while True:
    for lenght in ['krótką', '']:
        for emotion_name, emotion in EMOTIONS.items():
            result = generate_gpt3_response(f"Wygeneruj {lenght}, {random.choice(emotion.get('text',[]))} wypowiedź człowieka, inną niż poprzednia.")
            row = [result.replace("\n",""), emotion.get('label')]
            with open('data_generator/generated_datatset.csv', 'a') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(row)
                f_object.close()

