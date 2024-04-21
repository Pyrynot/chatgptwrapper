**main.py**: main app

**models.py**: models

# How to run

- create .env file in the root, with the following variables:
- **API_KEY**
- **OPENAI_API_KEY**
- **OPENAI_API_URL**
  

docker build -t chatgpt .

docker run -p 80:80 chatgpt

- Not all model attributes are tested.
- Attribute stream, which uses server side events to stream the response, does not work.

Example curl to the API:

```bash
curl -X POST 'http://localhost/chat/' \
-H 'accept: application/json' \
-H 'X-API-KEY: perse' \
-H 'Content-Type: application/json' \
-d '{
  "messages": [
    {
      "role": "user",
      "content": "Tell me something interesting"
    }
  ],
  "model": "gpt-3.5-turbo"
}'
```

Example response:

```JSON
{
  "id": "chatcmpl-99cROb8UJr4sze6uUpmkIc5MXI3f4",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "message": {
        "content": "Did you know that honey never spoils? Archeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible. Honey's natural acidity and low moisture content create an inhospitable environment for bacteria and other microorganisms, making it one of the only foods that never spoils.",
        "role": "assistant",
        "function_call": null,
        "tool_calls": null
      }
    }
  ],
  "created": 1712079746,
  "model": "gpt-3.5-turbo-0125",
  "object": "chat.completion",
  "system_fingerprint": "fp_b28b39ffa8",
  "usage": {
    "completion_tokens": 69,
    "prompt_tokens": 11,
    "total_tokens": 80
  }
}
```