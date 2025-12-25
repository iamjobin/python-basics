class AgentError(Exception):
    pass

class ToolError(AgentError):
    pass

class MemoryError(AgentError):
    pass

class LLMError(AgentError):
    pass
