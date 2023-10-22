import json
import openai
from dotenv import load_dotenv
import os

def generateUniqueQuestions():

    load_dotenv()
    openai.api_key = os.getenv("OPENAIAPIKEY")
    openai.organization = os.getenv("OPENAIORGANIZATION")   

    model = "gpt-3.5-turbo"

    messages = [
        {
            "role": "system",
            "content": "You are a function that outputs 3 unique questions to gauge how a construction worker is feeling on a specific day. Questions can span health, personal, or job related questions."
        },
    ]

    function_call = {
        "name": "DailyWellnessCheckQuestionMaker",
    }

    functions = [
        {
            "name": "DailyWellnessCheckQuestionMaker",
            "description": "Output 3 unique questions to gauge how a construction worker is feeling on a specific day. Questions can span health, personal, or job related questions.",
            "parameters": {
                "type": "object",
                "properties": {
                    "PositiveHealthQuestion": {
                        "type": "string",
                        "description": "The first question that can be asked a construction worker in the morning. The question should focus on a health related topic."
                    },
                    "PositiveHomeQuestion": {
                        "type": "string",
                        "description": "The first question that can be asked a construction worker in the morning. The question should focus on a home/personal related topic."
                    },
                    "PositiveJobQuestion": {
                        "type": "string",
                        "description": "The first question that can be asked a construction worker in the morning. The question should focus on a job related topic."
                    }
                }
            }
        }
    ]

    completion = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        function_call=function_call,
        functions=functions,
    )

    response = completion['choices'][0]['message']['function_call']['arguments']

    finalResponse = json.loads(response)

    responseList = [finalResponse['PositiveHealthQuestion'], finalResponse['PositiveHomeQuestion'], finalResponse['PositiveJobQuestion']]

    return responseList