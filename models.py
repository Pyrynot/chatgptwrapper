from pydantic import BaseModel, Json, Field
from typing import List, Optional, Dict, Any, Union

# Define data model
class ChatMessage(BaseModel):
    role: str
    content: str

class ToolFunction(BaseModel):
    name: str
    description: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None

class ToolChoice(BaseModel):
    type: str
    function: ToolFunction

# Define request body model. Note that only messages and model are necessary to call the model, all other attributes are optional.
# Not all of the attributes are tested if they work.
class ChatRequest(BaseModel):
    messages: List[ChatMessage]
    model: str
    frequency_penalty: Optional[float] = Field(default=None)
    logit_bias: Optional[Dict[int, float]] = Field(default=None)
    logprobs: Optional[bool] = Field(default=None)
    top_logprobs: Optional[int] = Field(default=None)
    max_tokens: Optional[int] = Field(default=None)
    n: Optional[int] = Field(default=None)
    presence_penalty: Optional[float] = Field(default=None)
    response_format: Optional[Dict[str, Union[str, Json[Any]]]] = Field(default=None, example={"type": "text"})
    seed: Optional[int] = Field(default=None)
    stop: Optional[Union[str, List[str]]] = Field(default=None)
    #stream: Optional[bool] = Field(default=None) can't get this to work
    temperature: Optional[float] = Field(default=None)
    top_p: Optional[float] = Field(default=None)
    tool_choice: Optional[Union[str, ToolChoice]] = Field(default=None)
    user: Optional[str] = Field(default=None)