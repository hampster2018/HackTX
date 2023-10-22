
class prompts:


    sentimentAnalysisConfig = {
        "choices": [
          {
            "finish_reason": "function_call",
            "index": 0,
            "message": {
              "content": None,
              "function_call": {
                "arguments": "{\n  \"location\": \"Boston, MA\"\n}",
                "name": "get_current_weather"
              },
              "role": "assistant"
            }
          }
        ],
        "created": 1694028367,
        "model": "gpt-3.5-turbo-0613",
        "object": "chat.completion",
        "usage": {
          "completion_tokens": 18,
          "prompt_tokens": 82,
          "total_tokens": 100
        }
    }