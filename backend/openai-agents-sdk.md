### RealtimeAgent > instructions

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/agent

The `instructions` attribute defines the agent's system prompt. It can be a static string or a dynamic function that generates instructions based on the current context and agent instance. This guides the agent's behavior and response format.

--------------------------------

### Guide > Handoffs > Creating Handoffs

Source: https://openai.github.io/openai-agents-python/realtime/guide

Handoffs allow transferring conversations between specialized agents.

--------------------------------

### ModelSettings > truncation

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

The truncation strategy to use when calling the model. See Responses API documentation for more details.

--------------------------------

### Agent Class > Constructor Arguments

Source: https://openai.github.io/openai-agents-python/ref/agent

The `Agent` constructor accepts several key arguments to customize agent behavior. `instructions` provides the core directives for the agent's operation, guiding its responses and decision-making. `tools` is a list of `Tool` objects that the agent can utilize to perform specific actions or access external information. `name` and `description` offer metadata for identifying and explaining the agent's purpose. `description_template` allows for dynamic generation of the agent's description, while `verbose` controls the level of logging output during execution. `max_tool_use_attempts` limits the number of times an agent can attempt to use a tool in a single turn.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/zh/ref/model_settings

The `reasoning` parameter allows for configuration of advanced reasoning capabilities, potentially enabling more complex problem-solving and thought processes within the model's responses. Consult the relevant documentation for detailed guidance on its usage and features.

--------------------------------

### Quickstart > Concepts

Source: https://openai.github.io/openai-agents-python/voice/quickstart

The main concept to know about is a `VoicePipeline`, which is a 3 step process:
1. Run a speech-to-text model to turn audio into text.
2. Run your code, which is usually an agentic workflow, to produce a result.
3. Run a text-to-speech model to turn the result text back into audio.

--------------------------------

### Agent Attributes

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

The `instructions` attribute defines the guiding principles for an agent's behavior. It serves as the 'system prompt' when the agent is activated, detailing its objectives and response patterns. This can be provided as a static string or a dynamic function. If a function is used, it receives the current context and the agent instance, and must return a string representing the instructions.

--------------------------------

### Next steps

Source: https://openai.github.io/openai-agents-python/realtime/quickstart

After setting up your realtime agent, there are several next steps to enhance your application. You can delve deeper into the concepts of realtime agents by learning more about their architecture and functionalities. Exploring the provided examples in the `examples/realtime` folder can offer practical insights. Integrating tools to extend the agent's capabilities, implementing seamless handoffs between different agents, and setting up guardrails for safety are also recommended for building robust applications.

--------------------------------

### Model Settings > truncation

Source: https://openai.github.io/openai-agents-python/ref/model_settings

The truncation strategy to use when calling the model. See Responses API documentation for more details.

--------------------------------

### RealtimeAgent > instructions

Source: https://openai.github.io/openai-agents-python/ref/realtime/agent

The `instructions` attribute defines the system prompt for the agent. This prompt guides the agent's behavior and response generation. It can be provided as a static string or a dynamic function that generates instructions based on the current context and agent instance. If a function is provided, it must return a string.

--------------------------------

### Agent Class Attributes > instructions

Source: https://openai.github.io/openai-agents-python/ko/ref/agent

The `instructions` attribute defines the core directives for the agent. It serves as the 'system prompt' guiding the agent's behavior and response generation. This can be provided as a simple string or as a callable function that dynamically generates instructions based on the provided context and agent instance. The callable function must return a string.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

The `reasoning` parameter is for configuring advanced reasoning capabilities. This is relevant when utilizing models designed for complex problem-solving and logical deduction, as outlined in the [reasoning models guide](https://platform.openai.com/docs/guides/reasoning).

--------------------------------

### Guide > Overview

Source: https://openai.github.io/openai-agents-python/realtime/guide

Realtime agents allow for conversational flows, processing audio and text inputs in real time and responding with realtime audio. They maintain persistent connections with OpenAI's Realtime API, enabling natural voice conversations with low latency and the ability to handle interruptions gracefully.

--------------------------------

### Agent `dataclass` > instructions

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

The `instructions` parameter defines the "system prompt" for the agent, guiding its behavior and response format. This can be provided as a static string or dynamically generated by a function that receives the current context and agent instance. The function must return a string to be used as the instructions.

--------------------------------

### Guide > Tools and Functions > Adding Tools

Source: https://openai.github.io/openai-agents-python/realtime/guide

Just like regular agents, realtime agents support function tools that execute during conversations.

--------------------------------

### Agent `dataclass`

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

The `instructions` parameter for an agent defines its core behavior, serving as the "system prompt". It dictates what the agent should accomplish and how it should formulate its responses. This can be provided as a static string or dynamically generated by a function. If a function is used, it receives the current context and the agent instance, and must return a string that will be used as the instructions. This is a crucial element for guiding the agent's actions and ensuring it aligns with the desired task.

--------------------------------

### Examples > Categories > reasoning_content

Source: https://openai.github.io/openai-agents-python/examples

Examples demonstrating how to work with reasoning content and structured outputs.

--------------------------------

### Agents > Multi-agent system design patterns > Manager (agents as tools)

Source: https://openai.github.io/openai-agents-python/agents

The `customer_facing_agent` handles all user interaction and invokes specialized sub‑agents exposed as tools. Read more in the tools documentation.

--------------------------------

### Examples

Source: https://openai.github.io/openai-agents-python/realtime/guide

For complete working examples, check out the examples/realtime directory which includes demos with and without UI components.

--------------------------------

### Function schema > FuncSchema dataclass > name instance-attribute

Source: https://openai.github.io/openai-agents-python/zh/ref/function_schema

The `name` attribute of a `FuncSchema` instance stores the name of the function as a string. This is a fundamental piece of information used to identify and invoke the function.

--------------------------------

### TranscriptionSpanData

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

Represents a Transcription Span in the trace. Includes input, output, model, and model configuration.

--------------------------------

### tracing

Source: https://openai.github.io/openai-agents-python/ko/ref/run

Tracing configuration for this run.

--------------------------------

### Running agents > Streaming

Source: https://openai.github.io/openai-agents-python/running_agents

Streaming allows you to additionally receive streaming events as the LLM runs. Once the stream is done, the `RunResultStreaming` will contain the complete information about the run, including all the new outputs produced. You can call `.stream_events()` for the streaming events. Read more in the streaming guide.

--------------------------------

### handoff_input_filter

Source: https://openai.github.io/openai-agents-python/ko/ref/run

A global input filter to apply to all handoffs. If `Handoff.input_filter` is set, then that will take precedence. The input filter allows you to edit the inputs that are sent to the new agent. See the documentation in `Handoff.input_filter` for more details.

--------------------------------

### Examples > Categories > basic

Source: https://openai.github.io/openai-agents-python/examples

These examples showcase foundational capabilities of the SDK, such as Hello world examples (Default model, GPT-5, open-weight model), Agent lifecycle management, Dynamic system prompts, Streaming outputs (text, items, function call args), Prompt templates, File handling (local and remote, images and PDFs), Usage tracking, Non-strict output types, and Previous response ID usage.

--------------------------------

### ModelSettings > reasoning

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

Configuration options for reasoning models.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

The `response_include` parameter lets you specify additional data to be included in the model's output. This can range from specific fields like `"message.output_text.logprobs"` to broader categories. Refer to the [include parameter documentation](https://platform.openai.com/docs/api-reference/responses/create#responses-create-include) for a comprehensive list of available options.

--------------------------------

### Tracing

Source: https://openai.github.io/openai-agents-python/voice/tracing

Voice pipelines are automatically traced, similar to how agents are traced. While basic tracing information is available in the general tracing documentation, you can specifically configure the tracing of a pipeline using `VoicePipelineConfig`. This configuration object allows you to manage various aspects of tracing for your voice pipelines.

--------------------------------

### Model Settings > reasoning

Source: https://openai.github.io/openai-agents-python/ref/model_settings

Configuration options for reasoning models.

--------------------------------

### trace > metadata

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

Optional dictionary of additional metadata to attach to the trace.

--------------------------------

### function_tool

Source: https://openai.github.io/openai-agents-python/ref/tool

The `function_tool` decorator offers several parameters to customize the behavior and metadata of the created tool:

*   `func`: This is the core argument, representing the Python function that you want to wrap as a tool. It can be `None` if you intend to use the decorator in a way that delays function binding.
*   `name_override`: If you wish to provide a different name for the tool than the function's actual name, you can specify it here. This is useful for clarity or to avoid naming conflicts.
*   `description_override`: This parameter allows you to provide a custom description for the tool, overriding any description that might be inferred from the function's docstring. This is helpful for providing more context or specific details about the tool's purpose.
*   `docstring_style`: You can explicitly set the style of the docstring to be parsed (e.g., Google, NumPy, reST). If left as `None`, the system will attempt to automatically detect the docstring style.
*   `use_docstring_info`: A boolean flag that, when set to `True`, instructs the decorator to use information from the function's docstring for the tool's description and argument descriptions. Setting it to `False` would prevent this automatic population.
*   `failure_error_function`: This parameter accepts a callable that will be used to generate an error message when a tool call fails. This message is then sent to the Large Language Model (LLM). If you pass `None`, the tool call will raise a standard Python exception instead of sending an error message to the LLM.
*   `strict_mode`: A boolean that enables or disables strict mode for the tool's JSON schema generation. It is strongly recommended to set this to `True` as it improves the accuracy of JSON input validation. When `False`, non-strict JSON schemas are allowed, which might make parameters with default values optional or permit additional properties, potentially leading to less predictable behavior. Refer to the OpenAI documentation on structured outputs for more details on schema behavior.
*   `is_enabled`: This parameter determines whether the tool is active and available for the agent to use. It can be a simple boolean value (`True` or `False`), or it can be a callable. If it's a callable, it should accept the run context and the agent instance, and return a boolean indicating whether the tool should be enabled in the current situation. Disabled tools are hidden from the LLM's view at runtime.
*   `tool_input_guardrails`: An optional list of guardrail objects that are executed *before* the tool is invoked. These guardrails can be used to validate or sanitize the input parameters passed to the tool.
*   `tool_output_guardrails`: Similar to input guardrails, this is an optional list of guardrails that are executed *after* the tool has returned its output. These can be used to validate or transform the tool's results before they are passed back to the agent.

--------------------------------

### Agent Class > `get_system_prompt` Method

Source: https://openai.github.io/openai-agents-python/ref/agent

The `get_system_prompt` method is designed to retrieve the system prompt for the agent. If the agent's `instructions` are provided as a string, this method directly returns them. This allows the agent to have a static, predefined system prompt that guides its overall behavior and persona.

--------------------------------

### trace_metadata

Source: https://openai.github.io/openai-agents-python/ko/ref/run

An optional dictionary of additional metadata to include with the trace.

--------------------------------

### FunctionTool `dataclass` > description `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ref/tool

The `description` attribute of a `FunctionTool` provides a textual explanation of the tool's purpose and functionality, which is presented to the LLM to aid in its decision-making process for tool selection and usage.

--------------------------------

### Structured queries > Message structure

Source: https://openai.github.io/openai-agents-python/sessions/advanced_sqlite_session

The session automatically tracks message structure, providing comprehensive data for analysis. This includes categorizing messages by their type, such as user input, assistant responses, or tool calls. For tool-related messages, the specific tool name is recorded. The system also maintains the turn number and sequence number for each message, as well as its association with a particular branch within the conversation. Timestamps are logged for each message, enabling chronological analysis of the conversation flow.

--------------------------------

### Agents > Multi-agent system design patterns > Handoffs

Source: https://openai.github.io/openai-agents-python/agents

Handoffs are sub‑agents the agent can delegate to. When a handoff occurs, the delegated agent receives the conversation history and takes over the conversation. This pattern enables modular, specialized agents that excel at a single task. Read more in the handoffs documentation.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/zh/ref/model_settings

The `ModelSettings` class holds optional model configuration parameters such as temperature, top_p, penalties, truncation, and more. It's important to note that not all models or providers support every parameter. Therefore, it is recommended to consult the API documentation for the specific model and provider you are utilizing to ensure compatibility and proper usage of these settings.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/zh/ref/model_settings

The `truncation` parameter dictates how the model handles input that exceeds its maximum token limit. Options typically include an `auto` strategy, which attempts to manage truncation intelligently, or `disabled`, which prevents truncation. Refer to the specific API documentation for detailed behavior.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ko/ref/model_settings

The `ModelSettings` class holds optional model configuration parameters such as temperature, top_p, penalties, and truncation. It's important to note that not all models or providers support all of these parameters. Therefore, you should consult the API documentation for the specific model and provider you are utilizing to ensure compatibility and understand available options.

--------------------------------

### Trace with metadata and grouping

Source: https://openai.github.io/openai-agents-python/ref/tracing

The `Trace` class provides several key methods and properties. The `__enter__` and `__exit__` methods enable its use as a context manager for reliable resource handling. `start()` initializes the trace and can optionally mark it as the current trace, which is necessary before adding any spans. `finish()` completes the trace, finalizing all open spans. The `trace_id` property provides a unique identifier for the trace, useful for linking spans and looking up traces in a dashboard. The `name` property offers a human-readable workflow name.

--------------------------------

### Agent Attributes > instructions

Source: https://openai.github.io/openai-agents-python/ref/agent

The `instructions` attribute defines the core behavior of an agent. It can be set as a static string, acting as a system prompt, or as a callable function. If a function is provided, it will be executed with the current `run_context` and the `agent` instance itself, allowing for dynamic instruction generation based on runtime conditions. The function must return a string, which will then be used to guide the agent's responses.

--------------------------------

### Guide > Architecture > Core Components

Source: https://openai.github.io/openai-agents-python/realtime/guide

The realtime system consists of several key components: **RealtimeAgent**: An agent, configured with instructions, tools and handoffs. **RealtimeRunner**: Manages configuration. You can call `runner.run()` to get a session. **RealtimeSession**: A single interaction session. You typically create one each time a user starts a conversation, and keep it alive until the conversation is done. **RealtimeModel**: The underlying model interface (typically OpenAI's WebSocket implementation)

--------------------------------

### Examples > Categories > tools

Source: https://openai.github.io/openai-agents-python/examples

Learn how to implement OAI hosted tools such as: Web search and web search with filters, File search, Code interpreter, Computer use, and Image generation.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ref/model_settings

The `ModelSettings` class holds optional model configuration parameters such as temperature, top_p, penalties, and truncation. It's important to note that not all models or providers support every parameter. Therefore, it's recommended to consult the API documentation for the specific model and provider you are using to ensure compatibility and proper usage of these settings.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

The `ModelSettings` class holds optional model configuration parameters such as temperature, top_p, penalties, and truncation. It's important to note that not all models or providers support every parameter. Therefore, you should consult the API documentation for the specific model and provider you are using to confirm compatibility and understand the available options.

--------------------------------

### Handoff dataclass > tool_description instance-attribute

Source: https://openai.github.io/openai-agents-python/ja/ref/handoffs

The description of the tool that represents the handoff.

--------------------------------

### Span

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

Base class for representing traceable operations with timing and context. A span represents a single operation within a trace (e.g., an LLM call, tool execution, or agent run). Spans track timing, relationships between operations, and operation-specific data.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/zh/ref/model_settings

The `prompt_cache_retention` setting influences how long prompts are cached. Setting it to `24h` enables extended prompt caching, keeping cached prefixes active for up to 24 hours, which can improve performance for repeated or similar prompts. Refer to the prompt caching documentation for more details.

--------------------------------

### Examples > Categories > customer_service

Source: https://openai.github.io/openai-agents-python/examples

An example customer service system for an airline.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

The `truncation` parameter manages how the model handles input that exceeds its maximum token limit. Options include `'auto'`, which attempts to intelligently truncate the input, and `'disabled'`, which prevents truncation. For more details, refer to the [Responses API documentation](https://platform.openai.com/docs/api-reference/responses/create#responses_create-truncation).

--------------------------------

### SpeechSpanData

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

Represents a Speech Span in the trace. Includes input, output, model, model configuration, and first content timestamp.

--------------------------------

### Spans > Trace

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

A complete end-to-end workflow containing related spans and metadata. A trace represents a logical workflow or operation (e.g., "Customer Service Query" or "Code Generation") and contains all the spans (individual operations) that occur during that workflow.

--------------------------------

### openai-agents-python/span_data.py > Span

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

The `Span` class serves as the abstract base class for all traceable operations. It provides the fundamental structure for representing a single operation within a trace, encompassing timing information, the hierarchical relationships between operations, and any operation-specific data. Examples of spans include LLM calls, tool executions, or agent runs. The `Span` class facilitates the creation of custom spans using context managers, allowing developers to easily instrument their code for monitoring and debugging.

--------------------------------

### Quickstart

Source: https://openai.github.io/openai-agents-python/realtime/quickstart

Realtime agents enable voice conversations with your AI agents using OpenAI's Realtime API. This guide walks you through creating your first realtime voice agent. Note that realtime agents are currently a beta feature, and users should expect potential breaking changes as the implementation is refined.

--------------------------------

### ModelSettings > metadata

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

Metadata to include with the model response call.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

`prompt_cache_retention` influences how long prompt caching is maintained. Setting this to `'24h'` enables extended prompt caching, keeping cached information active for up to 24 hours, which can improve performance on repeated queries. Learn more about this feature in the [prompt caching guide](https://platform.openai.com/docs/guides/prompt-caching#prompt-cache-retention).

--------------------------------

### OpenAI Agents Python/realtime/config.py/Tracing Configuration/metadata

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/config

The `metadata` is an instance attribute that allows for the inclusion of additional metadata with a trace. This can be any dictionary of key-value pairs that provides extra context or information relevant to the trace, enhancing its utility for debugging and analysis.

--------------------------------

### Trace

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

A trace represents a logical workflow or operation (e.g., "Customer Service Query" or "Code Generation") and contains all the spans (individual operations) that occur during that workflow.

**Basic trace usage**
```python
with trace("Order Processing") as t:
    validation_result = await Runner.run(validator, order_data)
    if validation_result.approved:
        await Runner.run(processor, order_data)
```

**Trace with metadata and grouping**
```python
with trace(
    "Customer Service",
    group_id="chat_123",
    metadata={"customer": "user_456"}
) as t:
    result = await Runner.run(support_agent, query)
```

Notes:
- Use descriptive workflow names
- Group related traces with consistent group_ids
- Add relevant metadata for filtering/analysis
- Use context managers for reliable cleanup
- Consider privacy when adding trace data

--------------------------------

### Handoff dataclass > tool_description instance-attribute

Source: https://openai.github.io/openai-agents-python/ref/handoffs

The `tool_description` attribute provides a human-readable description for the handoff tool. This description explains the purpose of the handoff, including which agent the task is being transferred to and any specific capabilities of that agent, aiding in clarity and discoverability.

--------------------------------

### Examples > Categories > hosted_mcp

Source: https://openai.github.io/openai-agents-python/examples

Examples demonstrating how to use hosted MCP (Model Context Protocol) connectors and approvals.

--------------------------------

### Agent Attributes > tools

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

A list containing the tools that the agent is permitted to utilize during its operations.

--------------------------------

### openai-agents-python/src/agents/realtime/config.py > Tracing Configuration > metadata

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/config

Additional metadata to include with the trace.

--------------------------------

### 4. stdio MCP servers

Source: https://openai.github.io/openai-agents-python/mcp

For MCP servers that run as local subprocesses, use `MCPServerStdio`. The SDK spawns the process, keeps the pipes open, and closes them automatically when the context manager exits. This option is helpful for quick proofs of concept or when the server only exposes a command line entry point.

--------------------------------

### Trace with metadata and grouping

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

The `Trace` class provides an abstract interface for managing tracing operations. It includes methods for starting (`start`) and finishing (`finish`) a trace, which can optionally manage the current execution context. The `trace_id` property provides a globally unique identifier for the trace, essential for linking spans and looking up traces in a dashboard. The `name` property offers a human-readable description of the workflow, useful for grouping and filtering. The `export` method allows for serializing trace data, including spans and metadata, for transmission to backend systems, while `tracing_api_key` specifies the key for exporting.

--------------------------------

### Trace with metadata and grouping

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/traces

When using the `trace` context manager, it is recommended to follow several best practices to ensure effective tracing. Always use descriptive names for your workflows to make them easily understandable. Grouping related traces with consistent `group_ids` facilitates the aggregation and analysis of similar operations. Adding relevant `metadata` is crucial for filtering traces based on specific attributes, which aids in debugging and performance monitoring. Utilizing context managers ensures reliable cleanup of tracing resources. Additionally, it is essential to consider privacy implications when adding any trace data, especially sensitive information.

--------------------------------

### Guide > Architecture > Session flow

Source: https://openai.github.io/openai-agents-python/realtime/guide

A typical realtime session follows this flow: 1. **Create your RealtimeAgent(s)** with instructions, tools and handoffs. 2. **Set up a RealtimeRunner** with the agent and configuration options 3. **Start the session** using `await runner.run()` which returns a RealtimeSession. 4. **Send audio or text messages** to the session using `send_audio()` or `send_message()` 5. **Listen for events** by iterating over the session - events include audio output, transcripts, tool calls, handoffs, and errors 6. **Handle interruptions** when users speak over the agent, which automatically stops current audio generation. The session maintains the conversation history and manages the persistent connection with the realtime model.

--------------------------------

### Guide > Session configuration > Model settings

Source: https://openai.github.io/openai-agents-python/realtime/guide

The session configuration allows you to control the underlying realtime model behavior. You can configure the model name (such as `gpt-realtime`), voice selection (alloy, echo, fable, onyx, nova, shimmer), and supported modalities (text and/or audio). Audio formats can be set for both input and output, with PCM16 being the default.

--------------------------------

### MCPServerStdio

Source: https://openai.github.io/openai-agents-python/ja/ref/mcp/server

The `MCPServerStdio` class is an implementation of the MCP (Model Context Protocol) server that utilizes the stdio (standard input/output) transport mechanism. This means that communication between the client and the server occurs through the standard input and output streams of a process. For detailed information about the stdio transport specification, you can refer to the official Model Context Protocol documentation.

--------------------------------

### Trace with metadata and grouping

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/traces

A trace represents a logical workflow or operation (e.g., "Customer Service Query" or "Code Generation") and contains all the spans (individual operations) that occur during that workflow. You can use the `trace` context manager to instrument your code. For example, a basic trace can be created with `with trace("Order Processing") as t:`, where `t` can be used to manage the trace. For more advanced usage, you can include a `group_id` to group related traces and `metadata` (a dictionary) for filtering and analysis, as shown in `with trace("Customer Service", group_id="chat_123", metadata={"customer": "user_456"}) as t:`.

--------------------------------

### Examples > Categories > realtime

Source: https://openai.github.io/openai-agents-python/examples

Examples showing how to build real-time experiences using the SDK, including: Web applications, Command-line interfaces, and Twilio integration.

--------------------------------

### LitellmModel

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/litellm

The `LitellmModel` class is designed to integrate with any language model that is compatible with the LiteLLM library. LiteLLM acts as a universal interface, allowing you to interact with a wide array of LLM providers, including OpenAI, Anthropic, Gemini, Mistral, and many others. This abstraction simplifies the process of switching between different models or leveraging diverse LLM capabilities within your application without significant code changes. You can find a comprehensive list of supported models and providers in the [LiteLLM documentation](https://docs.litellm.ai/docs/providers).

--------------------------------

### Using any model via LiteLLM > Example

Source: https://openai.github.io/openai-agents-python/models/litellm

When using `LitellmModel`, you will be prompted to provide the specific model name and its corresponding API key. For instance, you can specify models like `openai/gpt-4.1` with your OpenAI API key, or `anthropic/claude-3-5-sonnet-20240620` with your Anthropic API key, among many others. A comprehensive list of models supported by LiteLLM can be found in the official LiteLLM providers documentation.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/zh/ref/model_settings

The `metadata` field allows you to include custom key-value string pairs with your model request. This can be useful for tracking or categorizing calls.

--------------------------------

### OpenAI Agents Python > Guardrails

Source: https://openai.github.io/openai-agents-python/agents

Guardrails enable you to perform checks and validations on both user input and the agent's output. These validations run in parallel with the agent's execution. For instance, you can screen both the user's input and the agent's output to ensure relevance. Further details can be found in the dedicated guardrails documentation.

--------------------------------

### Handoff dataclass > tool_description instance-attribute

Source: https://openai.github.io/openai-agents-python/zh/ref/handoffs

The `tool_description` provides a human-readable and machine-understandable explanation of what the handoff tool does. This description is vital for the language model to accurately comprehend the purpose of the handoff and when it should be invoked. It typically includes the name of the agent being handed off to and potentially a brief explanation of that agent's specialized function, drawing from the `handoff_description` of the target agent.

--------------------------------

### Guide > Session configuration > Audio configuration

Source: https://openai.github.io/openai-agents-python/realtime/guide

Audio settings control how the session handles voice input and output. You can configure input audio transcription using models like Whisper, set language preferences, and provide transcription prompts to improve accuracy for domain-specific terms. Turn detection settings control when the agent should start and stop responding, with options for voice activity detection thresholds, silence duration, and padding around detected speech.

--------------------------------

### Guide > Agent configuration

Source: https://openai.github.io/openai-agents-python/realtime/guide

RealtimeAgent works similarly to the regular Agent class with some key differences. Key differences from regular agents: Model choice is configured at the session level, not the agent level. No structured output support (`outputType` is not supported). Voice can be configured per agent but cannot be changed after the first agent speaks. All other features like tools, handoffs, and instructions work the same way.

--------------------------------

### MCPServerStreamableHttp

Source: https://openai.github.io/openai-agents-python/zh/ref/mcp/server

The `MCPServerStreamableHttp` class is an implementation of the MCP server that utilizes the Streamable HTTP transport mechanism. This class inherits from `_MCPServerWithClientSession` and is designed to facilitate communication using the Streamable HTTP protocol. For detailed specifications and understanding of this transport, refer to the official documentation at https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http. The source code for this implementation can be found in `src/agents/mcp/server.py`.

--------------------------------

### Model Settings > metadata

Source: https://openai.github.io/openai-agents-python/ref/model_settings

Metadata to include with the model response call.

--------------------------------

### Usage

Source: https://openai.github.io/openai-agents-python/ref/usage

The `Usage` dataclass is designed to meticulously track token consumption and API requests within the OpenAI agents Python library. It aggregates total requests, input tokens, and output tokens, providing a comprehensive overview of resource utilization. The class also distinguishes between cached and reasoning tokens for input and output respectively, offering granular insights into how tokens are being processed. Furthermore, it maintains a list of `RequestUsage` entries, which is crucial for accurate per-request cost calculations and for understanding the breakdown of token usage across individual API calls. This detailed tracking is essential for cost management and performance optimization.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ko/ref/model_settings

The `ModelSettings` class supports advanced features like `truncation` strategies, which can be set to 'auto' or 'disabled' to manage response length according to the [Responses API documentation](https://platform.openai.com/docs/api-reference/responses/create#responses_create-truncation). It also allows for setting `max_tokens` to limit the output size and configuring `reasoning` models for more complex problem-solving. For controlling the verbosity of the model's output, a `verbosity` parameter can be set to 'low', 'medium', or 'high'.

--------------------------------

### ToolOutputFileContent

Source: https://openai.github.io/openai-agents-python/ref/tool

Represents a tool output that should be sent to the model as a file. Provide one of `file_data` (base64), `file_url`, or `file_id`. You may also provide an optional `filename` when using `file_data` to hint file name.

--------------------------------

### MCP Servers > MCPServer

Source: https://openai.github.io/openai-agents-python/ja/ref/mcp/server

The `MCPServer` class serves as the base class for all Model Context Protocol (MCP) servers. It defines the fundamental interface that MCP servers must adhere to, ensuring a consistent way to interact with different server implementations. This class is abstract, meaning it cannot be instantiated directly and requires subclasses to implement its abstract methods. These methods cover essential server operations such as connecting to the server, cleaning up resources, listing available tools and prompts, and calling tools or retrieving specific prompts. The `__init__` method includes an option `use_structured_content` to control whether structured content from tool results should be prioritized, which is useful for backward compatibility and avoiding duplicate information.

--------------------------------

### openai-agents-python/function_schema.py > FuncDocumentation

Source: https://openai.github.io/openai-agents-python/ref/function_schema

The `FuncDocumentation` dataclass is designed to hold metadata pertaining to a Python function, extracted from its docstring. It stores the function's `name` (obtained from `__name__`), its `description` (derived from the docstring's main body), and a dictionary of `param_descriptions` that map parameter names to their respective descriptions found within the docstring.

--------------------------------

### Trace with metadata and grouping > Trace

Source: https://openai.github.io/openai-agents-python/ref/tracing/traces

The `Trace` class provides several key methods and properties for managing traces. The `__enter__` and `__exit__` methods enable its use as a context manager for reliable cleanup. `start()` initiates the trace and can optionally mark it as the current trace, which must be called before adding any spans. `finish()` completes the trace, finalizing all open spans, and can optionally reset the current trace. The `trace_id` property returns a unique identifier for the trace, useful for linking spans and looking up traces in a dashboard. The `name` property provides the human-readable workflow name, which aids in grouping and filtering. Finally, `export()` allows for the trace data, including spans and metadata, to be serialized into a dictionary for backend transmission, and `tracing_api_key` provides the API key for exporting this trace and its spans.

--------------------------------

### openai_agents_python > __init__

Source: https://openai.github.io/openai-agents-python/zh/ref/models/multi_provider

Create a new OpenAI provider.

Parameters:
`provider_map`: A MultiProviderMap that maps prefixes to ModelProviders. If not provided, we will use a default mapping. See the documentation for this class to see the default mapping.
`openai_api_key`: The API key to use for the OpenAI provider. If not provided, we will use the default API key.
`openai_base_url`: The base URL to use for the OpenAI provider. If not provided, we will use the default base URL.
`openai_client`: An optional OpenAI client to use. If not provided, we will create a new OpenAI client using the api_key and base_url.
`openai_organization`: The organization to use for the OpenAI provider.
`openai_project`: The project to use for the OpenAI provider.
`openai_use_responses`: Whether to use the OpenAI responses API.

--------------------------------

### Agent Attributes > handoff_description

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

This description is utilized when the agent is employed as a handoff mechanism. It provides an LLM with information about the agent's purpose and the conditions under which it should be invoked.

--------------------------------

### function_tool

Source: https://openai.github.io/openai-agents-python/zh/ref/tool

The `function_tool` decorator is used to transform a Python function into a tool that can be utilized by an agent. When you decorate a function with `function_tool`, it automatically handles several tasks to make your function compatible with the agent's tool-use system. Firstly, it inspects the function's signature to generate a JSON schema that defines the expected input parameters for the tool. This schema is crucial for the agent to understand how to call your function correctly. Secondly, it leverages the function's docstring to provide a description for the tool. This means that a well-written docstring can serve both as documentation for developers and as explanatory information for the agent. Furthermore, it can also use the docstring to describe the individual arguments of the function. The decorator attempts to auto-detect the style of your docstring (e.g., reST, Google, NumPy), but you have the option to explicitly specify the style if needed. An important consideration is that if your function is designed to accept a `RunContextWrapper` as its first argument, this context object must be compatible with the specific type of agent that will be using the tool. This ensures that the agent can properly pass its runtime context to your tool function.

--------------------------------

### Agent Attributes > tools

Source: https://openai.github.io/openai-agents-python/ref/agent

This attribute is a list containing the tools that the agent is capable of using.

--------------------------------

### Agent Attributes > handoff_description

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

This optional string attribute provides a description for the agent. It's particularly useful when the agent is employed as a 'handoff' mechanism, allowing a larger LLM to understand the agent's capabilities and determine the appropriate time to invoke it.

--------------------------------

### MCPServerSse

Source: https://openai.github.io/openai-agents-python/zh/ref/mcp/server

The `MCPServerSse` class is an implementation of the MCP server that utilizes the HTTP with Server-Sent Events (SSE) transport protocol. This class is designed to facilitate communication between an MCP server and its clients over an HTTP connection, with SSE enabling real-time updates from the server to the client. For detailed specifications on this transport mechanism, refer to the [official documentation](https://spec.modelcontextprotocol.io/specification/2024-11-05/basic/transports/#http-with-sse). The source code for this implementation can be found in the `src/agents/mcp/server.py` file.

--------------------------------

### RealtimeAgent > prompt

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/agent

The `prompt` attribute allows for dynamic configuration of an agent's instructions, tools, and other settings outside of the code. This feature is exclusively available for OpenAI models.

--------------------------------

### Model > TTSModelSettings

Source: https://openai.github.io/openai-agents-python/ja/ref/voice/model

The `TTSModelSettings` dataclass is used to configure the settings for a Text-to-Speech (TTS) model. It allows specifying the `voice` to be used, with a default voice being employed if none is explicitly provided. The `buffer_size` determines the minimal size of audio data chunks for streaming, and `dtype` specifies the data type for the returned audio data, defaulting to `np.int16`. Additionally, a `transform_data` function can be supplied to modify the audio data shape, and `instructions` can guide the tone and output style of the TTS model. For custom text segmentation, a `text_splitter` function can be provided, and the `speed` attribute controls the reading rate, ranging from 0.25 to 4.0.

--------------------------------

### Tracing > Traces and spans

Source: https://openai.github.io/openai-agents-python/tracing

**Traces** represent a single end-to-end operation of a "workflow". They're composed of Spans. Traces have the following properties: `workflow_name`: This is the logical workflow or app. For example "Code generation" or "Customer service". `trace_id`: A unique ID for the trace. Automatically generated if you don't pass one. Must have the format `trace_<32_alphanumeric>`. `group_id`: Optional group ID, to link multiple traces from the same conversation. For example, you might use a chat thread ID. `disabled`: If True, the trace will not be recorded. `metadata`: Optional metadata for the trace. **Spans** represent operations that have a start and end time. Spans have: `started_at` and `ended_at` timestamps. `trace_id`, to represent the trace they belong to `parent_id`, which points to the parent Span of this Span (if any) `span_data`, which is information about the Span. For example, `AgentSpanData` contains information about the Agent, `GenerationSpanData` contains information about the LLM generation, etc.

--------------------------------

### workflow_name

Source: https://openai.github.io/openai-agents-python/ko/ref/run

The name of the run, used for tracing. Should be a logical name for the run, like "Code generation workflow" or "Customer support agent".

--------------------------------

### MCPServerStreamableHttp

Source: https://openai.github.io/openai-agents-python/ko/ref/mcp/server

The `MCPServerStreamableHttp` class is an implementation of the MCP server that utilizes the Streamable HTTP transport. This transport mechanism is designed for efficient, real-time communication, allowing for the streaming of messages between the client and server. The class inherits from `_MCPServerWithClientSession`, indicating that it manages client sessions and integrates with the MCP protocol's session management features. For detailed specifications on the Streamable HTTP transport, refer to the official documentation at https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http.

--------------------------------

### Trace with metadata and grouping > Trace

Source: https://openai.github.io/openai-agents-python/ref/tracing/traces

When initiating a trace, you can provide a descriptive workflow name, a `group_id` to associate related traces, and arbitrary `metadata` as a dictionary for enhanced filtering and analysis. For example, `with trace("Customer Service", group_id="chat_123", metadata={"customer": "user_456"}) as t:` creates a trace for customer service interactions, groups it under `chat_123`, and includes specific customer information in the metadata.

--------------------------------

### Agent Attributes > instructions

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

The instructions for the agent. Will be used as the "system prompt" when this agent is invoked. Describes what the agent should do, and how it responds. Can either be a string, or a function that dynamically generates instructions for the agent. If you provide a function, it will be called with the context and the agent instance. It must return a string.

--------------------------------

### Trace with metadata and grouping

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/traces

A trace represents a complete end-to-end workflow, encompassing all related spans and metadata. It signifies a logical operation, such as a 'Customer Service Query' or 'Code Generation', and aggregates all the individual operations (spans) performed during that workflow. The `trace` function, used as a context manager, allows you to define these workflows. You can provide a descriptive name for the trace, and optionally group related traces using a `group_id` and add relevant `metadata` for easier filtering and analysis. For instance, a customer service interaction can be traced with a specific `group_id` like 'chat_123' and metadata such as `{"customer": "user_456"}` to identify the user involved.

--------------------------------

### Model > TTSModelSettings

Source: https://openai.github.io/openai-agents-python/ref/voice/model

TTSModelSettings is a dataclass that holds the configuration for a TTS model. It includes settings such as the voice to be used, the buffer size for audio chunks, the data type for audio output, a function to transform the audio data, instructions for the TTS model's behavior, a text splitter function, and the desired speech speed. The `voice` attribute allows selection from predefined TTSVoice options, defaulting to the model's default if not specified. `buffer_size` determines the minimal size of streamed audio data chunks. `dtype` sets the audio data type, defaulting to np.int16. `transform_data` is an optional callable for custom audio data manipulation. `instructions` can guide the tone and delivery of the audio output. `text_splitter` is a function for segmenting input text before processing, and `speed` controls the playback rate between 0.25 and 4.0.

--------------------------------

### Tools > Tool

Source: https://openai.github.io/openai-agents-python/zh/ref/tool

A tool that can be used in an agent.

--------------------------------

### Trace with metadata and grouping

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

A trace represents a complete end-to-end workflow, encompassing all related spans and metadata. It signifies a logical operation, such as a "Customer Service Query" or "Code Generation," and aggregates all the individual operations (spans) performed during that workflow.

For example, a basic trace can be initiated using a context manager for operations like order processing:
```python
with trace("Order Processing") as t:
    validation_result = await Runner.run(validator, order_data)
    if validation_result.approved:
        await Runner.run(processor, order_data)
```

Traces can also be enhanced with metadata and grouping for better organization and analysis. This involves providing a `group_id` to link related traces and a `metadata` dictionary for specific details:
```python
with trace(
    "Customer Service",
    group_id="chat_123",
    metadata={"customer": "user_456"}
) as t:
    result = await Runner.run(support_agent, query)
```

Key recommendations for effective tracing include using descriptive names for workflows, assigning consistent `group_id`s to related traces, and adding relevant metadata for filtering and analysis. It's also important to utilize context managers for reliable cleanup and to consider privacy implications when including trace data.

--------------------------------

### RealtimeAgent > prompt

Source: https://openai.github.io/openai-agents-python/ref/realtime/agent

The `prompt` parameter allows for external configuration of an agent's instructions, tools, and other settings, making it particularly useful for OpenAI models. This feature enables developers to manage agent behavior outside of their core code, offering a more modular approach to agent design.

--------------------------------

### Agent Attributes > handoff_description

Source: https://openai.github.io/openai-agents-python/ref/agent

This attribute provides a description for the agent. It's utilized when the agent functions as a handoff, enabling an LLM to understand its purpose and determine when to invoke it.

--------------------------------

### Agent Attributes > tools

Source: https://openai.github.io/openai-agents-python/ko/ref/agent

This attribute holds a list of `Tool` objects that the agent is configured to use. These tools represent the functionalities the agent can access and leverage during its operation.

--------------------------------

### Agent Attributes > tools

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

This attribute holds a list of `Tool` objects that the agent is equipped to use. These tools represent specific functions or capabilities that the agent can leverage to accomplish its tasks.

--------------------------------

Source: https://openai.github.io/openai-agents-python/zh/ref/extensions/litellm

--------------------------------

### ComputerProvider

Source: https://openai.github.io/openai-agents-python/ref/tool

Configures create/dispose hooks for per-run computer lifecycle management.

--------------------------------

### Trace with metadata and grouping

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/traces

A trace represents a logical workflow or operation (e.g., "Customer Service Query" or "Code Generation") and contains all the spans (individual operations) that occur during that workflow. It's essential for organizing and understanding the flow of complex processes. For example, in customer service scenarios, a trace can encapsulate the entire interaction from receiving a query to providing a response. Similarly, in code generation, a trace can cover the steps from prompt input to final code output.

--------------------------------

### Agent Attributes > handoff_description

Source: https://openai.github.io/openai-agents-python/ko/ref/agent

This optional string attribute provides a description for the agent. It is particularly useful when the agent is intended to be used as a 'handoff', allowing another LLM to understand the agent's purpose and determine when it should be invoked.

--------------------------------

### Database schema > message_structure table

Source: https://openai.github.io/openai-agents-python/sessions/advanced_sqlite_session

The `message_structure` table is crucial for understanding the detailed composition of a conversation. It records each message's unique identifier, its association with a session and branch, its type (e.g., user, assistant, tool_call), its position in the sequence, and the turn it belongs to within a user's interaction or a specific branch. It also logs any tool names used in tool calls, the timestamp of creation, and foreign key relationships to the `agent_sessions` and `agent_messages` tables, ensuring data integrity.

--------------------------------

### FunctionToolResult > tool

Source: https://openai.github.io/openai-agents-python/ref/tool

The tool that was run.

--------------------------------

### Span

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

A span represents a single operation within a trace (e.g., an LLM call, tool execution, or agent run). Spans track timing, relationships between operations, and operation-specific data.

**Notes:**
- Spans automatically nest under the current trace
- Use context managers for reliable start/finish
- Include relevant data but avoid sensitive information
- Handle errors properly using `set_error()`

--------------------------------

### Context management

Source: https://openai.github.io/openai-agents-python/context

Context in this library refers to two main categories: 
1. **Local Context**: Data and dependencies accessible within your code, such as for tool functions, callbacks (`on_handoff`), and lifecycle hooks. 
2. **LLM Context**: Data that the Language Model (LLM) receives to generate a response.

This distinction is crucial for understanding how data flows and is utilized within the agent system.

--------------------------------

### Database schema

Source: https://openai.github.io/openai-agents-python/sessions/advanced_sqlite_session

The `AdvancedSQLiteSession` class provides enhanced functionality for managing and analyzing conversations. It extends the basic SQLite schema with two additional tables: `message_structure` and `turn_usage`. The `message_structure` table stores detailed information about each message, including its type, sequence number, turn and branch associations, tool usage, and timestamps. The `turn_usage` table tracks the usage statistics for each turn within a session and branch, recording the number of requests, input/output/total tokens, and detailed token breakdown.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

The `metadata` field allows you to attach custom key-value string pairs to the model's response call. This can be useful for tracking or categorizing requests.

--------------------------------

### Quickstart > Put it all together

Source: https://openai.github.io/openai-agents-python/voice/quickstart

This is a complete example combining all the previous steps. It includes setting up two agents (one for general assistance and one for Spanish), defining a weather tool, initializing a `VoicePipeline` with a `SingleAgentVoiceWorkflow`, and running the pipeline with sample audio input. The output audio is then played back.

--------------------------------

### RealtimeAgent > prompt

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/agent

The `prompt` attribute allows for the dynamic configuration of an agent's instructions, tools, and other settings outside of the direct code. This feature is exclusively available for use with OpenAI models.

--------------------------------

### Agent `dataclass` > prompt

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

The `prompt` parameter allows for dynamic configuration of an agent's instructions, tools, and other settings outside of the core code. This feature is specifically designed for use with OpenAI models via the Responses API, enabling flexible prompt management.

--------------------------------

### Examples > Categories > handoffs

Source: https://openai.github.io/openai-agents-python/examples

See practical examples of agent handoffs with message filtering.

--------------------------------

### Span > start

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/spans

The `start()` method begins the execution of the span. It can optionally mark the span as the current span in the trace.

--------------------------------

### Trace with metadata and grouping

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/traces

When using traces, it's recommended to follow several best practices for effective instrumentation. Use descriptive workflow names to clearly indicate the purpose of the trace. Group related traces together by using consistent `group_ids`, which helps in organizing and querying traces later. Add relevant `metadata` to traces to enable filtering and analysis based on specific attributes, such as user IDs or session information. Always use context managers (like `with trace(...)`) for reliable cleanup of trace resources. Finally, consider privacy implications when adding trace data, ensuring sensitive information is not inadvertently logged.

--------------------------------

### Workflow > VoiceWorkflowBase > on_start

Source: https://openai.github.io/openai-agents-python/ko/ref/voice/workflow

Optional method that runs before any user input is received. Can be used to deliver a greeting or instruction via TTS. Defaults to doing nothing.

--------------------------------

### ModelSettings > tool_choice

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

The tool choice to use when calling the model.

--------------------------------

### AdvancedSQLiteSession > _init_structure_tables

Source: https://openai.github.io/openai-agents-python/ko/ref/extensions/memory/advanced_sqlite_session

The `_init_structure_tables` method is responsible for setting up the database schema required for advanced features like conversation branching and usage tracking. It creates two essential tables: `message_structure` and `turn_usage`. The `message_structure` table stores information about each message, including its association with a specific `branch_id`, allowing for the reconstruction of conversation histories along different branches. The `turn_usage` table logs detailed usage statistics for each turn within a conversation, including token counts (both total and detailed breakdowns) and the number of requests made. Appropriate foreign key constraints and indexes are established to ensure data integrity and efficient querying.

--------------------------------

### spans.py > Trace

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

A complete end-to-end workflow containing related spans and metadata.
A trace represents a logical workflow or operation (e.g., "Customer Service Query" or "Code Generation") and contains all the spans (individual operations) that occur during that workflow.
Example
```
# Basic trace usage
with trace("Order Processing") as t:
    validation_result = await Runner.run(validator, order_data)
    if validation_result.approved:
        await Runner.run(processor, order_data)
```

--------------------------------

### RealtimeAgent > prompt

Source: https://openai.github.io/openai-agents-python/ref/realtime/agent

The `prompt` attribute allows for dynamic configuration of agent settings, including instructions, tools, and other parameters, outside of the codebase. This feature is specifically designed for use with OpenAI models.

--------------------------------

### trace > tracing

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

Optional tracing configuration for exporting this trace.

--------------------------------

### RealtimeAgent > instructions

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/agent

The `instructions` attribute defines the behavior of the agent. It can be a static string, serving as the system prompt, or a callable function that dynamically generates instructions based on the current context and agent instance. This flexibility allows for dynamic adaptation of the agent's responses and actions.

--------------------------------

### Agent dataclass > instructions

Source: https://openai.github.io/openai-agents-python/ref/agent

The instructions for the agent. Will be used as the "system prompt" when this agent is invoked. Describes what the agent should do, and how it responds.

Can either be a string, or a function that dynamically generates instructions for the agent. If you provide a function, it will be called with the context and the agent instance. It must return a string.

--------------------------------

### Trace with metadata and grouping

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

A trace represents a complete end-to-end workflow, encompassing all related spans and metadata. It serves as a logical container for operations within a specific process, such as 'Customer Service Query' or 'Code Generation'. By using a context manager (`with trace(...)`), developers can ensure reliable cleanup of traced operations. Key practices include using descriptive workflow names, grouping related traces with consistent `group_id`s, adding relevant `metadata` for filtering and analysis, and considering data privacy when including trace information.

--------------------------------

### Structured queries > Conversation analysis

Source: https://openai.github.io/openai-agents-python/sessions/advanced_sqlite_session

The `AdvancedSQLiteSession` offers powerful tools for analyzing conversation structure and content. You can retrieve the entire conversation organized by turns using `session.get_conversation_by_turns()`, which returns a dictionary where keys are turn numbers and values are lists of message items within that turn. Additionally, `session.get_tool_usage()` provides statistics on tool invocation, detailing which tools were used, how many times, and in which turn. For specific content searches, `session.find_turns_by_content(content)` can identify and return all turns that contain a given text string.

--------------------------------

### Classes > Agent > Attributes > trace_metadata

Source: https://openai.github.io/openai-agents-python/zh/ref/run

The `trace_metadata` attribute allows you to include an optional dictionary of additional metadata with the trace. This can be used to attach any relevant contextual information, such as user IDs, session details, or configuration parameters, to the trace data for enhanced analysis.

--------------------------------

### Span > start

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/spans

The `start()` method begins the span's execution. If `mark_as_current` is set to true, the span will be marked as the current span within the trace.

--------------------------------

### Trace > tracing_api_key

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The API key to use when exporting this trace and its spans.

--------------------------------

### Classes > Agent > Attributes > tracing

Source: https://openai.github.io/openai-agents-python/zh/ref/run

The `tracing` attribute allows for detailed configuration of tracing for an agent run. This can include settings for what data to capture, sampling rates, and integration with tracing backends. Proper tracing is crucial for debugging and understanding the agent's execution flow.

--------------------------------

### Span Class

Source: https://openai.github.io/openai-agents-python/ref/tracing

The `Span` class provides several essential properties and methods for managing traceable operations. Key properties include `trace_id` for the parent trace's ID, `span_id` for the unique ID of the span itself, `span_data` for operation-specific details, `parent_id` for the ID of the parent span (if any), `error` to capture any exceptions that occurred, and `started_at` and `ended_at` for timing information. Methods like `start()`, `finish()`, `__enter__()`, `__exit__()`, `set_error()`, and `export()` facilitate the lifecycle and data management of a span.

--------------------------------

### Agent Attributes

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

The `prompt` attribute allows for dynamic configuration of an agent's instructions, tools, and other settings, separate from the core code. This feature is specifically designed for use with OpenAI models via the Responses API, enabling flexible prompt management.

--------------------------------

### Function schema > FuncSchema dataclass > description instance-attribute

Source: https://openai.github.io/openai-agents-python/zh/ref/function_schema

The `description` attribute of a `FuncSchema` instance provides an optional string description for the function. This description is crucial for the LLM to understand the function's purpose and when to use it.

--------------------------------

### Model Settings > tool_choice

Source: https://openai.github.io/openai-agents-python/ref/model_settings

The tool choice to use when calling the model.

--------------------------------

### Trace with metadata and grouping > Trace

Source: https://openai.github.io/openai-agents-python/ref/tracing/traces

A trace represents a complete end-to-end workflow, encompassing all related spans and metadata. It signifies a logical operation, such as 'Customer Service Query' or 'Code Generation', and includes all the individual operations (spans) performed during that workflow. The `trace` context manager facilitates the creation and management of these traces, allowing for descriptive workflow names, grouping of related traces using consistent `group_id`s, and the addition of relevant metadata for effective filtering and analysis. It also ensures reliable cleanup through its context management features.

--------------------------------

### ComputerCreate

Source: https://openai.github.io/openai-agents-python/ref/tool

Initializes a computer for the current run context.

--------------------------------

### Tracing > name

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `name` property provides a human-readable name for a workflow trace, such as "Customer Service" or "Data Processing". This name should be descriptive and meaningful, aiding in the grouping and filtering of traces within the dashboard. It helps users quickly identify the purpose of a particular trace.

--------------------------------

### ModelSettings > response_include

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

Additional output data to include in the model response. include parameter

--------------------------------

### Spans > Span

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/spans

A span represents a single operation within a trace (e.g., an LLM call, tool execution, or agent run). Spans track timing, relationships between operations, and operation-specific data.

--------------------------------

### Examples > Categories > research_bot

Source: https://openai.github.io/openai-agents-python/examples

A simple deep research clone that demonstrates complex multi-agent research workflows.

--------------------------------

### FunctionToolResult > output

Source: https://openai.github.io/openai-agents-python/ref/tool

The output of the tool.

--------------------------------

### RealtimeAgent > prompt

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/agent

The `prompt` attribute allows for dynamic configuration of an agent's instructions, tools, and other settings outside of the direct code. This feature is specifically designed for use with OpenAI models, offering a way to externalize and manage agent configurations.

--------------------------------

### Span Class > start

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `start()` method begins the span's execution. If `mark_as_current` is true, the span will be marked as the current span.

--------------------------------

### Trace with metadata and grouping

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/traces

When using the `trace` context manager, it's recommended to use descriptive workflow names that clearly indicate the purpose of the trace. Grouping related traces with consistent `group_ids` facilitates easier analysis and debugging of specific workflows. Adding relevant metadata, such as user IDs or request parameters, enables powerful filtering capabilities in the tracing dashboard. It's also important to use context managers for reliable cleanup of trace resources and to consider data privacy when adding trace data, especially if it contains sensitive information.

--------------------------------

### Agent Attributes > prompt

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

A prompt object (or a function that returns a Prompt). Prompts allow you to dynamically configure the instructions, tools and other config for an agent outside of your code. Only usable with OpenAI models, using the Responses API.

--------------------------------

### RealtimeAgent > prompt

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/agent

The `prompt` parameter accepts a `Prompt` object, which enables dynamic configuration of instructions, tools, and other settings for an agent outside of the main codebase. This feature is exclusively usable with OpenAI models, allowing for greater flexibility in prompt management.

--------------------------------

### Handoff dataclass > tool_name instance-attribute

Source: https://openai.github.io/openai-agents-python/ja/ref/handoffs

The name of the tool that represents the handoff.

--------------------------------

### Trace with metadata and grouping

Source: https://openai.github.io/openai-agents-python/ref/tracing

The `export()` method allows you to serialize the trace data, including all spans and their associated information, into a dictionary. This is essential for sending trace data to backend systems for storage and analysis. The `export()` method may also include metadata and the group ID if they were provided when the trace was created. If tracing is disabled, this method returns `None`.

--------------------------------

### Span > __enter__

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/spans

The `__enter__` method is part of the context manager protocol, allowing spans to be used with the `with` statement. It typically starts the span.

--------------------------------

### Span Class > __enter__

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `__enter__` method is used to enter the span's context, typically within a `with` statement.

--------------------------------

### function_tool

Source: https://openai.github.io/openai-agents-python/ja/ref/tool

The `function_tool` decorator offers several parameters to customize the behavior and definition of the created tool. You can provide `name_override` and `description_override` to use custom names and descriptions instead of those derived from the function. The `docstring_style` parameter allows explicit specification of the docstring format, defaulting to auto-detection. `use_docstring_info` controls whether docstring content is used for descriptions. A `failure_error_function` can be specified to handle tool call failures, controlling whether an exception is raised or a custom error message is sent to the LLM. `strict_mode` (recommended to be `True`) enforces strict JSON schema validation for tool inputs, improving the reliability of JSON parsing. The `is_enabled` parameter can be a boolean or a callable that dynamically determines if the tool should be available to the LLM at runtime. Additionally, `tool_input_guardrails` and `tool_output_guardrails` can be provided as lists of guardrail objects to enforce specific rules before tool execution and after tool completion, respectively.

--------------------------------

### openai_github_io_openai-agents-python > function_schema

Source: https://openai.github.io/openai-agents-python/ja/ref/function_schema

When extracting parameter information, `function_schema` intelligently combines data from multiple sources. It first inspects the function's type hints, including any additional metadata provided through `typing.Annotated`. Descriptions found within these annotations are collected. Subsequently, if `use_docstring_info` is enabled, it parses the docstring for parameter descriptions. The function then merges these descriptions, prioritizing those derived from annotations if a parameter has descriptions from both sources. This approach ensures that detailed information, whether embedded directly in type hints or within the docstring, is captured and incorporated into the final `FuncSchema`.

--------------------------------

### trace > workflow_name

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The name of the logical app or workflow. For example, you might provide "code_bot" for a coding agent, or "customer_support_agent" for a customer support agent.

--------------------------------

### MCPServerStdio

Source: https://openai.github.io/openai-agents-python/ja/ref/mcp/server

The `__init__` method for `MCPServerStdio` allows for comprehensive configuration of the server. Key parameters include `params`, which is a dictionary containing essential settings like the command to execute for the server process, its arguments, environment variables, working directory, and text encoding for communication. Other important parameters include `cache_tools_list` for optimizing tool listing latency, `client_session_timeout_seconds` for setting read timeouts, `tool_filter` for managing tool visibility, `use_structured_content` to control how tool results are handled (with considerations for backward compatibility), and parameters for managing retries and backoff delays for tool calls. An optional `message_handler` can also be provided.

--------------------------------

### Span > __enter__

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/spans

The `__enter__` method is part of the context manager protocol, allowing spans to be used with the `with` statement for automatic start and finish operations.

--------------------------------

### Examples > Categories > financial_research_agent

Source: https://openai.github.io/openai-agents-python/examples

A financial research agent that demonstrates structured research workflows with agents and tools for financial data analysis.

--------------------------------

### RunConfig `dataclass` > tracing `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ja/ref/run

Detailed tracing configuration for a run is provided through the `tracing` attribute in `RunConfig`. This allows for fine-grained control over how tracing is performed, including endpoints, sampling rates, and other related parameters.

--------------------------------

### tool.py > CodeInterpreterTool dataclass

Source: https://openai.github.io/openai-agents-python/ref/tool

A tool that allows the LLM to execute code in a sandboxed environment. This tool provides the capability for the language model to run code safely within isolated execution contexts. The configuration for this tool includes settings related to the container environment and other relevant parameters for code execution.

--------------------------------

### Recommended prompts

Source: https://openai.github.io/openai-agents-python/handoffs

To ensure LLMs correctly interpret handoffs, it's recommended to incorporate handoff information into your agents. A suggested prefix is available in `agents.extensions.handoff_prompt.RECOMMENDED_PROMPT_PREFIX`. Alternatively, the `agents.extensions.handoff_prompt.prompt_with_handoff_instructions` function can automatically append recommended data to your prompts.

--------------------------------

### AdvancedSQLiteSession > _init_structure_tables

Source: https://openai.github.io/openai-agents-python/ref/extensions/memory/advanced_sqlite_session

The `_init_structure_tables` method is responsible for creating the database tables required for conversation branching and usage analytics. It defines two new tables: `message_structure` for tracking message metadata including session ID, message ID, branch ID, message type, sequence number, turn numbers, and tool name; and `turn_usage` for logging resource consumption at each turn, including session ID, branch ID, user turn number, token counts (requests, input, output, total), and detailed token breakdowns in JSON format. It also creates relevant indexes to optimize queries on these tables.

--------------------------------

### trace > group_id

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

Optional grouping identifier to link multiple traces from the same conversation or process. For instance, you might use a chat thread ID.

--------------------------------

### Tools > ToolOutputText

Source: https://openai.github.io/openai-agents-python/zh/ref/tool

Represents a tool output that should be sent to the model as text.

--------------------------------

### Spans > started_at

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

When the span started execution. This is an ISO format timestamp indicating the exact moment the operation began. If the span has not yet started, this will be `None`.

--------------------------------

### Function schema > FuncSchema dataclass > signature instance-attribute

Source: https://openai.github.io/openai-agents-python/zh/ref/function_schema

The `signature` attribute stores the `inspect.Signature` object for the function. This provides detailed information about the function's parameters, including their names, kinds, and annotations, which is used internally for argument mapping.

--------------------------------

### spans.py > Span > tracing_api_key

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

The API key to use when exporting this span.

--------------------------------

### Event handling

Source: https://openai.github.io/openai-agents-python/realtime/guide

The session streams events that you can listen to by iterating over the session object. Events include audio output chunks, transcription results, tool execution start and end, agent handoffs, and errors. Key events to handle include:
  * **audio** : Raw audio data from the agent's response
  * **audio_end** : Agent finished speaking
  * **audio_interrupted** : User interrupted the agent
  * **tool_start/tool_end** : Tool execution lifecycle
  * **handoff** : Agent handoff occurred
  * **error** : Error occurred during processing

For complete event details, see `RealtimeSessionEvent`.

--------------------------------

### SessionABC > add_items

Source: https://openai.github.io/openai-agents-python/ko/ref/memory/session

Add new items to the conversation history.

--------------------------------

### RealtimeAgent > instructions

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/agent

The `instructions` attribute defines the system prompt for the agent. It dictates the agent's behavior and response style. This can be provided as a static string or dynamically generated by a function. If a function is used, it receives the `RunContextWrapper` and the agent instance as arguments and must return a string representing the instructions.

--------------------------------

### Session

Source: https://openai.github.io/openai-agents-python/ko/ref/memory/session

The `Session` protocol defines the interface for managing conversation history within a specific session. It enables agents to retain context across interactions without the need for manual memory management. Implementations of this protocol are responsible for storing and retrieving conversation turns.

--------------------------------

### ModelSettings > include_usage

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

Whether to include usage chunk. Only available for Chat Completions API.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/zh/ref/model_settings

The `include_usage` parameter, when set to `True`, ensures that usage statistics (e.g., token counts) are included in the model's response. This feature is specifically available for the Chat Completions API.

--------------------------------

### RealtimeAgent > handoff_description

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/agent

The `handoff_description` attribute offers a textual description of the agent's purpose. This is particularly useful when the agent is acting as a handoff to another agent, providing an LLM with the necessary information to decide when to invoke it.

--------------------------------

### RunConfig `dataclass` > trace_metadata `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ja/ref/run

Additional metadata can be associated with a trace through the `trace_metadata` dictionary in `RunConfig`. This optional field allows for the inclusion of custom key-value pairs, enriching the trace data with relevant context.

--------------------------------

### ComputerDispose

Source: https://openai.github.io/openai-agents-python/ref/tool

Cleans up a computer initialized for a run context.

--------------------------------

### openai-agents-python/span_data.py > TranscriptionSpanData

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

The `TranscriptionSpanData` class is designed to represent a transcription span within a trace. Similar to `SpeechSpanData`, it extends `SpanData` and captures the input, output, model, and model configuration associated with a transcription process. This allows for detailed logging and analysis of transcription tasks.

--------------------------------

### traces.py > name

Source: https://openai.github.io/openai-agents-python/ref/tracing/traces

The `name` property provides a human-readable name for the workflow trace. This name should be descriptive and meaningful, aiding in grouping and filtering traces in the dashboard. It helps in quickly identifying the purpose of a particular trace.

--------------------------------

### OpenAI Agents Python API Reference > nest_handoff_history

Source: https://openai.github.io/openai-agents-python/ja/ref/handoffs

Summarize the previous transcript for the next agent.

--------------------------------

### Trace with metadata and grouping

Source: https://openai.github.io/openai-agents-python/ref/tracing

A `Trace` object represents a logical workflow or operation. It contains all the spans that occur during that workflow. For example, you can use `with trace("Order Processing") as t:` to create a trace for order processing, and within its block, execute operations like validation and processing. This helps in organizing and understanding the flow of operations.

--------------------------------

### Trace with metadata and grouping

Source: https://openai.github.io/openai-agents-python/ref/tracing

The `trace` context manager is used to define a complete end-to-end workflow, such as 'Customer Service Query' or 'Code Generation'. It encompasses all individual operations (spans) within that workflow. You can provide a descriptive name for the workflow, a `group_id` to associate related traces, and `metadata` (e.g., customer ID) for enhanced filtering and analysis. Using context managers ensures reliable cleanup of trace resources. When adding trace data, always consider privacy implications.

--------------------------------

### Spans

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/spans

A span represents a single operation within a trace (e.g., an LLM call, tool execution, or agent run). Spans track timing, relationships between operations, and operation-specific data. Spans automatically nest under the current trace, and context managers should be used for reliable start and finish operations. It's important to include relevant data within spans but avoid sensitive information. Errors should be handled properly using the `set_error()` method.

--------------------------------

### Spans > tracing_api_key

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The API key to use when exporting this span. This key is utilized for sending tracing data to an external service.

--------------------------------

### Spans > span_data

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

Operation-specific data for this span. This field holds data relevant to the particular operation the span represents, such as details of an LLM generation or a tool execution.

--------------------------------

### Span > start

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

Start the span. If `mark_as_current` is true, the span will be marked as the current span.

--------------------------------

### ModelSettings > top_p

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

The top_p to use when calling the model.

--------------------------------

### Span

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/spans

A span represents a single operation within a trace (e.g., an LLM call, tool execution, or agent run). Spans track timing, relationships between operations, and operation-specific data. Spans automatically nest under the current trace, and context managers should be used for reliable start and finish operations. It is important to include relevant data but avoid sensitive information, and to handle errors properly using the `set_error()` method.

--------------------------------

### Usage

Source: https://openai.github.io/openai-agents-python/ja/ref/usage

The `Usage` dataclass serves as a comprehensive tracker for token consumption in LLM API interactions. It aggregates several key metrics:

*   `requests`: The total number of API requests made.
*   `input_tokens`: The cumulative count of tokens sent to the LLM.
*   `input_tokens_details`: Provides a granular breakdown of input tokens, aligning with API usage details, including cached tokens.
*   `output_tokens`: The cumulative count of tokens received from the LLM.
*   `output_tokens_details`: Offers a detailed breakdown of output tokens, such as reasoning tokens.
*   `total_tokens`: The sum of all input and output tokens across all requests.
*   `request_usage_entries`: A list that stores individual `RequestUsage` objects, crucial for precise per-request cost calculations. Each call to the `add()` method that involves actual token usage will create a new entry in this list, preserving the ability to analyze costs or context window usage at a granular level.

--------------------------------

### spans.py > start

Source: https://openai.github.io/openai-agents-python/ref/tracing

Start the span. This method initiates the timing and recording of the span's execution. The `mark_as_current` parameter, when set to `True`, designates this span as the active span in the current context.

--------------------------------

### Agent `dataclass`

Source: https://openai.github.io/openai-agents-python/ko/ref/agent

An agent is an AI model configured with instructions, tools, guardrails, handoffs and more. We strongly recommend passing `instructions`, which is the "system prompt" for the agent. In addition, you can pass `handoff_description`, which is a human-readable description of the agent, used when the agent is used inside tools/handoffs. Agents are generic on the context type. The context is a (mutable) object you create. It is passed to tool functions, handoffs, guardrails, etc. See `AgentBase` for base parameters that are shared with `RealtimeAgent`s.

--------------------------------

### Model Settings > response_include

Source: https://openai.github.io/openai-agents-python/ref/model_settings

Additional output data to include in the model response. include parameter

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ref/model_settings

For maximum flexibility, `ModelSettings` includes parameters for passing extra information directly to the underlying model API. `extra_query`, `extra_body`, and `extra_headers` allow you to append custom fields, data, or headers to the API request. `extra_args` is a dictionary for passing any arbitrary keyword arguments that are supported by the specific model provider's API, enabling advanced customization beyond the standard parameters.

--------------------------------

### Agent `dataclass`

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

The `prompt` parameter allows for dynamic configuration of an agent's instructions, tools, and other settings outside of the main codebase. This feature is specifically designed for use with OpenAI models and the Responses API. It can accept either a `Prompt` object or a function that generates a `Prompt`. This provides flexibility in managing agent configurations, enabling easier adjustments and experimentation without altering the core agent logic.

--------------------------------

### Span Class

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

A span represents a single operation within a trace (e.g., an LLM call, tool execution, or agent run). Spans track timing, relationships between operations, and operation-specific data.

Use context managers for reliable start/finish. Spans automatically nest under the current trace. Include relevant data but avoid sensitive information. Handle errors properly using `set_error()`.

--------------------------------

### group_id

Source: https://openai.github.io/openai-agents-python/ko/ref/run

A grouping identifier to use for tracing, to link multiple traces from the same conversation or process. For example, you might use a chat thread ID.

--------------------------------

### Traces > Trace

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/traces

A trace represents a logical workflow or operation (e.g., "Customer Service Query" or "Code Generation") and contains all the spans (individual operations) that occur during that workflow.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ref/model_settings

Additional settings within `ModelSettings` offer finer control over the LLM's output and behavior. `max_tokens` limits the length of the generated response. `reasoning` allows configuration for reasoning models, while `verbosity` controls the level of detail in the model's response. `metadata` can be used to attach custom information to the model call. The `store` parameter determines whether the generated response is saved for later retrieval, with different default behaviors for the Responses API and Chat Completions API.

--------------------------------

### tool.py > MCPToolApprovalRequest dataclass

Source: https://openai.github.io/openai-agents-python/ref/tool

A request to approve a tool call. This dataclass encapsulates the necessary information when a tool call requires explicit approval. It holds the run context and the specific data pertaining to the approval request originating from the MCP (Machine Control Protocol) system.

--------------------------------

### Trace with metadata and grouping

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/traces

The `trace` context manager allows you to define a descriptive workflow name, assign a `group_id` to group related traces, and attach arbitrary `metadata` for filtering and analysis. This is particularly useful for debugging and monitoring, as it provides context for individual operations within a larger workflow. For instance, you can group all traces belonging to a specific chat session using a consistent `group_id` or add metadata like customer IDs to filter traces related to a particular user.

--------------------------------

### Agent Class Attributes > prompt

Source: https://openai.github.io/openai-agents-python/ko/ref/agent

The `prompt` attribute allows for flexible and dynamic configuration of an agent's instructions, tools, and other settings. This feature is exclusively available for OpenAI models when utilizing the Responses API. It can accept either a `Prompt` object or a function that produces a `Prompt`, enabling external configuration of agent behavior.

--------------------------------

### Tools > ToolOutputImage

Source: https://openai.github.io/openai-agents-python/zh/ref/tool

Represents a tool output that should be sent to the model as an image. You can provide either an `image_url` (URL or data URL) or a `file_id` for previously uploaded content. The optional `detail` can control vision detail.

--------------------------------

### RunConfig `dataclass` > trace_metadata `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ref/run

Additional metadata relevant to the trace can be included using the `trace_metadata` attribute in `RunConfig`. This attribute accepts a dictionary where arbitrary key-value pairs can be stored, allowing for the enrichment of trace data with custom information pertinent to the specific agent run or its context.

--------------------------------

### spans.py > Span > span_data

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

Operation-specific data for this span.

--------------------------------

### Examples > Categories > voice

Source: https://openai.github.io/openai-agents-python/examples

See examples of voice agents, using our TTS and STT models, including streamed voice examples.

--------------------------------

### Span > span_data

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

Operation-specific data for this span. Data specific to this type of span (e.g., LLM generation data).

--------------------------------

### Agents > Agent

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

A class that receives callbacks on various lifecycle events for this agent.

--------------------------------

### Agent dataclass

Source: https://openai.github.io/openai-agents-python/ref/agent

An agent is an AI model configured with instructions, tools, guardrails, handoffs and more. We strongly recommend passing `instructions`, which is the "system prompt" for the agent. In addition, you can pass `handoff_description`, which is a human-readable description of the agent, used when the agent is used inside tools/handoffs.

Agents are generic on the context type. The context is a (mutable) object you create. It is passed to tool functions, handoffs, guardrails, etc.

See `AgentBase` for base parameters that are shared with `RealtimeAgent`s.

--------------------------------

### Examples > Categories > mcp

Source: https://openai.github.io/openai-agents-python/examples

Learn how to build agents with MCP (Model Context Protocol), including: Filesystem examples, Git examples, MCP prompt server examples, SSE (Server-Sent Events) examples, and Streamable HTTP examples.

--------------------------------

### Tools > ToolOutputTextDict

Source: https://openai.github.io/openai-agents-python/zh/ref/tool

TypedDict variant for text tool outputs.

--------------------------------

### AgentBase `dataclass`

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

The `AgentBase` class serves as the foundational class for both `Agent` and `RealtimeAgent`. It defines common attributes and methods shared by these agent types. Key attributes include `name` for identifying the agent, `handoff_description` for LLM understanding during handoffs, and `tools` which is a list of tools the agent can utilize. It also supports integration with Model Context Protocol (MCP) servers via `mcp_servers` and `mcp_config` for enhanced functionality and tool availability.

--------------------------------

### function_tool

Source: https://openai.github.io/openai-agents-python/zh/ref/tool

The `function_tool` decorator offers a comprehensive set of parameters to customize the behavior and appearance of the created tool. You can override the default name and description of the tool using `name_override` and `description_override`, respectively, which is useful if the function name or docstring isn't ideal for the agent's perspective. The `docstring_style` parameter allows explicit control over how docstring information is parsed, although auto-detection is usually sufficient. The `use_docstring_info` flag, set to `True` by default, controls whether docstring content is used for descriptions; setting it to `False` would require providing descriptions solely through overrides. Error handling can be customized with `failure_error_function`, which defines how tool failures are reported back to the agent; by default, exceptions are raised, but you can opt to send a formatted error message to the LLM instead. For enhanced reliability, `strict_mode` (defaulting to `True`) enforces stricter JSON schema validation, reducing the chances of malformed input being sent to your tool. The `is_enabled` parameter provides a dynamic way to control tool availability, accepting either a boolean or a callable that checks the agent's context and returns whether the tool should be active. Finally, `tool_input_guardrails` and `tool_output_guardrails` allow you to specify lists of functions that will be executed before and after the tool's main logic, respectively, enabling pre-computation checks or post-processing of results.

--------------------------------

### ToolOutputFileContentDict

Source: https://openai.github.io/openai-agents-python/ref/tool

TypedDict variant for file content tool outputs.

--------------------------------

### openai_agents.store.SQLiteSession._add_structure_metadata

Source: https://openai.github.io/openai-agents-python/ref/extensions/memory/advanced_sqlite_session

The `_add_structure_metadata` method is crucial for preparing items before they are added to the session. It ensures that turn numbers are assigned on a per-branch basis, not globally, and assigns explicit sequence numbers for precise ordering of messages. This method also links messages to their unique database IDs, which is essential for tracking the message structure. It is designed to correctly handle scenarios where multiple user messages are processed in a single batch.

--------------------------------

### Usage

Source: https://openai.github.io/openai-agents-python/ref/usage

The `add` method in the `Usage` class provides a convenient way to aggregate usage data from multiple `Usage` objects. It sums up the total requests, input tokens, output tokens, and total tokens. Importantly, this method also intelligently preserves the `request_usage_entries` list. If the `other` `Usage` object being added represents a single, distinct API request with a non-zero token count, it is automatically appended to the `request_usage_entries` list of the aggregated object. This ensures that the detailed breakdown of individual requests is maintained, even when usage is consolidated.

--------------------------------

### Model Settings > top_p

Source: https://openai.github.io/openai-agents-python/ref/model_settings

The top_p to use when calling the model.

--------------------------------

### Memory > Session

Source: https://openai.github.io/openai-agents-python/ko/ref/memory

Session stores conversation history for a specific session, allowing agents to maintain context without requiring explicit manual memory management.

--------------------------------

### spans.py > started_at

Source: https://openai.github.io/openai-agents-python/ref/tracing

When the span started execution. This is typically an ISO format timestamp. If the span has not yet started, this value will be None.

--------------------------------

### Usage

Source: https://openai.github.io/openai-agents-python/ko/ref/usage

The `Usage` dataclass is designed to track various aspects of token usage in interactions with Large Language Models (LLMs). It records the total number of requests made, the cumulative input and output tokens, and detailed breakdowns of these tokens. Specifically, `input_tokens_details` and `output_tokens_details` provide granular information that aligns with API usage reporting, such as cached tokens and reasoning tokens. The `total_tokens` field offers a simple sum of all tokens processed. A key feature is `request_usage_entries`, a list that stores individual usage records for each distinct API request, which is crucial for accurate cost calculations and understanding context window management across multiple calls.

--------------------------------

### RealtimeAgent > handoff_description

Source: https://openai.github.io/openai-agents-python/ref/realtime/agent

The `handoff_description` attribute provides a textual description of the agent's purpose. This description is utilized when the agent is acting as a handoff, enabling an LLM to understand its functionality and determine when to invoke it.

--------------------------------

### RealtimeAgent > handoff_description

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/agent

The `handoff_description` attribute provides a textual description of the agent. This is crucial when the agent is utilized as a 'handoff' to another agent, enabling an LLM to understand the agent's purpose and determine when it should be invoked.

--------------------------------

### OpenAI Agents Python > MCP Server > __init__

Source: https://openai.github.io/openai-agents-python/ref/mcp/server

This section describes the `__init__` method for creating a new MCP server based on the Streamable HTTP transport. It details the various parameters available for configuring the server, including connection details, caching mechanisms, naming, timeouts, tool filtering, structured content usage, retry logic, and message handling.  The `params` argument is crucial for setting up the server's connection, encompassing the URL, headers, and various timeout settings.  The `cache_tools_list` parameter offers a performance optimization by caching the tools list, which is beneficial when the server's tools are static.  The `use_structured_content` flag addresses compatibility with different server implementations regarding how structured content is returned.  Retry mechanisms are also configurable to handle transient failures in tool listing or execution.

--------------------------------

### Quickstart > Agents

Source: https://openai.github.io/openai-agents-python/voice/quickstart

First, let's set up some Agents. This should feel familiar to you if you've built any agents with this SDK. We'll have a couple of Agents, a handoff, and a tool.

This example demonstrates setting up a Spanish-speaking agent and a main assistant agent that can handoff to the Spanish agent if the user speaks Spanish. It also includes a `get_weather` tool for the assistant agent.

--------------------------------

### Spans

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

A span represents a single operation within a trace, such as an LLM call, tool execution, or agent run. Spans track timing, relationships between operations, and operation-specific data. They are essential for understanding the flow and performance of complex operations. Spans automatically nest under the current trace, and context managers should be used for reliable start and finish operations. It is important to include relevant data but avoid sensitive information. Errors should be handled properly using the `set_error()` method.

--------------------------------

### OpenAI Agents Python > tracing

Source: https://openai.github.io/openai-agents-python/ref/run

The `tracing` attribute allows for detailed configuration of tracing for agent runs. This can include specifying endpoints, sampling rates, and other parameters to control how traces are generated and stored.

--------------------------------

### Results > New items

Source: https://openai.github.io/openai-agents-python/results

The `new_items` property contains the `RunItem`s generated during the run. Each `RunItem` wraps the raw item produced by the LLM. These items can indicate different types of outputs: `MessageOutputItem` for LLM messages, `HandoffCallItem` for LLM tool calls to handoff, `HandoffOutputItem` for handoff occurrences, `ToolCallItem` for LLM tool invocations, `ToolCallOutputItem` for tool responses, and `ReasoningItem` for LLM reasoning.

--------------------------------

### Examples > Categories > model_providers

Source: https://openai.github.io/openai-agents-python/examples

Explore how to use non-OpenAI models with the SDK, including custom providers and LiteLLM integration.

--------------------------------

### Spans

Source: https://openai.github.io/openai-agents-python/ref/tracing/spans

The `start()` method initiates the span's execution. If `mark_as_current` is set to `True`, this span will be designated as the current span within the trace context.

The `finish()` method concludes the span's execution. If `reset_current` is `True`, the current span context will be reset after finishing this span.

--------------------------------

### Spans

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/spans

The `Span` class is the base class for representing traceable operations with timing and context. It includes abstract methods for managing the span's lifecycle, such as `start()`, `finish()`, `__enter__()`, and `__exit__()`. It also provides properties to access the `trace_id`, `span_id`, `span_data`, `parent_id`, `error` information, and timestamps for `started_at` and `ended_at`. The `set_error()` method is used to record any errors that occur during the span's execution, and the `export()` method allows for the serialization of span data.

--------------------------------

### spans.py > Span > started_at

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

When the span started execution.

--------------------------------

### Agent Visualization > Generating a Graph > Example Usage

Source: https://openai.github.io/openai-agents-python/visualization

This generates a graph that visually represents the structure of the **triage agent** and its connections to sub-agents and tools.

--------------------------------

### input_guardrails

Source: https://openai.github.io/openai-agents-python/ko/ref/run

A list of input guardrails to run on the initial run input.

--------------------------------

### Spans

Source: https://openai.github.io/openai-agents-python/ref/tracing/spans

A span represents a single operation within a trace (e.g., an LLM call, tool execution, or agent run). Spans track timing, relationships between operations, and operation-specific data.

When creating a custom span, it's recommended to use context managers for reliable start and finish operations. You should also include relevant data but avoid sensitive information. If an error occurs during the span's execution, it should be handled properly using the `set_error()` method to record the error details.

--------------------------------

### __init__

Source: https://openai.github.io/openai-agents-python/ja/ref/memory

Initialize the SQLite session.

Args:
    session_id: Unique identifier for the conversation session
    db_path: Path to the SQLite database file. Defaults to ':memory:' (in-memory database)
    sessions_table: Name of the table to store session metadata. Defaults to
        'agent_sessions'
    messages_table: Name of the table to store message data. Defaults to 'agent_messages'

--------------------------------

### Orchestrating multiple agents > Orchestrating via LLM

Source: https://openai.github.io/openai-agents-python/multi_agent

An agent is an LLM equipped with instructions, tools and handoffs. This means that given an open-ended task, the LLM can autonomously plan how it will tackle the task, using tools to take actions and acquire data, and using handoffs to delegate tasks to sub-agents. For example, a research agent could be equipped with tools like:
* Web search to find information online
* File search and retrieval to search through proprietary data and connections
* Computer use to take actions on a computer
* Code execution to do data analysis
* Handoffs to specialized agents that are great at planning, report writing and more.

This pattern is great when the task is open-ended and you want to rely on the intelligence of an LLM. The most important tactics here are:
1. Invest in good prompts. Make it clear what tools are available, how to use them, and what parameters it must operate within.
2. Monitor your app and iterate on it. See where things go wrong, and iterate on your prompts.
3. Allow the agent to introspect and improve. For example, run it in a loop, and let it critique itself; or, provide error messages and let it improve.
4. Have specialized agents that excel in one task, rather than having a general purpose agent that is expected to be good at anything.
5. Invest in evals. This lets you train your agents to improve and get better at tasks.

--------------------------------

### Agents > as_tool

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

The `tool_name` parameter specifies the name of the tool. If this parameter is not explicitly provided, the agent's own name will be used as the tool's name. The `tool_description` parameter is crucial for defining the tool's purpose and usage. It should clearly articulate what the tool does and the conditions under which it should be invoked, enabling other agents to understand and utilize it effectively.

--------------------------------

### FunctionTool `dataclass` > on_invoke_tool `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ref/tool

The `on_invoke_tool` attribute is a callable that defines the core logic for invoking the wrapped function. It accepts a `ToolContext` and a JSON string representing the arguments. The callable must return a structured tool output type (like `ToolOutputText`, `ToolOutputImage`, `ToolOutputFileContent`), a string representation of the output, a list of outputs, or any object that can be converted to a string. Errors can be handled by raising an exception or returning an error message string, which will be relayed back to the LLM.

--------------------------------

### spans.py > tracing_api_key

Source: https://openai.github.io/openai-agents-python/ref/tracing

The API key to use when exporting this span. This key is utilized for authentication and authorization when sending span data to an external tracing service.

--------------------------------

### Usage

Source: https://openai.github.io/openai-agents-python/zh/ref/usage

The `add` method allows for the aggregation of `Usage` objects. When one `Usage` object is added to another, all the respective fields (requests, input tokens, output tokens, total tokens) are summed up. This method is designed to automatically preserve the `request_usage_entries` list. If the `other` `Usage` object represents a single API request with a non-zero token count, it is added to the `request_usage_entries` list of the aggregated object. This ensures that the per-request granularity is maintained even after combining multiple `Usage` instances.

--------------------------------

### RealtimeAgent > handoff_description

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/agent

The `handoff_description` attribute provides a textual description of the agent's purpose and functionality. This description is particularly important when the agent is utilized as a handoff to another agent, as it informs an LLM about what the agent does and when it should be invoked.

--------------------------------

### tool.py > ComputerToolSafetyCheckData dataclass

Source: https://openai.github.io/openai-agents-python/ref/tool

Information about a computer tool safety check. This dataclass contains details relevant to ensuring the safety of operations performed by a computer tool. It includes the run context, the agent executing the action, the specific tool call being made, and the pending safety check that requires acknowledgment.

--------------------------------

### MCPServerStdio > __init__

Source: https://openai.github.io/openai-agents-python/ja/ref/mcp/server

Creates a new MCP server utilizing the stdio transport mechanism. This constructor allows for detailed configuration of the server's behavior and communication.

Key parameters include `params`, which defines how the server process is spawned and communicates (command, arguments, environment variables, working directory, and text encoding). The `cache_tools_list` boolean can significantly improve performance by fetching the tool list only once if the server's tools are static. A `name` can be provided for easier identification, otherwise, it's derived from the server command. The `client_session_timeout_seconds` sets a timeout for client sessions, while `tool_filter` allows for custom filtering of available tools. `use_structured_content` controls whether to leverage structured content from tool results, defaulting to `False` for backward compatibility. Finally, `max_retry_attempts` and `retry_backoff_seconds_base` configure automatic retries for failed calls, and `message_handler` allows for custom processing of session messages.

--------------------------------

### Spans > start

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

Start the span. This method marks the beginning of the span's execution. The `mark_as_current` parameter can be used to set this span as the currently active span in the execution context.

--------------------------------

### Usage > input_tokens_details

Source: https://openai.github.io/openai-agents-python/ref/usage

The `input_tokens_details` attribute provides granular information about the input tokens, mirroring the usage details returned by the responses API. This allows for a more precise analysis of how input tokens are composed, potentially including cached tokens.

--------------------------------

### Usage > requests

Source: https://openai.github.io/openai-agents-python/ref/usage

The `requests` attribute tallies the total number of requests made to the LLM API. This is a straightforward count of each interaction with the API.

--------------------------------

### Agents > Dynamic instructions

Source: https://openai.github.io/openai-agents-python/agents

In most cases, you can provide instructions when you create the agent. However, you can also provide dynamic instructions via a function. The function will receive the agent and context, and must return the prompt. Both regular and `async` functions are accepted.

--------------------------------

### Span > export

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

Export the span data as a dictionary. This can be useful for serialization or sending span data to an external system.

--------------------------------

### Agent/LLM context

Source: https://openai.github.io/openai-agents-python/context

When an LLM is called, the **only** data it can see is from the conversation history. This means that if you want to make some new data available to the LLM, you must do it in a way that makes it available in that history. There are a few ways to do this:
1. You can add it to the Agent `instructions`. This is also known as a "system prompt" or "developer message". System prompts can be static strings, or they can be dynamic functions that receive the context and output a string. This is a common tactic for information that is always useful (for example, the user's name or the current date).
2. Add it to the `input` when calling the `Runner.run` functions. This is similar to the `instructions` tactic, but allows you to have messages that are lower in the chain of command.
3. Expose it via function tools. This is useful for _on-demand_ context - the LLM decides when it needs some data, and can call the tool to fetch that data.
4. Use retrieval or web search. These are special tools that are able to fetch relevant data from files or databases (retrieval), or from the web (web search). This is useful for "grounding" the response in relevant contextual data.

--------------------------------

### Span > finish

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/spans

The `finish()` method concludes the execution of the span. It can optionally reset the current span, especially when exiting a context manager.

--------------------------------

### Agent Attributes > prompt

Source: https://openai.github.io/openai-agents-python/ref/agent

The `prompt` attribute allows for dynamic configuration of an agent's instructions, tools, and other settings outside of direct code. This feature is specifically designed for use with OpenAI models via the Responses API. It can accept either a `Prompt` object or a function that generates a `Prompt`, enabling flexible and externalized control over agent behavior.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

`verbosity` controls the level of detail in the model's responses, with options typically including `'low'`, `'medium'`, and `'high'`.

--------------------------------

### SQLAlchemySession > __init__

Source: https://openai.github.io/openai-agents-python/ref/extensions/memory/sqlalchemy_session

The `SQLAlchemySession` defines two primary tables: `agent_sessions` and `agent_messages`. The `sessions_table` stores metadata about each conversation, including `session_id`, `created_at`, and `updated_at` timestamps. The `messages_table` stores the actual conversation messages, linked to a session via `session_id`. It includes columns for a unique message `id`, the `message_data` itself, and a `created_at` timestamp. An index is created on `session_id` and `created_at` in the messages table to optimize retrieval of messages within a session.

--------------------------------

### trace_include_sensitive_data

Source: https://openai.github.io/openai-agents-python/ko/ref/run

Whether we include potentially sensitive data (for example: inputs/outputs of tool calls or LLM generations) in traces. If False, we'll still create spans for these events, but the sensitive data will not be included.

--------------------------------

### spans.py > SpanError

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

Represents an error that occurred during span execution.

Attributes:
    message: A human-readable error description
    data: Optional dictionary containing additional error context

--------------------------------

### Usage

Source: https://openai.github.io/openai-agents-python/ko/ref/usage

The `__post_init__` method in the `Usage` class performs essential data normalization upon object initialization. It addresses potential issues where certain token detail fields (like `cached_tokens` or `reasoning_tokens`) might be `None` or missing, especially if the LLM provider does not populate them or if the SDK bypasses Pydantic validation. By default, these fields are set to `0` if they are `None`, ensuring that subsequent operations do not encounter `TypeError` exceptions. This proactive handling of missing data guarantees the integrity and reliability of token usage tracking.

--------------------------------

### trace

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

The `trace` function is used to create a new trace. A trace represents a logical unit of work and can be used for monitoring and debugging. The trace is not started automatically upon creation. You must explicitly start and finish it, either by using it as a context manager with the `with` statement or by manually calling `trace.start()` and `trace.finish()` methods. This function allows you to associate a `workflow_name` which describes the purpose of the trace, such as "code_bot" for a coding agent or "customer_support_agent" for a support agent. Additionally, you can provide an optional `trace_id` and `group_id` for better organization and linking of related traces. A `metadata` dictionary can also be included to attach custom information.

--------------------------------

### Tools > ToolOutputImageDict

Source: https://openai.github.io/openai-agents-python/zh/ref/tool

TypedDict variant for image tool outputs.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ref/model_settings

The `ModelSettings` class also provides advanced options for prompt caching and response customization. `prompt_cache_retention` allows for extended caching durations, improving performance for repeated prompts. `include_usage` (available for the Chat Completions API) ensures usage statistics are returned. `response_include` lets you specify additional output data to be included in the model's response, such as log probabilities or specific sources. `top_logprobs` can be set to retrieve log probabilities for the most likely tokens.

--------------------------------

### spans.py > Trace

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

The `Trace` class is an abstract base class representing a complete end-to-end workflow containing related spans and metadata. A trace signifies a logical workflow or operation, such as "Customer Service Query" or "Code Generation", and encompasses all the individual operations (spans) performed during that workflow. For example, a basic trace usage could involve starting a trace named "Order Processing", running a validator, and then conditionally running a processor if the validation is approved.

--------------------------------

### Span > export

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/spans

The `export()` method is intended for exporting the span's data, likely for storage or transmission to a tracing backend. It returns a dictionary representation of the span or `None` if export is not applicable.

--------------------------------

### Context management > Advanced: `ToolContext`

Source: https://openai.github.io/openai-agents-python/context

The `ToolContext` class extends `RunContextWrapper` and provides access to additional metadata specific to the tool currently being executed. This includes:
* `tool_name`: The name of the invoked tool.
* `tool_call_id`: A unique identifier for the specific tool invocation.
* `tool_arguments`: The raw string representation of the arguments passed to the tool.

`ToolContext` is useful when your tools need to be aware of their execution environment, such as logging or debugging specific tool calls. It retains the `.context` property for accessing general context data, while adding these tool-specific details.

--------------------------------

### Trace Class > name

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/traces

The `name` property returns a human-readable name for the workflow trace. This name should be descriptive and meaningful, aiding in the grouping and filtering of traces within the dashboard. It helps users quickly identify the purpose of a particular trace, such as 'Customer Service' or 'Data Processing'.

--------------------------------

### openai-agents-python/src/langchain_openai/chat_models/orm.py > SQLiteSession > _add_structure_metadata

Source: https://openai.github.io/openai-agents-python/zh/ref/extensions/memory/advanced_sqlite_session

The `_add_structure_metadata` method enriches incoming message items with essential structural information before they are stored. It assigns turn numbers on a per-branch basis, ensuring that turns are tracked independently for different conversational branches. Additionally, it assigns explicit sequence numbers to guarantee precise ordering of messages, even within the same turn. This method also links messages to their unique database IDs, facilitating future reference and updates, and correctly handles scenarios where multiple user messages might be sent in a single batch.

--------------------------------

### traces.py > name

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/traces

The `name` property retrieves the human-readable name of this workflow trace. This name should be descriptive and meaningful, aiding in grouping and filtering traces in the dashboard. It helps in identifying the specific purpose of a given trace.

--------------------------------

### Model Settings > include_usage

Source: https://openai.github.io/openai-agents-python/ref/model_settings

Whether to include usage chunk. Only available for Chat Completions API.

--------------------------------

### Source code in src/agents/result.py

Source: https://openai.github.io/openai-agents-python/ko/ref/result

Creates a new input list, merging the original input with all the new items generated.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

`include_usage` is a boolean flag that, when set to `True`, includes usage statistics in the model's response. This feature is exclusively available for the Chat Completions API.

--------------------------------

### Agent Visualization > Understanding the Visualization

Source: https://openai.github.io/openai-agents-python/visualization

The generated graph includes:
  * A **start node** (`__start__`) indicating the entry point.
  * Agents represented as **rectangles** with yellow fill.
  * Tools represented as **ellipses** with green fill.
  * MCP Servers represented as **rectangles** with grey fill.
  * Directed edges indicating interactions:
  * **Solid arrows** for agent-to-agent handoffs.
  * **Dotted arrows** for tool invocations.
  * **Dashed arrows** for MCP server invocations.
  * An **end node** (`__end__`) indicating where execution terminates.

**Note:** MCP servers are rendered in recent versions of the `agents` package (verified in **v0.2.8**). If you don’t see MCP boxes in your visualization, upgrade to the latest release.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/zh/ref/model_settings

The `response_include` parameter allows you to request additional output data within the model's response. This can be useful for obtaining specific details or auxiliary information. The exact types of data that can be included are defined by `ResponseIncludable` or can be specified as strings for certain advanced options.

--------------------------------

### openai-agents-python/src/agents/realtime/config.py > User Input Types > RealtimeUserInputMessage > content

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/config

List of content items (text and image) in the message.

--------------------------------

### OpenAI Agents Python > as_tool

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

The `tool_name` parameter specifies the name of the tool. If this parameter is not provided, the agent's own name will be used as the tool's name. The `tool_description` parameter is crucial for defining what the tool does and in which scenarios it should be utilized. This description is used by the language model to determine when to invoke this tool.

--------------------------------

### OpenAI Agents Python > trace_metadata

Source: https://openai.github.io/openai-agents-python/ref/run

The `trace_metadata` attribute is an optional dictionary that can be used to include additional key-value pairs of metadata alongside the trace information. This allows for the enrichment of traces with custom data relevant to the specific run or context.

--------------------------------

### Spans

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

The `Span` class serves as the base class for representing traceable operations, including their timing and context. It provides methods to start and finish operations, manage span-specific data, and record errors. Key properties include `trace_id` for the parent trace's ID, `span_id` for the unique identifier of the span, and `span_data` for operation-specific details. The `parent_id` property indicates the ID of the parent span, if one exists.

--------------------------------

### Session

Source: https://openai.github.io/openai-agents-python/zh/ref/memory/session

The `Session` protocol defines the interface for managing conversation history within a specific session. It allows agents to maintain context over time without needing explicit manual memory management. Implementations of this protocol are responsible for storing and retrieving past interactions.

Key methods include `get_items` to retrieve the conversation history, `add_items` to append new exchanges, `pop_item` to remove and return the most recent interaction, and `clear_session` to reset the conversation history.

--------------------------------

### Handoff prompt

Source: https://openai.github.io/openai-agents-python/zh/ref/extensions/handoff_prompt

The `RECOMMENDED_PROMPT_PREFIX` is a system context designed for multi-agent systems like the Agents SDK. It defines the core purpose of the system: to simplify agent coordination and execution. The system primarily uses two abstractions: **Agents** and **Handoffs**. An agent is responsible for instructions and tools and can delegate a conversation to another agent when it's suitable. This delegation, or handoff, is performed by invoking a specific handoff function, typically named `transfer_to_<agent_name>`. These transfers are managed internally without explicit mention to the user.

--------------------------------

### API Reference > __init__

Source: https://openai.github.io/openai-agents-python/ko/ref/memory/sqlite_session

Initializes the SQLite session. The `session_id` is a unique identifier for the conversation. The `db_path` specifies the location of the SQLite database file, defaulting to an in-memory database (`':memory:'`). Table names for session metadata (`sessions_table`) and message data (`messages_table`) can also be customized, with defaults of `'agent_sessions'` and `'agent_messages'` respectively. The constructor manages connection pooling, using a shared connection for in-memory databases to ensure thread safety and thread-local connections for file-based databases to optimize concurrency. Database schema initialization is performed once for file-based databases, ensuring persistence.

--------------------------------

### MCP Servers > MCPServer > __init__

Source: https://openai.github.io/openai-agents-python/ref/mcp/server

The `__init__` method initializes an `MCPServer` instance. It accepts a `use_structured_content` parameter, which defaults to `False`. This parameter dictates whether the server should prioritize using `tool_result.structured_content` when invoking an MCP tool. Setting it to `True` is recommended if the server does not duplicate structured information within the `tool_result.content` field, preventing redundant data.

--------------------------------

### Source code in src/agents/tracing/traces.py

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/traces

A no-op implementation of Trace that doesn't record any data. It is used when tracing is disabled but trace operations still need to function. This class maintains proper context management but does not store or export any data, ensuring that operations can proceed without interruption or data logging when tracing is not active. For example, when tracing is disabled, traces automatically become instances of `NoOpTrace`, allowing operations like `Runner.run` to execute without recording any trace information.

--------------------------------

### function_schema

Source: https://openai.github.io/openai-agents-python/zh/ref/function_schema

The `function_schema` function takes a Python function as input and extracts a `FuncSchema` object. This schema contains crucial metadata about the function, including its name, a detailed description, and descriptions for each of its parameters. It supports overriding the function's default name and description, and intelligently uses docstring information to populate these fields. The `use_docstring_info` parameter controls whether docstring content is leveraged for generating metadata, while `strict_json_schema` ensures the output adheres to the strict JSON schema standard expected by the OpenAI API, which is highly recommended for better LLM interaction.

--------------------------------

### ModelSettings > extra_query

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

Additional query fields to provide with the request. Defaults to None if not provided.

--------------------------------

### Spans

Source: https://openai.github.io/openai-agents-python/ref/tracing/spans

The `export()` method is intended to serialize the span's data into a dictionary format, which can be useful for logging or sending to external tracing systems. It may return `None` if the span is not yet ready for export or if there's no data to export.

The `started_at` property indicates when the span began its execution, returning an ISO format timestamp. If the span has not yet started, it returns `None`.

The `ended_at` property indicates when the span completed its execution, returning an ISO format timestamp. If the span has not yet finished, it returns `None`.

--------------------------------

### __init__

Source: https://openai.github.io/openai-agents-python/ref/memory

The `__init__` method configures the SQLite session by establishing a connection to the database. It handles both in-memory and file-based databases. For in-memory databases, a shared connection is used to ensure thread safety. For file-based databases, thread-local connections are employed for better concurrency. The database is configured to use `PRAGMA journal_mode=WAL` for improved write performance and durability. The `_init_db_for_connection` method is called to set up the necessary database schema if it doesn't already exist.

--------------------------------

### Trace > export

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

Export the trace data as a serializable dictionary.

Returns:
    dict | None: Dictionary containing trace data, or None if tracing is disabled.

Notes:
- Includes all spans and their data
- Used for sending traces to backends
- May include metadata and group ID

--------------------------------

### Complete example

Source: https://openai.github.io/openai-agents-python/realtime/quickstart

This section provides a complete, working example demonstrating the capabilities of the OpenAI Agents Python library. It illustrates how to create a `RealtimeAgent`, configure a `RealtimeRunner` with specific model and audio settings, and then run a session. The example showcases handling various events during the session, such as agent start/end, tool usage, and audio processing. It also includes utility functions for managing output and running the asyncio event loop.

--------------------------------

### Usage

Source: https://openai.github.io/openai-agents-python/ja/ref/usage

The `__post_init__` method in the `Usage` class is designed to normalize token details, ensuring consistency even when certain fields are not provided or are `None`. This is particularly important because some LLM providers might omit optional token detail fields, and the generated SDK code could potentially bypass Pydantic validation, allowing `None` values. By explicitly checking for `None` values in `input_tokens_details.cached_tokens` and `output_tokens_details.reasoning_tokens`, this method ensures that these fields are initialized to `0`, thereby preventing potential `TypeError` exceptions during subsequent operations.

--------------------------------

### __init__

Source: https://openai.github.io/openai-agents-python/ref/memory

Initializes the SQLite session. The `session_id` parameter is a required unique identifier for the conversation session. The `db_path` specifies the location of the SQLite database file, defaulting to an in-memory database (`:memory:`). You can also provide a file path for persistent storage. The `sessions_table` and `messages_table` parameters allow customization of the table names used for storing session metadata and message data, respectively, with default names provided.

--------------------------------

### Span

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/spans

A span represents a single operation within a trace (e.g., an LLM call, tool execution, or agent run). Spans track timing, relationships between operations, and operation-specific data. They automatically nest under the current trace and should be managed using context managers for reliable start and finish.

When handling errors, use the `set_error()` method to record details about the exception, including a message and any relevant data. It's important to avoid including sensitive information in the error data. The example demonstrates wrapping a potentially risky operation in a `try...except` block to catch exceptions and log them using `span.set_error()` before re-raising the exception.

--------------------------------

### OpenAI Agents Python > input_tokens_details

Source: https://openai.github.io/openai-agents-python/ko/ref/usage

Details about the input tokens, matching responses API usage details.

--------------------------------

### Span Class

Source: https://openai.github.io/openai-agents-python/ref/tracing

A span represents a single operation within a trace (e.g., an LLM call, tool execution, or agent run). Spans track timing, relationships between operations, and operation-specific data. They are designed to be used with context managers for reliable start and finish, and automatically nest under the current trace. It's important to handle errors properly using the `set_error()` method and to include relevant data without sensitive information.

--------------------------------

### store_run_usage `async`

Source: https://openai.github.io/openai-agents-python/ko/ref/extensions/memory/advanced_sqlite_session

Store usage data for the current conversation turn. This is designed to be called after `Runner.run()` completes. Session-level usage can be aggregated from turn data when needed.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ref/model_settings

The `ModelSettings` class includes parameters to control various aspects of LLM behavior. `temperature` and `top_p` influence the randomness and creativity of the output. `frequency_penalty` and `presence_penalty` can be used to discourage repetitive language. `tool_choice` and `parallel_tool_calls` govern how the model interacts with tools, allowing for single or multiple tool invocations per turn. `truncation` manages how long text inputs are handled, with options for automatic or disabled strategies.

--------------------------------

### Tracing > Higher level traces

Source: https://openai.github.io/openai-agents-python/tracing

Sometimes, you might want multiple calls to `run()` to be part of a single trace. You can do this by wrapping the entire code in a `trace()`. Example: ```python from agents import Agent, Runner, trace async def main(): agent = Agent(name="Joke generator", instructions="Tell funny jokes.") with trace("Joke workflow"): first_result = await Runner.run(agent, "Tell me a joke") second_result = await Runner.run(agent, f"Rate this joke: {first_result.final_output}") print(f"Joke: {first_result.final_output}") print(f"Rating: {second_result.final_output}") ```

--------------------------------

### Usage

Source: https://openai.github.io/openai-agents-python/ko/ref/usage

The `add` method facilitates the aggregation of usage data from one `Usage` object into another. This is particularly useful when combining usage statistics from multiple LLM calls or different components of an application. The method increments the total counts for requests, input tokens, output tokens, and total tokens. It also carefully merges the token detail fields, summing up `cached_tokens` and `reasoning_tokens`. A significant aspect of this method is its automatic preservation of `request_usage_entries`. If the `other` `Usage` object represents a single, distinct request with a non-zero token count, it is appended to the `request_usage_entries` list of the current object, maintaining a detailed history of individual request costs.

--------------------------------

### handoff_history_mapper

Source: https://openai.github.io/openai-agents-python/ko/ref/run

Optional function that receives the normalized transcript (history + handoff items) and returns the input history that should be passed to the next agent. When left as `None`, the runner collapses the transcript into a single assistant message. This function only runs when `nest_handoff_history` is True.

--------------------------------

### spans.py > span_data

Source: https://openai.github.io/openai-agents-python/ref/tracing

Operation-specific data for this span. This attribute holds data tailored to the specific type of span, such as details related to a Large Language Model (LLM) generation.

--------------------------------

### Handoffs

Source: https://openai.github.io/openai-agents-python/ko/ref/handoffs

The `default_handoff_history_mapper` function, when provided with a transcript (a list of `TResponseInputItem`), returns a single assistant message that summarizes the transcript. This is used to condense the conversation history before passing it to the next agent in a handoff process.

--------------------------------

### RunConfig `dataclass` > trace_metadata `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/zh/ref/run

The `trace_metadata` attribute is an optional dictionary that can include additional metadata to be associated with the trace. This allows for the enrichment of trace data with custom information relevant to the specific run, which can be helpful for analysis and filtering.

--------------------------------

### Usage > Enabling usage with LiteLLM models

Source: https://openai.github.io/openai-agents-python/usage

When using LiteLLM providers, usage metrics are not reported by default. To enable usage tracking, you must pass `ModelSettings(include_usage=True)` when initializing your `LitellmModel`. This ensures that LiteLLM responses populate the `result.context_wrapper.usage` object.

Example:
```python
from agents import Agent, ModelSettings, Runner
from agents.extensions.models.litellm_model import LitellmModel

agent = Agent(
    name="Assistant",
    model=LitellmModel(model="your/model", api_key="..."),
    model_settings=ModelSettings(include_usage=True),
)

result = await Runner.run(agent, "What's the weather in Tokyo?")
print(result.context_wrapper.usage.total_tokens)
```

--------------------------------

### trace

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

The `trace` function is used to create a new trace. A trace represents a logical workflow or process. You must either use the trace as a context manager (using `with trace(...)`) or manually call `trace.start()` and `trace.finish()` to manage its lifecycle. This function allows you to specify a `workflow_name` to identify the logical application or workflow, such as "code_bot" for a coding agent. Optionally, you can provide a `trace_id` for a specific trace, a `group_id` to link multiple related traces (e.g., from the same conversation), and a `metadata` dictionary for attaching custom information. The `tracing` parameter allows for optional tracing configuration for exporting, and `disabled` can be set to `True` to create a trace object that will not be recorded. If `trace_id` is not provided, a new ID will be generated, and it's recommended to use `util.gen_trace_id()` for correct formatting.

--------------------------------

### AdvancedSQLiteSession > __init__

Source: https://openai.github.io/openai-agents-python/ref/extensions/memory/advanced_sqlite_session

The `__init__` method for `AdvancedSQLiteSession` initializes the session with a `session_id`, a path to the SQLite database (`db_path`), an option to create tables (`create_tables`), and a logger. If `create_tables` is set to `True`, it calls `_init_structure_tables()` to set up the necessary database schema. It also initializes `_current_branch_id` to 'main' and sets up the logger.

--------------------------------

### __init__

Source: https://openai.github.io/openai-agents-python/zh/ref/memory

The `__init__` method initializes the SQLite session. It takes a unique `session_id` for the conversation, an optional `db_path` for the database file (defaulting to an in-memory database), and optional names for the session and message tables. It configures the database connection, including setting `PRAGMA journal_mode=WAL` for improved performance. For in-memory databases, a shared connection is used to avoid thread isolation issues, while file-based databases utilize thread-local connections. The database schema is initialized once for persistent file databases.

--------------------------------

### trace

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

Create a new trace. The trace will not be started automatically; you should either use it as a context manager (`with trace(...):`) or call `trace.start()` + `trace.finish()` manually.

In addition to the workflow name and optional grouping identifier, you can provide an arbitrary metadata dictionary to attach additional user-defined information to the trace.

--------------------------------

### openai-agents-python/message_structure.py > MessageStructure > _add_structure_metadata

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/memory/advanced_sqlite_session

The `_add_structure_metadata` method enriches incoming message items with crucial structural metadata before they are added to the session. This metadata includes assigning turn numbers that are specific to each branch (not global), explicit sequence numbers for precise ordering of messages within a turn, and linking messages to their unique database IDs for robust tracking. It also correctly handles scenarios where multiple user messages are submitted in a single batch.

--------------------------------

### `Handoff prompt`

Source: https://openai.github.io/openai-agents-python/ko/ref/extensions/handoff_prompt

The `RECOMMENDED_PROMPT_PREFIX` is a system context that defines the agent's role within a multi-agent system called the Agents SDK. It emphasizes that the system is designed to make agent coordination and execution easy.

--------------------------------

### __init__

Source: https://openai.github.io/openai-agents-python/zh/ref/memory/sqlite_session

The `__init__` method initializes the `SqliteSession` object. It sets up the session ID, database path, and table names for sessions and messages. It also initializes threading locals and locks for managing database connections. A key aspect is how it handles in-memory versus file-based databases: in-memory databases use a shared connection across threads, while file-based databases utilize thread-local connections for better concurrency. The database schema is initialized once for file-based databases, ensuring persistence.

--------------------------------

### Agent Attributes > name

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

Represents the unique identifier for the agent.

--------------------------------

### Trace Class > export

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/traces

The `export` method serializes the trace data into a dictionary. This dictionary contains all recorded spans and their associated data, and can be used for sending traces to various backends. If tracing is disabled, this method returns `None`. The exported data may also include additional metadata and group identifiers.

--------------------------------

### engine `property`

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/memory/sqlalchemy_session

This property provides direct access to the engine for advanced use cases, such as checking connection pool status, configuring engine settings, or manually disposing the engine when needed.

--------------------------------

### Usage

Source: https://openai.github.io/openai-agents-python/zh/ref/usage

The `Usage` dataclass is used to track the token consumption and request counts for LLM API interactions. It includes fields for total requests, input tokens, output tokens, and detailed token breakdowns for both input and output. The `input_tokens_details` and `output_tokens_details` provide more granular information, such as cached tokens and reasoning tokens, which can be helpful for cost analysis and understanding API behavior. The `total_tokens` field represents the sum of input and output tokens for all requests.

Additionally, the `request_usage_entries` list stores individual `RequestUsage` objects, preserving a per-request breakdown of token usage. This is particularly useful when detailed cost calculations or context window management are required, as it allows for analysis of each API call's contribution to the overall token count.

--------------------------------

### RealtimeAgent > instructions

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/agent

The `instructions` parameter for `RealtimeAgent` defines the agent's system prompt. It can be provided as a plain string or as a callable function that dynamically generates instructions. If a function is provided, it will be invoked with the `RunContextWrapper` and the agent instance itself, and it must return a string. This allows for flexible and context-aware instruction generation. If `instructions` is neither a string nor a callable, an error will be logged.

--------------------------------

### Span Class > export

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `export()` method is used to export the span's data, typically for logging or transmission to a tracing backend. It returns a dictionary representation of the span or `None` if no data is available.

--------------------------------

### openai-agents-python/span_data.py > SpeechSpanData

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

The `SpeechSpanData` class represents a speech-related span in the trace. It inherits from `SpanData` and includes details such as input, output, the model used, model configuration, and the timestamp of the first content. This class is useful for tracking and analyzing speech processing operations within a larger trace.

--------------------------------

### Spans > ended_at

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

When the span finished execution. This is an ISO format timestamp indicating the exact moment the operation concluded. If the span has not yet finished, this will be `None`.

--------------------------------

### MCP Servers > MCPServer

Source: https://openai.github.io/openai-agents-python/ref/mcp/server

The `MCPServer` class serves as the base class for Model Context Protocol (MCP) servers. It defines the core interface that all MCP servers must implement. This includes methods for connecting to and cleaning up the server connection, listing available tools and prompts, and calling specific tools or retrieving prompts. The constructor also accepts an optional `use_structured_content` boolean argument, which determines whether to utilize structured content from tool results. This parameter defaults to `False` for backward compatibility, as many existing MCP servers embed structured data within the general content field.

--------------------------------

### MCPServerStreamableHttp > __init__

Source: https://openai.github.io/openai-agents-python/ja/ref/mcp/server

The `__init__` method for `MCPServerStreamableHttp` allows for detailed configuration of the server. Key parameters include `params`, which holds server configuration such as URL, headers, and timeouts for both HTTP requests and Streamable HTTP connections. Additional options include `cache_tools_list` to optimize latency by caching tool lists, `name` for server identification, `client_session_timeout_seconds` for the client session read timeout, `tool_filter` for controlling tool accessibility, `use_structured_content` to manage how tool results are processed, and parameters for retry mechanisms (`max_retry_attempts`, `retry_backoff_seconds_base`). An optional `message_handler` can also be provided.

--------------------------------

### function_tool

Source: https://openai.github.io/openai-agents-python/ko/ref/tool

The `function_tool` decorator offers several parameters for customization. The `name_override` and `description_override` parameters allow you to specify a custom name and description for the tool, respectively, instead of using the function's name and docstring. The `use_docstring_info` boolean flag (defaulting to `True`) controls whether the docstring is used for description generation. For error handling, `failure_error_function` can be provided to customize error messages sent to the LLM upon tool failure; if set to `None`, an exception will be raised instead. The `strict_mode` parameter (defaulting to `True`) enforces strict JSON schema validation, which is recommended for better input accuracy. The `is_enabled` parameter, which can be a boolean or a callable, determines if the tool is visible to the LLM at runtime. Finally, `tool_input_guardrails` and `tool_output_guardrails` allow for pre- and post-invocation validation of tool inputs and outputs.

--------------------------------

### openai-agents-python/src/session.py > SQLiteSession > _add_structure_metadata

Source: https://openai.github.io/openai-agents-python/ko/ref/extensions/memory/advanced_sqlite_session

The `_add_structure_metadata` method is designed to enrich incoming message items with crucial structural metadata before they are stored. This process involves assigning turn numbers on a per-branch basis, rather than a global session-wide count, ensuring that conversation flow is tracked accurately within different branches. It also assigns explicit sequence numbers to guarantee the precise ordering of messages, which is vital for reconstructing conversation history. Furthermore, it links each message to its corresponding database ID for efficient structure tracking and correctly handles scenarios where multiple user messages might be submitted within a single batch.

--------------------------------

### ReasoningItem `dataclass`

Source: https://openai.github.io/openai-agents-python/ko/ref/items

The `ReasoningItem` dataclass represents a reasoning item within the agent's run. It holds the raw reasoning item and specifies its type as 'reasoning_item'.

--------------------------------

### RealtimeAgent > handoffs

Source: https://openai.github.io/openai-agents-python/ref/realtime/agent

Handoffs enable an agent to delegate tasks to other sub-agents. By providing a list of `handoffs`, the agent can intelligently choose to delegate when appropriate, promoting modularity and separation of concerns within the agent system.

--------------------------------

### openai-agents-python/src/agents/realtime/config.py > Client Messages > type

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/config

The type of the message.

--------------------------------

### Spans > trace_id

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The ID of the trace this span belongs to. This is a unique identifier that links this span to its parent trace, allowing for the reconstruction of the entire workflow.

--------------------------------

Source: https://openai.github.io/openai-agents-python/zh/ref/extensions/litellm

The `_convert_gemini_extra_content_to_provider_specific_fields` method is designed to transform Gemini model-specific `extra_content` into the `provider_specific_fields` format required by `litellm`. This is particularly useful for handling tool calls that include a `thought_signature` for Gemini. The method identifies tool calls within assistant messages that appear after the last user message. It then restructures these tool calls

--------------------------------

### ModelSettings > temperature

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

The temperature to use when calling the model.

--------------------------------

### Model Settings > temperature

Source: https://openai.github.io/openai-agents-python/ref/model_settings

The temperature to use when calling the model.

--------------------------------

### AgentBase `dataclass` > handoff_description `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

The `handoff_description` is an optional string that provides a summary of the agent's purpose and functionality. This description is particularly useful when an agent is designed to be handed off to another agent or system, such as a large language model (LLM). It enables the receiving entity to understand what the agent does and determine the appropriate conditions under which to invoke it.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ko/ref/model_settings

The `ModelSettings` class allows for the configuration of various parameters that influence how a Large Language Model (LLM) behaves. These include `temperature` for controlling randomness, `top_p` for nucleus sampling, `frequency_penalty` and `presence_penalty` for adjusting token repetition, and `tool_choice` for specifying how tools should be utilized. Additionally, `parallel_tool_calls` can be enabled or disabled to control whether the model can execute multiple tool calls simultaneously.

--------------------------------

### __init__

Source: https://openai.github.io/openai-agents-python/ja/ref/memory/sqlite_session

The `__init__` method initializes the SQLite session. It takes a `session_id` as a required argument, which is a unique identifier for the conversation. Optional arguments include `db_path` for specifying the database file location (defaults to an in-memory database), `sessions_table` for the name of the table storing session metadata (defaults to 'agent_sessions'), and `messages_table` for the name of the table storing message data (defaults to 'agent_messages'). The constructor sets up threading locals and locks for managing database connections, distinguishing between in-memory and file-based databases for appropriate connection handling. For in-memory databases, a shared connection is established, while file-based databases use thread-local connections. The database schema is initialized using `_init_db_for_connection`.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/zh/ref/model_settings

The `verbosity` setting controls the level of detail in the model's response. Options usually range from `low` for concise answers to `high` for more elaborate explanations.

--------------------------------

### OpenAI Agents Python API Reference > default_handoff_history_mapper

Source: https://openai.github.io/openai-agents-python/ja/ref/handoffs

Return a single assistant message summarizing the transcript.

--------------------------------

### speech_span

Source: https://openai.github.io/openai-agents-python/ref/tracing

The `speech_span` function is used to create a new speech span for tracing purposes. This span is not automatically started; you must explicitly start and finish it using either a `with speech_span() as span:` block or by calling `span.start()` and `span.finish()` manually. This function allows you to log details related to text-to-speech operations, such as the model used, the input text, and the audio output format. It also supports configuring various parameters like `model_config`, `first_content_at`, `span_id`, and `parent` for detailed tracing.

--------------------------------

### SQLiteSession

Source: https://openai.github.io/openai-agents-python/ja/ref/memory

The `_init_db_for_connection` method is responsible for setting up the necessary database schema. It creates two tables if they do not already exist: `agent_sessions` for storing session metadata like `session_id`, `created_at`, and `updated_at`; and `agent_messages` for storing the actual message data, including a unique `id`, the `session_id` it belongs to, the `message_data` itself, and a `created_at` timestamp. This ensures the database is properly structured for storing conversation history.

--------------------------------

### Agent Attributes > handoffs

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

Handoffs are sub-agents that the agent can delegate to. You can provide a list of handoffs, and the agent can choose to delegate to them if relevant. Allows for separation of concerns and modularity.

--------------------------------

### RunConfig `dataclass` > tracing `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/zh/ref/run

The `tracing` attribute allows for detailed configuration of tracing for an agent run. It accepts a `TracingConfig` object, enabling fine-grained control over how traces are generated, stored, and analyzed. This is essential for debugging, monitoring, and understanding the execution flow of complex agent workflows.

--------------------------------

### Automatic argument and docstring parsing

Source: https://openai.github.io/openai-agents-python/tools

The `agents` library automatically parses function signatures to extract the schema for the tool and parses docstrings to extract descriptions for the tool and its arguments. Signature parsing uses the `inspect` module and type annotations to build a Pydantic model for the schema, supporting various types like primitives, Pydantic models, and TypedDicts. Docstring parsing utilizes `griffe` for `google`, `sphinx`, and `numpy` formats, with automatic detection or explicit setting. Docstring parsing can be disabled by setting `use_docstring_info` to `False`.

--------------------------------

### RealtimeAgent > tools

Source: https://openai.github.io/openai-agents-python/ref/realtime/agent

The `tools` attribute is a list of tools that the agent can access and utilize to perform its tasks. These tools extend the agent's capabilities beyond its core functionality.

--------------------------------

### OutputGuardrail `dataclass` > name `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ja/ref/guardrail

The name of the guardrail, used for tracing. If not provided, we'll use the guardrail function's name.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ko/ref/model_settings

For managing model responses and caching, `ModelSettings` includes options like `metadata` for additional information, `store` to control response persistence, and `prompt_cache_retention` which can be set to 'in_memory' or '24h' to extend prompt caching durations. The `include_usage` boolean flag can be set to true to include usage data, specifically for the Chat Completions API. The `response_include` parameter allows for specifying additional output data to be included in the model's response.

--------------------------------

### Span > export

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/spans

The `export()` method is used to export the span's data, typically for logging or transmission to a tracing backend. It returns a dictionary representation of the span or `None` if the span has not been exported.

--------------------------------

### Memory > Session > add_items

Source: https://openai.github.io/openai-agents-python/ko/ref/memory

Add new items to the conversation history. The `items` parameter is a list of input items to be added to the session's history.

--------------------------------

### spans.py > ended_at

Source: https://openai.github.io/openai-agents-python/ref/tracing

When the span finished execution. Similar to `started_at`, this is an ISO format timestamp. If the span has not yet completed, this value will be None.

--------------------------------

### SessionABC

Source: https://openai.github.io/openai-agents-python/ja/ref/memory/session

Session stores conversation history for a specific session, allowing agents to maintain context without requiring explicit manual memory management. This ABC is intended for internal use and as a base class for concrete implementations. Third-party libraries should implement the Session protocol instead.

--------------------------------

### openai-agents-python/src/agents/realtime/config.py > Tracing Configuration > group_id

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/config

A group identifier to use for tracing, to link multiple traces together.

--------------------------------

### FunctionTool `dataclass`

Source: https://openai.github.io/openai-agents-python/ref/tool

The `FunctionTool` dataclass represents a tool that wraps a Python function. It is designed to be easily integrated with language models by providing essential metadata. The `name` attribute serves as the identifier for the tool as presented to the LLM, typically mirroring the function's name. A detailed `description` is also provided for the LLM to understand the tool's purpose. The `params_json_schema` defines the expected structure and types of arguments the tool accepts, ensuring that the LLM generates valid inputs. The core functionality is encapsulated in the `on_invoke_tool` callable, which executes the wrapped function with the provided context and arguments. Additionally, `strict_json_schema` enforces adherence to the defined schema, improving input reliability. The `is_enabled` attribute allows for dynamic control over tool availability, either as a static boolean or a callable that checks conditions based on the current run context and agent state. Finally, `tool_input_guardrails` and `tool_output_guardrails` can be specified to add pre- and post-invocation validation steps, respectively, enhancing robustness and safety.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

Use `extra_body` to include any additional fields in the request body that are not part of the standard `ModelSettings`. These extra fields are passed directly to the model provider's API.

--------------------------------

### Tools > ShellExecutor

Source: https://openai.github.io/openai-agents-python/zh/ref/tool

Executes a shell command sequence and returns either text or structured output.

--------------------------------

### OpenAI Agents Python > function_tool.py

Source: https://openai.github.io/openai-agents-python/ref/tool

The `function_tool` decorator offers several customization options. You can override the default tool name and description using `name_override` and `description_override`. The `docstring_style` parameter allows you to specify the docstring format if auto-detection fails. By default, `use_docstring_info` is `True`, enabling the use of docstring content for descriptions. You can define a custom `failure_error_function` to handle tool call failures, which sends an error message to the LLM. The `strict_mode` parameter, recommended to be `True`, enforces strict JSON schema validation for tool inputs, improving reliability. The `is_enabled` parameter controls whether the tool is available to the LLM, accepting a boolean or a callable that dynamically determines enablement based on the run context and agent.

--------------------------------

### RealtimeAgent > instructions

Source: https://openai.github.io/openai-agents-python/ref/realtime/agent

The `instructions` parameter for `RealtimeAgent` defines the agent's behavior and response strategy, serving as its system prompt. It can be provided as a static string or a dynamically generated function. If a function is supplied, it receives the `run_context` and the `agent` instance, and must return a string. This allows for flexible and context-aware instruction generation.

--------------------------------

### Agent Configuration > Agent Attributes > Hooks

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

The `hooks` attribute allows for callbacks during various lifecycle events of the agent. This is useful for monitoring or reacting to specific stages of agent execution.

--------------------------------

### custom_span

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

When creating a custom span, you must provide a `name` which is a string representing the span's identifier. You can also optionally include `data`, a dictionary for arbitrary structured information, a `span_id` if you wish to manually assign one (though it's recommended to use `util.gen_span_id()` for proper formatting), and a `parent` span or trace. If no parent is specified, the current trace or span will be used automatically. Setting `disabled` to `True` will create a Span object but prevent it from being recorded.

--------------------------------

### Tracing > export

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `export` method serializes the trace data, including all spans and their associated information, into a dictionary. This dictionary can then be used for sending trace data to external backends or for logging purposes. If tracing is disabled, this method may return `None`. The exported data might also include metadata and a group ID for further organization.

--------------------------------

### AgentBase `dataclass`

Source: https://openai.github.io/openai-agents-python/ref/agent

The `AgentBase` is a `dataclass` that serves as the foundational base class for both `Agent` and `RealtimeAgent`. It is generic over a `TContext` type. It includes several key attributes:

*   `name`: A `str` representing the unique identifier for the agent.
*   `handoff_description`: An optional `str` that provides a description of the agent's purpose. This is crucial for LLMs to understand what the agent does and when to invoke it, especially when it's used as a handoff.
*   `tools`: A `list` of `Tool` objects that the agent can utilize to perform actions.
*   `mcp_servers`: A `list` of `MCPServer` objects. These servers provide additional tools to the agent. The agent will incorporate tools from these servers every time it runs. It's important to note that the developer is responsible for managing the lifecycle of these MCP servers, including connecting them before use and cleaning them up afterwards.
*   `mcp_config`: An `MCPConfig` object that holds configuration settings for the MCP servers.

--------------------------------

### AgentBase `dataclass` > handoff_description `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

The `handoff_description` is an optional string that provides a clear explanation of the agent's purpose and capabilities. This description is particularly important when the agent is being handed off to another system or an LLM, ensuring the receiving entity understands what the agent does and when it should be invoked.

--------------------------------

### Span Class > span_data

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `span_data` property returns operation-specific data for this span, such as LLM generation data.

--------------------------------

### OpenAI Agents Python API Reference > get_conversation_history_wrappers

Source: https://openai.github.io/openai-agents-python/ja/ref/handoffs

Return the current start/end markers used for the nested conversation summary.

--------------------------------

### Tracing

Source: https://openai.github.io/openai-agents-python/mcp

Tracing automatically captures MCP activity, including calls to the MCP server to list tools and MCP-related information on tool calls.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/zh/ref/model_settings

The `extra_query` field allows you to provide additional query parameters that will be appended to the request. This can be used for options not explicitly covered by the `ModelSettings` class but supported by the underlying API.

--------------------------------

### Handoffs

Source: https://openai.github.io/openai-agents-python/ko/ref/handoffs

The `get_conversation_history_wrappers` function returns the current start and end markers used for nested conversation summaries. These markers define the boundaries of the conversation history that will be included in summaries.

--------------------------------

### __init__

Source: https://openai.github.io/openai-agents-python/zh/ref/voice/pipeline

The `__init__` method is the constructor for the Voice Pipeline. It allows you to create a new voice pipeline instance by specifying the core components it requires. You must provide a `workflow` object, which defines the sequence of operations the pipeline will perform. Optionally, you can specify the speech-to-text (`stt_model`) and text-to-speech (`tts_model`) models to be used. If these are not provided, the pipeline will default to using OpenAI's standard models. Furthermore, you can customize the pipeline's behavior through a `VoicePipelineConfig` object; if no configuration is supplied, a default configuration will be applied.

--------------------------------

### FunctionTool `dataclass` > name `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ref/tool

The `name` attribute of a `FunctionTool` is a string that represents the tool's identifier as it will be shown to the Language Model (LLM). It generally corresponds to the name of the Python function being wrapped.

--------------------------------

### Handoff prompt > RECOMMENDED_PROMPT_PREFIX

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/handoff_prompt

The `RECOMMENDED_PROMPT_PREFIX` is a system context provided to agents within the Agents SDK. It establishes the agent's role as part of a multi-agent system designed for easy coordination and execution. The core abstractions are **Agents** and **Handoffs**. Agents contain instructions and tools and can transfer the conversation to another agent when necessary. These transfers are initiated by calling a handoff function, typically named `transfer_to_<agent_name>`. The system handles these transfers in the background, and agents should not explicitly mention or draw attention to them during user interactions.

--------------------------------

### RealtimeAgent > tools

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/agent

The `tools` attribute is a list of available tools that the agent can leverage to perform its tasks. This allows agents to extend their capabilities by utilizing predefined functions or services.

--------------------------------

### Orchestrating multiple agents > Orchestrating via code

Source: https://openai.github.io/openai-agents-python/multi_agent

While orchestrating via LLM is powerful, orchestrating via code makes tasks more deterministic and predictable, in terms of speed, cost and performance. Common patterns here are:
* Using structured outputs to generate well formed data that you can inspect with your code. For example, you might ask an agent to classify the task into a few categories, and then pick the next agent based on the category.
* Chaining multiple agents by transforming the output of one into the input of the next. You can decompose a task like writing a blog post into a series of steps - do research, write an outline, write the blog post, critique it, and then improve it.
* Running the agent that performs the task in a `while` loop with an agent that evaluates and provides feedback, until the evaluator says the output passes certain criteria.
* Running multiple agents in parallel, e.g. via Python primitives like `asyncio.gather`. This is useful for speed when you have multiple tasks that don't depend on each other.

We have a number of examples in `examples/agent_patterns`.

--------------------------------

### Usage

Source: https://openai.github.io/openai-agents-python/ref/usage

The `__post_init__` method within the `Usage` class ensures data integrity by normalizing token details. It handles cases where certain token detail fields, such as `cached_tokens` or `reasoning_tokens`, might be missing or `None`, especially when providers do not populate them or when the Pydantic validation is bypassed. By defaulting these to 0, the method prevents potential `TypeError` exceptions, ensuring that all calculations involving these fields can proceed without errors. This defensive programming makes the `Usage` class more robust when interacting with various LLM providers and SDK versions.

--------------------------------

### Sessions > Memory operations > Basic operations

Source: https://openai.github.io/openai-agents-python/sessions

Sessions supports several operations for managing conversation history:
*   **Get all items**: Retrieves all stored conversation entries.
*   **Add new items**: Appends new user or assistant messages to the session.
*   **Remove and return the most recent item**: Useful for undoing or correcting the last turn in a conversation.
*   **Clear all items**: Empties the entire conversation history for the session.

--------------------------------

### Trace with metadata and grouping

Source: https://openai.github.io/openai-agents-python/ref/tracing

The `tracing_api_key` property holds the API key required for exporting the trace and its spans. This key is used for authentication when sending trace data to a remote service or backend.

--------------------------------

### Spans > span_id

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

Unique identifier for this span. This ID uniquely distinguishes this span within its trace, enabling precise referencing and analysis of individual operations.

--------------------------------

### AdvancedSQLiteSession > __init__

Source: https://openai.github.io/openai-agents-python/ko/ref/extensions/memory/advanced_sqlite_session

The `__init__` method for `AdvancedSQLiteSession` initializes the session with a unique `session_id`, a path to the SQLite database (`db_path`), and an option to create necessary tables (`create_tables`). It also accepts a `logger` object for custom logging and `**kwargs` for additional parameters. If `create_tables` is set to `True`, it calls `_init_structure_tables()` to set up the database schema. The session starts with a default branch ID of 'main', and any provided logger is assigned to `_logger`.

--------------------------------

### Span Class > finish

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `finish()` method concludes the span's execution. If `reset_current` is true, the span will be reset as the current span.

--------------------------------

### traces.py > start

Source: https://openai.github.io/openai-agents-python/ref/tracing/traces

The `start` method initiates a trace and has an option to mark it as the current trace in the execution context. This method must be called before any spans can be added to the trace. It's important to note that only one trace can be the current trace at any given time. The `mark_as_current` parameter, when set to `True`, designates this trace as the active one.

--------------------------------

### session_input_callback

Source: https://openai.github.io/openai-agents-python/ko/ref/run

Defines how to handle session history when new input is provided. - `None` (default): The new input is appended to the session history. - `SessionInputCallback`: A custom function that receives the history and new input, and returns the desired combined list of items.

--------------------------------

### Results > RunResultBase dataclass > input instance-attribute

Source: https://openai.github.io/openai-agents-python/ko/ref/result

The `input` attribute of the `RunResultBase` dataclass stores the initial data provided to the agent. This can be a single string or a list of `TResponseInputItem` objects. It's important to note that this `input` might be a modified version of the very first input if any `handoff input filters` were applied, which could alter the data before it's processed by the main agent logic.

--------------------------------

### MCPServerStdio > __init__

Source: https://openai.github.io/openai-agents-python/ko/ref/mcp/server

The `use_structured_content` parameter in `MCPServerStdio` determines whether the `tool_result.structured_content` field is utilized when invoking an MCP tool. By default, this is set to `False` for backward compatibility, as many existing MCP servers embed structured content within the `tool_result.content` field, leading to duplication if `use_structured_content` were `True`. Setting this to `True` is advisable only if you are certain that the server does not duplicate structured content in its regular content field.

--------------------------------

### Trace Class > start

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/traces

The `start` method initializes a trace. It can optionally mark the trace as the current trace in the execution context. This method must be called before any spans can be added to the trace. While only one trace can be the current trace at any given time, the `start` method is thread-safe when `mark_as_current` is used.

--------------------------------

### traces.py > export

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/traces

The `export` method serializes the trace data into a dictionary. This dictionary contains all recorded spans and their associated data, making it suitable for sending to backend systems. If tracing is disabled, this method returns `None`. The exported data may also include metadata and group IDs.

--------------------------------

### Agent Parameters

Source: https://openai.github.io/openai-agents-python/ref/agent

Whether to reset the tool choice to the default value after a tool has been called. Defaults to True. This ensures that the agent doesn't enter an infinite loop of tool usage.

--------------------------------

### openai-agents-python/src/agents/realtime/config.py > Tracing Configuration > workflow_name

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/config

The workflow name to use for tracing.

--------------------------------

### Tools > MCPToolApprovalFunction

Source: https://openai.github.io/openai-agents-python/zh/ref/tool

A function that approves or rejects a tool call.

--------------------------------

### Workflow > VoiceWorkflowBase

Source: https://openai.github.io/openai-agents-python/ko/ref/voice/workflow

A base class for a voice workflow. You must implement the `run` method. A "workflow" is any code you want, that receives a transcription and yields text that will be turned into speech by a text-to-speech model. In most cases, you'll create `Agent`s and use `Runner.run_streamed()` to run them, returning some or all of the text events from the stream. You can use the `VoiceWorkflowHelper` class to help with extracting text events from the stream. If you have a simple workflow that has a single starting agent and no custom logic, you can use `SingleAgentVoiceWorkflow` directly.

--------------------------------

### Usage > request_usage_entries

Source: https://openai.github.io/openai-agents-python/ref/usage

The `request_usage_entries` attribute is a list that stores detailed `RequestUsage` objects for each individual LLM API call. When new usage is added via the `add()` method, an entry is created in this list if the usage represents a distinct request (i.e., has non-zero tokens). This list is essential for accurate per-request cost calculation and can also be valuable for managing context window limitations. For instance, if a run involves three API calls with distinct input token counts (e.g., 100K, 150K, and 80K), the aggregated `input_tokens` would sum these up (330K), but `request_usage_entries` would maintain the individual [100K, 150K, 80K] breakdown, allowing for more granular analysis.

--------------------------------

### Voice Workflow API > SingleAgentVoiceWorkflow

Source: https://openai.github.io/openai-agents-python/ko/ref/voice/workflow

A simple voice workflow that runs a single agent. Each transcription and result is added to the input history. For more complex workflows (e.g. multiple Runner calls, custom message history, custom logic, custom configs), subclass `VoiceWorkflowBase` and implement your own logic.

--------------------------------

### SQLiteSession

Source: https://openai.github.io/openai-agents-python/ko/ref/memory/sqlite_session

The `_init_db_for_connection` method is responsible for setting up the necessary database schema. It creates two tables if they do not already exist: `agent_sessions` for storing session metadata (like `session_id`, `created_at`, `updated_at`) and `agent_messages` for storing the actual conversation messages (including `session_id`, `message_data`, and `created_at`). This ensures that the database is properly structured to store and retrieve conversation data.

--------------------------------

### FunctionTool `dataclass`

Source: https://openai.github.io/openai-agents-python/zh/ref/tool

The `FunctionTool` offers several configuration options to enhance its utility and safety. The `strict_json_schema` attribute, recommended to be set to `True`, enforces that the parameters provided by the LLM adhere strictly to the defined JSON schema, which helps in preventing errors and ensuring predictable behavior. The `is_enabled` attribute provides flexibility by allowing the tool to be dynamically enabled or disabled, either through a simple boolean flag or a callable function that can assess the current run context and agent state. Furthermore, `tool_input_guardrails` and `tool_output_guardrails` can be specified as lists of guardrail objects to pre-process tool inputs and post-process tool outputs, respectively, adding layers of validation and transformation to the tool's interaction.

--------------------------------

### Tracing > start

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `start` method initiates a trace. It can optionally mark the trace as the current one in the execution context by setting `mark_as_current` to `True`. This method must be called before any spans can be added to the trace. It's important to note that only one trace can be the 'current' trace at any given time, and the `start` method is thread-safe when `mark_as_current` is used.

--------------------------------

### __init__

Source: https://openai.github.io/openai-agents-python/ko/ref/memory

The `__init__` method initializes the SQLite session with a unique `session_id`. It allows specifying the path to the SQLite database file (`db_path`), which defaults to an in-memory database (`:memory:`). You can also customize the names of the tables used for storing session metadata (`sessions_table`) and message data (`messages_table`). The initialization logic differs based on whether an in-memory or a file-based database is used. For in-memory databases, a shared connection is established to manage thread isolation, while file-based databases utilize thread-local connections for concurrency. The database schema is initialized once for file-based databases as it persists across sessions.

--------------------------------

### DaprSession

Source: https://openai.github.io/openai-agents-python/ref/extensions/memory/dapr_session

The `DaprSession` class provides an implementation of the `SessionABC` for managing conversation sessions using Dapr's state store. It allows for persistent storage of session data, including messages and metadata, leveraging Dapr's capabilities for distributed state management.

Key features include:
*   **Session Identification**: Each session is uniquely identified by a `session_id`.
*   **Dapr Integration**: It utilizes a `DaprClient` to interact with a specified Dapr state store component, identified by `state_store_name`.
*   **Time-to-Live (TTL)**: Supports setting a TTL for session data, though this depends on the underlying Dapr state store's capabilities.
*   **Consistency Levels**: Allows configuration of consistency levels for state operations, supporting `DAPR_CONSISTENCY_EVENTUAL` and `DAPR_CONSISTENCY_STRONG`.
*   **State Keys**: Manages distinct keys for storing messages (`{session_id}:messages`) and metadata (`{session_id}:metadata`) within the Dapr state store.

--------------------------------

### src/agents/mcp/server.py > __init__

Source: https://openai.github.io/openai-agents-python/ko/ref/mcp/server

Create a new MCP server based on the Streamable HTTP transport.

Parameters:
`params`: The params that configure the server. This includes the URL of the server, the headers to send to the server, the timeout for the HTTP request, the timeout for the Streamable HTTP connection, whether we need to terminate on close, and an optional custom HTTP client factory.

`cache_tools_list`: Whether to cache the tools list. If `True`, the tools list will be cached and only fetched from the server once. If `False`, the tools list will be fetched from the server on each call to `list_tools()`. The cache can be invalidated by calling `invalidate_tools_cache()`. You should set this to `True` if you know the server will not change its tools list, because it can drastically improve latency (by avoiding a round-trip to the server every time).

`name`: A readable name for the server. If not provided, we'll create one from the URL.

`client_session_timeout_seconds`: the read timeout passed to the MCP ClientSession.
`tool_filter`: The tool filter to use for filtering tools.
`use_structured_content`: Whether to use `tool_result.structured_content` when calling an MCP tool. Defaults to False for backwards compatibility - most MCP servers still include the structured content in the `tool_result.content`, and using it by default will cause duplicate content. You can set this to True if you know the server will not duplicate the structured content in the `tool_result.content`.
`max_retry_attempts`: Number of times to retry failed list_tools/call_tool calls. Defaults to no retries.

--------------------------------

### FunctionTool `dataclass`

Source: https://openai.github.io/openai-agents-python/zh/ref/tool

The `FunctionTool` is a dataclass designed to wrap a Python function, making it usable as a tool within an agentic system. It simplifies the process of exposing Python functions to large language models (LLMs) by providing a structured way to define their name, description, and parameters. The `FunctionTool` itself holds the core components necessary for an LLM to understand and invoke a function: a `name` for identification, a `description` to explain its purpose, and `params_json_schema` to define the expected input arguments in a machine-readable format. Additionally, it includes an `on_invoke_tool` callable, which is the actual implementation that gets executed when the LLM decides to use the tool, receiving context and parameters, and returning the tool's output or an error.

--------------------------------

### RealtimeModelConfig > initial_model_settings

Source: https://openai.github.io/openai-agents-python/ref/realtime/model

The `initial_model_settings` allows specifying configuration parameters for the model at the start of a session.

--------------------------------

### Session > get_items

Source: https://openai.github.io/openai-agents-python/ref/memory/session

Retrieve the conversation history for this session. You can specify a limit to retrieve the latest N items in chronological order, or retrieve all items if the limit is not specified.

--------------------------------

### function_span

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

The `function_span` function accepts several parameters to configure the span. The `name` parameter is mandatory and specifies the name of the function being traced. Optional parameters include `input` and `output` for logging the function's arguments and return value, respectively. You can also provide a custom `span_id` or let the system generate one automatically, though using `util.gen_span_id()` is recommended for correct formatting. The `parent` parameter allows you to link this span to an existing trace or another span, defaulting to the current active trace/span if not provided. Finally, the `disabled` parameter, when set to `True`, will create a Span object but prevent it from being recorded, which can be useful for conditional tracing.

--------------------------------

### Tracing Exporter > export

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/processor_interface

The `export` method within the `TracingExporter` is an abstract method responsible for exporting a given list of traces and spans. Concrete implementations must define how these items are processed and sent to their intended destination. The `items` parameter is a list containing the traces and spans to be exported.

--------------------------------

### Voice Workflow API > SingleAgentWorkflowCallbacks > on_run

Source: https://openai.github.io/openai-agents-python/ko/ref/voice/workflow

Called when the workflow is run.

--------------------------------

### RealtimeRunner > run

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/runner

Starts and returns a realtime session. This session object allows for bidirectional communication with the realtime model. The `context` parameter can be used to provide initial context for the session, and `model_config` allows for overriding model-specific parameters.

--------------------------------

### Span > span_data

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/spans

The `span_data` property returns operation-specific data for this span, such as LLM generation data. This property is generic and can hold any type of span-specific data.

--------------------------------

### __init__

Source: https://openai.github.io/openai-agents-python/ja/ref/memory

The `__init__` method sets up the SQLite session. It takes a `session_id`, the `db_path` for the SQLite file (defaulting to an in-memory database), and the names for the `sessions_table` and `messages_table`. It initializes thread-local storage and a lock for managing database connections. A key distinction is made between in-memory databases, which use a shared connection to bypass thread isolation issues, and file-based databases, which utilize thread-local connections for better concurrency. For file-based databases, the schema is initialized once as it's persistent.

--------------------------------

### OpenAI Agents Python > openai_agents/llm/openai.py

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/litellm

This section of the code handles the completion call to the `litellm.acompletion` function, passing various parameters such as the model name, messages, tools, temperature, top_p, and other settings. It also manages `stream_options` and `extra_kwargs` derived from `model_settings.extra_query`, `model_settings.metadata`, `model_settings.extra_body`, and `model_settings.extra_args`. A key aspect is the careful handling of `reasoning_effort`, ensuring it's correctly passed and not duplicated if promoted to a top-level argument. The function returns either a `ModelResponse` object or a tuple containing a `Response` object and the raw completion result, depending on the input and processing.

--------------------------------

### Agents

Source: https://openai.github.io/openai-agents-python/agents

Agents are the core building block in your apps. An agent is a large language model (LLM), configured with instructions and tools.

The most common properties of an agent you'll configure are:
  * `name`: A required string that identifies your agent.
  * `instructions`: also known as a developer message or system prompt.
  * `model`: which LLM to use, and optional `model_settings` to configure model tuning parameters like temperature, top_p, etc.
  * `tools`: Tools that the agent can use to achieve its tasks.

--------------------------------

### function_schema

Source: https://openai.github.io/openai-agents-python/ko/ref/function_schema

Given a Python function, extracts a `FuncSchema` from it, capturing the name, description, parameter descriptions, and other metadata.

Args:
    func: The function to extract the schema from.
    docstring_style: The style of the docstring to use for parsing. If not provided, we will attempt to auto-detect the style.
    name_override: If provided, use this name instead of the function's `__name__`.
    description_override: If provided, use this description instead of the one derived from the docstring.
    use_docstring_info: If True, uses the docstring to generate the description and parameter descriptions.
    strict_json_schema: Whether the JSON schema is in strict mode. If True, we'll ensure that the schema adheres to the "strict" standard the OpenAI API expects. We **strongly** recommend setting this to True, as it increases the likelihood of the LLM producing correct JSON input.

Returns:
A `FuncSchema` object containing the function's name, description, parameter descriptions, and other metadata.

--------------------------------

### Spans

Source: https://openai.github.io/openai-agents-python/ref/tracing/spans

The `__enter__` method is part of the context manager protocol, allowing spans to be used with the `with` statement. It typically starts the span and potentially marks it as the current span.

The `__exit__` method is also part of the context manager protocol and is called when exiting the `with` block. It is responsible for finishing the span and handling any exceptions that occurred within the block.

--------------------------------

### BatchTraceProcessor

Source: https://openai.github.io/openai-agents-python/ref/tracing/processors

The `on_trace_start`, `on_trace_end`, `on_span_start`, and `on_span_end` methods handle the ingestion of tracing data.

*   `on_trace_start` and `on_span_end` are responsible for adding traces and spans, respectively, to the internal queue. They first ensure the background worker thread is running using `_ensure_thread_started`. If the queue is full when attempting to add an item, a warning is logged, and the item is dropped.
*   `on_trace_end` and `on_span_start` are no-ops in this implementation, as the processing and export logic is handled by the other two methods and the background worker.

--------------------------------

### ToolGuardrailFunctionOutput dataclass

Source: https://openai.github.io/openai-agents-python/zh/ref/tool_guardrails

The `ToolGuardrailFunctionOutput` dataclass represents the result of a tool guardrail function. It contains two main attributes: `output_info` and `behavior`.

- `output_info`: This attribute holds optional data about any checks performed by the guardrail. It can include details about the checks conducted and their specific outcomes.
- `behavior`: This attribute defines how the system should react based on the guardrail's result. The possible behaviors are:
  - `allow`: Permits the normal execution of the tool to proceed without any intervention.
  - `reject_content`: Stops the tool call or output but allows the execution to continue, providing a message to the model.
  - `raise_exception`: Halts the execution entirely by triggering a `ToolGuardrailTripwireTriggered` exception.

--------------------------------

### Usage > output_tokens_details

Source: https://openai.github.io/openai-agents-python/ref/usage

The `output_tokens_details` attribute offers detailed insights into the output tokens, aligning with the usage details provided by the responses API. This can include specific breakdowns such as reasoning tokens, enabling a deeper understanding of the model's output.

--------------------------------

### MCP Server Streamable HTTP Transport > __init__ > use_structured_content

Source: https://openai.github.io/openai-agents-python/ja/ref/mcp/server

When `use_structured_content` is `True`, the `tool_result.structured_content` will be used for MCP tool calls. The default is `False` for backward compatibility, as many servers include structured content within `tool_result.content`, which could lead to duplication. Enable this option if your server does not duplicate structured content.

--------------------------------

### Spans > parent_id

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

ID of the parent span, if any. This establishes the hierarchical relationship between spans, indicating which span initiated this one. If this is `None`, the span is considered a root span within the trace.

--------------------------------

### Branch workflow example

Source: https://openai.github.io/openai-agents-python/sessions/advanced_sqlite_session

The branch workflow example demonstrates a practical application of branching in conversations. It starts with an initial conversation, storing the usage for each run. A new branch, "weather_focus," is then created from a specific turn (the second turn in this case). Subsequent conversational turns can occur within this new branch, allowing for a focused exploration of a topic. After completing the tasks in the new branch, you can seamlessly switch back to the "main" branch to continue the original conversation flow.

--------------------------------

### Usage > input_tokens_details

Source: https://openai.github.io/openai-agents-python/zh/ref/usage

The `input_tokens_details` attribute provides a more granular breakdown of input token usage, aligning with the details provided in the responses API usage information. It is an instance of `InputTokensDetails`, initialized with cached tokens set to 0 by default.

--------------------------------

### Memory > Session > get_items

Source: https://openai.github.io/openai-agents-python/ref/memory

Retrieve the conversation history for this session. You can specify a limit to retrieve the latest N items in chronological order, or retrieve all items if no limit is specified. The function returns a list of input items representing the conversation history.

--------------------------------

### Mixing models across providers

Source: https://openai.github.io/openai-agents-python/models

You need to be aware of feature differences between model providers, or you may run into errors. For example, OpenAI supports structured outputs, multimodal input, and hosted file search and web search, but many other providers don't support these features. Be aware of these limitations:
  * Don't send unsupported `tools` to providers that don't understand them
  * Filter out multimodal inputs before calling models that are text-only
  * Be aware that providers that don't support structured JSON outputs will occasionally produce invalid JSON.

--------------------------------

### Trace Class > tracing_api_key

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/traces

The `tracing_api_key` property holds the API key used for exporting trace and span data. This key is essential for authenticating and sending trace information to external backends or storage.

--------------------------------

### openai_github_io_openai-agents-python > function_schema

Source: https://openai.github.io/openai-agents-python/ref/function_schema

The `function_schema` function intelligently extracts information for the `FuncSchema` by first looking at the docstring if `use_docstring_info` is `True`. It can also automatically detect the docstring style or accept a specified `docstring_style`. Additionally, it uses type hints from the function signature to infer parameter types. For parameters that have `Annotated` type hints, it can extract descriptions directly from the metadata associated with those annotations, merging this with information derived from the docstring.

--------------------------------

### Memory > Session > add_items

Source: https://openai.github.io/openai-agents-python/ref/memory

Add new items to the conversation history. This function takes a list of input items and appends them to the existing conversation history for the session.

--------------------------------

### Span > started_at

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

When the span started execution. Returns the ISO format timestamp of span start, or `None` if not started.

--------------------------------

### RealtimeAgent > handoffs

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/agent

Handoffs enable an agent to delegate tasks to other sub-agents. By providing a list of `RealtimeAgent` or `Handoff` objects to the `handoffs` attribute, the agent can intelligently choose to delegate when appropriate, promoting modularity and separation of concerns.

--------------------------------

### Span Class > started_at

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `started_at` property returns the ISO format timestamp of when the span started execution. It returns `None` if the span has not yet started.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/zh/ref/model_settings

The `extra_body` parameter enables the inclusion of arbitrary JSON fields directly within the request body. This is useful for passing custom data or parameters that the API might support but are not exposed as specific arguments.

--------------------------------

### Session > add_items

Source: https://openai.github.io/openai-agents-python/ko/ref/memory/session

The `add_items` asynchronous method is used to append new conversation turns to the session's history. It takes a list of `TResponseInputItem` objects as input, which are then added to the stored conversation.

--------------------------------

### MCP Servers > MCPServer > __init__

Source: https://openai.github.io/openai-agents-python/ja/ref/mcp/server

The `__init__` method for `MCPServer` initializes the server instance. It accepts an optional boolean parameter `use_structured_content`, which defaults to `False`. This parameter determines whether the server should prioritize using the `tool_result.structured_content` when invoking an MCP tool. The default setting of `False` is maintained for backward compatibility, as many existing MCP servers embed structured content within the regular `tool_result.content`, leading to potential duplication if `use_structured_content` is enabled. Users can set this to `True` if they are certain that the specific MCP server they are using does not duplicate structured content in its general content field.

--------------------------------

### Session > add_items

Source: https://openai.github.io/openai-agents-python/ref/memory/session

Add new items to the conversation history. This method takes a list of input items and appends them to the existing conversation history for the session.

--------------------------------

### Tracing > Default tracing

Source: https://openai.github.io/openai-agents-python/tracing

By default, the SDK traces the entire `Runner.{run, run_sync, run_streamed}()` which is wrapped in a `trace()`. Each time an agent runs, it is wrapped in `agent_span()`. LLM generations are wrapped in `generation_span()`. Function tool calls are each wrapped in `function_span()`. Guardrails are wrapped in `guardrail_span()`. Handoffs are wrapped in `handoff_span()`. Audio inputs (speech-to-text) are wrapped in a `transcription_span()`. Audio outputs (text-to-speech) are wrapped in a `speech_span()`. Related audio spans may be parented under a `speech_group_span()`. By default, the trace is named "Agent workflow". You can set this name if you use `trace`, or you can configure the name and other properties with the `RunConfig`. In addition, you can set up custom trace processors to push traces to other destinations (as a replacement, or secondary destination).

--------------------------------

### SQLiteSession

Source: https://openai.github.io/openai-agents-python/ref/memory/sqlite_session

The `SQLiteSession` class is initialized with a unique `session_id`, an optional `db_path` for the SQLite database (defaults to an in-memory database), and names for the sessions and messages tables. It handles connection management, differentiating between in-memory databases (using a shared connection for all threads) and file-based databases (using thread-local connections for better concurrency). The database schema, including tables for session metadata and message data, is created if it doesn't already exist.

--------------------------------

### SessionABC > get_items

Source: https://openai.github.io/openai-agents-python/ko/ref/memory/session

Retrieve the conversation history for this session. You can specify a limit to retrieve the latest N items in chronological order, or retrieve all items if no limit is specified.

--------------------------------

### FunctionTool `dataclass` > params_json_schema `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ref/tool

The `params_json_schema` attribute of a `FunctionTool` is a dictionary that defines the JSON schema for the parameters expected by the wrapped function. This schema dictates the structure, data types, and constraints of the arguments that the LLM should provide when invoking the tool.

--------------------------------

### traces.py > export

Source: https://openai.github.io/openai-agents-python/ref/tracing/traces

The `export` method serializes the collected trace data into a dictionary. This dictionary contains all associated spans and their respective data. It is primarily used for sending trace information to external backends for storage and analysis. If tracing is disabled, this method will return `None`.

--------------------------------

### output_guardrails

Source: https://openai.github.io/openai-agents-python/ko/ref/run

A list of output guardrails to run on the final output of the run.

--------------------------------

### Handoffs > Handoff inputs

Source: https://openai.github.io/openai-agents-python/handoffs

In certain situations, you want the LLM to provide some data when it calls a handoff. For example, imagine a handoff to an "Escalation agent". You might want a reason to be provided, so you can log it. This is achieved by specifying an `input_type` which is a Pydantic `BaseModel` for structured data, and defining the `on_handoff` callback to accept this data type.

--------------------------------

### Run context > RunContextWrapper dataclass > usage class-attribute instance-attribute

Source: https://openai.github.io/openai-agents-python/ref/run_context

The `usage` instance attribute of `RunContextWrapper` provides information about the agent run's usage so far. For responses that are streamed, this usage information might be outdated until the final chunk of the stream is processed.

--------------------------------

### openai-agents-python/result.py > new_items

Source: https://openai.github.io/openai-agents-python/ja/ref/result

The new items generated during the agent run. These include things like new messages, tool calls and their outputs, etc.

--------------------------------

### Usage

Source: https://openai.github.io/openai-agents-python/zh/ref/usage

The `__post_init__` method in the `Usage` class is responsible for normalizing token detail fields. It addresses potential issues where certain API providers might not populate optional token detail fields (like `cached_tokens` or `reasoning_tokens`), or where generated Pydantic models might allow `None` values through bypasses like `model_construct`. By default, these fields are initialized to `0` if they are `None`, ensuring that subsequent calculations do not encounter `TypeError` exceptions.

--------------------------------

### AgentBase `dataclass` > tools `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

The `tools` attribute is a list designed to hold various `Tool` objects that the agent can utilize. These tools represent the functionalities and capabilities that the agent can access and execute. By default, this list is initialized as empty, allowing developers to dynamically add the necessary tools required for the agent's operation.

--------------------------------

### nest_handoff_history

Source: https://openai.github.io/openai-agents-python/ko/ref/run

Wrap prior run history in a single assistant message before handing off when no custom input filter is set. Set to False to preserve the raw transcript behavior from previous releases.

--------------------------------

### Handoff dataclass > tool_name instance-attribute

Source: https://openai.github.io/openai-agents-python/ref/handoffs

The `tool_name` attribute is a string that specifies the name of the tool which will be used to represent this handoff action. This allows the system to identify and invoke the handoff process through a named tool interface.

--------------------------------

### Agent Attributes > name

Source: https://openai.github.io/openai-agents-python/ref/agent

This attribute holds the name of the agent.

--------------------------------

### `Handoff prompt`

Source: https://openai.github.io/openai-agents-python/ko/ref/extensions/handoff_prompt

The `prompt_with_handoff_instructions` function takes a prompt string as input and returns a new string with the recommended instructions prepended. This function is located in the `src/agents/extensions/handoff_prompt.py` file.

--------------------------------

### RealtimeAgent > tools

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/agent

The `tools` attribute is a list of tools that the agent can access and utilize to perform its tasks. This enables the agent to extend its capabilities beyond its core logic by leveraging external functions or services.

--------------------------------

### OpenAI Agents Python > output_tokens_details

Source: https://openai.github.io/openai-agents-python/ko/ref/usage

Details about the output tokens, matching responses API usage details.

--------------------------------

### Release process/changelog > Breaking change changelog > 0.6.0

Source: https://openai.github.io/openai-agents-python/release

In version 0.6.0, the default handoff history is now packaged into a single assistant message instead of exposing the raw user/assistant turns. This provides downstream agents with a concise, predictable recap. The existing single-message handoff transcript now by default starts with "For context, here is the conversation so far between the user and the previous agent:" before the `<CONVERSATION HISTORY>` block, ensuring a clearly labeled recap for downstream agents.

--------------------------------

### MCPServerStdio

Source: https://openai.github.io/openai-agents-python/zh/ref/mcp/server

The `__init__` method for `MCPServerStdio` initializes the server with various parameters that control its behavior and communication. Key parameters include `params`, which defines the command to execute, its arguments, environment variables, working directory, and encoding settings for inter-process communication. Other important parameters are `cache_tools_list` for optimizing tool listing latency, `client_session_timeout_seconds` for setting read timeouts, `tool_filter` for managing tool accessibility, `use_structured_content` for controlling how tool results are processed, and parameters related to retry mechanisms (`max_retry_attempts`, `retry_backoff_seconds_base`) for handling transient failures. An optional `message_handler` can also be provided for custom processing of session messages.

--------------------------------

### trace > disabled

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

If True, we will return a Trace but the Trace will not be recorded.

--------------------------------

### SQLiteSession > __init__

Source: https://openai.github.io/openai-agents-python/ko/ref/memory

The `__init__` method for `SQLiteSession` sets up the session by initializing the database connection. For in-memory databases (`db_path=':memory:'`), a single shared connection is used across all threads to prevent issues with thread isolation. This connection is configured to use Write-Ahead Logging (WAL) for improved performance and its schema is initialized immediately. For file-based databases, a connection is established to the specified file path, WAL is enabled, and the schema is initialized once to ensure persistence. The `_local` attribute is a `threading.local` object used to manage thread-specific database connections when not using an in-memory database.

--------------------------------

### openai-agents-python/function_tool.py

Source: https://openai.github.io/openai-agents-python/ko/ref/tool

The `function_tool` decorator offers several customization options to fine-tune the behavior and representation of the created tool. You can override the default `name` and `description` of the tool using `name_override` and `description_override`, respectively. The `use_docstring_info` flag controls whether the docstring content is used for populating the tool's metadata.

Error handling can be customized via `failure_error_function`, allowing you to specify how tool invocation failures are reported to the LLM. The `strict_mode` parameter, when set to `True` (which is strongly recommended), enforces a stricter JSON schema for tool inputs, enhancing the reliability of data exchange. This aligns with OpenAI's guidance on structured outputs to ensure more accurate parsing of LLM responses.

--------------------------------

### Usage

Source: https://openai.github.io/openai-agents-python/ja/ref/usage

The `add` method in the `Usage` class facilitates the aggregation of token usage data from another `Usage` object. It systematically adds the `requests`, `input_tokens`, `output_tokens`, and `total_tokens` from the `other` Usage object to the current instance. This method also intelligently handles the `request_usage_entries` list, preserving the detailed breakdown of usage if the `other` Usage object represents a single, distinct request with non-zero token counts. Null guards are employed for nested token details to manage cases where `other` might have bypassed Pydantic validation, ensuring that `cached_tokens` and `reasoning_tokens` are treated as `0` if they are `None` or missing.

--------------------------------

### openai-agents-python/src/agents/realtime/config.py > Client Messages > other_data

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/config

Merged into the message body.

--------------------------------

### Handoff dataclass > on_invoke_handoff instance-attribute

Source: https://openai.github.io/openai-agents-python/ja/ref/handoffs

The function that invokes the handoff. The parameters passed are: (1) the handoff run context, (2) the arguments from the LLM as a JSON string (or an empty string if `input_json_schema` is empty). Must return an agent.

--------------------------------

### Usage > request_usage_entries

Source: https://openai.github.io/openai-agents-python/zh/ref/usage

The `request_usage_entries` attribute is a list designed to store individual `RequestUsage` objects. Each entry in this list captures the token usage for a specific API request, enabling accurate per-request cost calculations and detailed analysis of context window management. When new usage is added via the `add()` method, a new entry is automatically created in this list if the usage represents a distinct request (i.e., has non-zero tokens). This preserves the breakdown of token counts for multiple API calls, rather than just providing a single aggregated total.

--------------------------------

### Model > RealtimePlaybackTracker > on_play_ms

Source: https://openai.github.io/openai-agents-python/ref/realtime/model

The `on_play_ms` method is used to directly report the duration in milliseconds (`ms`) of audio that has been played, along with the `item_id` and `item_content_index`. If the playback is for a new audio item or a new content index within the current item, it resets the `_elapsed_ms` to the newly played duration and updates `_current_item`. If playback continues for the same item and content index, it adds the `ms` to the existing `_elapsed_ms`.

--------------------------------

### spans.py > error

Source: https://openai.github.io/openai-agents-python/ref/tracing

Any error that occurred during span execution. If an error occurred, this attribute will contain detailed information about the error, including a message and optional context. Otherwise, it will be None.

--------------------------------

### spans.py > SpanError

Source: https://openai.github.io/openai-agents-python/ref/tracing

Represents an error that occurred during span execution. It includes a human-readable `message` describing the error and an optional `data` dictionary for additional context.

--------------------------------

### ToolOutputFileContent > check_at_least_one_required_field

Source: https://openai.github.io/openai-agents-python/ref/tool

Validate that at least one of file_data, file_url, or file_id is provided.

--------------------------------

### Run context > RunContextWrapper dataclass > usage class-attribute instance-attribute

Source: https://openai.github.io/openai-agents-python/ja/ref/run_context

The `usage` instance attribute within `RunContextWrapper` tracks the usage of the agent run to date. For streamed responses, this usage information may be outdated until the final chunk of the stream has been processed.

--------------------------------

### tool.py > MCPToolApprovalFunctionResult

Source: https://openai.github.io/openai-agents-python/ref/tool

The result of an MCP tool approval function. This TypedDict defines the structure for the outcome of an approval process for a tool call mediated by the MCP. It indicates whether the tool call should be approved and optionally provides a reason if the approval is rejected.

--------------------------------

### Usage > requests

Source: https://openai.github.io/openai-agents-python/zh/ref/usage

The `requests` attribute tracks the total number of requests made to the LLM API. This is a simple integer count, incremented each time an API call is initiated.

--------------------------------

### spans.py > Span > start

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

Start the span.

Args:
    mark_as_current: If true, the span will be marked as the current span.

--------------------------------

### AgentBase `dataclass` > tools `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

The `tools` attribute is a list that holds all the `Tool` objects available for the agent to use. This allows agents to perform various actions and access different functionalities by leveraging the tools provided in this list. The list is initialized as empty by default.

--------------------------------

### RealtimeAgent > tools

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/agent

The `tools` attribute is a list of `Tool` objects that the agent can access and utilize during its operation. These tools extend the agent's capabilities, allowing it to perform a wider range of tasks.

--------------------------------

### spans.py > Span > ended_at

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

When the span finished execution.

--------------------------------

### Run context > RunContextWrapper dataclass > usage class-attribute instance-attribute

Source: https://openai.github.io/openai-agents-python/ko/ref/run_context

The `usage` instance attribute within `RunContextWrapper` tracks the agent run's usage. This attribute defaults to a new `Usage` object. For responses that are streamed, the usage information might be outdated until the final chunk of the stream has been processed.

--------------------------------

### InputGuardrail dataclass > name class-attribute instance-attribute

Source: https://openai.github.io/openai-agents-python/ref/guardrail

The `name` attribute provides a name for the guardrail, which is useful for tracing purposes. If no name is explicitly provided, the system will automatically use the name of the guardrail function.

--------------------------------

### openai_github_io_openai-agents-python > function_schema

Source: https://openai.github.io/openai-agents-python/ja/ref/function_schema

The `function_schema` function offers granular control over how it extracts information. The `use_docstring_info` parameter, when set to `True` (the default), instructs the function to parse the docstring to derive the function's description and parameter descriptions. If `use_docstring_info` is `False`, these details must be provided explicitly through other means, such as type hint annotations or overrides. Additionally, the `strict_json_schema` parameter, also defaulting to `True`, is crucial for ensuring that the generated JSON schema adheres to the strict standards expected by the OpenAI API. Setting this to `True` significantly increases the probability that an LLM will generate correct JSON input when interacting with the function.

--------------------------------

### ToolGuardrailFunctionOutput `dataclass`

Source: https://openai.github.io/openai-agents-python/ko/ref/tool_guardrails

The `ToolGuardrailFunctionOutput` dataclass represents the result of a tool guardrail function. It contains two main attributes: `output_info` and `behavior`.

- `output_info`: This attribute can hold any optional data related to the checks performed by the guardrail. For instance, it might include details about the specific checks that were executed and their granular outcomes.
- `behavior`: This attribute defines the system's response to the guardrail's result. It can be one of three types:
    - `AllowBehavior`: Allows the normal tool execution to proceed without any interruption (this is the default behavior).
    - `RejectContentBehavior`: Rejects the tool's call or output but allows the execution to continue, typically by providing a message to the model.
    - `RaiseExceptionBehavior`: Halts the execution by triggering a `ToolGuardrailTripwireTriggered` exception.

--------------------------------

### Spans > SpanError

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

Represents an error that occurred during span execution. It includes a human-readable `message` and an optional `data` dictionary for additional context.

--------------------------------

### Span > finish

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/spans

The `finish()` method concludes the span's execution. If `reset_current` is set to true, the span will be reset as the current span after finishing.

--------------------------------

### `repl` > `run_demo_loop`

Source: https://openai.github.io/openai-agents-python/zh/ref/repl

Run a simple REPL loop with the given agent. This utility allows quick manual testing and debugging of an agent from the command line. Conversation state is preserved across turns. Enter `exit` or `quit` to stop the loop.

--------------------------------

### MultiProvider

Source: https://openai.github.io/openai-agents-python/ja/ref/models/multi_provider

The `__init__` method for `MultiProvider` allows for the customization of model provider mappings and the configuration of the `OpenAIProvider`. Users can provide a `provider_map` to define custom prefix-to-provider associations. Additionally, parameters like `openai_api_key`, `openai_base_url`, and an optional `openai_client` can be passed to configure the underlying `OpenAIProvider`.

--------------------------------

### Handoff dataclass > input_json_schema instance-attribute

Source: https://openai.github.io/openai-agents-python/ja/ref/handoffs

The JSON schema for the handoff input. Can be empty if the handoff does not take an input.

--------------------------------

### Agent Parameters

Source: https://openai.github.io/openai-agents-python/ref/agent

This lets you configure how tool use is handled.
- "run_llm_again": The default behavior. Tools are run, and then the LLM receives the results and gets to respond.
- "stop_on_first_tool": The output from the first tool call is treated as the final result. In other words, it isn’t sent back to the LLM for further processing but is used directly as the final output.
- A `StopAtTools` object: The agent will stop running if any of the tools listed in `stop_at_tool_names` is called. The final output will be the output of the first matching tool call. The LLM does not process the result of the tool call.
- A function: If you pass a function, it will be called with the run context and the list of tool results. It must return a `ToolsToFinalOutputResult`, which determines whether the tool calls result in a final output.
NOTE: This configuration is specific to FunctionTools. Hosted tools, such as file search, web search, etc. are always processed by the LLM.

--------------------------------

### Release process/changelog

Source: https://openai.github.io/openai-agents-python/release

The project follows a slightly modified version of semantic versioning using the form `0.Y.Z`. The leading `0` indicates the SDK is still evolving rapidly. Minor (`Y`) versions are increased for **breaking changes** to any public interfaces that are not marked as beta. For example, going from `0.0.x` to `0.1.x` might include breaking changes. If you don't want breaking changes, we recommend pinning to `0.0.x` versions in your project. Patch (`Z`) versions are incremented for non-breaking changes, including bug fixes, new features, changes to private interfaces, and updates to beta features.

--------------------------------

### Advanced SQLite Sessions > Usage tracking

Source: https://openai.github.io/openai-agents-python/sessions/advanced_sqlite_session

AdvancedSQLiteSession provides detailed usage analytics by storing token usage data per conversation turn. **This is entirely dependent on the `store_run_usage` method being called after each agent run.**

--------------------------------

### Run context > AgentHookContext dataclass

Source: https://openai.github.io/openai-agents-python/ref/run_context

The `AgentHookContext` dataclass is passed to agent hooks, specifically `on_start` and `on_end`.

--------------------------------

### Agent Configuration > Checks

Source: https://openai.github.io/openai-agents-python/ko/ref/agent

A list of checks that run on the final output of the agent, after generating a response. These checks only run if the agent successfully produces a final output.

--------------------------------

### ModelSettings > store

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

Whether to store the generated model response for later retrieval. For Responses API: automatically enabled when not specified. For Chat Completions API: disabled when not specified.

--------------------------------

### Spans

Source: https://openai.github.io/openai-agents-python/ref/tracing/spans

The `trace_id` property returns the ID of the trace this span belongs to, which is a unique identifier for the parent trace.

The `span_id` property provides a unique identifier for this specific span within its trace.

The `span_data` property holds operation-specific data relevant to this span, such as LLM generation details or tool execution parameters.

--------------------------------

### openai-agents-python/agents.py > Agent class > find_turns_by_content

Source: https://openai.github.io/openai-agents-python/ref/extensions/memory/advanced_sqlite_session

To facilitate searching through conversation history, the `find_turns_by_content` method allows users to locate specific turns based on text content. This method searches the user messages within a given branch for a specified search term. It returns a list of matching turns, each formatted similarly to the output of `get_conversation_turns`, enabling users to quickly find relevant parts of the conversation.

--------------------------------

### SQLiteSession > _init_db_for_connection

Source: https://openai.github.io/openai-agents-python/ko/ref/memory

The `_init_db_for_connection` method is used to set up the necessary database schema. It creates two tables if they do not already exist: `agent_sessions` for storing session metadata (like `session_id`, `created_at`, `updated_at`) and `agent_messages` for storing individual message data associated with a session. The `agent_sessions` table uses `session_id` as its primary key. The `agent_messages` table is auto-incrementing and includes columns for `session_id`, `message_data`, and `created_at`, linking each message to its corresponding session.

--------------------------------

### OpenAI Agents Python > requests

Source: https://openai.github.io/openai-agents-python/ko/ref/usage

Total requests made to the LLM API.

--------------------------------

### MCPServerStdio

Source: https://openai.github.io/openai-agents-python/ko/ref/mcp/server

The `MCPServerStdio` class constructor accepts several parameters to configure the server's behavior. The `params` argument is crucial, as it includes details like the command to run, its arguments, environment variables, and the working directory. Other important parameters include `cache_tools_list` to optimize tool fetching latency, `client_session_timeout_seconds` for managing connection timeouts, and `tool_filter` for specifying which tools are accessible. Additionally, `use_structured_content` controls how tool results are handled, while `max_retry_attempts` and `retry_backoff_seconds_base` manage retry logic for failed operations. An optional `message_handler` can be provided for custom session message processing.

--------------------------------

### Span > span_data

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/spans

The `span_data` property returns operation-specific data associated with this span. The type of this data depends on the specific type of span (e.g., LLM generation data for an LLM span).

--------------------------------

### Agent Attributes > handoffs

Source: https://openai.github.io/openai-agents-python/ref/agent

Handoffs enable an agent to delegate tasks to other specialized agents. By providing a list of `handoffs`, an agent can intelligently decide when to pass control to a sub-agent that is better suited for a particular sub-task. This promotes modularity and separation of concerns within complex agent systems.

--------------------------------

### SessionABC > clear_session

Source: https://openai.github.io/openai-agents-python/ja/ref/memory/session

Clear all items for this session.

--------------------------------

### openai-agents-python/result.py > context_wrapper

Source: https://openai.github.io/openai-agents-python/ja/ref/result

The context wrapper for the agent run.

--------------------------------

### Trace > name

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

Get the human-readable name of this workflow trace.

Returns:
    str: The workflow name (e.g., "Customer Service", "Data Processing")

Notes:
- Should be descriptive and meaningful
- Used for grouping and filtering in the dashboard
- Helps identify the purpose of the trace

--------------------------------

### Agent Attributes

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

Handoffs enable an agent to delegate tasks to other specialized sub-agents. By providing a list of `Agent` objects or `Handoff` configurations, the agent can intelligently route specific responsibilities to the most appropriate sub-agent. This promotes modularity and a clear separation of concerns within complex agent systems.

--------------------------------

### Session > add_items

Source: https://openai.github.io/openai-agents-python/zh/ref/memory/session

The `add_items` method is used to append new interactions to the session's history. It takes a list of `TResponseInputItem` objects, representing the latest exchanges, and adds them to the stored conversation. This ensures that the agent's context is continuously updated with new information.

--------------------------------

### Runner > run

Source: https://openai.github.io/openai-agents-python/ko/ref/run

The `run` method accepts several parameters to configure the agent execution. `starting_agent` is the entry point of the workflow. `input` is the initial data provided to the agent. `context` allows for passing external state. `max_turns` limits the number of execution cycles. `hooks` provide callbacks for lifecycle events. `run_config` offers global settings for the entire run. `previous_response_id` and `auto_previous_response_id` are used for managing conversation history, especially when interacting with OpenAI's Responses API. `conversation_id` enables the use of OpenAI's conversation state feature, allowing agents to read and write to a persistent conversation history. A `session` object can also be provided for automatic conversation history management.

--------------------------------

### Model Settings > extra_query

Source: https://openai.github.io/openai-agents-python/ref/model_settings

Additional query fields to provide with the request. Defaults to None if not provided.

--------------------------------

### DaprSession

Source: https://openai.github.io/openai-agents-python/ref/extensions/memory/dapr_session

The `__init__` method initializes a `DaprSession` instance. It takes the `session_id`, the name of the Dapr state store (`state_store_name`), and an initialized `dapr_client` as essential parameters. Optional parameters include `ttl` for data persistence duration and `consistency` level for state operations. The constructor also sets up internal state keys for messages and metadata, and initializes an asyncio lock for thread-safe operations. A flag `_owns_client` is used to track whether the `DaprSession` instance is responsible for managing the lifecycle of the `dapr_client`.

--------------------------------

### openai-agents-python/src/agents/realtime/config.py > User Input Types > RealtimeUserInputMessage > type

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/config

The type identifier for message inputs.

--------------------------------

### FunctionTool `dataclass`

Source: https://openai.github.io/openai-agents-python/ja/ref/tool

The `FunctionTool` is a dataclass designed to wrap a Python function, making it usable as a tool within the agent framework. While you can instantiate it directly, it's generally recommended to use the `function_tool` helper functions for easier integration. These helpers streamline the process of wrapping your Python functions, ensuring they are correctly configured with necessary metadata for the agent to understand and utilize. The `FunctionTool` includes essential attributes like `name` and `description` for identification and communication with the language model, and `params_json_schema` to define the expected input structure.

--------------------------------

### Agent Attributes > mcp_config

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

Configuration settings for the MCP servers, allowing for customization of their behavior and integration with the agent.

--------------------------------

### Agent `dataclass` > handoffs

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

Handoffs represent sub-agents that an agent can delegate tasks to. By providing a list of handoffs, the main agent can choose to delegate relevant sub-tasks to specialized agents, promoting modularity and separation of concerns within the system.

--------------------------------

### Usage > Accessing usage from a run

Source: https://openai.github.io/openai-agents-python/usage

After calling `Runner.run(...)`, you can access the usage information via `result.context_wrapper.usage`. This aggregated usage includes all model calls during the run, encompassing tool calls and handoffs between different parts of the agent.

Example:
```python
result = await Runner.run(agent, "What's the weather in Tokyo?")
usage = result.context_wrapper.usage

print("Requests:", usage.requests)
print("Input tokens:", usage.input_tokens)
print("Output tokens:", usage.output_tokens)
print("Total tokens:", usage.total_tokens)
```

--------------------------------

### OpenAI Agents Python > __init__

Source: https://openai.github.io/openai-agents-python/zh/ref/mcp/server

Create a new MCP server based on the HTTP with SSE transport. The `params` argument configures the server, including its URL, headers, and various timeouts for HTTP requests and SSE connections.  Other parameters control caching of tool lists, naming the server, filtering tools, handling structured content, and managing retries for failed calls. An optional `message_handler` can be provided to process session messages.

--------------------------------

### openai-agents-python/src/agents/realtime/config.py > User Input Types > RealtimeUserInputMessage > role

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/config

The role identifier for user messages.

--------------------------------

### openai-agents-python/function_tool.py > function_tool

Source: https://openai.github.io/openai-agents-python/ja/ref/tool

The `function_tool` decorator offers several customization options to tailor the behavior and appearance of the created `FunctionTool`:

*   `name_override`: Allows you to specify a custom name for the tool, distinct from the original function's name.
*   `description_override`: Lets you provide a specific description for the tool, bypassing the automatic extraction from the docstring.
*   `docstring_style`: Enables you to explicitly define the docstring style for parsing, useful when auto-detection might fail.
*   `use_docstring_info`: A boolean flag (defaulting to `True`) to control whether the docstring content is used for populating the tool's description and argument descriptions.
*   `failure_error_function`: A custom function that generates error messages sent to the LLM when a tool invocation fails. If set to `None`, an exception is raised instead of sending an error message.
*   `strict_mode`: A boolean flag (recommended to be `True`) that enforces strict JSON schema validation for tool inputs. This significantly improves the likelihood of receiving correctly formatted JSON. When `False`, it allows for more lenient schemas, potentially making parameters optional or permitting additional properties.
*   `is_enabled`: Determines if the tool is active. This can be a static boolean or a callable that dynamically checks the tool's enablement based on the current run context and agent.
*   `tool_input_guardrails`: An optional list of guardrails to execute before the tool is invoked, allowing for pre-invocation validation.
*   `tool_output_guardrails`: An optional list of guardrails to execute after the tool has returned a result, enabling post-invocation checks.

--------------------------------

### SQLiteSession

Source: https://openai.github.io/openai-agents-python/zh/ref/memory

When initializing `SQLiteSession`, you can specify the `session_id`, `db_path`, `sessions_table`, and `messages_table`. The `db_path` defaults to `:memory:`, meaning the database resides in RAM and is cleared upon process termination. If a file path is provided, the database will be persisted to disk. The `sessions_table` is used for storing session metadata like creation and update times, while `messages_table` stores the actual conversation messages. The class also utilizes a threading lock and thread-local connections for managing database access, especially when dealing with file-based databases to ensure thread safety.

--------------------------------

### ReasoningItem `dataclass` > raw_item `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ko/ref/items

The `raw_item` attribute within `ReasoningItem` stores the actual raw reasoning data. This attribute is of type `ResponseReasoningItem`.

--------------------------------

### spans.py > Span > span_id

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

Unique identifier for this span.

--------------------------------

### Agent Class Attributes > handoffs

Source: https://openai.github.io/openai-agents-python/ko/ref/agent

Handoffs enable an agent to delegate tasks to other sub-agents. By providing a list of `Agent` or `Handoff` objects, the agent can intelligently decide when to transfer control to a more specialized agent. This mechanism promotes modularity and separation of concerns within complex agent systems.

--------------------------------

### Span > started_at

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/spans

The `started_at` property returns the ISO format timestamp indicating when the span began execution. It returns `None` if the span has not yet started.

--------------------------------

### RealtimeAgent > handoffs

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/agent

Handoffs enable an agent to delegate tasks to other sub-agents. By providing a list of `handoffs`, the agent can intelligently choose to delegate specific tasks to specialized sub-agents when relevant. This promotes modularity and separation of concerns within complex agent systems.

--------------------------------

### RealtimeModelConfig > initial_model_settings

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/model

The `initial_model_settings` allow you to configure the model at the start of the connection. This provides an initial state or parameters for the realtime model session.

--------------------------------

### Span > started_at

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/spans

The `started_at` property returns the timestamp indicating when the span began execution. The timestamp is in ISO format. If the span has not yet started, it returns `None`.

--------------------------------

### Agent Class > `register_tool` Method > Customization Parameters

Source: https://openai.github.io/openai-agents-python/ref/agent

The `Agent.register_tool` decorator can be customized with various parameters to fine-tune how the tool is exposed to the agent. `name_override` allows for specifying a custom name for the tool, distinct from the function's name. `description_override` provides a detailed explanation of the tool's purpose and usage. `is_enabled` controls whether the tool is available to the LLM at runtime; it can be a boolean or a callable that dynamically determines enablement based on the current context. `failure_error_function` specifies a function to generate an error message if the tool execution fails, which is then sent to the LLM. If not provided, the exception is raised.

--------------------------------

### Model > TTSModelSettings > instructions

Source: https://openai.github.io/openai-agents-python/ref/voice/model

The `instructions` attribute in TTSModelSettings provides a way to control the TTS model's output behavior. For instance, setting it to 'You will receive partial sentences. Do not complete the sentence just read out the text.' can influence the model to read text verbatim without attempting to complete sentences, useful for specific audio generation tasks.

--------------------------------

### ModelSettings > frequency_penalty

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

The frequency penalty to use when calling the model.

--------------------------------

### Trace > start

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

Start the trace and optionally mark it as the current trace.

Args:
    mark_as_current: If true, marks this trace as the current trace
        in the execution context.

Notes:
- Must be called before any spans can be added
- Only one trace can be current at a time
- Thread-safe when using mark_as_current

--------------------------------

### MCPServerStreamableHttp > __init__

Source: https://openai.github.io/openai-agents-python/zh/ref/mcp/server

The `MCPServerStreamableHttp` class offers a constructor that allows for the creation of a new MCP server instance using the Streamable HTTP transport. Key parameters include `params` for server configuration (URL, headers, timeouts), `cache_tools_list` to optimize tool list retrieval, `name` for identification, `client_session_timeout_seconds` for session timeouts, `tool_filter` for managing tool accessibility, `use_structured_content` to control the use of structured content in tool results, and parameters for managing retries (`max_retry_attempts`, `retry_backoff_seconds_base`). An optional `message_handler` can also be provided.

--------------------------------

### AgentBase `dataclass` > name `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

The `name` attribute is a string that uniquely identifies the agent. This is a crucial piece of information for distinguishing between different agents, especially when multiple agents are operating within the same environment or system. A clear and descriptive name helps in debugging, logging, and user-facing interactions.

--------------------------------

### DaprSession

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/memory/dapr_session

The `DaprSession` class provides an implementation of the `SessionABC` abstract base class, specifically designed to leverage Dapr's state store capabilities for managing conversation sessions. It allows for the persistence and retrieval of session data, including messages and metadata, using Dapr's distributed state management features. This class is initialized with a unique `session_id`, the name of the Dapr state store component to be used, and an instance of `DaprClient`. Optional parameters include `ttl` for setting a time-to-live for session data and `consistency` to specify the desired consistency level for state operations, such as `DAPR_CONSISTENCY_EVENTUAL` or `DAPR_CONSISTENCY_STRONG`.

--------------------------------

### Handoff prompt > prompt_with_handoff_instructions

Source: https://openai.github.io/openai-agents-python/zh/ref/extensions/handoff_prompt

The `prompt_with_handoff_instructions` function takes a prompt string as input and returns a new string with recommended instructions for agents that utilize handoffs. It prepends the `RECOMMENDED_PROMPT_PREFIX` to the provided prompt, ensuring that the agent has the necessary system context for proper handoff operations.

--------------------------------

### OpenAI Agents Python SDK > Usage Attributes > requests

Source: https://openai.github.io/openai-agents-python/ja/ref/usage

The `requests` attribute represents the total number of requests made to the LLM API. It is an integer value, initialized to 0, and tracks each individual API call made during the agent's operation.

--------------------------------

### Examples > Categories > agent_patterns

Source: https://openai.github.io/openai-agents-python/examples

Examples in this category illustrate common agent design patterns, such as Deterministic workflows, Agents as tools, Parallel agent execution, Conditional tool usage, Input/output guardrails, LLM as a judge, Routing, and Streaming guardrails.

--------------------------------

### Model Settings > frequency_penalty

Source: https://openai.github.io/openai-agents-python/ref/model_settings

The frequency penalty to use when calling the model.

--------------------------------

### FunctionTool `dataclass` > `on_invoke_tool` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ja/ref/tool

The `on_invoke_tool` attribute is a crucial part of the `FunctionTool`, defining the actual logic for executing the wrapped function. It's defined as an awaitable callable that accepts `ToolContext` and a JSON string of parameters. This function is responsible for performing the tool's action and returning the result. The return value should be one of the structured tool output types (e.g., `ToolOutputText`, `ToolOutputImage`, `ToolOutputFileContent`), a string representation of the output, a list of outputs, or any object that can be converted to a string. Error handling is also managed here; you can either raise an exception to fail the run or return a string error message to be communicated back to the LLM.

--------------------------------

### RunResult dataclass > input instance-attribute

Source: https://openai.github.io/openai-agents-python/ja/ref/result

The `input` attribute stores the original input items provided to the agent before the `run()` method was called. This attribute can hold either a string or a list of `TResponseInputItem`. It's important to note that this input might be a mutated version if handoff input filters have modified it.

--------------------------------

### Tools > LocalShellExecutor

Source: https://openai.github.io/openai-agents-python/zh/ref/tool

A function that executes a command on a shell.

--------------------------------

### trace

Source: https://openai.github.io/openai-agents-python/ref/tracing

The `trace` function is used to create a new trace object. This trace is not started automatically; you must explicitly start and finish it using `trace.start()` and `trace.finish()`, or by using it as a context manager with the `with` statement. The function accepts a `workflow_name` which identifies the logical application or workflow, such as 'code_bot' or 'customer_support_agent'. Optionally, you can provide a `trace_id` for a specific trace, a `group_id` to link related traces (e.g., from the same conversation), and a `metadata` dictionary for custom information. A `tracing` configuration can also be supplied for exporting trace data, and a `disabled` flag can be set to `True` to prevent the trace from being recorded. The function returns the created `Trace` object.

--------------------------------

### openai-agents-python/src/agents/realtime/config.py > User Input Types > RealtimeUserInputText > type

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/config

The type identifier for text input.

--------------------------------

### AgentBase `dataclass` > name `instance-attribute`

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

The `name` attribute is a string that uniquely identifies the agent. This is crucial for distinguishing between different agents, especially in scenarios where multiple agents might be operating or interacting.

--------------------------------

### Advanced SQLite Sessions

Source: https://openai.github.io/openai-agents-python/sessions/advanced_sqlite_session

`AdvancedSQLiteSession` is an enhanced version of the basic `SQLiteSession` that provides advanced conversation management capabilities including conversation branching, detailed usage analytics, and structured conversation queries.

--------------------------------

### Handoff dataclass > input_json_schema instance-attribute

Source: https://openai.github.io/openai-agents-python/zh/ref/handoffs

The `input_json_schema` defines the expected structure and data types for any input arguments that need to be passed to the agent receiving the handoff. If the target agent requires specific information to process the request, this schema ensures that the input provided by the language model conforms to the expected format. If no input is required, this can be an empty dictionary. This helps in creating robust and predictable agent interactions.

--------------------------------

### Span > finish

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

Finish the span. If `reset_current` is true, the span will be reset as the current span.

--------------------------------

### RealtimeAgent > handoffs

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/agent

Handoffs enable an agent to delegate tasks to specialized sub-agents. By providing a list of these sub-agents, the main agent can intelligently select and transfer relevant responsibilities, promoting modularity and separation of concerns.

--------------------------------

### Creating traces/spans > trace

Source: https://openai.github.io/openai-agents-python/ref/tracing/create

The `trace` function is used to create a new trace. This trace is not automatically started; you must either use it as a context manager with a `with trace(...):` statement or manually call `trace.start()` followed by `trace.finish()`. You can provide a `workflow_name`, an optional `trace_id` (or let the system generate one using `util.gen_trace_id()`), and an optional `group_id` to link related traces, such as those from the same conversation. Additionally, an arbitrary `metadata` dictionary can be supplied to attach custom user-defined information to the trace. Tracing can also be configured with `tracing` settings or disabled entirely by setting `disabled=True`. The function returns a `Trace` object.

--------------------------------

### MultiProvider

Source: https://openai.github.io/openai-agents-python/zh/ref/models/multi_provider

The `__init__` method for `MultiProvider` allows for customization of the model provider mapping. You can provide a `provider_map` argument to define custom mappings between prefixes and `ModelProvider` instances. Additionally, you can configure specific parameters for the `OpenAIProvider`, such as the API key, base URL, client, organization, project, and whether to use response streaming. If a `provider_map` is not supplied, a default mapping is utilized. This initialization process ensures that the `MultiProvider` is set up according to your desired configuration.

--------------------------------

### Creating traces/spans > trace

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/create

The `trace` function is used to create a new trace. A trace represents a logical unit of work, such as a specific agent's execution or a conversation flow. The trace is not automatically started; you need to either use it as a context manager with a `with` statement or manually call `trace.start()` and `trace.finish()`. You can provide a `workflow_name` to identify the logical application or workflow, such as "code_bot" for a coding agent. Optionally, you can specify a `trace_id` (or let the system generate one), a `group_id` to link related traces (e.g., from the same chat thread), and a `metadata` dictionary for additional user-defined information. The `tracing` parameter allows for optional tracing configuration, and the `disabled` flag, when set to `True`, will return a `Trace` object but prevent it from being recorded.

--------------------------------

### MultiProvider

Source: https://openai.github.io/openai-agents-python/zh/ref/models/multi_provider

The `MultiProvider` class allows you to map different model providers based on the prefix of a model name. This provides flexibility in how you route requests to various language models. By default, if a model name starts with "openai/" or has no prefix, it will be directed to the `OpenAIProvider`. If the model name is prefixed with "litellm/", it will be routed to the `LitellmProvider`. This default behavior can be customized to suit your specific needs, allowing for a dynamic and adaptable model selection process.

--------------------------------

### Memory > Session > get_items

Source: https://openai.github.io/openai-agents-python/ko/ref/memory

Retrieve the conversation history for this session. The `limit` parameter specifies the maximum number of items to retrieve. If `limit` is `None`, all items are retrieved. When a limit is specified, the function returns the latest N items in chronological order.

--------------------------------

### spans.py > parent_id

Source: https://openai.github.io/openai-agents-python/ref/tracing

ID of the parent span, if any. This is useful for establishing a hierarchy of operations within a trace. If the span is a root span (meaning it does not have a parent), this value will be None.

--------------------------------

### Handoffs

Source: https://openai.github.io/openai-agents-python/ko/ref/handoffs

The `nest_handoff_history` function is responsible for summarizing the previous transcript for the subsequent agent. It takes `HandoffInputData` and an optional `history_mapper` as input. It normalizes and flattens the input history, processes any pre-handoff items and new items, and then applies the `history_mapper` to create a summarized history. Finally, it returns a new `HandoffInputData` object with the summarized history and potentially filtered pre-handoff items.

--------------------------------

### Run config

Source: https://openai.github.io/openai-agents-python/running_agents

The `run_config` parameter provides global settings for an agent run. It allows configuring the LLM `model` and `model_provider`, overriding agent-specific `model_settings` like `temperature` or `top_p`, and specifying `input_guardrails` and `output_guardrails` to be applied to all runs. Additionally, `handoff_input_filter` can be set to globally edit inputs sent during agent handoffs, and `nest_handoff_history` controls whether the prior transcript is collapsed into a single assistant message before invoking the next agent. The default behavior (`True`) summarizes the conversation history, while `False` passes the raw transcript. `handoff_history_mapper` offers a way to customize this summary without a full handoff filter. Global tracing can be managed with `tracing_disabled`, `trace_include_sensitive_data`, `workflow_name`, `trace_id`, `group_id`, and `trace_metadata`.

--------------------------------

### Pipelines and workflows > Configuring a pipeline

Source: https://openai.github.io/openai-agents-python/voice/pipeline

When you create a pipeline, you can set a few things:
  1. The `workflow`, which is the code that runs each time new audio is transcribed.
  2. The `speech-to-text` and `text-to-speech` models used
  3. The `config`, which lets you configure things like:
     * A model provider, which can map model names to models
     * Tracing, including whether to disable tracing, whether audio files are uploaded, the workflow name, trace IDs etc.
     * Settings on the TTS and STT models, like the prompt, language and data types used.

--------------------------------

### spans.py > Span > error

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

Any error that occurred during span execution.

--------------------------------

### MCPServerStreamableHttp

Source: https://openai.github.io/openai-agents-python/ko/ref/mcp/server

The constructor for `MCPServerStreamableHttp` accepts several parameters to configure its behavior. `params` is a mandatory argument containing server configuration details such as the URL, headers, and various timeout settings. `cache_tools_list` (defaulting to `False`) determines whether the list of available tools is cached after the first fetch, which can significantly improve latency if the tools list is static. `client_session_timeout_seconds` sets the read timeout for the underlying MCP client session. `tool_filter` allows for specifying a filter to narrow down the tools available to the client. `use_structured_content` (defaulting to `False`) controls whether to use the `structured_content` field in tool results, which is important for backward compatibility as many servers include structured data within the general `content` field. Additionally, parameters for retry attempts (`max_retry_attempts`) and backoff intervals (`retry_backoff_seconds_base`) are provided for handling transient failures in tool calls.

--------------------------------

### custom_span

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/create

The `custom_span` function allows you to create a new span with custom metadata. This span is not started automatically, meaning you need to explicitly start and finish it using a `with` statement or by calling `span.start()` and `span.finish()` methods.

Parameters:
* `name` (str): The name of the custom span. This is a required parameter.
* `data` (dict[str, Any] | None): Arbitrary structured data that can be associated with the span. Defaults to `None`.
* `span_id` (str | None): An optional unique identifier for the span. If not provided, an ID will be generated. It is recommended to use `util.gen_span_id()` for correctly formatted IDs.
* `parent` (Trace | Span[Any] | None): Specifies the parent span or trace for this custom span. If omitted, the current trace or span will be used as the parent.
* `disabled` (bool): If set to `True`, a Span object will be returned, but it will not be recorded. Defaults to `False`.

The function returns a `Span[CustomSpanData]` object, representing the newly created custom span.

--------------------------------

### openai-agents-python/openai_agents/llm/litellm.py > _convert_gemini_extra_content_to_provider_specific_fields

Source: https://openai.github.io/openai-agents-python/ko/ref/extensions/litellm

The `_convert_gemini_extra_content_to_provider_specific_fields` method is responsible for transforming Gemini's unique `extra_content` format for tool calls into the `provider_specific_fields` format expected by LiteLLM. This is crucial for correctly passing tool call information, specifically thought signatures, to Gemini models.

The method identifies the last user message in the conversation history to ensure that only tool calls appearing after this point are processed. This behavior aligns with how Gemini handles tool calls in relation to user prompts. It iterates through the messages, focusing on assistant messages that contain `tool_calls`. For each tool call, it attempts to extract the `google` specific content and map the `thought_signature` to the `provider_specific_fields` dictionary. If a valid `thought_signature` is found, it's added; otherwise, a default skip behavior is maintained.

--------------------------------

### custom_span

Source: https://openai.github.io/openai-agents-python/ref/tracing

The `custom_span` function allows you to create a new custom span with your own metadata. This span is not automatically started, so you need to manage its lifecycle manually using either a `with` statement (`with custom_span() ...`) or by explicitly calling `span.start()` and `span.finish()`. You can provide a name, arbitrary structured data, an optional span ID (or let it generate one), a parent span or trace, and a flag to disable recording. The function returns the newly created custom span, which can hold `CustomSpanData`.

--------------------------------

### LitellmModel

Source: https://openai.github.io/openai-agents-python/ref/extensions/litellm

The `LitellmModel` class serves as an interface to utilize a wide array of language models through the LiteLLM library. LiteLLM simplifies access to various providers such as OpenAI, Anthropic, Gemini, and Mistral. This abstraction allows developers to switch between different models and providers with minimal code changes, as long as they are supported by LiteLLM. The class is initialized with the model name, and optionally a base URL and API key if custom configurations are needed.

--------------------------------

### Span > __exit__

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/spans

The `__exit__` method is part of the context manager protocol, handling the cleanup and finalization of a span when exiting a `with` block, including error handling.

--------------------------------

### Mixing and matching models

Source: https://openai.github.io/openai-agents-python/models

When you want to further configure the model used for an agent, you can pass `ModelSettings`, which provides optional model configuration parameters such as temperature.

--------------------------------

### NoOpSpan

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/spans

The `NoOpSpan` class is a no-operation implementation of the `Span` abstract base class. It is designed to be used when tracing functionality is disabled within the application. Despite not recording any tracing data, it ensures that span-related operations, such as starting, finishing, and error handling, can still be called without raising errors. This allows the rest of the application code that interacts with spans to function correctly even when tracing is off. The `span_data` parameter, which is required, holds the operation-specific data for the span, although this data is not utilized by `NoOpSpan` itself.

--------------------------------

### Agent Class

Source: https://openai.github.io/openai-agents-python/ref/agent

The `Agent` class is the core of the openai-agents library, enabling the creation of sophisticated conversational agents. It allows developers to define agent behavior, including instructions, tools, and execution logic. The `Agent` class acts as a blueprint for creating instances that can engage in multi-turn conversations, leverage external tools, and respond dynamically to user inputs. Its design emphasizes modularity and extensibility, making it suitable for a wide range of applications from simple chatbots to complex AI assistants.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

The `extra_query` field allows you to provide additional query parameters that are not covered by the standard `ModelSettings`. These are passed directly to the underlying model provider's API.

--------------------------------

### Root > agent_span

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `agent_span` function is used to create a new agent span. This span is not started automatically, so you must either use it within a `with` statement (e.g., `with agent_span(...) ...`) or manually call `span.start()` and `span.finish()`.

Key parameters include:
* `name`: The required name of the agent.
* `handoffs`: An optional list of agent names to which control might be handed off.
* `tools`: An optional list of tool names available to the agent.
* `output_type`: An optional name describing the agent's output.
* `span_id`: An optional unique identifier for the span. If not provided, one will be generated. It's recommended to use `util.gen_span_id()` for proper formatting.
* `parent`: The parent span or trace. If omitted, the current trace/span will be used automatically.
* `disabled`: A boolean flag. If `True`, the span is created but not recorded.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

`extra_args` is a dictionary for passing arbitrary keyword arguments directly to the model API call. This provides maximum flexibility, allowing you to use any parameters supported by the specific model provider's API that are not explicitly defined in `ModelSettings`.

--------------------------------

### Conversations/chat threads > Manual conversation management

Source: https://openai.github.io/openai-agents-python/running_agents

Manual management of conversation history is supported using the `RunResultBase.to_input_list()` method. This method retrieves the inputs necessary for the subsequent turn in a conversation. In the example provided, after the first turn, `result.to_input_list()` is called to get the history, which is then appended with a new user message before being passed to `Runner.run` for the second turn. This allows for building multi-turn conversations by explicitly managing the input for each subsequent agent run.

--------------------------------

### openai-agents-python/run.py

Source: https://openai.github.io/openai-agents-python/ko/ref/result

The `_create_error_details()` method is a utility function that constructs a `RunErrorDetails` object. This object encapsulates various pieces of information relevant to an agent run that has encountered an error. It includes details such as the initial input provided to the agent, any new items generated, raw responses received, the last agent that was active, context wrapper information, and the results of both input and output guardrails. This detailed error information can be invaluable for debugging and understanding the context in which an error occurred.

--------------------------------

### OpenAI Agents Python

Source: https://openai.github.io/openai-agents-python/ref/model_settings

The `extra_body` attribute allows you to provide additional body fields with the request. It defaults to `None` if not explicitly provided.

--------------------------------

### openai-agents-python/openai_agents/openai_agent.py

Source: https://openai.github.io/openai-agents-python/ref/extensions/litellm

The `_convert_gemini_extra_content_to_provider_specific_fields` method is designed to transform the way tool calls are represented for Gemini models. Specifically, it converts an internal format `extra_content={'google': {'thought_signature': '...'}}` into the `provider_specific_fields={'thought_signature': '...'}` format that LiteLLM expects. This conversion is crucial for ensuring that tool calls, particularly those involving thought signatures, are correctly interpreted by the underlying Gemini API. The method prioritizes processing tool calls that appear after the last user message in the conversation history, aligning with Gemini API's handling of such interactions. If no user message is present, all messages are considered for processing. The method iterates through messages, identifies assistant messages with tool calls, and then applies the transformation to the `provider_specific_fields` attribute within each tool call, setting it to an empty dictionary by default.

--------------------------------

### Agent Visualization

Source: https://openai.github.io/openai-agents-python/visualization

Agent visualization allows you to generate a structured graphical representation of agents and their relationships using **Graphviz**. This is useful for understanding how agents, tools, and handoffs interact within an application.

--------------------------------

### DaprSession > __aenter__

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/memory/dapr_session

Enters the asynchronous context manager for the DaprSession. It simply returns the session instance itself, allowing for the use of `async with` syntax to manage the session's lifecycle.

--------------------------------

### Handoff prompt > prompt_with_handoff_instructions

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/handoff_prompt

The `prompt_with_handoff_instructions` function is a utility designed to enhance agent prompts by including recommended instructions for agents that utilize handoffs. This function takes a user-provided prompt as input and prepends the `RECOMMENDED_PROMPT_PREFIX` to it, ensuring that the agent receives the necessary system context for proper operation within the multi-agent system. This is particularly useful for setting up agents that need to seamlessly transfer conversations to other agents.

--------------------------------

### Usage > Accessing usage with sessions

Source: https://openai.github.io/openai-agents-python/usage

When using sessions, such as `SQLiteSession`, each call to `Runner.run(...)` provides usage metrics specific to that particular run. While sessions maintain the conversation history for context, the usage recorded is independent for each execution. Previous messages might be re-sent as input in subsequent runs, which will impact the input token count for those turns.

Example:
```python
session = SQLiteSession("my_conversation")

first = await Runner.run(agent, "Hi!", session=session)
print(first.context_wrapper.usage.total_tokens)  # Usage for first run

second = await Runner.run(agent, "Can you elaborate?", session=session)
print(second.context_wrapper.usage.total_tokens)  # Usage for second run
```

--------------------------------

### Handoff dataclass > input_json_schema instance-attribute

Source: https://openai.github.io/openai-agents-python/ref/handoffs

The `input_json_schema` attribute defines the expected structure for any data that needs to be passed as input to the agent receiving the handoff. This schema ensures that the data is formatted correctly, and it can be an empty dictionary if the handoff does not require any specific input.

--------------------------------

### openai-agents-python/function_tool.py > function_tool

Source: https://openai.github.io/openai-agents-python/zh/ref/tool

The `function_tool` decorator offers several customization options. You can override the tool's name and description using `name_override` and `description_override`. The `docstring_style` can be explicitly set, or left to auto-detection. The `use_docstring_info` flag controls whether the docstring is used for description generation. A `failure_error_function` can be provided to customize error messages sent to the LLM upon tool failure; if set to `None`, an exception is raised instead. Strict mode for the tool's JSON schema is enabled by default (`strict_mode=True`) and is strongly recommended to improve the accuracy of JSON inputs.

--------------------------------

### Sessions > Session types > SQLite sessions

Source: https://openai.github.io/openai-agents-python/sessions

The default, lightweight session implementation uses SQLite. This provides a simple and efficient way to store conversation history. You can choose between an in-memory database, which is lost when the process ends, or a persistent file-based database for longer-term storage. This is a good starting point for many applications due to its ease of use and minimal setup.

--------------------------------

### BatchTraceProcessor

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/processors

The `on_trace_start` and `on_span_end` methods are responsible for adding trace and span data to the internal queue. Before attempting to add an item, they call `_ensure_thread_started` to make sure the background export thread is active. They then use `_queue.put_nowait` to add the item to the queue. If the queue is full (`queue.Full` exception), a warning is logged, and the item is dropped to prevent blocking.

--------------------------------

### MCP Server Configuration > MCPServerStdioParams > Structured Content Usage

Source: https://openai.github.io/openai-agents-python/zh/ref/mcp/server

The `use_structured_content` parameter in the MCP server configuration determines whether to utilize `tool_result.structured_content` during MCP tool calls. It defaults to `False` for backward compatibility, as many servers include structured data within the regular `tool_result.content`. Set this to `True` if your server guarantees that structured content is not duplicated in the general content field to avoid redundant data.

--------------------------------

### REPL utility

Source: https://openai.github.io/openai-agents-python/repl

The SDK provides `run_demo_loop` for quick, interactive testing of an agent's behavior directly in your terminal. `run_demo_loop` prompts for user input in a loop, keeping the conversation history between turns. By default, it streams model output as it is produced. When you run the example above, run_demo_loop starts an interactive chat session. It continuously asks for your input, remembers the entire conversation history between turns (so your agent knows what's been discussed) and automatically streams the agent's responses to you in real-time as they are generated.
To end this chat session, simply type `quit` or `exit` (and press Enter) or use the `Ctrl-D` keyboard shortcut.

--------------------------------

### Agent `dataclass`

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

Handoffs enable an agent to delegate tasks to other specialized agents, promoting modularity and separation of concerns. You can define a list of `handoffs`, which are essentially sub-agents that the primary agent can choose to transfer control to if deemed relevant. This hierarchical structure allows for complex workflows to be broken down into manageable components, where each agent focuses on a specific aspect of the overall task.

--------------------------------

### Span Class > __exit__

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `__exit__` method is used to exit the span's context, handling cleanup and potential exceptions.

--------------------------------

### InputGuardrail `dataclass` > name `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ja/ref/guardrail

The `name` attribute provides a name for the guardrail, which is useful for tracing purposes. If no name is explicitly provided, the system will use the name of the guardrail function by default.

--------------------------------

### ModelSettings > presence_penalty

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

The presence penalty to use when calling the model.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/zh/ref/model_settings

The `store` parameter determines whether the model's generated response should be saved for later retrieval. For the Responses API, this is typically enabled by default when not specified. For the Chat Completions API, it is disabled by default.

--------------------------------

### Database schema > turn_usage table

Source: https://openai.github.io/openai-agents-python/sessions/advanced_sqlite_session

The `turn_usage` table provides a granular view of resource consumption within a conversation. For each session, branch, and user turn, it logs the number of requests made, the total input, output, and combined tokens used. It also includes JSON fields for `input_tokens_details` and `output_tokens_details`, allowing for in-depth analysis of token distribution across different components or tools. This table is designed with a unique constraint on `session_id`, `branch_id`, and `user_turn_number` to prevent duplicate entries and ensure accurate tracking.

--------------------------------

### SQLAlchemySession > __init__

Source: https://openai.github.io/openai-agents-python/ref/extensions/memory/sqlalchemy_session

The `SQLAlchemySession` is initialized with a `session_id`, an `AsyncEngine`, and optional parameters for table creation and naming. The `AsyncEngine` must be configured with an asynchronous database driver. If `create_tables` is set to `True`, the class will automatically generate the necessary database tables and indexes for storing session metadata and messages. Otherwise, it assumes the tables already exist. Table names for sessions and messages can be customized using `sessions_table` and `messages_table` arguments respectively. A lock (`asyncio.Lock`) is used to ensure thread-safe access to the session.

--------------------------------

### AdvancedSQLiteSession

Source: https://openai.github.io/openai-agents-python/ko/ref/extensions/memory/advanced_sqlite_session

The `AdvancedSQLiteSession` class is an enhanced version of `SQLiteSession` designed to provide advanced features for managing conversational data. It introduces capabilities for conversation branching, allowing users to explore different conversational paths, and detailed usage analytics, which track token consumption and other metrics at a per-turn level. This class is particularly useful for applications that require robust logging, history management, and performance monitoring of AI agent interactions.

--------------------------------

### to_input_list

Source: https://openai.github.io/openai-agents-python/ref/result

The `to_input_list()` method creates and returns a new list that combines the original input items with any newly generated items. It first converts the original input into a new list format using `ItemHelpers.input_to_new_input_list()`. Then, it transforms each of the `new_items` into their input item representation using `item.to_input_item()`. Finally, it concatenates these two lists to form the complete input list, reflecting both the initial state and the additions made during the agent's run.

--------------------------------

### SingleAgentVoiceWorkflow

Source: https://openai.github.io/openai-agents-python/ja/ref/voice/workflow

The `on_start` method is an optional asynchronous method within the workflow. It is designed to be executed before any user input is received. This method can be utilized to generate an initial greeting or provide instructions to the user using Text-to-Speech (TTS) capabilities. By default, this method does nothing and returns an empty asynchronous iterator, signifying no action is taken.

--------------------------------

### OpenAI Agents Python API Reference > Handoff History Functions > nest_handoff_history

Source: https://openai.github.io/openai-agents-python/ref/handoffs

Summarize the previous transcript for the next agent. This function normalizes and flattens the input history, then applies a specified or default history mapper to create a summarized transcript. It filters out assistant messages from the pre-handoff items and returns a new `HandoffInputData` object with the updated input history and pre-handoff items.

--------------------------------

### spans.py > finish

Source: https://openai.github.io/openai-agents-python/ref/tracing

Finish the span. This method marks the completion of the span's execution, recording its duration. If `reset_current` is `True`, the span will be unset as the current span, potentially reverting to a previous one in the call stack.

--------------------------------

### ModelSettings > max_tokens

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

The maximum number of output tokens to generate.

--------------------------------

### Handoffs

Source: https://openai.github.io/openai-agents-python/ko/ref/handoffs

The `reset_conversation_history_wrappers` function restores the default markers used for nested conversation summaries. This is useful for ensuring that the conversation history is consistently marked, especially when dealing with multiple nested summaries.

--------------------------------

### Raw Model Events

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/events

The `RealtimeRawModelEvent` dataclass is used to forward raw events originating from the model layer. It encapsulates the `data`, which is of type `RealtimeModelEvent`, representing the actual raw information from the model. Similar to other events, it includes common `info` from `RealtimeEventInfo` for context. The `type` is set to 'raw_model_event' for clear identification.

--------------------------------

### openai_agents_python > custom_span

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/create

The `custom_span` function allows you to create a new custom span for detailed tracing and metadata association. This span is not automatically started; you need to explicitly manage its lifecycle using a `with` statement or by manually calling `span.start()` and `span.finish()`.

Key parameters include:
*   `name`: A required string for the span's name.
*   `data`: An optional dictionary for structured metadata.
*   `span_id`: An optional string for a custom span ID; otherwise, one is generated.
*   `parent`: An optional trace or span to set as the parent; defaults to the current context.
*   `disabled`: A boolean flag to prevent the span from being recorded.

--------------------------------

### traces.py > tracing_api_key

Source: https://openai.github.io/openai-agents-python/ref/tracing/traces

The `tracing_api_key` property represents the API key used for exporting trace and span data. This key is essential for authenticating with tracing backends when sending collected data.

--------------------------------

### AdvancedSQLiteSession

Source: https://openai.github.io/openai-agents-python/ref/extensions/memory/advanced_sqlite_session

The `AdvancedSQLiteSession` class is an enhanced version of `SQLiteSession` designed to support conversation branching and detailed usage analytics. It extends the functionality by introducing new database tables to manage conversation structures across different branches and to log token usage at a granular, turn-by-turn level. This allows for more complex conversation flows and better monitoring of resource consumption.

--------------------------------

### Model Settings > presence_penalty

Source: https://openai.github.io/openai-agents-python/ref/model_settings

The presence penalty to use when calling the model.

--------------------------------

### RealtimeModelConfig > initial_model_settings

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/model

The `initial_model_settings` parameter specifies the configuration to be used when establishing a connection to the realtime model.

--------------------------------

### Results > Other information > Original input

Source: https://openai.github.io/openai-agents-python/results

The `input` property stores the original input provided to the `run` method. While typically not needed, it is available in case you require access to it.

--------------------------------

### OpenAI Agents Python

Source: https://openai.github.io/openai-agents-python/ref/model_settings

The `extra_args` attribute is for arbitrary keyword arguments that can be passed directly to the model API call. These arguments are passed verbatim to the underlying model provider's API. Use this feature with caution, as not all models support all parameters.

--------------------------------

### Usage > Using usage in hooks

Source: https://openai.github.io/openai-agents-python/usage

If you are implementing `RunHooks`, the `context` object passed to each hook includes the `usage` information. This allows you to integrate usage logging directly into the agent's lifecycle, for instance, logging the total requests and tokens after an agent run completes.

Example:
```python
class MyHooks(RunHooks):
    async def on_agent_end(self, context: RunContextWrapper, agent: Agent, output: Any) -> None:
        u = context.usage
        print(f"{agent.name} → {u.requests} requests, {u.total_tokens} total tokens")
```

--------------------------------

### openai_github_io_openai-agents-python > function_schema

Source: https://openai.github.io/openai-agents-python/ja/ref/function_schema

The `function_schema` function, located in `src/agents/function_schema.py`, is designed to extract a structured representation of a Python function, known as a `FuncSchema`. This schema encapsulates essential details such as the function's name, a descriptive explanation, and descriptions for each of its parameters. It leverages information from the function's signature, type hints, and docstring to build this comprehensive schema. The function provides several parameters to customize the schema extraction process, including options to override the function's name and description, control the usage of docstring information, and enforce strict JSON schema compliance for better compatibility with LLM interpretation.

--------------------------------

### Agents > Agent

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

A list of checks that run on the final output of the agent, after generating a response. These checks only run if the agent produces a final output.

--------------------------------

### RealtimeRunner > run

Source: https://openai.github.io/openai-agents-python/ref/realtime/runner

Starts and returns a realtime session. This method establishes a connection and returns a `RealtimeSession` object, which facilitates bidirectional communication with the realtime model. The session object can be used to send messages and receive events asynchronously.

--------------------------------

### OpenAI Agents Python/realtime/config.py/Client Messages/type

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/config

The `type` attribute for `RealtimeClientMessage` is an instance attribute that specifies the type of the message being sent to the model. This field is explicitly required and defines the nature of the client's communication.

--------------------------------

### call_model_input_filter

Source: https://openai.github.io/openai-agents-python/ko/ref/run

Optional callback that is invoked immediately before calling the model. It receives the current agent, context and the model input (instructions and input items), and must return a possibly modified `ModelInputData` to use for the model call. This allows you to edit the input sent to the model e.g. to stay within a token limit. For example, you can use this to add a system prompt to the input.

--------------------------------

### litellm_model.py > convert_message_to_openai

Source: https://openai.github.io/openai-agents-python/ref/extensions/litellm

The `convert_message_to_openai` class method facilitates the conversion of a LiteLLM `Message` object into the OpenAI `ChatCompletionMessage` format. This method is crucial for standardizing message structures when interacting with different language models. It first validates that the message role is 'assistant,' as this is the expected role for this conversion. It then processes any `tool_calls` associated with the message, converting each one to the OpenAI format using the `convert_tool_call_to_openai` function. Additionally, it handles `provider_specific_fields`, extracting information like `refusal` status. It also consolidates `reasoning_content` and processes `thinking_blocks`, converting them into a dictionary format for consistent handling. Finally, it constructs and returns an `InternalChatCompletionMessage` object, which includes the message content, refusal status, role, annotations, audio information, tool calls, reasoning content, and thinking blocks, ensuring all relevant data is preserved in a format compatible with OpenAI's API.

--------------------------------

### Session sharing

Source: https://openai.github.io/openai-agents-python/sessions

The session management system supports session sharing, enabling different agents to interact within the same conversation history. This is achieved by using a single session object across multiple agent instances. Consequently, all agents interacting with the shared session will have access to the entire conversation's context, allowing for collaborative or multi-agent interactions within a unified dialogue.

--------------------------------

### Quickstart > Voice pipeline

Source: https://openai.github.io/openai-agents-python/voice/quickstart

We'll set up a simple voice pipeline, using `SingleAgentVoiceWorkflow` as the workflow. This class is designed to handle a single agent's interaction within the voice pipeline.

--------------------------------

### AgentBase `dataclass`

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

The `AgentBase` class serves as the foundational building block for both `Agent` and `RealtimeAgent` in the system. It is defined as a generic `dataclass` that accepts a type parameter `TContext` for context management. This base class encapsulates common attributes and behaviors shared by different agent types, promoting code reusability and a consistent structure for agent development.

--------------------------------

### `Handoff prompt`

Source: https://openai.github.io/openai-agents-python/ko/ref/extensions/handoff_prompt

Agents use two primary abstractions: **Agents** and **Handoffs**. An agent encompasses instructions and tools and can hand off a conversation to another agent when appropriate. Handoffs are achieved by calling a handoff function, generally named `transfer_to_<agent_name>`. Transfers between agents are handled seamlessly in the background; do not mention or draw attention to these transfers in your conversation with the user.

--------------------------------

### generation_span

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

Create a new generation span. The span will not be started automatically, you should either do `with generation_span() ...` or call `span.start()` + `span.finish()` manually. This span captures the details of a model generation, including the input message sequence, any generated outputs, the model name and configuration, and usage data. If you only need to capture a model response identifier, use `response_span()` instead.

--------------------------------

### openai-agents-python/src/agents/realtime/config.py > User Input Types > RealtimeUserInputText > text

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/config

The text content from the user.

--------------------------------

### openai-agents-python > agent.py > as_tool

Source: https://openai.github.io/openai-agents-python/ref/agent

The `as_tool` method accepts several parameters to configure the behavior of the agent when it's used as a tool. The `tool_name` parameter allows you to specify a name for the tool; if omitted, the agent's own name will be used. The `tool_description` is crucial for explaining the tool's purpose and when it should be invoked. An optional `custom_output_extractor` can be provided to define how the tool's output should be parsed, with a default behavior of using the agent's last message.

--------------------------------

### traces.py > start

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/traces

The `start` method initiates a trace. It can optionally mark the trace as the current trace in the execution context by setting `mark_as_current` to `True`. This method must be called before any spans can be added to the trace, and only one trace can be active as the 'current' trace at any given time. The operation is thread-safe when `mark_as_current` is used.

--------------------------------

### DaprSession > __aenter__

Source: https://openai.github.io/openai-agents-python/zh/ref/extensions/memory/dapr_session

Enters the asynchronous context manager for the DaprSession. This method is part of the asynchronous context management protocol and simply returns the session object itself, allowing for `async with` usage.

--------------------------------

### RealtimeAgent > name

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/agent

The `name` attribute provides a unique identifier for the agent, crucial for distinguishing and referencing it within a system.

--------------------------------

### Processor Interface > on_trace_start

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/processor_interface

The `on_trace_start` method is invoked synchronously whenever a new trace begins execution. The `trace` object passed to this method contains the workflow name and associated metadata. Implementations should return quickly to avoid blocking the execution flow and should handle any internal errors gracefully.

--------------------------------

### VoiceModelProvider > create_session

Source: https://openai.github.io/openai-agents-python/ko/ref/voice/model

Creates a new transcription session, which you can push audio to, and receive a stream of text transcriptions. This method requires the audio input to transcribe, the settings to use for the transcription, and boolean flags to indicate whether to include sensitive data and sensitive audio data in traces. It returns a `StreamedTranscriptionSession` object, which represents the active transcription session.

--------------------------------

### SQLiteSession

Source: https://openai.github.io/openai-agents-python/zh/ref/memory

This implementation stores conversation history in a SQLite database. By default, it uses an in-memory database that is lost when the process ends. For persistent storage, you can provide a file path to the `db_path` argument during initialization. The `SQLiteSession` class manages two tables: one for session metadata (defaulting to `agent_sessions`) and another for message data (defaulting to `agent_messages`). It handles connection management differently for in-memory and file-based databases to optimize concurrency and data persistence.

--------------------------------

### SingleAgentVoiceWorkflow > __init__

Source: https://openai.github.io/openai-agents-python/ref/voice/workflow

The `__init__` method initializes a new instance of the `SingleAgentVoiceWorkflow`. It takes an `agent` as a required argument, which is the agent that will be executed within the workflow. An optional `callbacks` argument can also be provided to specify callbacks that will be invoked during the workflow's execution. Internally, it initializes an empty list for `_input_history`, stores the provided `agent` in `_current_agent`, and saves the `callbacks`.

--------------------------------

### TracingProcessor

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/processor_interface

The `on_trace_start` method is invoked synchronously when a new trace begins. It receives the `trace` object, which contains workflow details and metadata. Implementations should execute quickly to avoid blocking the agent's execution and must handle any internal errors to ensure smooth operation. Similarly, `on_trace_end` is called synchronously upon trace completion, providing the full trace object with all its spans and results. This is an opportune moment for exporting completed trace data and performing any necessary trace-specific resource cleanup.

--------------------------------

### `RealtimeSession`

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/session

The initialization of `RealtimeSession` requires several key arguments: the `model` to connect to, the `agent` associated with the session, a `context` object, and optional configurations for the model (`model_config`) and the run (`run_config`). These parameters define the environment and behavior of the realtime connection.

--------------------------------

### MCP Server Configuration > MCPServerStdioParams

Source: https://openai.github.io/openai-agents-python/zh/ref/mcp/server

The `MCPServerStdioParams` configure the server, including the command to execute, its arguments, environment variables, working directory, and text encoding for communication. This class is essential for setting up a new MCP server that communicates via standard input/output.

--------------------------------

### Agent Configuration > Reset Tool Choice

Source: https://openai.github.io/openai-agents-python/ko/ref/agent

Determines whether the tool choice is reset to its default value after a tool has been called. Defaults to `True`, which helps prevent the agent from entering an infinite loop of tool usage.

--------------------------------

### MCPServerStdio

Source: https://openai.github.io/openai-agents-python/ref/mcp/server

The `MCPServerStdio` class implements the Model Context Protocol (MCP) server using the stdio transport. This means that communication between the client and server happens through standard input and output streams. The constructor for `MCPServerStdio` accepts a `params` object, which is crucial for configuring the server. This `params` object should contain details such as the command to execute for starting the server, any arguments to pass to that command, environment variables to set, the working directory for the process, and the text encoding to use for messages. Additional optional parameters allow for controlling tool list caching, setting a readable name for the server, configuring client session timeouts, applying tool filters, specifying whether to use structured content in tool results, and setting retry parameters for tool calls.

--------------------------------

### Model Settings > store

Source: https://openai.github.io/openai-agents-python/ref/model_settings

Whether to store the generated model response for later retrieval. For Responses API: automatically enabled when not specified. For Chat Completions API: disabled when not specified.

--------------------------------

### OpenAI Agents Python > input_tokens

Source: https://openai.github.io/openai-agents-python/ko/ref/usage

Total input tokens sent, across all requests.

--------------------------------

### RunResult dataclass > input instance-attribute

Source: https://openai.github.io/openai-agents-python/ref/result

The `input` attribute holds the original input items provided to the agent before the `run()` method was invoked. This could be a single string or a list of `TResponseInputItem` objects. It's important to note that this attribute might contain a modified version of the input if any handoff input filters were applied, which could alter the input before it's processed by the agent.

--------------------------------

### ModelSettings > top_logprobs

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

Number of top tokens to return logprobs for. Setting this will automatically include `"message.output_text.logprobs"` in the response.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

The `store` parameter determines whether the model's generated response should be saved for later retrieval. For the Responses API, this is automatically enabled if not specified. However, for the Chat Completions API, it is disabled by default unless explicitly enabled.

--------------------------------

### agent `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ko/ref/items

The `agent` attribute represents the agent whose run generated this item. It holds a reference to the agent instance.

--------------------------------

### Lifecycle > RunHooksBase

Source: https://openai.github.io/openai-agents-python/ref/lifecycle

The `RunHooksBase` class provides a framework for receiving callbacks on various lifecycle events that occur during an agent's run. By subclassing `RunHooksBase` and overriding its methods, developers can inject custom logic at specific points in the agent's execution flow. This allows for detailed monitoring, modification, or extension of agent behavior. For instance, you can implement `on_llm_start` to log LLM requests, `on_agent_end` to process the final output of an agent, or `on_handoff` to manage transitions between agents.

--------------------------------

### Runner > run

Source: https://openai.github.io/openai-agents-python/ref/run

The `run` method in the `Runner` class executes an agent workflow. It takes the `starting_agent`, initial `input`, and optional parameters such as `context`, `max_turns`, `hooks`, `run_config`, `previous_response_id`, `auto_previous_response_id`, `conversation_id`, and `session`.

- `starting_agent`: The first agent in the workflow.
- `input`: The data fed to the initial agent. Can be a string or a list of input items.
- `context`: Optional contextual information for the agent's execution.
- `max_turns`: The maximum number of agent invocations (including tool calls) allowed per run.
- `hooks`: Callbacks for lifecycle events during the run.
- `run_config`: Global configuration settings for the entire agent execution.
- `previous_response_id`: Used with OpenAI Responses API to potentially skip re-sending previous input.
- `auto_previous_response_id`: A boolean flag related to automatically managing `previous_response_id`.
- `conversation_id`: An identifier for a conversation, enabling the agent to access and write to conversation history. Recommended for OpenAI models.
- `session`: A session object for managing conversation history automatically.

This method returns a `RunResult` object, which contains all inputs, guardrail outcomes, and the final output from the agent. Since agents can perform handoffs, the exact type of the output is not predetermined.

--------------------------------

### FunctionTool dataclass

Source: https://openai.github.io/openai-agents-python/ko/ref/tool

The `FunctionTool` is a dataclass designed to wrap a Python function, making it usable as a tool within the agent framework. It provides a structured way to define the tool's name, description, and parameter schema, which are essential for the Language Model (LLM) to understand and interact with the tool. The `on_invoke_tool` field is a crucial callable that defines the actual logic to be executed when the tool is invoked, handling the tool's context and parameters passed from the LLM. The `strict_json_schema` attribute, recommended to be set to `True`, enforces a stricter adherence to the defined JSON schema for tool parameters, improving the reliability of input validation.

--------------------------------

### RealtimeRunner > __init__

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/runner

Initializes the realtime runner. The `starting_agent` parameter is required and specifies the agent to begin the session with. The `model` parameter is optional; if not provided, a default OpenAI realtime model will be used. The `config` parameter allows overriding run parameters for the entire session.

--------------------------------

### Tracing > tracing_api_key

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `tracing_api_key` is the API key used for exporting trace data and its associated spans. This key is essential for authenticating and authorizing the transmission of tracing information to external backends or monitoring systems.

--------------------------------

### MCP Server Streamable HTTP Transport > __init__ > name

Source: https://openai.github.io/openai-agents-python/ja/ref/mcp/server

The `name` parameter provides a human-readable identifier for the server. If omitted, a name is automatically generated based on the server's URL.

--------------------------------

### FunctionToolResult > run_item

Source: https://openai.github.io/openai-agents-python/ref/tool

The run item that was produced as a result of the tool call.

--------------------------------

### SessionABC > add_items

Source: https://openai.github.io/openai-agents-python/ref/memory/session

Add new items to the conversation history. Args: items: List of input items to add to the history

--------------------------------

### Usage > input_tokens

Source: https://openai.github.io/openai-agents-python/zh/ref/usage

The `input_tokens` attribute represents the cumulative total of input tokens sent across all requests made to the LLM API. This provides an overall measure of the data processed as input.

--------------------------------

### RunResult dataclass > new_items instance-attribute

Source: https://openai.github.io/openai-agents-python/ja/ref/result

The `new_items` attribute is a list that holds all the new items generated during an agent's run. This typically includes new messages, tool calls made by the agent, and the outputs from those tool calls.

--------------------------------

### SQLAlchemySession

Source: https://openai.github.io/openai-agents-python/zh/ref/extensions/memory/sqlalchemy_session

The `SQLAlchemySession` is initialized with a `session_id` that uniquely identifies a conversation. It requires an `AsyncEngine` instance from SQLAlchemy, which must be configured for asynchronous database operations. The constructor also accepts `create_tables` (a boolean to automatically create necessary database tables), `sessions_table` (to specify the table name for session metadata), and `messages_table` (to specify the table name for conversation messages). The class defines the schema for both sessions and messages, including columns for session IDs, timestamps, and message data. It also sets up an asynchronous session factory using `async_sessionmaker`.

--------------------------------

### Agent Visualization > Customizing the Graph > Showing the Graph

Source: https://openai.github.io/openai-agents-python/visualization

By default, `draw_graph` displays the graph inline. To show the graph in a separate window, write the following:
```
draw_graph(triage_agent).view()
```

--------------------------------

### Model Settings > extra_args

Source: https://openai.github.io/openai-agents-python/ko/ref/model_settings

`extra_args`: Arbitrary keyword arguments to pass to the model API call. These will be passed directly to the underlying model provider's API. Use with caution as not all models support all parameters.

--------------------------------

### MultiProvider

Source: https://openai.github.io/openai-agents-python/ja/ref/models/multi_provider

The `MultiProvider` class maps a model to a specific `ModelProvider` based on the prefix of the model name. This allows for flexible routing of model requests to different underlying providers. By default, model names starting with "openai/" or having no prefix are directed to the `OpenAIProvider`. Model names prefixed with "litellm/" are routed to the `LitellmProvider`. This default behavior can be customized or overridden to suit specific project needs.

--------------------------------

### AgentManager > find_turns_by_content

Source: https://openai.github.io/openai-agents-python/zh/ref/extensions/memory/advanced_sqlite_session

The `find_turns_by_content` method allows searching for user turns that contain specific text within a given branch. It executes a SQL query to filter messages based on the provided `search_term`. The method returns a list of matching turns, formatted identically to the output of `get_conversation_turns`, enabling users to locate specific parts of the conversation history.

--------------------------------

### Realtime Configuration > Model Configuration > initial_model_settings

Source: https://openai.github.io/openai-agents-python/ref/realtime/config

The `initial_model_settings` attribute in Model Configuration allows you to specify the initial settings for the realtime model when establishing a connection. This enables pre-configuration of model behavior before the session begins.

--------------------------------

### RunResult dataclass > input instance-attribute

Source: https://openai.github.io/openai-agents-python/ko/ref/result

The `input` attribute stores the original input provided to the agent before its execution. This input can be a single item or a list of items. It's important to note that this attribute might contain a mutated version of the input if any handoff input filters were applied, which could alter the data before it's processed by the agent. This preserves the initial state for later inspection or debugging.

--------------------------------

### traces.py > finish

Source: https://openai.github.io/openai-agents-python/ref/tracing/traces

The `finish` method is responsible for completing a trace and has an option to reset the current trace. This action finalizes all open spans associated with the trace. The `reset_current` parameter, if set to `True`, will revert the current trace to the previous one in the execution context. This method must be called to ensure the trace is properly concluded.

--------------------------------

### Configuring the SDK > Debug logging

Source: https://openai.github.io/openai-agents-python/config

For more granular control over logging, you can customize the SDK's loggers by adding specific handlers, filters, and formatters. You can obtain a logger instance using `logging.getLogger()` with the appropriate name (e.g., `"openai.agents"` or `"openai.agents.tracing"`). You can then set the logging level (e.g., `logging.DEBUG`, `logging.INFO`, `logging.WARNING`) and add handlers, such as `logging.StreamHandler()`, to direct output as needed.

```python
import logging

logger = logging.getLogger("openai.agents") # or openai.agents.tracing for the Tracing logger

# To make all logs show up
logger.setLevel(logging.DEBUG)
# To make info and above show up
logger.setLevel(logging.INFO)
# To make warning and above show up
logger.setLevel(logging.WARNING)
# etc

# You can customize this as needed, but this will output to `stderr` by default
logger.addHandler(logging.StreamHandler())
```

--------------------------------

### RealtimeAgent > name

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/agent

The `name` attribute provides a unique identifier for the agent.

--------------------------------

### openai_github_io_openai-agents-python

Source: https://openai.github.io/openai-agents-python/ja/ref/mcp/server

Create a new MCP server based on the HTTP with SSE transport.

Parameters:
`params`: The params that configure the server. This includes the URL of the server, the headers to send to the server, the timeout for the HTTP request, and the timeout for the SSE connection.
`cache_tools_list`: Whether to cache the tools list. If `True`, the tools list will be cached and only fetched from the server once. If `False`, the tools list will be fetched from the server on each call to `list_tools()`. The cache can be invalidated by calling `invalidate_tools_cache()`. You should set this to `True` if you know the server will not change its tools list, because it can drastically improve latency (by avoiding a round-trip to the server every time).
`name`: A readable name for the server. If not provided, we'll create one from the URL.
`client_session_timeout_seconds`: the read timeout passed to the MCP ClientSession.
`tool_filter`: The tool filter to use for filtering tools.
`use_structured_content`: Whether to use `tool_result.structured_content` when calling an MCP tool. Defaults to False for backwards compatibility - most MCP servers still include the structured content in the `tool_result.content`, and using it by default will cause duplicate content. You can set this to True if you know the server will not duplicate the structured content in the `tool_result.content`.
`max_retry_attempts`: Number of times to retry failed list_tools/call_tool calls. Defaults to no retries.
`retry_backoff_seconds_base`: The base delay, in seconds, for exponential backoff between retries.
`message_handler`: Optional handler invoked for session messages as delivered by the ClientSession.

--------------------------------

### SQLiteSession

Source: https://openai.github.io/openai-agents-python/ko/ref/memory/sqlite_session

The `__init__` method for `SQLiteSession` initializes the session storage. It requires a unique `session_id` for each conversation. You can also specify the `db_path` for persistent storage, defaulting to an in-memory database. Additionally, you can customize the table names for storing session metadata (`sessions_table`) and message data (`messages_table`). The implementation manages database connections differently for in-memory and file-based databases to optimize for concurrency and persistence.

--------------------------------

### LitellmModel

Source: https://openai.github.io/openai-agents-python/ko/ref/extensions/litellm

The `LitellmModel` class serves as an interface to leverage any language model that is compatible with the LiteLLM library. LiteLLM is a powerful abstraction layer that unifies access to numerous LLM providers, including but not limited to OpenAI, Anthropic, Gemini, and Mistral. This class simplifies the process of integrating diverse models into your application by providing a consistent API, regardless of the underlying model provider. The primary configuration for `LitellmModel` involves specifying the `model` name, and optionally providing a `base_url` and `api_key` if required by the specific model or its hosting environment. This flexibility ensures that you can easily switch between or utilize multiple LLM backends without significant code changes.

--------------------------------

### Handoff dataclass > agent_name instance-attribute

Source: https://openai.github.io/openai-agents-python/ja/ref/handoffs

The name of the agent that is being handed off to.

--------------------------------

### SingleAgentVoiceWorkflow > on_start

Source: https://openai.github.io/openai-agents-python/ref/voice/workflow

The `on_start` method is an optional asynchronous method within the workflow. It is designed to be executed before any user input is processed. This method is ideal for tasks like delivering an initial greeting or providing instructions to the user via Text-to-Speech (TTS). By default, this method does nothing, allowing for flexibility in how the workflow begins.

--------------------------------

### DaprSession

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/memory/dapr_session

The `_get_read_metadata` method is an internal helper function within the `DaprSession` class. Its primary purpose is to construct and return a dictionary containing metadata relevant for read operations performed on the Dapr state store. This metadata includes the consistency level specified during the session's initialization. By passing the consistency level through `state_metadata` in Dapr's state API calls, the class ensures that read operations adhere to the desired consistency guarantees, whether it's eventual or strong consistency, depending on the configuration.

--------------------------------

### OpenAI Agents Python/realtime/config.py/User Input Types/RealtimeUserInputMessage/content

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/config

The `content` attribute within `RealtimeUserInputMessage` is an instance attribute that holds a list of content items. These items can be either text (`RealtimeUserInputText`) or images (`RealtimeUserInputImage`), allowing for rich and multimodal user messages to be sent to the model.

--------------------------------

### InputGuardrail `dataclass` > name `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ko/ref/guardrail

The `name` attribute is the name of the guardrail, used for tracing. If not provided, the guardrail function's name will be used.

--------------------------------

### SessionABC > add_items

Source: https://openai.github.io/openai-agents-python/ja/ref/memory/session

Add new items to the conversation history. Args: `items`: List of input items to add to the history

--------------------------------

### Tracing > Creating spans

Source: https://openai.github.io/openai-agents-python/tracing

You can use the various `*_span()` methods to create a span. In general, you don't need to manually create spans. A `custom_span()` function is available for tracking custom span information. Spans are automatically part of the current trace, and are nested under the nearest current span, which is tracked via a Python `contextvar`.

--------------------------------

### Usage

Source: https://openai.github.io/openai-agents-python/usage

The Agents SDK automatically tracks token usage for every run. You can access it from the run context and use it to monitor costs, enforce limits, or record analytics.

What is tracked includes:
* **requests**: number of LLM API calls made
* **input_tokens**: total input tokens sent
* **output_tokens**: total output tokens received
* **total_tokens**: input + output
* **request_usage_entries**: list of per-request usage breakdowns
* **details**: includes `input_tokens_details.cached_tokens` and `output_tokens_details.reasoning_tokens`.

--------------------------------

### Tools > Function tools > Returning images or files from function tools

Source: https://openai.github.io/openai-agents-python/tools

In addition to returning text outputs, you can return one or many images or files as the output of a function tool. To do so, you can return any of:
  * Images: `ToolOutputImage` (or the TypedDict version, `ToolOutputImageDict`)
  * Files: `ToolOutputFileContent` (or the TypedDict version, `ToolOutputFileContentDict`)
  * Text: either a string or stringable objects, or `ToolOutputText` (or the TypedDict version, `ToolOutputTextDict`)

--------------------------------

### function_tool

Source: https://openai.github.io/openai-agents-python/ref/tool

The `function_tool` decorator is used to convert a Python function into a `FunctionTool`. This tool can then be utilized by agents for various tasks.

By default, when you decorate a function with `function_tool`, the following actions are performed automatically:
1.  **Parameter Schema Generation**: The function's signature is parsed to automatically create a JSON schema that defines the tool's parameters. This schema is crucial for the agent to understand how to call the tool correctly.
2.  **Description Population**: The function's docstring is used to automatically populate the description of the tool. This provides a human-readable explanation of what the tool does.
3.  **Argument Description Population**: Similarly, the function's docstring is leveraged to provide descriptions for each argument the tool accepts.

The style of the docstring used for these purposes is typically auto-detected. However, you have the flexibility to override this auto-detection if needed.

**Context Handling**: If your function is designed to accept a `RunContextWrapper` as its first argument, it is imperative that the type of this context wrapper precisely matches the context type used by the agent that will be employing this tool. This ensures proper data flow and compatibility within the agent's execution environment.

--------------------------------

### SQLiteSession

Source: https://openai.github.io/openai-agents-python/ja/ref/memory/sqlite_session

The SQLiteSession is initialized with a unique `session_id` for each conversation. It also accepts optional parameters for `db_path` to specify the database file location (defaulting to an in-memory database), `sessions_table` for session metadata, and `messages_table` for storing message data. For in-memory databases, a shared connection is used to prevent thread isolation issues. For file-based databases, thread-local connections are employed to enhance concurrency, and the database schema is initialized once to ensure persistence.

--------------------------------

### Agent Attributes > name

Source: https://openai.github.io/openai-agents-python/ko/ref/agent

This attribute stores the unique name assigned to the agent, used for identification.

--------------------------------

### Lifecycle > AgentHooksBase

Source: https://openai.github.io/openai-agents-python/zh/ref/lifecycle

`AgentHooksBase` is a generic base class that provides callbacks for lifecycle events related to a specific agent. By subclassing `AgentHooksBase` and overriding its methods, developers can define custom actions that should occur at different points in an agent's lifecycle. Key methods include `on_start`, which is called before the agent is invoked, `on_end`, which is called when the agent produces its final output, `on_handoff`, which is called when the agent is being handed off to, `on_tool_start`, called before a tool is invoked by this agent, `on_tool_end`, called after a tool is invoked, `on_llm_start`, called before the agent makes an LLM call, and `on_llm_end`, called after the agent receives an LLM response.

--------------------------------

### src/agents/tracing/create.py > generation_span

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

Creates a new generation span. This span is used to capture the details of a model generation process. The span is not started automatically; you need to explicitly start and finish it using `with generation_span() ...` or by calling `span.start()` and `span.finish()` manually. It records information such as the input messages, generated outputs, model used, its configuration, and usage statistics. For simpler tracking of just a model response identifier, `response_span()` is recommended.

--------------------------------

### run_streamed `classmethod`

Source: https://openai.github.io/openai-agents-python/ref/run

The `run_streamed` classmethod executes a workflow beginning with a specified agent, operating in a streaming fashion. Upon completion, it returns a result object equipped with a method to stream semantic events as they are produced. The agent operates iteratively until a definitive output is achieved. This loop proceeds as follows: first, the agent is invoked with the provided input. If the agent generates a final output (identified by its `output_type`), the loop concludes. In the event of a handoff, the loop continues with the newly assigned agent. Otherwise, any associated tool calls are executed, and the loop resumes.

--------------------------------

### MCPServerStdio > __init__

Source: https://openai.github.io/openai-agents-python/ko/ref/mcp/server

The `MCPServerStdio` class creates a new MCP server utilizing the stdio transport mechanism. This server is configured through `MCPServerStdioParams`, which define crucial aspects such as the command to execute for starting the server, any arguments to pass to that command, environment variables to set for the server process, the working directory from which the process should be spawned, and the text encoding used for communication.  The initialization allows for optional parameters like a server name, a client session timeout, a tool filter, a flag to control the use of structured content, retry attempt configurations, and a custom message handler.

--------------------------------

### Usage > Per-request usage tracking

Source: https://openai.github.io/openai-agents-python/usage

The SDK automatically tracks the usage for each individual API request and stores it in `request_usage_entries`. This is particularly useful for detailed cost calculations and for monitoring how the context window is being consumed over multiple requests within a single run.

Example:
```python
result = await Runner.run(agent, "What's the weather in Tokyo?")

for i, request in enumerate(result.context_wrapper.usage.request_usage_entries):
    print(f"Request {i + 1}: {request.input_tokens} in, {request.output_tokens} out")
```

--------------------------------

### MCP Server Streamable HTTP Transport > __init__ > params

Source: https://openai.github.io/openai-agents-python/ja/ref/mcp/server

The `params` argument configures the server and includes the server's URL, necessary headers, HTTP request timeout, Streamable HTTP connection timeout, a flag to terminate on close, and an optional custom HTTP client factory.

--------------------------------

### TracingProcessor > on_span_start

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/processor_interface

The `on_span_start` method is called synchronously when a new span begins. It receives the `span` object, which contains details about the operation and its context. This method should return quickly to avoid blocking the agent's workflow. Spans are automatically managed with respect to nesting under the current trace or parent span.

--------------------------------

### Handoff Tool Construction and Enablement

Source: https://openai.github.io/openai-agents-python/zh/ref/handoffs

The `Handoff` tool is constructed with a `tool_name` and `tool_description`, which can be overridden or generated by default based on the agent. The `input_json_schema` is always ensured to be in strict mode. The `_is_enabled` helper function checks if the handoff is enabled, respecting whether `is_enabled` is a simple boolean or a callable that dynamically determines enablement based on the run context and agent.

--------------------------------

### Agent Attributes > model_settings

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

Configures model-specific tuning parameters (e.g. temperature, top_p).

--------------------------------

### openai_github_io_openai-agents-python > function_schema

Source: https://openai.github.io/openai-agents-python/ref/function_schema

The `function_schema` function is designed to extract a `FuncSchema` from a given Python function. This schema captures essential metadata about the function, including its name, description, and detailed parameter descriptions. It leverages the function's docstring and type hints to populate this information. The function offers several options for customization, such as overriding the function's name or description, and controlling whether docstring information is used.

--------------------------------

### Trace Class > finish

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/traces

The `finish` method is responsible for completing a trace. It finalizes all open spans and must be called to ensure the trace data is properly closed. Optionally, it can reset the current trace to the previous one in the execution context. This method is thread-safe when `reset_current` is utilized.

--------------------------------

### OpenAI Agents Python

Source: https://openai.github.io/openai-agents-python/zh/ref/extensions/litellm

The `acompletion` method in the `litellm` library is used for making asynchronous calls to various language models. It supports parameters such as `model`, `messages`, `tools`, `temperature`, `top_p`, `frequency_penalty`, `presence_penalty`, `max_tokens`, `tool_choice`, `response_format`, `parallel_tool_calls`, `stream`, `stream_options`, `reasoning_effort`, `top_logprobs`, `extra_headers`, `api_key`, and `base_url`. The method handles the merging of various settings, including `model_settings.extra_query`, `model_settings.metadata`, `model_settings.extra_body`, and `model_settings.extra_args`, into `extra_kwargs`. It also includes logic to prevent duplicate `reasoning_effort` arguments when it's promoted to a top-level argument. The method returns a `ModelResponse` object if successful, or a tuple containing a `Response` object and the raw model response.

--------------------------------

### OpenAI Agents Python SDK > Usage Attributes > output_tokens_details

Source: https://openai.github.io/openai-agents-python/ja/ref/usage

The `output_tokens_details` attribute offers detailed information about the output tokens received. It is an instance of `OutputTokensDetails`, with `reasoning_tokens` initialized to 0. Similar to `input_tokens_details`, this attribute aligns with the Responses API's usage details, facilitating a deeper analysis of the output.

--------------------------------

### `repl` > `run_demo_loop`

Source: https://openai.github.io/openai-agents-python/ref/repl

The `run_demo_loop` function facilitates a simple REPL (Read-Eval-Print Loop) for an agent. This is a valuable tool for immediate command-line testing and debugging of agents. Throughout the interaction, the conversation's state is maintained. To exit the loop, the user can type `exit` or `quit`.

--------------------------------

### TracingProcessor > on_span_start

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

When a new span begins execution, the `on_span_start` method is called. It receives the `span` object, which includes details about the operation and its context. This method, like `on_trace_start`, is called synchronously and should return quickly to prevent blocking the agent. Spans are automatically managed for nesting under the current trace or parent span.

--------------------------------

### MCP Server SSE Initialization

Source: https://openai.github.io/openai-agents-python/ko/ref/mcp/server

Creates a new MCP server utilizing the HTTP with SSE (Server-Sent Events) transport. This constructor accepts several parameters to configure the server's behavior, including connection details, caching mechanisms, and retry logic.

The `params` argument is crucial as it holds the server's URL, headers, and various timeout configurations for both HTTP requests and SSE connections.

The `cache_tools_list` parameter, when set to `True`, optimizes performance by caching the tools list, thus avoiding repeated server requests. This is recommended when the server's toolset is static. The cache can be explicitly invalidated using `invalidate_tools_cache()`.

Other parameters include an optional `name` for the server, `client_session_timeout_seconds` for read timeouts, a `tool_filter` for selective tool usage, `use_structured_content` to control the parsing of tool results, and configurations for retrying failed operations (`max_retry_attempts`, `retry_backoff_seconds_base`). An optional `message_handler` can also be provided to process session messages.

--------------------------------

### trace_id

Source: https://openai.github.io/openai-agents-python/ko/ref/run

A custom trace ID to use for tracing. If not provided, we will generate a new trace ID.

--------------------------------

### Usage > output_tokens_details

Source: https://openai.github.io/openai-agents-python/zh/ref/usage

The `output_tokens_details` attribute offers detailed insights into output token consumption, mirroring the usage details found in the responses API. It is an instance of `OutputTokensDetails`, with reasoning tokens defaulting to 0.

--------------------------------

### Agent Parameters

Source: https://openai.github.io/openai-agents-python/ref/agent

The type of the output object. If not provided, the output will be `str`. In most cases, you should pass a regular Python type (e.g. a dataclass, Pydantic model, TypedDict, etc).
You can customize this in two ways:
1. If you want non-strict schemas, pass `AgentOutputSchema(MyClass, strict_json_schema=False)`.
2. If you want to use a custom JSON schema (i.e. without using the SDK's automatic schema) creation, subclass and pass an `AgentOutputSchemaBase` subclass.

--------------------------------

### MCPServerSse

Source: https://openai.github.io/openai-agents-python/ko/ref/mcp/server

The `__init__` method for `MCPServerSse` allows for the creation of a new MCP server instance using the HTTP with SSE transport. It accepts several parameters to configure the server's behavior. `params` is a crucial argument, containing server details like the URL, headers, and various timeout configurations for HTTP requests and SSE connections. Optional arguments include `cache_tools_list` to optimize tool fetching latency, `name` for a human-readable server identifier, `client_session_timeout_seconds` for the client session's read timeout, `tool_filter` to specify which tools are permissible, `use_structured_content` to control the use of structured content in tool results, and parameters for managing retries (`max_retry_attempts`, `retry_backoff_seconds_base`) and handling session messages (`message_handler`).

--------------------------------

### speech_span

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/create

The `speech_span` function is used to create a new speech span for tracing text-to-speech operations. This span is not started automatically; you must explicitly start and finish it using a `with` statement or by calling `span.start()` and `span.finish()` methods. It accepts various parameters to configure the span, including the `model` name, `input` text, `output` audio data, `output_format`, `model_config` hyperparameters, `first_content_at` timestamp, an optional `span_id`, a `parent` span or trace, and a `disabled` flag. If `span_id` is not provided, one will be generated automatically, though using `util.gen_span_id()` is recommended for proper formatting. If `parent` is omitted, the current trace or span will be used as the parent.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/zh/ref/model_settings

The `extra_args` parameter is a dictionary for passing arbitrary keyword arguments directly to the underlying model provider's API call. This provides maximum flexibility for utilizing provider-specific features or parameters not otherwise exposed by the `ModelSettings` class.

--------------------------------

### Results > RunResultBase dataclass

Source: https://openai.github.io/openai-agents-python/zh/ref/result

The `context_wrapper` attribute in `RunResultBase` provides access to the context that was used during the agent's run. This context can contain various pieces of information or configurations that influenced the agent's behavior or that were updated during the run. It's typed generically as `RunContextWrapper[Any]` to accommodate different context implementations.

--------------------------------

### OpenAI Agents Python/realtime/config.py/Tracing Configuration/workflow_name

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/config

The `workflow_name` is an instance attribute used for tracing within realtime model sessions. It specifies the name of the workflow that will be associated with the trace, helping to categorize and identify related tracing data.

--------------------------------

### Agent Attributes > name

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

This attribute stores the unique name assigned to the agent.

--------------------------------

### store_run_usage

Source: https://openai.github.io/openai-agents-python/zh/ref/extensions/memory/advanced_sqlite_session

Store usage data for the current conversation turn. This is designed to be called after `Runner.run()` completes. Session-level usage can be aggregated from turn data when needed. The function takes a `RunResult` object as input, which contains the usage information from the completed run. It attempts to store this usage data, specifically focusing on turn-level usage, while noting that session-level usage is aggregated on demand. The internal method `_update_turn_usage_internal` is used for this purpose. If any exceptions occur during the process, an error message is logged.

--------------------------------

### RealtimeAgent > handoffs

Source: https://openai.github.io/openai-agents-python/ref/realtime/agent

The `handoffs` parameter is a list that enables the `RealtimeAgent` to delegate tasks to other specialized sub-agents, known as handoffs. This promotes modularity and separation of concerns within the agent architecture. The agent can dynamically choose to delegate to these handoffs when relevant, improving the overall organization and efficiency of the system.

--------------------------------

### Input > AudioInput > channels

Source: https://openai.github.io/openai-agents-python/zh/ref/voice/input

The `channels` instance attribute of `AudioInput` defines the number of audio channels. It defaults to 1, indicating mono audio.

--------------------------------

### DaprSession > clear_session

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/memory/dapr_session

Clears all items for this session. This is achieved by deleting the stored messages and metadata keys from the Dapr state store.

--------------------------------

### Model Settings > top_logprobs

Source: https://openai.github.io/openai-agents-python/ref/model_settings

Number of top tokens to return logprobs for. Setting this will automatically include "message.output_text.logprobs" in the response.

--------------------------------

### Examples > Categories > memory

Source: https://openai.github.io/openai-agents-python/examples

Examples of different memory implementations for agents, including: SQLite session storage, Advanced SQLite session storage, Redis session storage, SQLAlchemy session storage, Encrypted session storage, and OpenAI session storage.

--------------------------------

### openai-agents-python/agent.py

Source: https://openai.github.io/openai-agents-python/ko/ref/agent

The `tool_name` parameter is the name of the tool. If not provided, the agent's name will be used. The `tool_description` is the description of the tool, which should indicate what it does and when to use it. The `custom_output_extractor` is a function that extracts the output from the agent. If not provided, the last message from the agent will be used. The `is_enabled` parameter determines whether the tool is enabled. It can be a boolean or a callable that takes the run context and agent and returns whether the tool is enabled. Disabled tools are hidden from the LLM at runtime.

--------------------------------

### RunConfig `dataclass` > session_input_callback `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/zh/ref/run

The `session_input_callback` attribute defines how session history is handled when new input is provided. By default (`None`), new input is simply appended to the existing history. However, you can provide a custom `SessionInputCallback` function. This function receives the current history and the new input, and it's responsible for returning the desired combined list of items, offering control over history management.

--------------------------------

### __init__

Source: https://openai.github.io/openai-agents-python/ko/ref/extensions/memory/dapr_session

Initializes a new DaprSession.

Args:
    session_id (str): Unique identifier for the conversation.
    state_store_name (str): Name of the Dapr state store component.
    dapr_client (DaprClient): A pre-configured Dapr client.
    ttl (int | None, optional): Time-to-live in seconds for session data.
        If None, data persists indefinitely. Note that TTL support depends on
        the underlying state store implementation. Defaults to None.
    consistency (ConsistencyLevel, optional): Consistency level for state operations.
        Use DAPR_CONSISTENCY_EVENTUAL or DAPR_CONSISTENCY_STRONG constants.
        Defaults to DAPR_CONSISTENCY_EVENTUAL.

--------------------------------

### Processor Interface > shutdown

Source: https://openai.github.io/openai-agents-python/ref/tracing

The `shutdown` method is an abstract method called when the application is stopping. It is intended for releasing any held resources, such as flushing queued traces or spans, closing network connections, or freeing up memory. Proper implementation of this method ensures a clean termination of the tracing system.

--------------------------------

### generation_span

Source: https://openai.github.io/openai-agents-python/ref/tracing/create

The `generation_span` function is used to create a new span that captures the details of a model generation. This span includes the input message sequence, any generated outputs, the model name and configuration, and usage data. The span is not started automatically; you must either use a `with` statement (e.g., `with generation_span() ...`) or manually call `span.start()` and `span.finish()`.

Key parameters for `generation_span` include:
*   `input`: The sequence of messages sent to the model.
*   `output`: The sequence of messages received from the model.
*   `model`: The identifier of the model used.
*   `model_config`: The hyperparameters used for the model.
*   `usage`: A dictionary containing usage statistics like token counts.
*   `span_id`: An optional ID for the span; if not provided, one will be generated.
*   `parent`: The parent span or trace; defaults to the current trace/span if not specified.
*   `disabled`: A boolean flag to prevent the span from being recorded.

--------------------------------

### OpenAI Agents Python SDK > Usage Attributes > input_tokens_details

Source: https://openai.github.io/openai-agents-python/ja/ref/usage

The `input_tokens_details` attribute provides a more granular breakdown of the input tokens. It is an instance of `InputTokensDetails` and is initialized with `cached_tokens` set to 0. This attribute is designed to match the usage details found in the Responses API, allowing for precise tracking of input token characteristics.

--------------------------------

### run `async` `classmethod`

Source: https://openai.github.io/openai-agents-python/ref/run

The `run` class method initiates a workflow by starting with a specified agent. This agent will then operate in a loop, continuing until a definitive output is produced. The loop's execution follows a specific sequence: first, the agent is invoked with the provided input. If the agent's output matches its designated `output_type`, signifying a final result, the loop terminates. In cases where the agent hands off control to another agent, the loop restarts with the new agent. Otherwise, if there are any tool calls to be executed, they are processed, and the loop continues.

--------------------------------

### OpenAI Agents Python > Runner Class > Error Details Creation

Source: https://openai.github.io/openai-agents-python/ref/result

The `_create_error_details` method is a utility within the `Runner` class used to construct a `RunErrorDetails` object. This object encapsulates various pieces of information relevant to an agent run when an error occurs. It includes details such as the input provided to the agent, new items generated, raw responses, the last agent that was active, context wrapper information, and the results from both input and output guardrails.

--------------------------------

### openai-agents-python/openai_agents/llm/litellm.py > _get_completion

Source: https://openai.github.io/openai-agents-python/ko/ref/extensions/litellm

The `_get_completion` method orchestrates the call to `litellm.acompletion`, handling the retrieval and processing of model settings. It extracts parameters like `reasoning_effort`, `stream_options`, and various `extra_kwargs` from `model_settings`. It also handles the distinction between a direct `ModelResponse` and a custom `Response` object, ensuring that the output is formatted appropriately for downstream use. The method is designed to be flexible, accommodating different ways parameters can be specified, including through `extra_body` and `extra_args`.

It also ensures that `reasoning_effort` is not duplicated if it's already a top-level argument. If the `litellm.acompletion` call returns a `ModelResponse` instance, it's returned directly. Otherwise, a custom `Response` object is constructed, potentially including tool choices and other response metadata, along with the raw `ret` object from LiteLLM.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

The `tool_choice` parameter allows you to specify how the model should select tools for execution. This is particularly useful in agent-based systems where the model needs to decide which tools are most appropriate for a given task.

--------------------------------

### RunConfig `dataclass` > trace_include_sensitive_data `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/zh/ref/run

The `trace_include_sensitive_data` boolean attribute determines whether potentially sensitive information, such as inputs and outputs of tool calls or LLM generations, is included in traces. When set to `False`, spans for these events will still be created, but the sensitive data itself will be omitted. This provides a balance between traceability and data privacy.

--------------------------------

### OpenAI Agents Python/realtime/config.py/User Input Types/RealtimeUserInputText/text

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/config

The `text` attribute of `RealtimeUserInputText` is an instance attribute representing the actual text content provided by the user. This is the core textual data that the model will process as input.

--------------------------------

### Results > RunResultBase dataclass

Source: https://openai.github.io/openai-agents-python/ref/result

The `RunResultBase` dataclass contains several key attributes that capture the outcome of an agent's execution:

*   `input`: The initial input provided to the agent, which might be a single item or a list. This could be a mutated version if input filters were applied.
*   `new_items`: A list of `RunItem` objects representing all the newly generated elements during the agent's run. This includes messages, tool invocations, and their corresponding outputs.
*   `raw_responses`: A list containing the raw `ModelResponse` objects directly from the language model during the agent's operation.
*   `final_output`: The ultimate result produced by the agent after completing its task.
*   `input_guardrail_results`, `output_guardrail_results`, `tool_input_guardrail_results`, `tool_output_guardrail_results`: These attributes store the results from various guardrail checks performed on the input, output, and tool interactions.

--------------------------------

### traces.py > tracing_api_key

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/traces

The `tracing_api_key` property holds the API key required for exporting trace and span data. If tracing is disabled or not configured, this value may be `None`.

--------------------------------

### MCP Server Streamable HTTP Transport > __init__ > message_handler

Source: https://openai.github.io/openai-agents-python/ja/ref/mcp/server

An optional `message_handler` can be provided to process session messages delivered by the ClientSession.

--------------------------------

### RealtimeSession

Source: https://openai.github.io/openai-agents-python/ref/realtime/session

The `RealtimeSession` class represents a connection to a realtime model. It facilitates two-way communication by streaming events originating from the model directly to the user, while also enabling the user to send messages and audio data to the model. This allows for interactive and dynamic model engagement.

--------------------------------

### OpenAI Agents Python > __init__

Source: https://openai.github.io/openai-agents-python/ko/ref/models/multi_provider

The `__init__` method creates a new OpenAI provider. It accepts several optional parameters for configuration, including `provider_map`, `openai_api_key`, `openai_base_url`, `openai_client`, `openai_organization`, `openai_project`, and `openai_use_responses`. If `provider_map` is not provided, a default mapping is used. If the OpenAI API key, base URL, organization, or project are not specified, default values will be used. An existing `AsyncOpenAI` client can also be passed in; otherwise, a new one will be created.

--------------------------------

### Tracing Processor Interface > on_span_start

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/processor_interface

The `on_span_start` method is called synchronously at the beginning of a new span's execution. The `span` object passed contains details about the operation and its context. Implementations should ensure this method returns quickly to avoid blocking execution. Importantly, spans are automatically nested under the current trace or parent span.

--------------------------------

### Agent Configuration > Agent Attributes > Tool Use Behavior

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

The `tool_use_behavior` parameter configures how the agent handles tool usage. The default behavior, `'run_llm_again'`, is to run tools and then have the LLM process the results. Setting it to `'stop_on_first_tool'` means the output of the first tool call is directly used as the final output, bypassing further LLM processing. You can also provide a `StopAtTools` object to halt execution if specific tools are called, using the first matching tool's output as the final result. Alternatively, a custom function can be provided to determine the final output based on tool results, though this is specifically for `FunctionTools` as hosted tools are always processed by the LLM.

--------------------------------

### `RealtimeSession`

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/session

The `RealtimeSession` is typically managed within an `async with` block, often initiated by a `RealtimeRunner`. This context management ensures that the session is properly set up and torn down. Inside the context, you have access to the session object for sending data and receiving events.

--------------------------------

### ToolGuardrailFunctionOutput dataclass > output_info instance-attribute

Source: https://openai.github.io/openai-agents-python/ja/ref/tool_guardrails

The `output_info` attribute within `ToolGuardrailFunctionOutput` is an optional field that can contain data related to the checks performed by the guardrail. This allows for detailed reporting on the guardrail's activity, such as specific findings or granular results of the checks.

--------------------------------

### `repl` > `run_demo_loop`

Source: https://openai.github.io/openai-agents-python/ja/ref/repl

The `run_demo_loop` function facilitates a simple REPL loop for an agent. This utility is designed for quick manual testing and debugging of an agent directly from the command line. Importantly, the conversation state is maintained across multiple turns, allowing for a continuous dialogue with the agent. To exit the loop, users can simply type `exit` or `quit`.

--------------------------------

### VoicePipeline

Source: https://openai.github.io/openai-agents-python/ko/ref/voice/pipeline

The `VoicePipeline` class represents an opinionated voice agent pipeline. It's designed to streamline the process of handling voice interactions by breaking them down into three core steps.

First, it transcribes any incoming audio input into text. This text then serves as the input for the second step, which involves running a provided `workflow`. This `workflow` is responsible for processing the text and generating a sequence of text-based responses.

Finally, the pipeline takes these text responses and converts them into a streaming audio output, making the interaction feel natural and real-time. The source code for this pipeline can be found in `src/agents/voice/pipeline.py`.

--------------------------------

### MCP Servers > MCPServer > name

Source: https://openai.github.io/openai-agents-python/ref/mcp/server

The `name` property is an abstract method that must be implemented by any subclass of `MCPServer`. It is intended to provide a human-readable name for the server instance, which can be useful for identification and logging purposes.

--------------------------------

### RunConfig `dataclass` > trace_id `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ref/run

Custom trace and group identifiers can be provided using `trace_id` and `group_id` in `RunConfig`. `trace_id` allows for specifying a unique identifier for a single trace, while `group_id` can link multiple traces that belong to the same conversation or process, facilitating easier analysis of related agent activities.

--------------------------------

### RealtimeAgent > hooks

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/agent

The `hooks` attribute allows for integration with callbacks that are triggered at various stages of the agent's lifecycle. This enables custom logic to be executed during agent operation.

--------------------------------

### openai-agents-python/agents.py > Agent > _copy_sync

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/memory/advanced_sqlite_session

This section of the code handles the copying of messages to create new branches in a conversation. It first determines the starting sequence number for the new branch based on the existing messages in the session. Then, it iterates through the messages selected for copying, creating new entries in the `message_structure` table. These new entries retain the original `message_id` (to share message data) but are assigned a new `branch_id` and a sequential `sequence_number` within the new branch. The `user_turn_number` and `branch_turn_number` are preserved to maintain the conversational context. Finally, the changes are committed to the database.

--------------------------------

### MCPServerStreamableHttp

Source: https://openai.github.io/openai-agents-python/ref/mcp/server

The `__init__` method for `MCPServerStreamableHttp` initializes the server with various parameters to configure its behavior and connection. Key parameters include `params`, which contains server-specific configurations like the URL, headers, and timeouts for the HTTP and Streamable HTTP connections. Additional options allow for caching the tools list to improve latency, setting a custom name for the server, defining timeouts for the client session, applying a tool filter, controlling the use of structured content in tool results, and configuring retry attempts and backoff delays for failed operations. An optional `message_handler` can also be provided to process session messages.

--------------------------------

### Tracing

Source: https://openai.github.io/openai-agents-python/voice/tracing

Key tracing-related fields within `VoicePipelineConfig` allow for granular control over how traces are generated and what information they contain. The `tracing_disabled` field lets you turn tracing on or off, with tracing enabled by default. For privacy and security, `trace_include_sensitive_data` determines whether sensitive information, such as audio transcripts, is included in the traces. This setting is specific to the voice pipeline itself and does not affect data within your Workflow. Additionally, `trace_include_sensitive_audio_data` controls the inclusion of raw audio data in the traces. You can also assign a `workflow_name` to your trace and use a `group_id` to link multiple related traces together. Finally, `trace_metadata` provides a space to add any extra contextual information you wish to associate with the trace.

--------------------------------

### Usage > total_tokens

Source: https://openai.github.io/openai-agents-python/ref/usage

The `total_tokens` attribute summarizes the combined count of both input and output tokens for all requests. This provides a high-level view of the overall token consumption.

--------------------------------

### Tool filtering > Static tool filtering

Source: https://openai.github.io/openai-agents-python/mcp

Use `create_static_tool_filter` to configure simple allow/block lists: When both `allowed_tool_names` and `blocked_tool_names` are supplied the SDK applies the allow-list first and then removes any blocked tools from the remaining set.

--------------------------------

### Processor Interface

Source: https://openai.github.io/openai-agents-python/ref/tracing

The `ProcessorInterface` defines a set of abstract methods that are called at various points during the execution of a trace. These methods allow for custom processing, logging, or exporting of trace and span data. Concrete implementations of this interface can hook into the tracing lifecycle to perform specific actions when a new trace or span starts or ends.

--------------------------------

### model_provider

Source: https://openai.github.io/openai-agents-python/ko/ref/run

The model provider to use when looking up string model names. Defaults to OpenAI.

--------------------------------

### RealtimeRunner > __init__

Source: https://openai.github.io/openai-agents-python/ref/realtime/runner

Initializes the realtime runner. The `starting_agent` parameter is the agent to start the session with. The `model` parameter is the model to use; if not provided, a default OpenAI realtime model will be used. The `config` parameter allows overriding parameters for the entire run.

--------------------------------

### Prompts

Source: https://openai.github.io/openai-agents-python/mcp

MCP servers can also provide prompts that dynamically generate agent instructions. Servers supporting prompts expose two methods: `list_prompts()` to enumerate available prompt templates, and `get_prompt(name, arguments)` to fetch a specific prompt, optionally with parameters.

--------------------------------

### ToolGuardrailFunctionOutput dataclass

Source: https://openai.github.io/openai-agents-python/ja/ref/tool_guardrails

The `ToolGuardrailFunctionOutput` dataclass represents the result of a tool guardrail function. It includes `output_info` for optional data about performed checks and `behavior`, which defines how the system should respond. The `behavior` can be set to `allow` to continue normal tool execution, `reject_content` to reject the tool call/output with a message to the model, or `raise_exception` to halt execution by raising a `ToolGuardrailTripwireTriggered` exception. The default behavior is to allow.

--------------------------------

### openai_github_io_openai-agents-python/mcp/server.py > __init__

Source: https://openai.github.io/openai-agents-python/zh/ref/mcp/server

Create a new MCP server based on the Streamable HTTP transport.

Args:
    params: The params that configure the server. This includes the URL of the server, the headers to send to the server, the timeout for the HTTP request, the timeout for the Streamable HTTP connection, whether we need to terminate on close, and an optional custom HTTP client factory.

    cache_tools_list: Whether to cache the tools list. If `True`, the tools list will be cached and only fetched from the server once. If `False`, the tools list will be fetched from the server on each call to `list_tools()`. The cache can be invalidated by calling `invalidate_tools_cache()`. You should set this to `True` if you know the server will not change its tools list, because it can drastically improve latency (by avoiding a round-trip to the server every time).

    name: A readable name for the server. If not provided, we'll create one from the URL.

    client_session_timeout_seconds: the read timeout passed to the MCP ClientSession.
    tool_filter: The tool filter to use for filtering tools.
    use_structured_content: Whether to use `tool_result.structured_content` when calling an MCP tool. Defaults to False for backwards compatibility - most MCP servers still include the structured content in the `tool_result.content`, and using it by default will cause duplicate content. You can set this to True if you know the server will not duplicate the structured content in the `tool_result.content`.
    max_retry_attempts: Number of times to retry failed list_tools/call_tool calls. Defaults to no retries.

--------------------------------

### Run context > RunContextWrapper dataclass

Source: https://openai.github.io/openai-agents-python/ja/ref/run_context

The `RunContextWrapper` dataclass wraps the context object passed to `Runner.run()`. It also contains information about the usage of the agent run so far. Contexts are not passed to the LLM; they serve as a mechanism for passing dependencies and data to implemented code, such as tool functions, callbacks, and hooks.

--------------------------------

### OpenAI Agents Python > total_tokens

Source: https://openai.github.io/openai-agents-python/ko/ref/usage

Total tokens sent and received, across all requests.

--------------------------------

### tracing_disabled

Source: https://openai.github.io/openai-agents-python/ko/ref/run

Whether tracing is disabled for the agent run. If disabled, we will not trace the agent run.

--------------------------------

### Voice Workflow API > SingleAgentVoiceWorkflow > __init__

Source: https://openai.github.io/openai-agents-python/ko/ref/voice/workflow

Create a new single agent voice workflow.

Args:
    agent: The agent to run.
    callbacks: Optional callbacks to call during the workflow.

--------------------------------

### ToolGuardrailFunctionOutput dataclass > allow classmethod

Source: https://openai.github.io/openai-agents-python/zh/ref/tool_guardrails

The `allow` class method is used to create a `ToolGuardrailFunctionOutput` instance that permits the tool's execution to continue without interruption. It optionally accepts `output_info` to provide details about any checks performed. This is the default behavior if no specific behavior is defined.

--------------------------------

### SingleAgentVoiceWorkflow

Source: https://openai.github.io/openai-agents-python/zh/ref/voice/workflow

The `__init__` method for `SingleAgentVoiceWorkflow` initializes a new instance of the workflow. It requires an `agent` to be passed, which is the core component responsible for processing input and generating responses. An optional `callbacks` object, conforming to the `SingleAgentWorkflowCallbacks` interface, can also be provided to hook into specific events during the workflow's execution. Internally, it sets up an empty list for `_input_history` and stores the provided `agent` and `callbacks`.

--------------------------------

### custom_span

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

The `custom_span` function creates a new custom span, allowing you to add your own metadata. It's important to note that the span does not start automatically. You need to either use a `with custom_span() ...` block or manually call `span.start()` followed by `span.finish()`.

The function accepts several parameters:
- `name`: A required string representing the name of the custom span.
- `data`: An optional dictionary for arbitrary structured data to associate with the span.
- `span_id`: An optional string for the span ID. If not provided, an ID will be generated. Using `util.gen_span_id()` is recommended for correctly formatted IDs.
- `parent`: An optional `Trace` or `Span` object to set as the parent. If omitted, the current trace or span will be used.
- `disabled`: A boolean flag. If `True`, a `Span` object is returned, but it won't be recorded.

--------------------------------

### Tracing Processor Interface > on_trace_start

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/processor_interface

The `on_trace_start` method is invoked synchronously whenever a new trace begins its execution. The `trace` object passed as an argument contains the workflow name and associated metadata. It's important that this method returns quickly to avoid blocking the main execution flow. Any errors encountered within this method should be caught and handled internally to prevent disruptions.

--------------------------------

### Agents > Agent

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

The type of the output object. If not provided, the output will be `str`. In most cases, you should pass a regular Python type (e.g. a dataclass, Pydantic model, TypedDict, etc). You can customize this in two ways: 1. If you want non-strict schemas, pass `AgentOutputSchema(MyClass, strict_json_schema=False)`. 2. If you want to use a custom JSON schema (i.e. without using the SDK's automatic schema creation), subclass `AgentOutputSchemaBase` and pass an instance of your subclass.

--------------------------------

### Session Memory > Community session implementations

Source: https://openai.github.io/openai-agents-python/sessions

The community has contributed several additional session implementations beyond the built-in ones. For instance, `openai-django-sessions` provides Django ORM-based sessions compatible with any Django-supported database. The library also offers various other implementations accessible via its API Reference, including `OpenAIConversationsSession`, `SQLAlchemySession`, `DaprSession`, `AdvancedSQLiteSession`, and `EncryptedSession`, catering to diverse storage and encryption needs.

--------------------------------

### Span > ended_at

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

When the span finished execution. Returns the ISO format timestamp of span end, or `None` if not finished.

--------------------------------

### run_streamed `classmethod`

Source: https://openai.github.io/openai-agents-python/ko/ref/run

The `run_streamed` class method initiates a workflow starting with a specified agent and operates in streaming mode. It returns a result object equipped with a method to stream semantic events as they are produced. The agent operates within a loop, continuing until a definitive output is generated. This loop follows a sequence: first, the agent is invoked with the provided input. If the agent produces a final output (of type `agent.output_type`), the loop concludes. In cases of a handoff to another agent, the loop restarts with the new agent. Otherwise, any tool calls are executed, and the loop iterates again.

--------------------------------

### MCPServerSse

Source: https://openai.github.io/openai-agents-python/ja/ref/mcp/server

When initializing `MCPServerSse`, several parameters can be configured to tailor its behavior. The `params` argument is crucial, containing server URL, headers, and various timeout settings for both HTTP requests and SSE connections. You can also control whether the list of available tools is cached (`cache_tools_list`) to improve latency, provide a human-readable `name` for the server, set a `client_session_timeout_seconds` for read operations, specify a `tool_filter`, determine if `use_structured_content` should be employed (with a note on potential backwards compatibility issues), and configure retry attempts (`max_retry_attempts`) and backoff delays (`retry_backoff_seconds_base`) for failed operations. An optional `message_handler` can also be provided to process incoming session messages.

--------------------------------

### RunConfig `dataclass` > session_input_callback `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ja/ref/run

The `session_input_callback` in `RunConfig` defines how session history is managed when new input is provided. If set to `None` (the default), new input is simply appended to the existing history. Alternatively, a custom `SessionInputCallback` function can be supplied to dictate how the history and new input are combined.

--------------------------------

### RunConfig `dataclass` > group_id `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ja/ref/run

The `group_id` attribute in `RunConfig` serves as a grouping identifier for tracing. It allows multiple traces originating from the same conversation or process to be linked together, for instance, by using a chat thread ID.

--------------------------------

### OpenAI Agents Python > mcp.server > MCPServerStdio.__init__ > use_structured_content

Source: https://openai.github.io/openai-agents-python/ref/mcp/server

The `use_structured_content` parameter in `MCPServerStdio.__init__` controls the usage of `tool_result.structured_content` when invoking an MCP tool. By default, this is set to `False` for backward compatibility, as many existing MCP servers include structured content within the `tool_result.content` field, which would lead to duplicate information if `use_structured_content` were `True`. If you are certain that your MCP server does not duplicate structured content, you can set this parameter to `True` to utilize the dedicated `structured_content` field.

--------------------------------

### Span > __exit__

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/spans

The `__exit__` method is also part of the context manager protocol. It is called when exiting the `with` block and typically finishes the span, handling any exceptions that occurred.

--------------------------------

### openai-agents-python/agents.py > Agent > find_turns_by_content

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/memory/advanced_sqlite_session

The `find_turns_by_content` method enables searching for specific user messages within a conversation branch. Users provide a `search_term`, and optionally a `branch_id` (defaulting to the current branch if not specified). The search is performed by a synchronous helper function, `_search_sync`, which connects to the database. This helper is intended to execute a SQL query that selects messages from the `message_structure` and `agent_messages` tables, filtering by `session_id`, `branch_id`, and `message_type` ('user'). The query would likely involve a `LIKE` clause on the `message_data` to find messages containing the `search_term`. The results would then be formatted similarly to those returned by `get_conversation_turns`.

--------------------------------

### Results

Source: https://openai.github.io/openai-agents-python/results

When you call the `Runner.run` methods, you either get a `RunResult` if you call `run` or `run_sync`, or a `RunResultStreaming` if you call `run_streamed`. Both of these inherit from `RunResultBase`, which is where most useful information is present.

--------------------------------

### RunConfig `dataclass`

Source: https://openai.github.io/openai-agents-python/ko/ref/run

The `RunConfig` dataclass is used to configure settings for an entire agent run. It allows for global overrides and configurations that apply across all agents within a run.

Key settings include:
*   `model`: Specifies the default model to use for the run, overriding any model set on individual agents. The `model_provider` must be able to resolve this model name.
*   `model_provider`: Determines how model names are resolved. Defaults to `MultiProvider`.
*   `model_settings`: Allows for global configuration of model parameters, overriding agent-specific settings.
*   `handoff_input_filter`: A global filter applied to all handoffs between agents. If an agent-specific filter is set, it takes precedence. This filter can modify the inputs sent to the next agent.
*   `nest_handoff_history`: Controls how previous run history is handled during handoffs. When `True` (default), history is wrapped in a single assistant message. Setting to `False` preserves the raw transcript behavior.
*   `handoff_history_mapper`: An optional function to customize how the transcript is processed before being passed to the next agent, specifically when `nest_handoff_history` is `True`.
*   `input_guardrails` and `output_guardrails`: Lists of guardrails to apply to the initial input and final output of the run, respectively.
*   `tracing_disabled` and `tracing`: Options to disable tracing or configure tracing behavior.
*   `trace_include_sensitive_data`: Determines whether sensitive data is included in traces.
*   `workflow_name`: A descriptive name for the run, useful for tracing.
*   `trace_id` and `group_id`: For custom or grouped tracing.
*   `trace_metadata`: Additional metadata for traces.
*   `session_input_callback`: Customizes how session history is managed with new input.
*   `call_model_input_filter`: A callback invoked before calling the model, allowing modification of the model input.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/zh/ref/model_settings

Frequency and presence penalties can be used to discourage the model from repeating itself. `frequency_penalty` reduces the likelihood of repeating tokens based on their frequency in the generated text so far, while `presence_penalty` discourages repeating tokens that have already appeared.

--------------------------------

### Tracing Processor Interface > on_span_start

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/processor_interface

The `on_span_start` method is called synchronously when a new span begins execution. The `span` object, which contains operation details and context, is passed to this method. To avoid blocking the execution, this method should return promptly. It's important to note that spans are automatically nested under the current trace or parent span.

--------------------------------

### TracingProcessor > on_span_start

Source: https://openai.github.io/openai-agents-python/ref/tracing/processor_interface

The `on_span_start` method is triggered synchronously at the commencement of a new span's execution. It receives the `span` object, which details the operation being performed and its relevant context. Implementations should be designed for swift execution to prevent blocking the agent. Spans are automatically managed within the current trace and span hierarchy, simplifying their contextualization.

--------------------------------

### Lifecycle > RunHooksBase

Source: https://openai.github.io/openai-agents-python/zh/ref/lifecycle

`RunHooksBase` is a generic base class designed to receive callbacks on various lifecycle events within an agent run. It allows developers to subclass it and override specific methods to implement custom logic at different stages of the agent's execution. For example, `on_llm_start` is called just before an LLM is invoked, `on_llm_end` is called immediately after the LLM returns, `on_agent_start` is called before an agent is invoked, `on_agent_end` is called when an agent produces its final output, `on_handoff` is triggered during agent transitions, `on_tool_start` is called before a tool is used, and `on_tool_end` is called after a tool completes its execution.

--------------------------------

### custom_span

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

The `custom_span` function allows you to create a new custom span for adding your own metadata. It's important to note that the span is not started automatically. You need to explicitly start and finish it by using a `with custom_span() ...` block or by manually calling `span.start()` and `span.finish()`.

The function accepts several parameters:
* `name`: A required string representing the name of the custom span.
* `data`: An optional dictionary for arbitrary structured data to associate with the span.
* `span_id`: An optional string for the span's ID. If not provided, an ID will be generated. It's recommended to use `util.gen_span_id()` for correctly formatted IDs.
* `parent`: An optional `Trace` or `Span` object to set as the parent. If omitted, the current trace or span will be used as the parent.
* `disabled`: A boolean flag. If `True`, a `Span` object will be returned, but it won't be recorded.

--------------------------------

### Handoff dataclass

Source: https://openai.github.io/openai-agents-python/ref/handoffs

A `Handoff` object represents a mechanism by which one agent can delegate a task to another agent within the system. This is particularly useful in complex scenarios where different agents specialize in distinct areas. For example, a "triage agent" could analyze an incoming user request and determine which specialized sub-agent (e.g., billing, account management) is best suited to handle it. The `Handoff` class provides attributes to define the tool name and description for this delegation, the JSON schema for any input required by the next agent, and the core logic (`on_invoke_handoff`) that executes the handoff. It also specifies the name of the target agent and offers optional functionalities like input filtering and controlling history nesting.

--------------------------------

### DaprSession > get_items

Source: https://openai.github.io/openai-agents-python/ko/ref/extensions/memory/dapr_session

Retrieve the conversation history for this session. This asynchronous method fetches the messages stored for the current session. You can optionally specify a `limit` to retrieve only the most recent `N` items. If `limit` is `None`, all messages are retrieved. The method returns a list of input items representing the conversation history, ordered chronologically. It handles decoding messages from the Dapr state store and deserializing them into the appropriate item format, with error handling for potential decoding or type errors.

--------------------------------

### Spans > finish

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

Finish the span. This method signifies the completion of the span's execution. The `reset_current` parameter can be used to unset the current span after finishing.

--------------------------------

### OutputGuardrail dataclass > name class-attribute instance-attribute

Source: https://openai.github.io/openai-agents-python/zh/ref/guardrail

The `name` attribute provides an optional identifier for the guardrail, which is useful for tracing purposes. If this attribute is not explicitly set, the system will automatically use the name of the `guardrail_function` as the identifier.

--------------------------------

### Tools > Function tools

Source: https://openai.github.io/openai-agents-python/tools

You can use any Python function as a tool. The Agents SDK will setup the tool automatically:
  * The name of the tool will be the name of the Python function (or you can provide a name)
  * Tool description will be taken from the docstring of the function (or you can provide a description)
  * The schema for the function inputs is automatically created from the function's arguments
  * Descriptions for each input are taken from the docstring of the function, unless disabled

We use Python's `inspect` module to extract the function signature, along with `griffe` to parse docstrings and `pydantic` for schema creation.

--------------------------------

### OpenAI Agents SDK

Source: https://openai.github.io/openai-agents-python/index

The Agents SDK has a very small set of primitives: Agents, which are LLMs equipped with instructions and tools; Handoffs, which allow agents to delegate to other agents for specific tasks; Guardrails, which enable validation of agent inputs and outputs; and Sessions, which automatically maintains conversation history across agent runs. In combination with Python, these primitives are powerful enough to express complex relationships between tools and agents, and allow you to build real-world applications without a steep learning curve. In addition, the SDK comes with built-in tracing that lets you visualize and debug your agentic flows, as well as evaluate them and even fine-tune models for your application.

--------------------------------

### Tracing Processor Interface > on_trace_start

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/processor_interface

The `on_trace_start` method is invoked synchronously whenever a new trace begins execution. The `trace` object passed to this method contains the workflow name and associated metadata. Implementations should ensure this method returns quickly to avoid blocking the execution of the trace. Any errors encountered within this method should be caught and handled internally to prevent disruptions.

--------------------------------

### Memory > Session > clear_session

Source: https://openai.github.io/openai-agents-python/ko/ref/memory

Clear all items for this session, effectively resetting the conversation history.

--------------------------------

### Spans > error

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

Any error that occurred during span execution. If an error occurred, this field will contain a `SpanError` object with details; otherwise, it will be `None`.

--------------------------------

### Tracing Processor Interface > on_span_start

Source: https://openai.github.io/openai-agents-python/ref/tracing/processor_interface

The `on_span_start` method is called synchronously when a new span begins execution. The `span` object passed contains details about the operation and its context. This method should return quickly to avoid blocking execution. Spans are automatically nested under the current trace or parent span.

--------------------------------

### TracingProcessor > on_trace_start

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

The `on_trace_start` method is called when a new trace begins execution. It receives the `trace` object, which contains details like the workflow name and associated metadata. This method is expected to be called synchronously and should return quickly to avoid blocking the agent's execution. Any errors encountered within this method should be caught and handled internally to maintain stability.

--------------------------------

### Session > get_items

Source: https://openai.github.io/openai-agents-python/zh/ref/memory/session

The `get_items` method allows retrieval of the conversation history for a given session. You can optionally specify a `limit` to retrieve only the most recent N items. If no limit is provided, all items in the session's history will be returned. This method is crucial for agents to access past turns in the conversation to inform their responses.

--------------------------------

### Agent Configuration > Tool Use Behavior

Source: https://openai.github.io/openai-agents-python/ko/ref/agent

This configuration option lets you control how tool use is handled. The default behavior, `"run_llm_again"`, involves running tools and then sending their results back to the LLM for a response. Alternatively, `"stop_on_first_tool"` treats the output of the first tool call as the final result, bypassing further LLM processing. You can also use a `StopAtTools` object to halt execution if a specific tool is called, using that tool's output as the final result. For more advanced control, a function can be provided; this function receives the run context and tool results, and must return a `ToolsToFinalOutputResult` to determine if the tool calls should lead to a final output. Note that this `tool_use_behavior` setting is specific to `FunctionTools`; hosted tools like file or web search are always processed by the LLM.

--------------------------------

### Tracing Exporter

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/processor_interface

The `TracingExporter` is an abstract base class designed for exporting traces and spans. Its primary purpose is to provide a mechanism for sending telemetry data, such as traces and spans, to various destinations like logs or external backends. Concrete implementations of this class will define how the data is actually exported.

--------------------------------

### TracingProcessor > on_trace_start

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `on_trace_start` method is invoked when a new trace begins execution. It receives the `trace` object, which contains the workflow name and associated metadata. This method is called synchronously and should return quickly to avoid blocking the trace's execution. Any errors encountered during this call should be handled internally by the processor.

--------------------------------

### Agent Attributes > tool_use_behavior

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

This attribute configures how tool use is handled within the agent. The default behavior, "run_llm_again", involves running tools and then allowing the LLM to process their results. Alternatively, "stop_on_first_tool" treats the output of the very first tool call as the final result, bypassing further LLM processing. You can also define a custom stopping condition by passing a `StopAtTools` object, which halts execution if any specified tool is invoked, using that tool's output as the final result. Furthermore, a custom function can be provided to process tool results and determine if they should lead to a final output, returning a `ToolsToFinalOutputResult`. It's important to note that this configuration applies specifically to `FunctionTools`; hosted tools like file or web search are always processed by the LLM.

--------------------------------

### DaprSession > ping

Source: https://openai.github.io/openai-agents-python/zh/ref/extensions/memory/dapr_session

Tests the connectivity to Dapr by attempting to check metadata. This asynchronous method first tries to read a specific key (`__ping__`). If that fails (potentially because the store is not yet initialized), it attempts to save a value to the same key and then read it again. It returns `True` if Dapr is reachable and operational, and `False` otherwise, logging any connection errors encountered during the process.

--------------------------------

### Using any model via LiteLLM > Tracking usage data

Source: https://openai.github.io/openai-agents-python/models/litellm

To have LiteLLM responses contribute to the Agents SDK's usage metrics, you should instantiate your agent with `ModelSettings(include_usage=True)`. When this setting is enabled, LiteLLM requests will report token and request counts via `result.context_wrapper.usage`, mirroring the behavior of the SDK's built-in OpenAI models.

--------------------------------

### MCP Server Streamable HTTP Transport > __init__ > tool_filter

Source: https://openai.github.io/openai-agents-python/ja/ref/mcp/server

The `tool_filter` parameter allows for the specification of a filter to be applied to tools.

--------------------------------

### Agent Attributes > input_guardrails

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

A list of checks that run in parallel to the agent's execution, before generating a response. Runs only if the agent is the first agent in the chain.

--------------------------------

### Agent Configuration > Output Type

Source: https://openai.github.io/openai-agents-python/ko/ref/agent

The type of the output object. If not provided, the output will be `str`. In most cases, you should pass a regular Python type such as a dataclass, Pydantic model, or TypedDict. You can customize this by passing `AgentOutputSchema(MyClass, strict_json_schema=False)` for non-strict schemas, or by subclassing `AgentOutputSchemaBase` and passing an instance for custom JSON schema creation without SDK automatic schema generation.

--------------------------------

### Source code in src/agents/tracing/traces.py

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/traces

The `name` property of the `NoOpTrace` class returns the string "no-op". This represents the workflow name for a trace when tracing is disabled. It provides a descriptive placeholder that aligns with the expected interface without indicating a specific workflow.

--------------------------------

### OpenAI Agents Python/realtime/config.py/Client Messages/other_data

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/config

The `other_data` attribute for `RealtimeClientMessage` is an optional instance attribute that allows for merging additional data into the message body. This provides flexibility for sending extra information alongside the primary message content.

--------------------------------

### Run context > RunContextWrapper dataclass > context instance-attribute

Source: https://openai.github.io/openai-agents-python/ja/ref/run_context

The `context` instance attribute within `RunContextWrapper` holds the context object (or None) that was provided to `Runner.run()`.

--------------------------------

### RealtimeModelConfig > initial_model_settings

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/model

The `initial_model_settings` option allows you to configure the initial settings for the realtime model when establishing a connection.

--------------------------------

### Run context > RunContextWrapper dataclass

Source: https://openai.github.io/openai-agents-python/ko/ref/run_context

The `RunContextWrapper` dataclass wraps the context object provided to `Runner.run()`. It also keeps track of the agent run's usage information. It's important to note that contexts are not directly sent to the LLM. Instead, they serve as a mechanism for passing dependencies and data to custom code, such as tool functions, callbacks, and hooks.

--------------------------------

### ModelSettings > verbosity

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

Constrains the verbosity of the model's response.

--------------------------------

### MultiProvider

Source: https://openai.github.io/openai-agents-python/ref/models/multi_provider

The `MultiProvider` class is a `ModelProvider` that dynamically maps to a specific `Model` based on a prefix within the model name. It simplifies the management of different model providers by allowing a unified interface. By default, if a model name starts with the prefix "openai/" or has no prefix at all, it routes to the `OpenAIProvider`. For model names prefixed with "litellm/", it utilizes the `LitellmProvider`. This behavior is customizable, allowing users to define their own mappings for different prefixes.

--------------------------------

### openai-agents-python/runner.py > Runner > _create_error_details

Source: https://openai.github.io/openai-agents-python/ja/ref/result

The `_create_error_details()` method is a helper function that constructs a `RunErrorDetails` object. This object encapsulates various aspects of a failed or interrupted agent run, including the initial input, generated items, raw responses, the last agent involved, context wrapper, and guardrail results. This detailed information is crucial for diagnosing issues and understanding the state of the run when an error occurs.

--------------------------------

### Run context > AgentHookContext dataclass

Source: https://openai.github.io/openai-agents-python/ko/ref/run_context

The `AgentHookContext` dataclass inherits from `RunContextWrapper` and is specifically designed to be passed to agent hooks, such as `on_start` and `on_end`.

--------------------------------

### Processor Interface > on_span_start

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/processor_interface

The `on_span_start` method is called synchronously at the beginning of a new span's execution. The `span` object provides details about the operation and its context. Implementations should ensure this method returns quickly to prevent blocking. Spans are automatically managed within the current trace or parent span.

--------------------------------

### OpenAI Agents Python SDK > Usage Attributes > output_tokens

Source: https://openai.github.io/openai-agents-python/ja/ref/usage

The `output_tokens` attribute accumulates the total number of output tokens received from the LLM API across all requests. This integer attribute, initialized to 0, quantifies the volume of generated content returned by the API.

--------------------------------

### Tracing Processor Interface > on_trace_start

Source: https://openai.github.io/openai-agents-python/ref/tracing/processor_interface

The `on_trace_start` method is invoked synchronously whenever a new trace begins execution. The `trace` object passed to this method contains the workflow name and associated metadata. To ensure smooth operation and avoid blocking the execution flow, this method should return quickly. Any errors encountered within this method should be caught and handled internally to prevent disruptions.

--------------------------------

### openai-agents-python/runner.py > Runner > _create_error_details

Source: https://openai.github.io/openai-agents-python/zh/ref/result

The `_create_error_details()` method is a utility function that constructs and returns a `RunErrorDetails` object. This object encapsulates various attributes of the current run, including the input, new items generated, raw responses received, the last agent that acted, the context wrapper, and the results from both input and output guardrails. This is crucial for providing comprehensive context when exceptions related to the run occur, aiding in debugging and error analysis.

--------------------------------

### Agents > Context

Source: https://openai.github.io/openai-agents-python/agents

Agents are generic on their `context` type. Context is a dependency-injection tool: it's an object you create and pass to `Runner.run()`, that is passed to every agent, tool, handoff etc, and it serves as a grab bag of dependencies and state for the agent run. You can provide any Python object as the context.

--------------------------------

### TracingProcessor > on_trace_start

Source: https://openai.github.io/openai-agents-python/ref/tracing/processor_interface

The `on_trace_start` method is invoked synchronously whenever a new trace begins execution. It receives the `trace` object, which contains information about the workflow name and associated metadata. Implementations of this method should execute quickly to avoid blocking the agent's execution flow. Any errors that occur within this method should be caught and handled internally to ensure the trace initiation process completes smoothly.

--------------------------------

### Processor Interface > on_span_start

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `on_span_start` method is called synchronously when a new span begins execution. It accepts a `Span` object, which holds operation details and context. Implementations should ensure this method returns quickly to avoid blocking execution. Spans are automatically nested under the current trace or parent span.

--------------------------------

### RealtimeModelConfig > url

Source: https://openai.github.io/openai-agents-python/ref/realtime/model

The `url` specifies the connection endpoint. If omitted, a default URL, like the OpenAI WebSocket URL, is used.

--------------------------------

### RunResult dataclass > new_items instance-attribute

Source: https://openai.github.io/openai-agents-python/ko/ref/result

The `new_items` attribute is a list containing all the new items generated during the agent's run. This typically includes messages exchanged, tool calls made by the agent, and the corresponding outputs from those tools. These items represent the dynamic evolution of the agent's process and are essential for understanding the step-by-step execution flow and any side effects.

--------------------------------

### openai-agents-python/function_tool.py > function_tool

Source: https://openai.github.io/openai-agents-python/ja/ref/tool

The `function_tool` decorator is used to transform a Python function into a `FunctionTool`. This process involves several automatic steps:

1.  **Parameter Schema Generation**: It parses the function's signature to automatically create a JSON schema for the tool's parameters. This schema defines the expected input structure for the tool.
2.  **Description Population**: The function's docstring is utilized to automatically populate the `description` field of the tool. This provides a natural language explanation of what the tool does.
3.  **Argument Description Population**: Similarly, argument descriptions are derived from the function's docstring, making it clear what each parameter represents.

The decorator attempts to auto-detect the docstring style, but this can be manually overridden if needed. If the function includes a `RunContextWrapper` as its first argument, it must be compatible with the context type of the agent that will utilize this tool.

--------------------------------

### Results > RunResultBase dataclass

Source: https://openai.github.io/openai-agents-python/zh/ref/result

The `to_input_list` method in `RunResultBase` constructs and returns a new list of input items. It combines the original input items (potentially mutated) with all the new items that were generated during the agent's run. This provides a consolidated view of all inputs considered throughout the agent's execution, including those produced dynamically.

--------------------------------

### spans.py > Span > trace_id

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

The ID of the trace this span belongs to.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ko/ref/model_settings

The `ModelSettings` class also offers fine-grained control over log probabilities and external integrations. `top_logprobs` can be set to a specific integer to return the log probabilities for the top tokens, which automatically includes `message.output_text.logprobs` in the response. Furthermore, `extra_query`, `extra_body`, `extra_headers`, and `extra_args` allow for the inclusion of custom data and arguments that will be passed directly to the underlying model provider's API, offering flexibility for advanced use cases.

--------------------------------

### Run context > AgentHookContext dataclass

Source: https://openai.github.io/openai-agents-python/ja/ref/run_context

The `AgentHookContext` dataclass is passed to agent hooks, specifically for `on_start` and `on_end` events. It inherits from `RunContextWrapper` and adds specific information relevant to agent hook execution.

--------------------------------

### VoicePipeline > _process_audio_input

Source: https://openai.github.io/openai-agents-python/ko/ref/voice/pipeline

The `_process_audio_input` method handles the transcription of audio data into text. It utilizes the pipeline's speech-to-text (STT) model to perform this conversion. The transcription process can be further configured using settings defined in `self.config.stt_settings`. The method also incorporates options for including sensitive data and audio data in traces, controlled by `self.config.trace_include_sensitive_data` and `self.config.trace_include_sensitive_audio_data` respectively.

--------------------------------

### speech_group_span

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

The `speech_group_span` function is used to create a new span specifically for grouping speech-related operations within a trace. It's important to note that this span is not automatically started upon creation. You must explicitly manage its lifecycle by using a `with` statement (e.g., `with speech_group_span() as span:`), or by manually calling `span.start()` and `span.finish()` methods. This function accepts several parameters to configure the span, including `input` for the speech request text, an optional `span_id`, a `parent` span or trace, and a `disabled` flag to prevent recording.

--------------------------------

### Span > span_id

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/spans

The `span_id` property provides a unique identifier for this specific span within its trace.

--------------------------------

### TracingProcessor > on_span_start

Source: https://openai.github.io/openai-agents-python/ref/tracing

The `on_span_start` method is called synchronously when a new span begins execution. It receives the `span` object, which contains details about the operation and its context. Implementations should aim for quick execution to prevent blocking. The system automatically handles the nesting of spans under the current trace or parent span.

--------------------------------

### OutputGuardrail `dataclass` > name `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ref/guardrail

The `name` attribute provides an identifier for the guardrail, which is useful for logging and tracing purposes. If no name is explicitly provided when creating the `OutputGuardrail`, the system will automatically use the name of the underlying guardrail function.

--------------------------------

### Quickstart > Creating your first realtime agent > Start a session

Source: https://openai.github.io/openai-agents-python/realtime/quickstart

To initiate a realtime agent session, use the `run()` method of the `RealtimeRunner` object, which returns a session object. This session is managed using an `async with` statement. Within the session, you can process various events asynchronously, such as `agent_start`, `agent_end`, `handoff`, tool events, and audio-related events. This event-driven model allows for real-time interaction and feedback during the agent's operation, including handling audio streaming and potential interruptions.

--------------------------------

### Results > RunResultBase dataclass > input instance-attribute

Source: https://openai.github.io/openai-agents-python/zh/ref/result

The `input` attribute of `RunResultBase` holds the original input provided to the agent run. This could be a single string or a list of `TResponseInputItem` objects. It's important to note that this attribute might contain a mutated version of the input if any input filters were applied that modified the original data before the agent processed it.

--------------------------------

### RunConfig `dataclass` > trace_include_sensitive_data `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ref/run

The `trace_include_sensitive_data` flag determines whether potentially sensitive information, such as inputs and outputs of tool calls or LLM generations, is included in traces. When set to `False`, spans for these events are still created, but the sensitive data itself is omitted, enhancing privacy and security while maintaining visibility into the agent's execution flow.

--------------------------------

### speech_group_span

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/create

Create a new speech group span. The span will not be started automatically, you should either do `with speech_group_span() ...` or call `span.start()` + `span.finish()` manually.

Parameters:
`input`: The input text used for the speech request.
`span_id`: The ID of the span. Optional. If not provided, we will generate an ID. We recommend using `util.gen_span_id()` to generate a span ID, to guarantee that IDs are correctly formatted.
`parent`: The parent span or trace. If not provided, we will automatically use the current trace/span as the parent.
`disabled`: If True, we will return a Span but the Span will not be recorded.

--------------------------------

### generation_span

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/create

The `generation_span` function creates a new span to capture the details of a model generation. This span records the input message sequence, any generated outputs, the model name and configuration, and usage data. It's important to note that the span is not started automatically; you must explicitly start and finish it using either a `with` statement (e.g., `with generation_span() ...`) or by manually calling `span.start()` and `span.finish()`.

This function is useful for detailed tracing of model interactions. If your goal is solely to capture a model response identifier, the `response_span()` function is a more appropriate choice.

--------------------------------

### RealtimeSession

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/session

The `RealtimeSession` class establishes a connection to a realtime model. This session enables bidirectional communication: it streams events originating from the model directly to you, and conversely, it allows you to send messages and audio data to the model. This facilitates interactive and dynamic exchanges with the model in real-time.

--------------------------------

### Run config

Source: https://openai.github.io/openai-agents-python/running_agents

When an agent hands off to another agent, the SDK by default nests prior turns into a single assistant summary message. This reduces redundancy and keeps the full transcript concise for new agents to scan. To revert to the legacy behavior or customize this process, you can pass `RunConfig(nest_handoff_history=False)` or implement a `handoff_input_filter` or `handoff_history_mapper` that forwards the conversation as needed. Individual handoffs can also override this setting using `handoff(..., nest_handoff_history=False)` or `True`. To modify the wrapper text of the generated summary without a custom mapper, use `set_conversation_history_wrappers` and `reset_conversation_history_wrappers` to restore defaults.

--------------------------------

### Agent Attributes > tool_use_behavior

Source: https://openai.github.io/openai-agents-python/ref/agent

This attribute configures how tool use is handled. The default behavior, 'run_llm_again', means that tools are executed, and their results are then passed back to the LLM for a response. If 'stop_on_first_tool' is selected, the output of the very first tool call is considered the final result, bypassing further LLM processing. You can also provide a StopAtTools object to halt execution if a specified tool is called, using that tool's output as the final result without LLM involvement. Alternatively, a custom function can be supplied, which receives the run context and tool results, and must return a ToolsToFinalOutputResult to dictate if a final output is generated. This configuration specifically applies to FunctionTools; hosted tools like file or web search are always processed by the LLM.

--------------------------------

### RunConfig `dataclass` > workflow_name `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/zh/ref/run

The `workflow_name` attribute provides a descriptive string for the agent run, defaulting to "Agent workflow". This name is primarily used for tracing purposes and should be a logical identifier for the run, such as "Code generation workflow" or "Customer support agent". A clear workflow name aids in organizing and identifying traces.

--------------------------------

### function_span

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

The `function_span` function is used to create a new span that represents a function call within the tracing system. It's important to note that this span is not started automatically upon creation. You must explicitly manage its lifecycle by either using a `with` statement (e.g., `with function_span(...)`) or by manually calling the `start()` and `finish()` methods on the created span object. This gives you fine-grained control over when the function execution is recorded.

--------------------------------

### SQLiteSession

Source: https://openai.github.io/openai-agents-python/zh/ref/memory/sqlite_session

When initializing `SQLiteSession`, you can configure the database path, session table name, and messages table name. For in-memory databases, a shared connection is used to prevent thread isolation issues. For file-based databases, thread-local connections are employed to enhance concurrency. The database schema, including tables for session metadata and message data, is initialized upon connection.

--------------------------------

### RealtimePlaybackState

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/model

The `RealtimePlaybackState` is a `TypedDict` that represents the current state of real-time audio playback. It includes the `current_item_id` of the audio being played, the `current_item_content_index` within that item's content, and the `elapsed_ms` which is the number of milliseconds of audio that have been played.

--------------------------------

### Multiple sessions

Source: https://openai.github.io/openai-agents-python/sessions

The system allows for the management of multiple sessions simultaneously, with each session maintaining its own independent conversation history. This is demonstrated by creating distinct `SQLiteSession` objects for different users or contexts. When `Runner.run` is called, the specified session is used, ensuring that the conversation context is isolated between different calls, even when using the same agent.

--------------------------------

### Agents > Agent

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

Whether to reset the tool choice to the default value after a tool has been called. Defaults to `True`. This setting prevents the agent from entering an infinite loop of tool usage.

--------------------------------

### RunConfig `dataclass` > model `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ref/run

The `model` attribute within `RunConfig` specifies the language model to be used for the entire agent execution. If this attribute is set, it will take precedence over any model settings defined for individual agents within the run. The `model_provider` associated with this configuration must be capable of resolving the specified model name.

--------------------------------

### Tools

Source: https://openai.github.io/openai-agents-python/tools

Tools let agents take actions: things like fetching data, running code, calling external APIs, and even using a computer. There are three classes of tools in the Agent SDK:
  * Hosted tools: these run on LLM servers alongside the AI models. OpenAI offers retrieval, web search and computer use as hosted tools.
  * Function calling: these allow you to use any Python function as a tool.
  * Agents as tools: this allows you to use an agent as a tool, allowing Agents to call other agents without handing off to them.

--------------------------------

### MCPListToolsItem `dataclass` > raw_item `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ko/ref/items

The `raw_item` attribute in `MCPListToolsItem` stores the raw data corresponding to the MCP list tools call. The type is specified as `McpListTools`.

--------------------------------

### Tracing > finish

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `finish` method is called to complete a trace. It finalizes all open spans associated with the trace. Optionally, it can reset the current trace to the previous one in the execution context by setting `reset_current` to `True`. This method must be called to ensure the trace is properly closed and all its data is finalized. It is thread-safe when `reset_current` is utilized.

--------------------------------

### VoicePipeline

Source: https://openai.github.io/openai-agents-python/ref/voice/pipeline

The `_run_single_turn` method orchestrates the processing for a single audio input. It utilizes a `TraceCtxManager` to manage the lifecycle of a trace, capturing details about the workflow name, group ID, metadata, and tracing status. Within this context, it first transcribes the audio input to text using `_process_audio_input`. It then initializes a `StreamedAudioResult` object, which will handle the streaming of audio events. The transcribed text is passed to the `workflow.run` method, and each text event generated by the workflow is added to the `StreamedAudioResult`. Once the workflow completes, signals are sent to indicate the end of the turn and the completion of the audio output.

--------------------------------

### SQLiteSession

Source: https://openai.github.io/openai-agents-python/zh/ref/memory/sqlite_session

The `SQLiteSession` class allows for the storage of conversation history in a SQLite database. It provides flexibility by defaulting to an in-memory database for temporary storage, which is useful for testing or short-lived sessions. For scenarios requiring data persistence, a file path can be specified, ensuring that conversation history is saved and can be retrieved across different process executions.

--------------------------------

### Model > RealtimePlaybackState

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/model

The `RealtimePlaybackState` is a `TypedDict` that represents the current state of real-time audio playback. It includes the `current_item_id` of the item being played, the `current_item_content_index` within that item's content, and the `elapsed_ms` which is the duration of audio played so far in milliseconds. These attributes are crucial for tracking playback progress in real-time applications.

--------------------------------

### Agent Attributes > mcp_servers

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

A list of Model Context Protocol (MCP) servers that the agent can leverage. Each time the agent executes, it incorporates tools from these servers into its available toolset. It is crucial to manage the lifecycle of these servers, ensuring `server.connect()` is called before they are passed to the agent and `server.cleanup()` is invoked when they are no longer required.

--------------------------------

### Agent Attributes > clone

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

Creates a duplicate of the agent, allowing for modifications to specific arguments. This method employs `dataclasses.replace`, resulting in a shallow copy. Consequently, mutable attributes like `tools` and `handoffs` are shallow-copied as well; new list objects are generated only if these attributes are explicitly overridden. Otherwise, the contents of the original mutable attributes are shared with the new agent. To ensure independent modification of these mutable attributes, new lists should be provided when calling `clone()`. For example, `new_agent = agent.clone(instructions="New instructions")` demonstrates how to change the instructions.

--------------------------------

### Agent Attributes > output_type

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

The type of the output object. If not provided, the output will be `str`. In most cases, you should pass a regular Python type (e.g. a dataclass, Pydantic model, TypedDict, etc). You can customize this in two ways: 1. If you want non-strict schemas, pass `AgentOutputSchema(MyClass, strict_json_schema=False)`. 2. If you want to use a custom JSON schema (i.e. without using the SDK's automatic schema) creation, subclass and pass an `AgentOutputSchemaBase` subclass.

--------------------------------

### litellm_model.py > convert_tool_call_to_openai

Source: https://openai.github.io/openai-agents-python/ref/extensions/litellm

The `convert_tool_call_to_openai` function is responsible for transforming a tool call object from LiteLLM's internal format into the structure expected by OpenAI's Chat Completion API. It first extracts the `tool_call_id` and then constructs a base `ChatCompletionMessageFunctionToolCall` object, ensuring that the `id`, `type`, and function details (name and arguments) are correctly mapped. A key aspect of this function is its ability to preserve provider-specific fields, such as Gemini's `thought_signature`. If these fields are present and relevant (like the Gemini thought signature), they are nested within an `extra_content` dictionary to maintain compatibility with the OpenAI format. The function then returns an `InternalToolCall` object, which includes the base tool call information along with any preserved `extra_content`.

--------------------------------

### SQLAlchemySession

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/memory/sqlalchemy_session

The `SQLAlchemySession` class provides an implementation of the `SessionABC` for persisting conversation history using SQLAlchemy. It supports asynchronous operations and allows for custom table names for sessions and messages. The constructor accepts a SQLAlchemy `AsyncEngine` and an option to automatically create the necessary database tables if they don't exist. This is particularly useful for development and testing environments where manual migration management might be cumbersome. It also includes convenience methods like `from_url` to easily create a session instance using a database connection string.

--------------------------------

### Processor Interface > on_trace_start

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

The `on_trace_start` method is invoked synchronously when a new trace begins execution. It receives the `Trace` object, which includes the workflow name and associated metadata. Implementations of this method should return quickly to prevent blocking the execution flow. Any errors encountered during the execution of this method should be handled internally by catching and managing exceptions.

--------------------------------

### Agent Attributes > tool_use_behavior

Source: https://openai.github.io/openai-agents-python/ko/ref/agent

This attribute configures how tool use is managed within the agent. The default behavior, 'run_llm_again', involves executing tools and then allowing the LLM to process their results and formulate a response. Alternatively, 'stop_on_first_tool' treats the output of the very first tool called as the definitive final result, bypassing further LLM processing. For more nuanced control, a `StopAtTools` object can be provided, causing the agent to halt execution if any tool specified in `stop_at_tool_names` is invoked, with the first matching tool's output becoming the final result. A custom function can also be supplied; this function receives the run context and tool results, and must return a `ToolsToFinalOutputResult` to determine if the tool calls should lead to a final output. It's important to note that this configuration specifically applies to `FunctionTools`; hosted tools like file or web search are always processed by the LLM.

--------------------------------

### MultiProvider

Source: https://openai.github.io/openai-agents-python/ko/ref/models/multi_provider

The `MultiProvider` class maps models to specific `ModelProvider` instances based on a prefix in the model name. This allows for flexible routing of model requests. For instance, models prefixed with `openai/` or models without any prefix are directed to the `OpenAIProvider`. If a model name is prefixed with `litellm/`, it is routed to the `LitellmProvider`. This behavior can be customized to accommodate different provider configurations or custom mappings.

--------------------------------

### Run context > RunContextWrapper dataclass

Source: https://openai.github.io/openai-agents-python/ref/run_context

The `RunContextWrapper` dataclass wraps the context object provided to `Runner.run()`. It also keeps track of the agent run's usage information. It's important to note that contexts are not sent to the LLM. Instead, they serve as a mechanism for passing dependencies and data to custom code, such as tool functions, callbacks, and hooks.

--------------------------------

### SQLiteSession

Source: https://openai.github.io/openai-agents-python/ref/memory

The `SQLiteSession` class provides an interface for managing conversation history within a SQLite database. It allows for both in-memory sessions, which are temporary, and persistent sessions stored in a file. The class is initialized with a unique `session_id`, an optional `db_path` (defaulting to an in-memory database), and names for the sessions and messages tables.

--------------------------------

### Encrypted Sessions > Usage with different session types

Source: https://openai.github.io/openai-agents-python/sessions/encrypted_session

When using `EncryptedSession` with advanced session implementations like `AdvancedSQLiteSession`, it's important to note that certain methods relying on message content, such as `find_turns_by_content()`, may not function effectively. This is because the message content itself is encrypted, and therefore, content-based searches operate on this encrypted data, limiting their usefulness.

--------------------------------

### SQLAlchemySession

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/memory/sqlalchemy_session

The `SQLAlchemySession` is initialized with a unique `session_id` to identify a specific conversation. It requires a SQLAlchemy `AsyncEngine` which must be configured with an asynchronous driver for database interaction. Optional parameters allow for the automatic creation of `sessions` and `messages` tables if `create_tables` is set to `True`. This is convenient for initial setup or testing. Users can also specify custom names for these tables using `sessions_table` and `messages_table` arguments, offering flexibility in database schema design.

--------------------------------

### Agent Attributes > model

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

The model implementation to use when invoking the LLM. By default, if not set, the agent will use the default model configured in `agents.models.get_default_model()` (currently "gpt-4.1").

--------------------------------

### RunConfig `dataclass` > group_id `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/zh/ref/run

The `group_id` attribute is used to provide a grouping identifier for tracing. This allows multiple traces that are part of the same conversation or process to be linked together. For example, a chat thread ID could be used as a `group_id` to associate all traces from a single conversation.

--------------------------------

### Agent Class > `register_tool` Method

Source: https://openai.github.io/openai-agents-python/ref/agent

The `Agent.register_tool` method provides a convenient way to associate functions or methods with an `Agent` instance, making them available as tools for the agent to use. This decorator-based approach simplifies the process of exposing custom logic as callable tools. The `function_tool` decorator from the `openai.agents.tools` module is used to wrap the target function, automatically generating the necessary metadata such as name and description. This allows the agent to understand and invoke these registered functions during its conversational flow.

--------------------------------

### RealtimeAgent > name

Source: https://openai.github.io/openai-agents-python/ref/realtime/agent

The `name` attribute stores the unique identifier for the agent.

--------------------------------

### Model Settings > extra_body

Source: https://openai.github.io/openai-agents-python/ko/ref/model_settings

`extra_body`: Additional body fields to provide with the request. Defaults to None if not provided.

--------------------------------

### openai-agents-python/src/langchain_openai/chat_models/orm.py

Source: https://openai.github.io/openai-agents-python/zh/ref/extensions/memory/advanced_sqlite_session

The `SQLiteSession` class manages chat history and associated metadata within a SQLite database. It provides methods for retrieving messages, storing usage data, and tracking turn and branch numbers for conversations. The class supports both in-memory and file-based SQLite databases and uses a lock for thread safety when accessing the database.

Key functionalities include:
- Retrieving a specified number of messages for a given session and branch.
- Storing usage data associated with a `RunResult`.
- Determining the next available turn number for a specific branch.
- Determining the next available branch turn number for a specific branch.
- Retrieving the current turn number for the active branch.
- Adding structural metadata to messages, including branch-aware turn numbers and sequence numbers.

--------------------------------

### DaprSession > clear_session

Source: https://openai.github.io/openai-agents-python/zh/ref/extensions/memory/dapr_session

Clears all items for the current session. This operation is asynchronous and locks the session to prevent concurrent modifications during the clearing process. It specifically targets and deletes the keys for messages and metadata stored within the Dapr state store.

--------------------------------

### speech_span

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `speech_span` function is used to create a new speech span for tracing text-to-speech operations. This span is not automatically started, meaning you need to either use a `with speech_span() ...` block or manually call `span.start()` followed by `span.finish()`. The function accepts several parameters to configure the span, including the `model` name, the text `input`, the audio `output` (as base64 encoded PCM bytes), the `output_format`, `model_config` for hyperparameters, `first_content_at` for the timestamp of the first audio byte, an optional `span_id`, a `parent` span or trace, and a `disabled` flag to prevent recording.

--------------------------------

### RunConfig `dataclass` > trace_include_sensitive_data `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ja/ref/run

The `trace_include_sensitive_data` flag in `RunConfig` determines whether potentially sensitive information, such as inputs and outputs of tool calls or LLM generations, is included in traces. When set to `False`, spans for these events are still created, but the sensitive data itself is omitted.

--------------------------------

### Release process/changelog > Breaking change changelog > 0.1.0

Source: https://openai.github.io/openai-agents-python/release

Version 0.1.0 introduced two new parameters, `run_context` and `agent`, to `MCPServer.list_tools()`. Any classes that subclass `MCPServer` will need to include these new parameters in their implementations.

--------------------------------

### Using any model via LiteLLM

Source: https://openai.github.io/openai-agents-python/models/litellm

LiteLLM is a library designed to provide a unified interface for interacting with over 100 different AI models. The Agents SDK includes an integration with LiteLLM, enabling you to leverage any AI model supported by LiteLLM within the SDK's framework. This integration is currently in beta, and while it aims for broad compatibility, some model providers, particularly smaller ones, might present issues. Any problems encountered should be reported on GitHub for prompt resolution.

--------------------------------

### generation_span

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/create

The `generation_span` function is used to create a new span that captures the details of a model generation process. It allows you to record the input messages sent to the model, the outputs received, the model identifier, its configuration, and usage statistics. You are responsible for manually starting and finishing the span using either a `with` statement or explicit `start()` and `finish()` calls. For scenarios where only a model response identifier needs to be captured, the `response_span()` function is recommended.

--------------------------------

### Lifecycle > RunHooksBase

Source: https://openai.github.io/openai-agents-python/ko/ref/lifecycle

The `RunHooksBase` class is designed to receive callbacks on various lifecycle events occurring within an agent run. Developers can subclass this class and override the methods corresponding to the events they wish to handle.

Key methods include:
- `on_llm_start`: Called just before invoking the LLM for this agent.
- `on_llm_end`: Called immediately after the LLM call returns for this agent.
- `on_agent_start`: Called before the agent is invoked. This is triggered each time the current agent changes.
- `on_agent_end`: Called when the agent produces a final output.
- `on_handoff`: Called when a handoff between agents occurs.
- `on_tool_start`: Called immediately before a local tool is invoked.
- `on_tool_end`: Called immediately after a local tool is invoked.

--------------------------------

### Configuring the SDK > Tracing

Source: https://openai.github.io/openai-agents-python/config

Tracing is enabled by default and utilizes the OpenAI API keys configured for general LLM requests. You can specify a distinct API key for tracing exports using the `set_tracing_export_api_key()` function. This allows for separation of concerns between LLM requests and tracing data transmission.

```python
from agents import set_tracing_export_api_key

set_tracing_export_api_key("sk-...")
```

--------------------------------

### Tools > Hosted tools

Source: https://openai.github.io/openai-agents-python/tools

OpenAI offers a few built-in tools when using the `OpenAIResponsesModel`:
  * The `WebSearchTool` lets an agent search the web.
  * The `FileSearchTool` allows retrieving information from your OpenAI Vector Stores.
  * The `ComputerTool` allows automating computer use tasks.
  * The `CodeInterpreterTool` lets the LLM execute code in a sandboxed environment.
  * The `HostedMCPTool` exposes a remote MCP server's tools to the model.
  * The `ImageGenerationTool` generates images from a prompt.
  * The `LocalShellTool` runs shell commands on your machine.

--------------------------------

### Session > clear_session

Source: https://openai.github.io/openai-agents-python/ref/memory/session

Clear all items for this session. This effectively resets the conversation history.

--------------------------------

### OpenAI Agents Python > output_tokens

Source: https://openai.github.io/openai-agents-python/ko/ref/usage

Total output tokens received, across all requests.

--------------------------------

### ToolGuardrailFunctionOutput dataclass > reject_content classmethod

Source: https://openai.github.io/openai-agents-python/zh/ref/tool_guardrails

The `reject_content` class method generates a `ToolGuardrailFunctionOutput` that signals the rejection of a tool call or its output. Although the content is rejected, the execution process continues, and a specified message is communicated to the model. This method also allows for optional `output_info` to be included.

--------------------------------

### ToolGuardrailFunctionOutput `dataclass` > allow `classmethod`

Source: https://openai.github.io/openai-agents-python/ko/ref/tool_guardrails

The `allow` class method is used to create a `ToolGuardrailFunctionOutput` instance that permits the tool's execution to continue as normal. It takes an optional `output_info` argument, which can contain supplementary data about any checks performed. This method is useful when a guardrail determines that no specific action or intervention is required, and the tool's operation should proceed without modification.

--------------------------------

### RunResult dataclass > context_wrapper instance-attribute

Source: https://openai.github.io/openai-agents-python/ref/result

The `context_wrapper` attribute holds an instance of `RunContextWrapper`, which encapsulates the execution context for the agent run. This context can include various pieces of information relevant to the agent's operation, such as configuration, state, or shared resources. It allows for managing and passing context throughout the agent's execution lifecycle.

--------------------------------

### MCP Servers > MCPServer > name

Source: https://openai.github.io/openai-agents-python/ja/ref/mcp/server

The `name` property is an abstract method within the `MCPServer` base class. It is designed to return a human-readable string that identifies the server. This property is crucial for logging, debugging, and user interfaces, providing a clear and concise name for each specific MCP server implementation.

--------------------------------

### SQLiteSession

Source: https://openai.github.io/openai-agents-python/ja/ref/memory

The `__init__` method for `SQLiteSession` allows for customization of the session storage. It accepts a `session_id` to uniquely identify the conversation. The `db_path` parameter determines where the SQLite database is stored, defaulting to `':memory:'` for an in-memory database. Additionally, `sessions_table` and `messages_table` parameters can be used to specify the names of the tables used for storing session metadata and message data, respectively, with default names provided.

--------------------------------

### OpenAI Agents Python API Reference > reset_conversation_history_wrappers

Source: https://openai.github.io/openai-agents-python/ja/ref/handoffs

Restore the default `<CONVERSATION HISTORY>` markers.

--------------------------------

### speech_span

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

The `speech_span` function is used to create a new speech span for tracing purposes. This span is not automatically started; you must either use a `with speech_span() ...:` block or manually call `span.start()` and `span.finish()`. The function accepts several parameters to detail the speech operation, including `model` (the TTS model used), `input` (the text to be synthesized), and `output` (the resulting audio data). It also allows specifying `output_format`, `model_config` for hyperparameters, and `first_content_at` for timing information. Optional parameters like `span_id` and `parent` can be provided for custom span management, while `disabled` can be set to `True` to prevent the span from being recorded.

--------------------------------

### Run context > RunContextWrapper dataclass > context instance-attribute

Source: https://openai.github.io/openai-agents-python/ko/ref/run_context

The `context` instance attribute within `RunContextWrapper` holds the context object, which can be `None`, as passed by the user to `Runner.run()`.

--------------------------------

### openai-agents-python/result.py > final_output

Source: https://openai.github.io/openai-agents-python/ja/ref/result

The output of the last agent.

--------------------------------

### RealtimeAgent > name

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/agent

The `name` attribute stores the unique identifier for the agent, serving as its name.

--------------------------------

### trace > trace_id

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The ID of the trace. Optional. If not provided, we will generate an ID. We recommend using `util.gen_trace_id()` to generate a trace ID, to guarantee that IDs are correctly formatted.

--------------------------------

### TracingProcessor > on_trace_start

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/processor_interface

The `on_trace_start` method is invoked when a new trace begins. It receives the `trace` object, which includes the workflow name and associated metadata. This method is called synchronously and should execute quickly to prevent blocking the agent's execution. Any errors encountered within this method should be handled internally.

--------------------------------

### Tracing Processor Interface > shutdown

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/processor_interface

The `shutdown` method is called when the application stops and should perform any necessary cleanup. This includes flushing any queued traces or spans, closing active connections, and releasing any resources that were allocated during the tracing process. Proper implementation of `shutdown` ensures that all data is processed and resources are freed before the application terminates.

--------------------------------

### Conversations/chat threads

Source: https://openai.github.io/openai-agents-python/running_agents

A single call to any of the `run` methods, even if it involves multiple agents and LLM calls, represents one logical turn in a chat conversation. For instance, a user's text input initiates a `Runner.run` operation where the first agent might call an LLM, execute tools, and then hand off to a second agent. This second agent may run further tools before producing a final output. After the agent run completes, you have the flexibility to decide what information is presented to the user, whether it's every new item generated or just the final output. This output can then serve as the basis for the user's next follow-up question, prompting another call to the `run` method.

--------------------------------

### Tools > ToolOutputImage > check_at_least_one_required_field

Source: https://openai.github.io/openai-agents-python/zh/ref/tool

Validate that at least one of image_url or file_id is provided.

--------------------------------

### TracingProcessor

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `TracingProcessor` is an abstract class that defines the interface for all tracing processors within the OpenAI Agents system. Its primary role is to facilitate the processing and monitoring of traces and spans. Processors implementing this interface receive notifications at key moments: when traces and spans begin and end. This allows them to collect, process, and export tracing data effectively. The design emphasizes thread-safety, minimal blocking, and graceful error handling to ensure the smooth operation of agent execution.

--------------------------------

### DaprSession Class > get_items

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/memory/dapr_session

The `get_items` asynchronous method retrieves the conversation history stored for this `DaprSession`. You can optionally specify a `limit` to fetch only the most recent messages. If `limit` is `None` (the default), all available conversation history items will be returned. When a `limit` is provided, the method returns the latest `N` items in chronological order. The method reconstructs the conversation history by fetching data from the configured Dapr state store, decoding it, and deserializing each message into the appropriate `TResponseInputItem` format. It handles potential decoding or deserialization errors gracefully by skipping problematic entries.

--------------------------------

### RunConfig `dataclass` > model `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ko/ref/run

The `model` attribute within `RunConfig` specifies the LLM to be used for the entire agent execution. If this attribute is set, it will supersede any model configuration defined for individual agents within the run. It is crucial that the `model_provider` configured for the run is capable of resolving the model name provided here.

--------------------------------

### Source code in src/agents/tracing/create.py > speech_group_span

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/create

Create a new speech group span. The span will not be started automatically, you should either do `with speech_group_span() ...` or call `span.start()` + `span.finish()` manually. The `input` parameter is the text used for the speech request. `span_id` is optional and can be generated using `util.gen_span_id()`. The `parent` parameter specifies the parent span or trace, defaulting to the current one. `disabled` can be set to `True` to prevent the span from being recorded.

--------------------------------

### Usage > output_tokens

Source: https://openai.github.io/openai-agents-python/ref/usage

The `output_tokens` attribute tracks the total number of output tokens received from the LLM API across all requests. Monitoring this value helps in assessing the volume of generated content.

--------------------------------

### VoicePipeline > __init__

Source: https://openai.github.io/openai-agents-python/ko/ref/voice/pipeline

The `VoicePipeline` constructor allows for customization of its components. You can provide a specific `workflow` that the pipeline will execute. For speech-to-text (STT) and text-to-speech (TTS) functionalities, you can either specify particular models or let the pipeline use default OpenAI models if none are provided. Additionally, a `config` object can be passed to further tailor the pipeline's behavior, and if no configuration is given, a default one will be applied.

--------------------------------

### Agents > Multi-agent system design patterns

Source: https://openai.github.io/openai-agents-python/agents

There are many ways to design multi‑agent systems, but we commonly see two broadly applicable patterns:
  1. Manager (agents as tools): A central manager/orchestrator invokes specialized sub‑agents as tools and retains control of the conversation.
  2. Handoffs: Peer agents hand off control to a specialized agent that takes over the conversation. This is decentralized.

--------------------------------

### TracingProcessor > on_trace_start

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

The `on_trace_start` method is called synchronously when a new trace begins execution. It receives the `trace` object, which contains the workflow name and associated metadata. Implementations should ensure this method returns quickly to avoid blocking the agent's execution. Any errors encountered within this method should be caught and handled internally to maintain system stability.

--------------------------------

### Source code in src/agents/tracing/traces.py

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/traces

The `name` property returns the workflow name associated with the trace. For a `NoOpTrace`, which is used when tracing is disabled, this property returns 'no-op' to indicate that it represents a workflow without active tracing.

--------------------------------

### OpenAI Agents Python/realtime/config.py/User Input Types/RealtimeUserInputMessage/type

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/config

The `type` attribute for `RealtimeUserInputMessage` is an instance attribute that identifies the input as a 'message'. This distinguishes it from other input types, such as plain text.

--------------------------------

### Tracing Processor Interface > shutdown

Source: https://openai.github.io/openai-agents-python/ref/tracing/processor_interface

The `shutdown` method is called when the application stops and should be used to clean up any necessary resources. This includes flushing any queued traces or spans, closing active connections, and releasing any held resources.

--------------------------------

### function_span

Source: https://openai.github.io/openai-agents-python/ref/tracing

The `function_span` function is used to create a new span for tracing function calls. It's important to note that the span is not automatically started. You need to explicitly start and finish the span using either a `with` statement (e.g., `with function_span() ...`) or by manually calling `span.start()` and `span.finish()` methods. This function takes several parameters including the `name` of the function, its `input` and `output` (both optional strings), an optional `span_id`, an optional `parent` span or trace, and a `disabled` flag. If `span_id` is not provided, a unique ID will be generated. The `parent` parameter allows you to link this span to an existing trace or span; if omitted, it defaults to the current trace or span. The `disabled` parameter, when set to `True`, prevents the span from being recorded.

--------------------------------

### OpenAI Agents Python > request_usage_entries

Source: https://openai.github.io/openai-agents-python/ko/ref/usage

List of RequestUsage entries for accurate per-request cost calculation.
Each call to `add()` automatically creates an entry in this list if the added usage represents a new request (i.e., has non-zero tokens).
For a run that makes 3 API calls with 100K, 150K, and 80K input tokens each, the aggregated `input_tokens` would be 330K, but `request_usage_entries` would preserve the [100K, 150K, 80K] breakdown, which could be helpful for detailed cost calculation or context window management.

--------------------------------

### openai-agents-python > speech_group_span

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/create

Create a new speech group span. The span will not be started automatically, you should either do `with speech_group_span() ...` or call `span.start()` + `span.finish()` manually. The `input` parameter represents the text used for the speech request. An optional `span_id` can be provided; if omitted, an ID will be generated. The `parent` parameter allows specifying a parent trace or span, defaulting to the current context. Setting `disabled` to `True` will return a span that is not recorded.

--------------------------------

### Memory persistence

Source: https://openai.github.io/openai-agents-python/sessions

The library offers several options for memory persistence, catering to different use cases. For temporary conversations, in-memory SQLite is suitable. For persistent conversations, file-based SQLite or SQLAlchemy sessions with existing databases can be used. Production cloud-native deployments can benefit from Dapr state store sessions, offering telemetry and tracing. OpenAI-hosted storage is an option for those preferring to use the OpenAI Conversations API. For enhanced security, `EncryptedSession` can wrap any existing session. Custom backends can also be implemented for specialized needs like Redis or Django.

--------------------------------

### Agent > as_tool

Source: https://openai.github.io/openai-agents-python/ref/agent

The `as_tool` method transforms an agent into a tool that can be invoked by other agents. This functionality differs from agent handoffs in two key aspects. Firstly, when an agent is handed off, it receives the entire conversation history. In contrast, when an agent is converted into a tool, it only receives generated input for its execution. Secondly, in a handoff scenario, the new agent assumes control of the conversation. However, when an agent acts as a tool, it is called as a subordinate task, and the original agent continues to manage the conversation flow after the tool's execution.

--------------------------------

### Run context > AgentHookContext dataclass > turn_input class-attribute instance-attribute

Source: https://openai.github.io/openai-agents-python/ref/run_context

The `turn_input` instance attribute of `AgentHookContext` is a list containing the input items for the current turn.

--------------------------------

### custom_span

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `custom_span` function allows you to create a new span with custom metadata. Unlike other span creation methods, this span is not automatically started. You must explicitly start and finish the span using either a `with` statement (e.g., `with custom_span(...) as span:`) or by manually calling `span.start()` and `span.finish()` methods. This provides fine-grained control over when your custom span's timing and data are recorded.

--------------------------------

### TracingProcessor

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/processor_interface

The `on_span_start` method is called synchronously when a new span begins. The `span` object passed to this method contains details about the operation and its context. Like `on_trace_start`, this method should return quickly and handle errors internally, as spans are automatically nested within the current trace or parent span. The `on_span_end` method is also called synchronously when a span finishes execution. It receives the completed `span` object, and its implementation should not block or raise exceptions, ensuring the agent's execution remains uninterrupted.

--------------------------------

### RunResult dataclass > raw_responses instance-attribute

Source: https://openai.github.io/openai-agents-python/ja/ref/result

The `raw_responses` attribute contains a list of the raw responses generated by the language model during the agent's execution. These are the direct outputs from the LLM before any further processing or interpretation.

--------------------------------

### SQLAlchemy Sessions > Quick start > Using database URL

Source: https://openai.github.io/openai-agents-python/sessions/sqlalchemy_session

The simplest way to get started with `SQLAlchemySession` is by providing a database URL. This method allows you to create a session using a connection string that specifies the database dialect and connection details. The `SQLAlchemySession.from_url` method handles the creation of the session and can optionally create the necessary tables if `create_tables` is set to `True`.

--------------------------------

### MCPServerSse

Source: https://openai.github.io/openai-agents-python/zh/ref/mcp/server

When creating an instance of `MCPServerSse`, several parameters can be configured to tailor its behavior. The `params` argument is crucial as it contains essential server configuration, including the server's URL, any necessary HTTP headers, the timeout for standard HTTP requests, and the specific timeout for the SSE connection. Additionally, you can control whether the list of available tools is cached (`cache_tools_list`) to potentially improve latency by avoiding repeated server requests. A descriptive `name` can be provided for the server, or one will be automatically generated from its URL. Other configurable options include the `client_session_timeout_seconds`, a `tool_filter` for managing tool access, a flag `use_structured_content` to control the use of structured data in tool results, and parameters for managing retries (`max_retry_attempts`, `retry_backoff_seconds_base`) in case of communication failures. An optional `message_handler` can also be supplied to process session messages.

--------------------------------

### Agent Class > Initialization and Validation

Source: https://openai.github.io/openai-agents-python/ko/ref/agent

The `Agent` class constructor (`__init__`) is responsible for initializing an agent instance and performing crucial validation checks on its various parameters. It ensures that attributes like `input_guardrails` and `output_guardrails` are lists, `output_type` is a valid type or schema, and `hooks` conform to the `AgentHooksBase` interface. Additionally, it validates the `tool_use_behavior` parameter to ensure it's one of the accepted string values, a dictionary, or a callable, and that `reset_tool_choice` is a boolean. These checks are vital for maintaining the integrity and predictable behavior of the agent.

--------------------------------

### RealtimeRunner > __init__

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/runner

Initializes the realtime runner. The `starting_agent` is the agent to start the session with. If the `model` is not provided, a default OpenAI realtime model will be used. The `config` parameter can be used to override parameters for the entire run.

--------------------------------

### Agent dataclass > model

Source: https://openai.github.io/openai-agents-python/ref/agent

The model implementation to use when invoking the LLM.

By default, if not set, the agent will use the default model configured in `agents.models.get_default_model()` (currently "gpt-4.1").

--------------------------------

### AgentOutputSchema `dataclass`

Source: https://openai.github.io/openai-agents-python/ko/ref/agent_output

The `AgentOutputSchema` class provides several methods for interacting with the output schema and validated data. `is_plain_text()` returns `True` if the output is plain text, and `False` otherwise. `is_strict_json_schema()` indicates whether strict JSON schema validation is enabled. The `json_schema()` method returns the generated JSON schema for non-plain text outputs, raising an error if the output type is plain text. The `validate_json()` method takes a JSON string, validates it against the configured output type using `TypeAdapter`, and returns the validated object. It includes error handling for cases where the validated data is not in the expected dictionary format when wrapping is applied.

--------------------------------

### AgentManager > get_conversation_turns

Source: https://openai.github.io/openai-agents-python/zh/ref/extensions/memory/advanced_sqlite_session

The `get_conversation_turns` method retrieves a list of user turns from a specified branch, or the current branch if none is provided. It queries the `message_structure` and `agent_messages` tables to fetch the turn number, message content, and creation timestamp. The returned list contains dictionaries with turn details, including a truncated version of the content for browsing and the full content for complete review. All user messages are marked as branchable.

--------------------------------

### MCPServerStdio

Source: https://openai.github.io/openai-agents-python/ja/ref/mcp/server

The `name` property provides a human-readable identifier for the `MCPServerStdio` instance. If a name is not explicitly provided during initialization, it is automatically generated based on the command used to start the server, prefixed with 'stdio:'. This aids in identifying and distinguishing different server instances, especially in environments where multiple servers might be running.

--------------------------------

### Orchestrating multiple agents

Source: https://openai.github.io/openai-agents-python/multi_agent

Orchestration refers to the flow of agents in your app. Which agents run, in what order, and how do they decide what happens next? There are two main ways to orchestrate agents:
1. Allowing the LLM to make decisions: this uses the intelligence of an LLM to plan, reason, and decide on what steps to take based on that.
2. Orchestrating via code: determining the flow of agents via your code.
You can mix and match these patterns. Each has their own tradeoffs, described below.

--------------------------------

### RunConfig `dataclass` > workflow_name `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ja/ref/run

The `workflow_name` attribute in `RunConfig` provides a descriptive name for the agent run, primarily used for tracing purposes. Assigning a logical name, such as 'Code generation workflow' or 'Customer support agent', helps in organizing and identifying different agent processes within tracing systems.

--------------------------------

### openai-agents-python/result.py > input

Source: https://openai.github.io/openai-agents-python/ja/ref/result

The original input items i.e. the items before run() was called. This may be a mutated version of the input, if there are handoff input filters that mutate the input.

--------------------------------

### transcription_span

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/create

The `transcription_span` function is used to create a new span for speech-to-text transcriptions. This span is not started automatically; you must either use a `with` statement (e.g., `with transcription_span() ...`) or manually call `span.start()` followed by `span.finish()`. The function accepts several parameters to configure the transcription process, including the `model` name, the audio `input` (as a base64 encoded string), the `input_format` of the audio, and the expected `output`. Optional parameters include `model_config` for hyperparameters, `span_id` for custom span identification, and `parent` to link to an existing trace or span. A `disabled` flag can be set to `True` to create a span that will not be recorded.

--------------------------------

### Usage > output_tokens

Source: https://openai.github.io/openai-agents-python/zh/ref/usage

The `output_tokens` attribute reflects the total number of output tokens received from the LLM API across all requests. This metric quantifies the amount of generated content.

--------------------------------

### to_input_items

Source: https://openai.github.io/openai-agents-python/ko/ref/items

Convert the output into a list of input items suitable for passing to the model. The shape of the Pydantic output items are the same as the equivalent TypedDict input items, so we can just convert each one. This is also tested via unit tests.

--------------------------------

### run `async` `classmethod`

Source: https://openai.github.io/openai-agents-python/zh/ref/run

The `run` class method initiates a workflow beginning with a specified agent. This agent operates in an iterative loop until a definitive output is produced. The execution cycle proceeds as follows: first, the agent is invoked with the provided input. If the agent's output matches its designated `output_type`, signaling a final result, the loop concludes. Should the agent decide to hand off control to another agent, the loop restarts with the new agent. If no handoff occurs, any pending tool calls are executed, and the loop then resumes. During this process, two primary exceptions can be raised: `MaxTurnsExceeded` if the predefined maximum number of turns is surpassed, or `GuardrailTripwireTriggered` if a safety mechanism is activated. It's important to note that input guardrails are only evaluated for the very first agent in the sequence.

--------------------------------

### RunResult dataclass > new_items instance-attribute

Source: https://openai.github.io/openai-agents-python/ref/result

The `new_items` attribute is a list containing all the new items that were generated during the execution of an agent. This list can include various types of `RunItem` objects, such as new messages that were created, tool calls that the agent decided to make, and the corresponding outputs received from those tool executions. This provides a detailed log of the agent's actions and the information it produced beyond its final output.

--------------------------------

### Agent Attributes > tool_use_behavior

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

This attribute configures how tool use is handled within the agent. The default behavior, 'run_llm_again', involves running tools and then allowing the LLM to respond with the results. Alternatively, 'stop_on_first_tool' treats the output of the first tool call as the final result, bypassing further LLM processing. You can also provide a `StopAtTools` object to halt execution if specific tools are called, using the first matching tool's output as the final result. Additionally, a custom function can be supplied to process tool results and determine the final output via a `ToolsToFinalOutputResult` object. This configuration is specific to FunctionTools; hosted tools are always processed by the LLM.

--------------------------------

### Branch workflow example

Source: https://openai.github.io/openai-agents-python/sessions/advanced_sqlite_session

Managing conversation branches is a key feature for exploring different conversational paths. You can list all available branches using `session.list_branches()`, which also indicates the current branch and provides counts of user turns and messages within each. Switching between branches is straightforward with `session.switch_to_branch()`, accepting either the branch name or ID. Deleting a branch can be done using `session.delete_branch()`, with an option `force=True` to allow deletion of the currently active branch.

--------------------------------

### Model Settings > verbosity

Source: https://openai.github.io/openai-agents-python/ref/model_settings

Constrains the verbosity of the model's response.

--------------------------------

### OpenAI Agents Python

Source: https://openai.github.io/openai-agents-python/ref/model_settings

The `extra_headers` attribute enables you to include additional headers in your requests. This parameter defaults to `None` if no extra headers are specified.

--------------------------------

### Session > get_items

Source: https://openai.github.io/openai-agents-python/ko/ref/memory/session

The `get_items` asynchronous method allows retrieval of the conversation history for a given session. It accepts an optional `limit` parameter to specify the maximum number of items to return. If `limit` is `None`, all items in the history are returned. When a `limit` is provided, the method returns the `N` most recent items in chronological order.

--------------------------------

### Agent Attributes > mcp_config

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

This attribute holds the configuration settings for MCP (Model Context Protocol) servers. It allows for customization of how these servers interact with the agent.

--------------------------------

### RunConfig `dataclass`

Source: https://openai.github.io/openai-agents-python/ref/run

The `RunConfig` dataclass configures settings for the entire agent run. It allows for global overrides of model settings, input/output guardrails, and tracing configurations. It also provides mechanisms for handling conversation history during agent handoffs and customizing how session history is managed.

--------------------------------

### TracingProcessor

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

Implementing a custom `TracingProcessor` involves defining methods such as `on_trace_start`, `on_trace_end`, `on_span_start`, and `on_span_end`. These methods are called synchronously during the agent's execution. For example, `on_trace_start` is invoked when a new trace begins, and `on_span_start` is called when a new operation (span) within that trace starts. Similarly, `on_trace_end` and `on_span_end` are triggered upon completion. It's crucial that these methods are thread-safe, do not block for extended periods, and handle errors gracefully to ensure the agent's execution is not disrupted.

--------------------------------

### Run context > AgentHookContext dataclass > usage class-attribute instance-attribute

Source: https://openai.github.io/openai-agents-python/ko/ref/run_context

The `usage` instance attribute in `AgentHookContext` reflects the usage statistics of the agent run so far, defaulting to a new `Usage` object. For streamed responses, this data may not be fully updated until the stream concludes.

--------------------------------

### function_tool

Source: https://openai.github.io/openai-agents-python/ko/ref/tool

The `function_tool` decorator is used to convert a Python function into a `FunctionTool` object. This allows the function to be used as a tool within an agent. By default, the decorator automatically extracts information from the function's signature and docstring to define the tool's schema and description. Specifically, it parses the function signature to generate a JSON schema for the tool's parameters and uses the docstring to provide a description for the tool and its arguments. The decorator attempts to auto-detect the docstring style, but this can also be explicitly set using the `docstring_style` parameter. A crucial detail is that if the wrapped function accepts a `RunContextWrapper` as its first argument, this context type must be compatible with the agent that will be utilizing the tool.

--------------------------------

### Tracing > Creating traces

Source: https://openai.github.io/openai-agents-python/tracing

You can use the `trace()` function to create a trace. Traces need to be started and finished. You have two options to do so: **Recommended** : use the trace as a context manager, i.e. `with trace(...) as my_trace`. This will automatically start and end the trace at the right time. You can also manually call `trace.start()` and `trace.finish()`. The current trace is tracked via a Python `contextvar`. This means that it works with concurrency automatically. If you manually start/end a trace, you'll need to pass `mark_as_current` and `reset_current` to `start()`/`finish()` to update the current trace.

--------------------------------

### Agent Attributes > output_guardrails

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

A list of checks that run on the final output of the agent, after generating a response. Runs only if the agent produces a final output.

--------------------------------

### Processor Interface > on_trace_start

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `on_trace_start` method is called synchronously when a new trace begins execution. It receives a `Trace` object as an argument, which contains the workflow name and associated metadata. Implementations of this method should return quickly to avoid blocking the execution flow. Any errors encountered within this method should be caught and handled internally to prevent disruptions.

--------------------------------

### Agent Class Attributes > hooks

Source: https://openai.github.io/openai-agents-python/ko/ref/agent

The `hooks` attribute allows for the integration of an `AgentHooks` class, which provides callbacks for various events throughout the agent's lifecycle. This enables custom logic to be executed at specific points, such as before or after agent execution, or in response to errors.

--------------------------------

### TracingProcessor > on_span_start

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

The `on_span_start` method is called synchronously when a new span begins execution. It receives the `span` object, which contains details about the operation being performed and its associated context. Implementations should ensure this method executes quickly to avoid blocking agent execution. The system automatically handles the nesting of spans under the current trace or parent span.

--------------------------------

### RealtimeSession

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/session

The `RealtimeSession` class represents a connection to a realtime model. It facilitates bidirectional communication, allowing you to stream events from the model to your application and to send messages and audio data to the model. This class inherits from `RealtimeModelListener`, indicating its role in handling model-related events in real-time.

--------------------------------

### Sessions > Session types > OpenAI Conversations API sessions

Source: https://openai.github.io/openai-agents-python/sessions

Use OpenAI's Conversations API through `OpenAIConversationsSession`. This session type leverages OpenAI's dedicated API for managing conversational context. You can create a new conversation or optionally resume a previous one by providing a `conversation_id` when initializing the session. This is suitable for applications that need to integrate directly with OpenAI's conversational infrastructure.

--------------------------------

### tool.py > HostedMCPTool dataclass

Source: https://openai.github.io/openai-agents-python/ref/tool

A tool that allows the LLM to use a remote MCP server. The LLM will automatically list and call tools, without requiring a round trip back to your code. If you want to run MCP servers locally via stdio, in a VPC or other non-publicly-accessible environment, or you just prefer to run tool calls locally, then you can instead use the servers in `agents.mcp` and pass `Agent(mcp_servers=[...])` to the agent. This tool configuration includes the server URL and other settings for the MCP tool, and an optional function to handle approval requests.

--------------------------------

### Results > RunResultBase dataclass

Source: https://openai.github.io/openai-agents-python/zh/ref/result

The `new_items` attribute in `RunResultBase` is a list that captures all the new items generated during the execution of an agent. This typically includes things like new messages that were created, tool calls that were invoked, and the outputs received from those tool calls. These items represent the dynamic evolution of the agent's execution flow and its interactions.

--------------------------------

### RunResult dataclass

Source: https://openai.github.io/openai-agents-python/ko/ref/result

The `RunResult` dataclass, inheriting from `RunResultBase`, encapsulates the complete outcome of an agent's execution. It holds references to the last agent that was run and provides a way to access it via the `last_agent` property. Internally, it uses weak references to the agent to prevent memory leaks, managing these references through the `_last_agent_ref` attribute and the `_release_last_agent_reference` method. The `__post_init__` method ensures that a weak reference to the agent is set upon initialization. The `__str__` method provides a human-readable string representation of the result.

--------------------------------

### RunConfig `dataclass` > workflow_name `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ref/run

The `workflow_name` attribute in `RunConfig` provides a human-readable name for the agent run, primarily used for tracing purposes. Assigning a descriptive name, such as "Code generation workflow" or "Customer support agent", helps in identifying and categorizing different agent executions within tracing systems.

--------------------------------

### TracingProcessor > on_trace_start

Source: https://openai.github.io/openai-agents-python/ref/tracing

The `on_trace_start` method is called synchronously when a new trace begins its execution. It receives the `trace` object, which contains the workflow name and associated metadata. Implementations of this method should return quickly to avoid blocking the agent's execution. Any errors encountered within this method should be caught and handled internally.

--------------------------------

### RunResultStreaming `dataclass`

Source: https://openai.github.io/openai-agents-python/ko/ref/result

The `RunResultStreaming` class includes several key attributes to manage the agent's execution state. `current_agent` refers to the agent actively processing the current turn, while `current_turn` indicates the current step number in the agent's execution sequence. `max_turns` defines the upper limit for the number of turns the agent can execute. `final_output` holds the agent's ultimate result, which is initially `None` and populated only upon completion. The `is_complete` boolean flag signals whether the agent's run has successfully concluded. Internal attributes like `_current_agent_output_schema`, `trace`, `_current_agent_ref`, `_event_queue`, `_input_guardrail_queue`, `_run_impl_task`, `_input_guardrails_task`, `_output_guardrails_task`, `_stored_exception`, and `_cancel_mode` are used for internal state management, task coordination, and handling exceptions and cancellation.

--------------------------------

### RunConfig `dataclass` > session_input_callback `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ref/run

The `session_input_callback` attribute in `RunConfig` defines a custom strategy for managing session history when new input is provided. By default (`None`), new input is simply appended. However, a `SessionInputCallback` function can be supplied to dictate how the history and new input are combined, offering fine-grained control over the conversation context.

--------------------------------

### RealtimeSession

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/session

You can establish and manage a `RealtimeSession` using the `RealtimeRunner`. The `async with await runner.run() as session:` block ensures proper setup and teardown of the session. Within this context, you can interact with the model by sending messages using `session.send_message("Hello")` or audio data with `session.send_audio(audio_bytes)`. Additionally, you can asynchronously iterate over the `session` object to receive and process events streamed from the model, such as audio responses, using `async for event in session:`.

--------------------------------

### MCPListToolsItem `dataclass`

Source: https://openai.github.io/openai-agents-python/ko/ref/items

The `MCPListToolsItem` dataclass represents a call made to an MCP server to list available tools. It inherits from `RunItemBase` and holds the raw MCP list tools call.

--------------------------------

### Model Settings > resolve

Source: https://openai.github.io/openai-agents-python/ko/ref/model_settings

`resolve`: Produce a new `ModelSettings` by overlaying any non-None values from the override on top of this instance. If no override is provided, the current instance is returned. If an override is provided, a new instance is created with values from the override taking precedence. The `extra_args` are merged if both instances have them, otherwise they are replaced.

--------------------------------

### ToolGuardrailFunctionOutput dataclass > allow classmethod

Source: https://openai.github.io/openai-agents-python/ja/ref/tool_guardrails

The `allow` class method provides a convenient way to create a `ToolGuardrailFunctionOutput` instance that permits normal tool execution to proceed. It accepts an optional `output_info` argument to include details about any checks performed. This method simplifies the process of signaling that no guardrail-related intervention is necessary.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

`top_logprobs` specifies the number of top tokens for which log probabilities should be returned. When this parameter is set, it automatically includes `"message.output_text.logprobs"` in the response.

--------------------------------

### src/agents/tracing/create.py > generation_span

Source: https://openai.github.io/openai-agents-python/ref/tracing

Creates a new generation span. This span is not started automatically; you must either use a `with` statement (e.g., `with generation_span() ...`) or manually call `span.start()` followed by `span.finish()`. The `generation_span` captures detailed information about a model's generation process, including the input messages, the generated outputs, the model used, its configuration, and any associated usage data (like token counts). If you only need to track a model response identifier, the `response_span()` function is more suitable. The span can optionally take input, output, model details, model configuration, usage statistics, a specific span ID, and a parent span or trace. A `disabled` flag can be set to `True` to prevent the span from being recorded.

--------------------------------

### Processor Interface > on_trace_start

Source: https://openai.github.io/openai-agents-python/ref/tracing

The `on_trace_start` method is invoked synchronously when a new trace begins execution. It receives a `Trace` object containing the workflow name and associated metadata. Implementations should ensure this method returns quickly to avoid blocking the trace's execution and should handle any internal errors gracefully.

--------------------------------

### Processor Interface > on_span_start

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

The `on_span_start` method is called synchronously at the beginning of a new span's execution. It receives the `Span` object, which holds details about the operation and its context. Similar to `on_trace_start`, this method should execute quickly to avoid blocking. Spans are automatically managed within the current trace or span hierarchy.

--------------------------------

### Model Settings > max_tokens

Source: https://openai.github.io/openai-agents-python/ref/model_settings

The maximum number of output tokens to generate.

--------------------------------

### RunConfig `dataclass` > model_settings `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ja/ref/run

Global model settings can be configured using the `model_settings` attribute in `RunConfig`. Any non-null values provided here will take precedence over agent-specific model settings, allowing for uniform configuration across all agents in a run.

--------------------------------

### Audio processing

Source: https://openai.github.io/openai-agents-python/realtime/guide

Send audio to the session using `session.send_audio(audio_bytes)` or send text using `session.send_message()`. For audio output, listen for `audio` events and play the audio data through your preferred audio library. Make sure to listen for `audio_interrupted` events to stop playback immediately and clear any queued audio when the user interrupts the agent.

--------------------------------

### MCPServerStdio > name

Source: https://openai.github.io/openai-agents-python/ko/ref/mcp/server

The `name` property provides a human-readable identifier for the `MCPServerStdio` instance. If a name is not explicitly provided during initialization, it is automatically generated based on the command used to start the stdio server, for example, `stdio: <command>`. This makes it easier to distinguish between different server instances when debugging or monitoring.

--------------------------------

### Model > RealtimePlaybackState

Source: https://openai.github.io/openai-agents-python/ref/realtime/model

The `RealtimePlaybackState` is a `TypedDict` that represents the current state of real-time audio playback. It includes the `current_item_id` of the audio being played, the `current_item_content_index` which indicates the position within the item's content, and `elapsed_ms` representing the total milliseconds of audio that have been played. This state is crucial for managing and tracking audio playback progress in real-time applications.

--------------------------------

### Span > error

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

Any error that occurred during span execution. Returns error details if an error occurred, `None` otherwise.

--------------------------------

### TracingProcessor

Source: https://openai.github.io/openai-agents-python/ref/tracing

The `TracingProcessor` is an abstract class that defines the interface for processing and monitoring traces and spans within the OpenAI Agents system. Any custom tracing processor must implement this interface. Processors are notified when traces and spans begin and end, enabling them to collect, process, and export tracing data. Key methods include `on_trace_start`, `on_trace_end`, `on_span_start`, and `on_span_end`. It is crucial that all implemented methods are thread-safe, do not block for extended periods, and handle errors gracefully to avoid disrupting the agent's execution.

--------------------------------

### Classes > Agent > Attributes > session_input_callback

Source: https://openai.github.io/openai-agents-python/zh/ref/run

The `session_input_callback` attribute defines how session history is managed when new input is provided to the agent. If set to `None` (the default), new input is simply appended to the existing history. However, you can provide a custom `SessionInputCallback` function that receives both the history and the new input, and returns the desired combined list of items, offering flexibility in managing conversational context.

--------------------------------

### Configuring the SDK > Debug logging

Source: https://openai.github.io/openai-agents-python/config

The SDK includes two Python loggers, but they do not have any handlers configured by default. This means that by default, warnings and errors are output to `stdout`, while other log levels are suppressed. To enable verbose logging, use the `enable_verbose_stdout_logging()` function, which will direct all log messages to `stdout`.

```python
from agents import enable_verbose_stdout_logging

enable_verbose_stdout_logging()
```

--------------------------------

### generation_span

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/create

The `generation_span` function creates a new span that captures the details of a model generation. This includes the input message sequence, any generated outputs, the model name and configuration, and usage data. The span is not started automatically, so you must either use a `with` statement (e.g., `with generation_span() ...`) or manually call `span.start()` and `span.finish()`.

If you only need to capture a model response identifier, the `response_span()` function should be used instead.

--------------------------------

### openai_agents.store.SQLiteSession.store_run_usage

Source: https://openai.github.io/openai-agents-python/ref/extensions/memory/advanced_sqlite_session

The `store_run_usage` method is designed to be called after `Runner.run()` completes. It captures usage data for the current conversation turn. Session-level usage can be aggregated from these turn-level data points when necessary. It checks if there's any usage information in the `result.context_wrapper.usage` and proceeds to update the turn-level usage if available. Any exceptions during this process are logged as errors.

--------------------------------

### openai-agents-python/agents.py > Agent class > copy_message_structure

Source: https://openai.github.io/openai-agents-python/ref/extensions/memory/advanced_sqlite_session

Branching allows for exploring different conversation paths. When a user message is processed, the agent can create a new branch from that point, effectively forking the conversation history. This is managed by copying the relevant message structure to a new `branch_id`. The `copy_message_structure` method facilitates this by retrieving messages from a source branch and inserting them into the database under a new branch identifier, ensuring that subsequent messages are associated with the correct conversational fork.

--------------------------------

### OpenAI Agents Python > openai_agents/llm/openai.py > _convert_gemini_extra_content_to_provider_specific_fields

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/litellm

The `_convert_gemini_extra_content_to_provider_specific_fields` method is designed to transform the way tool calls are represented for Gemini models within the `litellm` framework. It specifically targets `extra_content` that contains Google-specific fields, such as `thought_signature`, and converts them into the `provider_specific_fields` format expected by `litellm`. This conversion is crucial for ensuring that Gemini's unique features, like thought signatures, are correctly interpreted and utilized by the underlying `litellm` calls. The method iterates through messages, focusing on assistant messages that appear after the last user message, to apply these transformations.

--------------------------------

### VoicePipeline

Source: https://openai.github.io/openai-agents-python/ja/ref/voice/pipeline

The `_process_audio_input` method handles the transcription of audio data using the configured STT model. It passes the audio input, along with any specified STT settings and trace configurations, to the model's `transcribe` method. The result is the transcribed text.

--------------------------------

### Workflow > VoiceWorkflowHelper > stream_text_from

Source: https://openai.github.io/openai-agents-python/ko/ref/voice/workflow

Wraps a `RunResultStreaming` object and yields text events from the stream.

--------------------------------

### Run context > RunContextWrapper dataclass > context instance-attribute

Source: https://openai.github.io/openai-agents-python/ref/run_context

The `context` instance attribute of `RunContextWrapper` holds the context object, which can be `None`, passed by the user to `Runner.run()`.

--------------------------------

### storage.py > engine

Source: https://openai.github.io/openai-agents-python/ko/ref/extensions/memory/sqlalchemy_session

This property provides direct access to the engine for advanced use cases, such as checking connection pool status, configuring engine settings, or manually disposing the engine when needed. It returns the SQLAlchemy async engine instance.

--------------------------------

### Agents > as_tool

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

The `on_stream` parameter provides an optional callback function that can be used to handle streaming events from the nested agent run. This callback can be either synchronous or asynchronous and receives an `AgentToolStreamEvent` object, which includes details about the nested agent, the originating tool call, and individual stream events. If `on_stream` is provided, the nested agent will be executed in streaming mode. The `failure_error_function` allows for custom error handling when the tool (agent) run fails. If a function is provided, it generates an error message that is sent to the LLM. If this parameter is set to `None`, any exceptions raised during the tool's execution will be propagated instead.

--------------------------------

### TracingProcessor > on_span_start

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `on_span_start` method is called synchronously when a new span begins execution. It receives the `span` object, which details the operation and its context. Similar to `on_trace_start`, this method should execute quickly to prevent blocking. Spans are automatically managed with respect to nesting under the current trace or parent span.

--------------------------------

### spans.py > Span > parent_id

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

ID of the parent span, if any.

--------------------------------

### Function schema > FuncSchema dataclass

Source: https://openai.github.io/openai-agents-python/zh/ref/function_schema

The `FuncSchema` dataclass captures the schema for a Python function, preparing it to be sent to an LLM as a tool. It stores the function's name, an optional description, and a Pydantic model representing its parameters. Additionally, it holds the JSON schema derived from the Pydantic model, the function's signature, and flags for handling context and JSON schema strictness. The `strict_json_schema` attribute is strongly recommended to be set to `True` to improve the accuracy of JSON input.

--------------------------------

### Agent > as_tool

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

The `as_tool` method allows an agent to be transformed into a tool that can be invoked by other agents. This functionality differs from agent handoffs in two key aspects. Firstly, when an agent is converted into a tool, it receives generated input directly, whereas in handoffs, the new agent inherits the conversation history. Secondly, when used as a tool, the agent is called within the context of a larger process, and the conversation continues with the original agent after the tool's execution. In contrast, with handoffs, the new agent takes full control of the conversation.

--------------------------------

### SessionABC > get_items

Source: https://openai.github.io/openai-agents-python/ref/memory/session

Retrieve the conversation history for this session. Args: limit: Maximum number of items to retrieve. If None, retrieves all items. When specified, returns the latest N items in chronological order. Returns: List of input items representing the conversation history

--------------------------------

### SingleAgentVoiceWorkflow

Source: https://openai.github.io/openai-agents-python/zh/ref/voice/workflow

The `on_start` method in `VoiceWorkflowBase` is an optional asynchronous method that executes before any user input is processed by the workflow. It can be utilized to send an initial greeting or set of instructions to the user through Text-to-Speech (TTS). By default, this method does nothing, providing a clean slate for subclasses to implement their own starting behavior if needed.

--------------------------------

### Handoff Class Configuration

Source: https://openai.github.io/openai-agents-python/zh/ref/handoffs

The `Handoff` class allows for defining actions or transitions to other agents within the agent's execution flow. It can be configured with an `input_type` to validate the input passed to the handoff function, and an `input_filter` to further process inputs. The `nest_handoff_history` flag controls whether the history of nested handoffs is included, defaulting to the run's configuration if not specified. The `is_enabled` parameter determines if the handoff is active, accepting a boolean or a callable that checks the run context and agent.

--------------------------------

### Agent `dataclass` > output_guardrails

Source: https://openai.github.io/openai-agents-python/ko/ref/agent

A list of checks that run in parallel to the agent's execution, after generating a response.

--------------------------------

### OpenAI Agents Python SDK > Usage Attributes > input_tokens

Source: https://openai.github.io/openai-agents-python/ja/ref/usage

The `input_tokens` attribute stores the total count of input tokens sent across all requests to the LLM API. This is an integer value, also initialized to 0, providing a cumulative measure of the data sent for processing.

--------------------------------

### SQLAlchemySession

Source: https://openai.github.io/openai-agents-python/zh/ref/extensions/memory/sqlalchemy_session

The `SQLAlchemySession` class provides an implementation of the `SessionABC` for managing conversation history using SQLAlchemy. It allows you to store and retrieve messages associated with a specific `session_id` in a relational database. This implementation is suitable for applications that require persistent storage of conversation data and can leverage SQLAlchemy's capabilities for database interactions.

When initializing `SQLAlchemySession`, you need to provide an asynchronous SQLAlchemy engine. The engine must be configured with an asynchronous driver compatible with your database (e.g., `postgresql+asyncpg`, `mysql+aiomysql`, `sqlite+aiosqlite`). You also have the option to specify whether the necessary database tables should be automatically created. For development and testing, setting `create_tables` to `True` can be convenient. However, in production environments, it's generally recommended to manage database schema migrations separately using your preferred migration tools.

--------------------------------

### RunResultStreaming `dataclass`

Source: https://openai.github.io/openai-agents-python/zh/ref/result

The `RunResultStreaming` class has several key attributes that provide information about the ongoing agent run. `current_agent` refers to the agent actively executing, while `current_turn` and `max_turns` indicate the progress and limits of the run. `final_output` holds the agent's ultimate result, which is initially `None` and populated upon completion. The `is_complete` flag signals whether the agent run has finished. Internally, it manages queues like `_event_queue` for streaming events and `_input_guardrail_queue` for input guardrail results, along with asyncio tasks for managing the run's execution and guardrail checks.

--------------------------------

### MCP Util > ToolFilterContext > agent

Source: https://openai.github.io/openai-agents-python/zh/ref/mcp/util

The `agent` attribute within ToolFilterContext refers to the agent that is requesting the tool list. This allows tool filters to access information about the agent itself, potentially enabling filters to tailor tool availability based on the agent's identity or capabilities.

--------------------------------

### openai-agents-python/function_tool.py

Source: https://openai.github.io/openai-agents-python/ko/ref/tool

The `function_tool` decorator allows you to easily convert Python functions into `FunctionTool` objects. This is particularly useful for enabling your agents to interact with external tools or APIs through natural language. By default, the decorator automatically infers the tool's schema by parsing the function's signature and utilizes the docstring to provide a description for the tool and its parameters.

It supports automatic detection of docstring styles, but you can manually specify a `docstring_style` if needed. If the decorated function accepts a `RunContextWrapper` as its first argument, it's crucial that this context type aligns with the agent that will be utilizing the tool.

--------------------------------

### Span Class > span_id

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `span_id` property returns a unique identifier for this span within its trace.

--------------------------------

### MCP Util > ToolFilter

Source: https://openai.github.io/openai-agents-python/ref/mcp/util

`ToolFilter` represents a mechanism for filtering tools. It can be either a `ToolFilterCallable` (a function that dynamically decides tool availability), a `ToolFilterStatic` configuration (using allowlists and blocklists), or `None` if no filtering is applied.

--------------------------------

### openai-agents-python/message_structure.py > MessageStructure > store_run_usage

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/memory/advanced_sqlite_session

The `store_run_usage` method is designed to be called after `Runner.run()` completes. It captures usage data for the current conversation turn. Session-level usage can be aggregated from this turn data when needed. If usage information is available in the `result.context_wrapper`, it retrieves the current turn number and updates the turn-level usage internally. Any exceptions encountered during this process are logged as errors.

--------------------------------

### Memory > Session > clear_session

Source: https://openai.github.io/openai-agents-python/ref/memory

Clear all items for this session. This action removes the entire conversation history associated with the current session.

--------------------------------

### RunResult dataclass > context_wrapper instance-attribute

Source: https://openai.github.io/openai-agents-python/ja/ref/result

The `context_wrapper` attribute holds a `RunContextWrapper` object, which provides the execution context for the agent run. This wrapper can contain various pieces of information relevant to how the agent operated.

--------------------------------

### Run context > AgentHookContext dataclass > turn_input class-attribute instance-attribute

Source: https://openai.github.io/openai-agents-python/ja/ref/run_context

The `turn_input` instance attribute within `AgentHookContext` is a list that holds the input items for the current turn of the agent's operation.

--------------------------------

### openai-agents-python/src/openai_agents/agents.py

Source: https://openai.github.io/openai-agents-python/zh/ref/models/openai_responses

This method prepares the arguments for calling the OpenAI API, specifically handling parameters related to response inclusion and model settings. It dynamically adds `logprobs` to the `include_set` if `top_logprobs` is specified in the model settings. It also constructs the `extra_args` dictionary, incorporating `top_logprobs` and verbosity settings for the response format. The function ensures that streaming is correctly configured by setting the `stream` parameter to `True` or `omit` based on the input. Finally, it makes the actual API call using `self._client.responses.create`, passing all processed arguments and returning the response, which can be either a direct `Response` object or an `AsyncStream` of `ResponseStreamEvent` for streaming scenarios.

--------------------------------

### OpenAI Agents Python > workflow_name

Source: https://openai.github.io/openai-agents-python/ref/run

The `workflow_name` attribute defines a descriptive name for the current agent run, which is primarily used for tracing purposes. Providing a logical name, such as "Code generation workflow" or "Customer support agent", helps in organizing and identifying different agent processes within the tracing system.

--------------------------------

### Usage > input_tokens

Source: https://openai.github.io/openai-agents-python/ref/usage

The `input_tokens` attribute represents the cumulative count of input tokens sent across all requests made to the LLM API. This metric is crucial for understanding the volume of data being processed by the model.

--------------------------------

### Source code in src/agents/tracing/create.py > mcp_tools_span

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/create

Create a new MCP list tools span. Similar to `speech_group_span`, this span is not started automatically and requires manual start/finish or use of a `with` statement. The `server` parameter specifies the MCP server name, and `result` contains the list of tools. Optional parameters include `span_id` for explicit ID generation, `parent` for defining the span hierarchy, and `disabled` to prevent recording.

--------------------------------

### OpenAI Agents Python SDK > Usage Attributes > total_tokens

Source: https://openai.github.io/openai-agents-python/ja/ref/usage

The `total_tokens` attribute sums up both the input and output tokens for all requests made to the LLM API. This integer attribute, initialized to 0, provides a comprehensive measure of the total token exchange.

--------------------------------

### Input > AudioInput > sample_width

Source: https://openai.github.io/openai-agents-python/zh/ref/voice/input

The `sample_width` instance attribute of `AudioInput` indicates the number of bytes per sample in the audio data. It defaults to 2, which corresponds to 16-bit audio.

--------------------------------

### Run context > AgentHookContext dataclass > turn_input class-attribute instance-attribute

Source: https://openai.github.io/openai-agents-python/ko/ref/run_context

The `turn_input` instance attribute within `AgentHookContext` is a list that holds the input items for the current turn. It defaults to an empty list.

--------------------------------

### traces.py > finish

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/traces

The `finish` method concludes a trace, finalizing all open spans. It can optionally reset the current trace to the previous one in the execution context by setting `reset_current` to `True`. This method must be called to ensure the trace is properly completed and its data is finalized. The operation is thread-safe when `reset_current` is used.

--------------------------------

### openai-agents-python/result.py > raw_responses

Source: https://openai.github.io/openai-agents-python/ja/ref/result

The raw LLM responses generated by the model during the agent run.

--------------------------------

### to_input_list

Source: https://openai.github.io/openai-agents-python/ja/ref/result

The `to_input_list()` method creates a new list of input items. It merges the original input with any newly generated items. This is useful for consolidating all input and output items into a single, unified list for subsequent processing.

--------------------------------

### MCPServerSse > name

Source: https://openai.github.io/openai-agents-python/ja/ref/mcp/server

The `name` property provides a human-readable identifier for the `MCPServerSse` instance. If a name is not explicitly provided during initialization, it will be automatically generated based on the server's URL, prefixed with 'sse:' to indicate the transport type.

--------------------------------

### OpenAI Agents Python SDK > Usage Attributes > request_usage_entries

Source: https://openai.github.io/openai-agents-python/ja/ref/usage

The `request_usage_entries` attribute is a list that stores individual `RequestUsage` objects. This list is initialized as an empty list using a default factory. It is crucial for accurate per-request cost calculation and detailed context window management. When usage is added using the `add()` method, a new entry is automatically created in this list if the added usage represents a distinct request (i.e., has non-zero tokens). This preserves the breakdown of tokens for each individual API call, rather than just providing a total sum.

--------------------------------

### BatchTraceProcessor

Source: https://openai.github.io/openai-agents-python/ref/tracing/processors

The `BatchTraceProcessor` is an implementation of `TracingProcessor` designed for efficient export of tracing data.

Key implementation details include:

*   **Thread-safe Queue**: It utilizes a `queue.Queue` for storing spans and traces, ensuring thread safety.
*   **Background Export Thread**: A dedicated background thread is responsible for exporting the collected spans, minimizing performance impact on the main application thread.
*   **In-Memory Storage**: Spans are held in memory until they are exported by the background thread.

--------------------------------

### RealtimeAgent > handoffs

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/agent

The `handoffs` parameter is a list that allows an agent to delegate tasks to other sub-agents. By providing a list of `RealtimeAgent` instances or `Handoff` objects, the agent can choose to transfer control to these sub-agents when relevant. This mechanism promotes modularity and separation of concerns within the agent architecture.

--------------------------------

### TracingProcessor

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/processor_interface

The `TracingProcessor` is an abstract base class that defines the interface for processing and monitoring traces and spans within the OpenAI Agents system. Any custom tracing processor must implement the methods defined by this interface. Processors are notified when traces and spans begin and end, enabling them to collect, process, and export tracing data. Implementing classes should ensure their methods are thread-safe, do not block for extended periods, and handle errors gracefully to avoid disrupting agent execution.

--------------------------------

### Span Class > ended_at

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `ended_at` property returns the ISO format timestamp of when the span finished execution. It returns `None` if the span has not yet finished.

--------------------------------

### SessionABC > get_items

Source: https://openai.github.io/openai-agents-python/ja/ref/memory/session

Retrieve the conversation history for this session. Args: `limit`: Maximum number of items to retrieve. If None, retrieves all items. When specified, returns the latest N items in chronological order. Returns: List of input items representing the conversation history

--------------------------------

### SingleAgentVoiceWorkflow

Source: https://openai.github.io/openai-agents-python/ja/ref/voice/workflow

The `__init__` method for `SingleAgentVoiceWorkflow` initializes a new instance of the workflow. It accepts an `agent` which is the specific agent that will be used to process the voice input. Additionally, it takes an optional `callbacks` parameter, which can be an instance of `SingleAgentWorkflowCallbacks`. If provided, these callbacks will be invoked at various stages of the workflow execution to allow for custom actions or logging. Internally, it sets up an empty list for `_input_history` and stores the provided agent and callbacks.

--------------------------------

### TracingProcessor

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/processor_interface

The `TracingProcessor` is an abstract base class that defines the interface for processing and monitoring traces and spans within the OpenAI Agents system. Any custom tracing processor must implement the methods defined in this interface. These processors are designed to receive notifications at various stages of trace and span lifecycles, such as when a trace or span starts or ends. This allows them to collect, process, and potentially export detailed tracing data, providing insights into the execution flow and performance of agents.

--------------------------------

### MCP Util > ToolFilter

Source: https://openai.github.io/openai-agents-python/ja/ref/mcp/util

ToolFilter can be one of three types: a ToolFilterCallable (a function), ToolFilterStatic (static configuration), or None (indicating no filtering). This provides flexibility in how tools are selected or excluded.

--------------------------------

### openai-agents-python/src/agents/tracing/create.py > response_span

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

Create a new response span. Similar to `mcp_tools_span`, this span is not started automatically and requires manual management with `with response_span() ...` or explicit `start()` and `finish()` calls. Key parameters are `response` for the OpenAI Response object, `span_id` for identification, `parent` to establish a hierarchical trace, and `disabled` to control recording.

--------------------------------

### Workflow > VoiceWorkflowBase > run

Source: https://openai.github.io/openai-agents-python/ko/ref/voice/workflow

Run the voice workflow. You will receive an input transcription, and must yield text that will be spoken to the user. You can run whatever logic you want here. In most cases, the final logic will involve calling `Runner.run_streamed()` and yielding any text events from the stream.

--------------------------------

### Handoff dataclass > tool_name instance-attribute

Source: https://openai.github.io/openai-agents-python/zh/ref/handoffs

The `tool_name` attribute specifies the name of the tool that will be used to represent this handoff operation. This name is crucial for the language model when it needs to decide to invoke a handoff, as it will identify the specific action to perform. For example, if an agent needs to transfer a request to a billing specialist, the `tool_name` might be something like `transfer_to_billing_agent`.

--------------------------------

### Quickstart > Prerequisites

Source: https://openai.github.io/openai-agents-python/realtime/quickstart

To begin using the Realtime Agents feature, ensure you have Python 3.9 or higher installed, an active OpenAI API key, and a foundational understanding of the OpenAI Agents SDK. These prerequisites are essential for setting up and running your realtime voice agent.

--------------------------------

### TracingProcessor

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/processor_interface

When implementing a `TracingProcessor`, it's crucial to adhere to certain guidelines to ensure the smooth operation of the agents. All methods within the processor must be thread-safe, as they can be invoked concurrently. Furthermore, these methods should avoid blocking for extended periods to prevent disruptions to agent execution. It is also important to handle any potential errors gracefully within the processor's methods, ensuring that exceptions do not propagate and halt the agent's workflow. The `shutdown` and `force_flush` methods are also part of the interface, providing mechanisms for resource cleanup and data flushing.

--------------------------------

### RealtimeModelConfig > url

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/model

The `url` parameter specifies the endpoint for connecting to the realtime model. If no URL is provided, a default URL is used. For example, the OpenAI Realtime model defaults to the standard OpenAI WebSocket URL.

--------------------------------

### Lifecycle > AgentHooksBase

Source: https://openai.github.io/openai-agents-python/ref/lifecycle

The `AgentHooksBase` class offers a mechanism to receive callbacks for lifecycle events related to a specific agent. This is particularly useful when you want to attach event handlers to an individual agent instance rather than globally for all runs. By setting an instance of a subclass of `AgentHooksBase` to an agent's `hooks` attribute (e.g., `agent.hooks = MyCustomAgentHooks()`), you can intercept events like the agent starting (`on_start`), ending (`on_end`), tool invocation (`on_tool_start`, `on_tool_end`), or LLM interactions (`on_llm_start`, `on_llm_end`).

--------------------------------

### DaprSession

Source: https://openai.github.io/openai-agents-python/zh/ref/extensions/memory/dapr_session

The `get_items` asynchronous method retrieves the conversation history associated with this session. You can optionally specify a `limit` to retrieve only the latest N items in chronological order. If `limit` is not provided or is `None`, all conversation history items will be retrieved. This method is useful for reconstructing past interactions or providing context for future responses. The conversation history is stored in a Dapr state store, and this method handles fetching and decoding the messages from that store.

--------------------------------

### AgentOutputSchema `dataclass`

Source: https://openai.github.io/openai-agents-python/ref/agent_output

The `AgentOutputSchema` class provides methods to interact with the output schema and validation. The `is_plain_text()` method checks if the defined output type is simply a string or None, indicating that no JSON schema is applicable. Conversely, `is_strict_json_schema()` returns whether the strict JSON schema mode is enabled. The `json_schema()` method returns the generated JSON schema for the output type, raising an error if the output is plain text. The `validate_json()` method takes a JSON string, validates it against the schema, and returns the parsed object. If the validation fails, it raises a `ModelBehaviorError` with details about the invalid JSON.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/zh/ref/model_settings

The `extra_headers` field allows you to add custom HTTP headers to the request. This can be necessary for authentication, specific service configurations, or other advanced use cases.

--------------------------------

### Agent Visualization > Customizing the Graph > Saving the Graph

Source: https://openai.github.io/openai-agents-python/visualization

By default, `draw_graph` displays the graph inline. To save it as a file, specify a filename:
```
draw_graph(triage_agent, filename="agent_graph")
```

This will generate `agent_graph.png` in the working directory.

--------------------------------

### Agent.as_tool

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

The `as_tool` method transforms an agent into a tool that can be invoked by other agents. This functionality differs from agent handoffs in two key aspects. Firstly, when an agent is handed off, it receives the entire conversation history. In contrast, when an agent is converted into a tool, it receives only the generated input for that specific tool invocation. Secondly, during a handoff, the new agent assumes control of the conversation. When acting as a tool, the agent is called within the context of the original agent, and the conversation continues to be managed by that original agent after the tool has completed its execution.

--------------------------------

### ToolGuardrailFunctionOutput dataclass > behavior class-attribute instance-attribute

Source: https://openai.github.io/openai-agents-python/ja/ref/tool_guardrails

The `behavior` attribute of `ToolGuardrailFunctionOutput` dictates the system's reaction to the guardrail's outcome. It can be configured using `AllowBehavior`, `RejectContentBehavior`, or `RaiseExceptionBehavior`. The default setting is `AllowBehavior`, meaning that by default, tool execution proceeds without interruption. Other options include rejecting content with a message or raising an exception to stop execution.

--------------------------------

### MCP Util > ToolFilterContext

Source: https://openai.github.io/openai-agents-python/ja/ref/mcp/util

ToolFilterContext provides context information to tool filter functions. This includes the current run context, the agent making the tool request, and the name of the MCP server.

--------------------------------

### DaprSession

Source: https://openai.github.io/openai-agents-python/ref/extensions/memory/dapr_session

The `_get_read_metadata` method is an internal helper function designed to retrieve metadata relevant for read operations. It constructs a dictionary that includes the specified consistency level for state operations. This is crucial for adhering to Dapr's state API requirements, where consistency can be passed via `state_metadata`. By incorporating the `_consistency` attribute, this method ensures that read requests are performed with the desired level of data consistency.

--------------------------------

### RealtimeRunner > __init__

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/runner

The `__init__` method initializes the realtime runner. It takes the `starting_agent` as a required argument, and optionally accepts a `model` and `config`. If no `model` is provided, it defaults to using `OpenAIRealtimeWebSocketModel()`. The `context` parameter is also mentioned as required in the description, although not explicitly in the method signature.

--------------------------------

### BatchTraceProcessor

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/processors

Data is ingested into the `BatchTraceProcessor` through its `on_trace_start` and `on_span_end` methods. When a trace starts or a span ends, these methods are called. They first ensure that the background worker thread is active by calling `_ensure_thread_started`. Then, they attempt to add the trace or span to the internal queue using `put_nowait` to avoid blocking. If the queue is full (`queue.Full` exception), a warning is logged, and the data is dropped. The `on_trace_end` and `on_span_start` methods are no-ops, as the processing logic is consolidated in the other two methods.

--------------------------------

### Agent Attributes > reset_tool_choice

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

Determines whether the tool choice is reset to its default after a tool has been invoked. The default value is True, which helps prevent the agent from entering an infinite loop of tool usage by ensuring a fresh tool selection process after each call.

--------------------------------

### FunctionTool `dataclass` > `strict_json_schema` `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ja/ref/tool

The `strict_json_schema` attribute, defaulting to `True`, enforces strict validation against the provided `params_json_schema`. When set to `True`, the `__post_init__` method ensures that the schema adheres to strict rules, which significantly improves the reliability of the JSON input received from the LLM. This is highly recommended to prevent parsing errors and ensure the tool receives correctly formatted arguments.

--------------------------------

### MCP Util > ToolFilterContext

Source: https://openai.github.io/openai-agents-python/zh/ref/mcp/util

ToolFilterContext provides context information to tool filter functions. It includes the current run context, the agent requesting the tool list, and the name of the MCP server. This data allows filter functions to make informed decisions about tool availability based on the operational environment.

--------------------------------

### VoicePipeline

Source: https://openai.github.io/openai-agents-python/ja/ref/voice/pipeline

The `_run_single_turn` method is designed for processing a single audio input. It utilizes a `TraceCtxManager` to handle the tracing lifecycle. Within this context, it transcribes the audio input to text, initializes a `StreamedAudioResult` with the TTS model and configuration, and then iterates through the text events generated by the workflow, adding them to the output stream.

--------------------------------

### SQLAlchemySession

Source: https://openai.github.io/openai-agents-python/ko/ref/extensions/memory/sqlalchemy_session

The `SQLAlchemySession` class provides a persistent memory backend for agents using SQLAlchemy. It allows conversations to be stored in a relational database, enabling persistence and retrieval of chat history. This implementation is built upon the `SessionABC` abstract base class, ensuring compatibility with the agent's memory management system. It supports asynchronous operations, making it suitable for modern Python applications. The session can be initialized with a pre-configured asynchronous SQLAlchemy engine, and optionally, it can automatically create the necessary database tables if they do not exist. This is particularly useful during development and testing phases.

--------------------------------

### Results > Other information > Guardrail results

Source: https://openai.github.io/openai-agents-python/results

The `input_guardrail_results` and `output_guardrail_results` properties provide access to the results of any guardrails applied during the run. These results might contain valuable information that you wish to log or store.

--------------------------------

### Results > Final output

Source: https://openai.github.io/openai-agents-python/results

The `final_output` property contains the final output of the last agent that ran. This is either a `str`, if the last agent didn't have an `output_type` defined, or an object of type `last_agent.output_type`, if the agent had an output type defined. `final_output` is of type `Any` because we can't statically type this due to potential handoffs between agents. If handoffs occur, any Agent might be the last agent, so the set of possible output types is not known statically.

--------------------------------

### Run context > AgentHookContext dataclass > usage class-attribute instance-attribute

Source: https://openai.github.io/openai-agents-python/ja/ref/run_context

The `usage` instance attribute in `AgentHookContext` tracks the agent run's usage, similar to `RunContextWrapper`. This information might be stale for streamed responses until the stream completes.

--------------------------------

### Spans

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

To handle errors within a span, the `set_error()` method should be utilized. This method allows you to record details about an exception that occurred during the span's execution. It's crucial to include a descriptive message and any relevant data that can help in debugging, while ensuring that sensitive information is not exposed. After setting the error, the exception should typically be re-raised to allow for further handling up the call stack.

--------------------------------

### Agent Class > `register_tool` Method > Streaming Execution (`on_stream`)

Source: https://openai.github.io/openai-agents-python/ref/agent

When `on_stream` is provided to the `register_tool` decorator, the nested agent is executed in streaming mode. This means that instead of waiting for the entire agent run to complete, you receive events as they are generated. The `on_stream` callback, which can be synchronous or asynchronous, receives an `AgentToolStreamEvent` object. This event contains the nested agent, the originating tool call (if available), and each stream event. Dispatching these events is handled in the background to prevent slow callback execution from blocking event consumption. The `dispatch_stream_events` function manages this process, putting events into a queue and executing user-defined handlers in a separate task.

--------------------------------

### RealtimeRunner > run

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/runner

The `run` method starts and returns a realtime session. This session object allows for bidirectional communication with the realtime model. An example demonstrates how to use it within an `async with` block, sending a message and then iterating through events received from the session.

--------------------------------

### Advanced SQLite Sessions > Conversation branching

Source: https://openai.github.io/openai-agents-python/sessions/advanced_sqlite_session

One of the key features of AdvancedSQLiteSession is the ability to create conversation branches from any user message, allowing you to explore alternative conversation paths.

--------------------------------

### to_input_items

Source: https://openai.github.io/openai-agents-python/ref/items

Convert the output into a list of input items suitable for passing to the model. The shape of the Pydantic output items are the same as the equivalent TypedDict input items, so they can be directly converted. This conversion is also verified through unit tests.

--------------------------------

### Model > RealtimePlaybackTracker > set_audio_format

Source: https://openai.github.io/openai-agents-python/ref/realtime/model

The `set_audio_format` method is called by the model to inform the `RealtimePlaybackTracker` about the audio format being used for playback. This information is stored in the `_format` attribute and is essential for accurately calculating audio lengths, particularly when using `on_play_bytes`.

--------------------------------

### SQLAlchemySession

Source: https://openai.github.io/openai-agents-python/zh/ref/extensions/memory/sqlalchemy_session

The `SQLAlchemySession` class supports constructing a session instance directly from a database URL string using the `from_url` class method. This method simplifies the setup process by allowing you to provide the connection details as a single URL. It also accepts optional `engine_kwargs` to further customize the SQLAlchemy engine configuration. This convenience constructor is particularly useful when you want to quickly set up a database connection without manually creating and configuring the `AsyncEngine` object.

--------------------------------

### Model > TTSModelSettings > voice

Source: https://openai.github.io/openai-agents-python/ref/voice/model

The `voice` attribute within TTSModelSettings specifies which voice to use for the Text-to-Speech (TTS) model. If no voice is explicitly provided, the TTS model will utilize its default voice setting. This allows for customization of the audio output's character.

--------------------------------

### SingleAgentVoiceWorkflow

Source: https://openai.github.io/openai-agents-python/zh/ref/voice/workflow

The `SingleAgentVoiceWorkflow` class provides a basic implementation for voice interactions using a single agent. It automatically appends each user transcription and the agent's response to an internal message history. This class is suitable for simple conversational flows. For more advanced use cases, such as employing multiple agents, managing message history differently, or incorporating custom logic and configurations, developers should create a subclass of `VoiceWorkflowBase` and define their own implementation.

--------------------------------

### Tracing Exporter > shutdown

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/processor_interface

The `shutdown` method is called when the application stops, and it's responsible for cleaning up any resources. This includes actions such as flushing queued traces and spans, closing connections, and releasing any other acquired resources. This ensures a clean exit and prevents resource leaks.

--------------------------------

### Agents > Agent

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

This lets you configure how tool use is handled. The default behavior is `run_llm_again`, where tools are run, and then the LLM receives the results and gets to respond. If you choose `stop_on_first_tool`, the output from the first tool call is treated as the final result and is not sent back to the LLM. You can also provide a `StopAtTools` object, which causes the agent to stop if any of the tools listed in `stop_at_tool_names` is called, with the final output being the result of the first matching tool call. Lastly, you can pass a function that will be called with the run context and tool results; this function must return a `ToolsToFinalOutputResult` to determine if the tool calls result in a final output. Note that this configuration is specific to FunctionTools; hosted tools are always processed by the LLM.

--------------------------------

### Session > clear_session

Source: https://openai.github.io/openai-agents-python/zh/ref/memory/session

The `clear_session` method provides a way to completely reset the conversation history for a session. This is useful for starting a new, independent conversation or when a user explicitly requests to clear the context.

--------------------------------

### BatchTraceProcessor

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/processors

The `BatchTraceProcessor` is designed to handle tracing data efficiently by processing it in batches. It employs a thread-safe `queue.Queue` to store incoming traces and spans. To avoid blocking the main application thread, a dedicated background thread is responsible for exporting these batched spans. This approach minimizes performance overhead, as the export operations are asynchronous. Spans are kept in memory within the queue until they are ready for export.

--------------------------------

### speech_group_span

Source: https://openai.github.io/openai-agents-python/ref/tracing

The `speech_group_span` function is used to create a new speech group span. This span is not automatically started; you must either use a `with` statement (e.g., `with speech_group_span() ...`) or manually call `span.start()` followed by `span.finish()`. The function accepts several parameters: `input` for the text used in the speech request, `span_id` for an optional span identifier (if not provided, one will be generated), `parent` to specify a parent trace or span (defaults to the current one), and `disabled` to prevent the span from being recorded if set to `True`.

--------------------------------

### SQLiteSession

Source: https://openai.github.io/openai-agents-python/ref/memory

This implementation stores conversation history in a SQLite database. By default, it uses an in-memory database that is lost when the process ends. For persistent storage, you should provide a file path for the database.

--------------------------------

### model_settings

Source: https://openai.github.io/openai-agents-python/ko/ref/run

Configure global model settings. Any non-null values will override the agent-specific model settings.

--------------------------------

### SQLiteSession

Source: https://openai.github.io/openai-agents-python/ja/ref/memory

The `SQLiteSession` class provides a SQLite-based implementation for session storage. This means it stores conversation history within a SQLite database. By default, it utilizes an in-memory database, which means the data is lost once the process terminates. For users who require persistent storage of conversation history, a file path can be provided to the constructor, ensuring the data is saved to a file and remains available across different process executions.

--------------------------------

### RunResult dataclass > raw_responses instance-attribute

Source: https://openai.github.io/openai-agents-python/ref/result

The `raw_responses` attribute stores a list of all the raw responses that were generated by the language model during the agent's run. These are the direct outputs from the LLM before any post-processing or interpretation by the agent's logic. This can be useful for debugging or for analyzing the model's behavior at a granular level.

--------------------------------

### VoicePipeline

Source: https://openai.github.io/openai-agents-python/ref/voice/pipeline

Internal helper methods like `_get_tts_model` and `_get_stt_model` are responsible for retrieving the appropriate text-to-speech and speech-to-text models. These methods ensure that a model instance is available, initializing it from the configuration if it hasn't been already. The `_process_audio_input` method takes an `AudioInput` object, retrieves the STT model, and then uses it to transcribe the audio into text, applying any specified STT settings and tracing configurations.

--------------------------------

### OpenAI Agents Python > trace_include_sensitive_data

Source: https://openai.github.io/openai-agents-python/ref/run

The `trace_include_sensitive_data` flag determines whether potentially sensitive information, such as inputs and outputs of tool calls or LLM generations, is included in the traces. When set to `False`, spans for these events are still created, but the sensitive data itself is omitted to enhance privacy and security.

--------------------------------

### Handoff dataclass > agent_name instance-attribute

Source: https://openai.github.io/openai-agents-python/ref/handoffs

The `agent_name` attribute stores the name of the specific agent to which the task is being handed off. This identifier is used to route the task to the correct specialized agent within the system.

--------------------------------

### OpenAI Agents Python > Tool Use Behavior

Source: https://openai.github.io/openai-agents-python/agents

The `tool_use_behavior` parameter in the `Agent` configuration dictates how tool outputs are processed. The default behavior, `'run_llm_again'`, involves running tools and then having the LLM process their results for a final response. Alternatively, `'stop_on_first_tool'` uses the output of the very first tool call as the final response, bypassing further LLM processing.

--------------------------------

### RealtimeModelConfig > url

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/model

The `url` specifies the connection endpoint. If this is not set, a default URL is used. For example, the OpenAI Realtime model defaults to the standard OpenAI WebSocket URL.

--------------------------------

### RealtimeModelConfig > url

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/model

The `url` option allows you to specify the connection URL for a realtime model. If no URL is provided, a default URL is used. For example, the OpenAI Realtime model utilizes its standard WebSocket URL.

--------------------------------

### RealtimePlaybackTracker > get_state

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/model

The `get_state` method is called by the model to retrieve the current playback status. It returns a `RealtimePlaybackState` dictionary containing the `current_item_id`, `current_item_content_index`, and `elapsed_ms`. If no audio is currently playing, all fields will be `None`.

--------------------------------

### Model > RealtimePlaybackTracker

Source: https://openai.github.io/openai-agents-python/ref/realtime/model

The `RealtimePlaybackTracker` class is designed for scenarios involving custom playback logic or when audio playback might be subject to delays or speed variations. Users are responsible for creating an instance of this class and passing it to the session. The tracker requires manual updates regarding audio playback progress through the `on_play_bytes` or `on_play_ms` methods, which should be called whenever a segment of audio has been played.

--------------------------------

### Sessions > How it works

Source: https://openai.github.io/openai-agents-python/sessions

When session memory is enabled:
  1. **Before each run** : The runner automatically retrieves the conversation history for the session and prepends it to the input items.
  2. **After each run** : All new items generated during the run (user input, assistant responses, tool calls, etc.) are automatically stored in the session.
  3. **Context preservation** : Each subsequent run with the same session includes the full conversation history, allowing the agent to maintain context.
This eliminates the need to manually call `.to_input_list()` and manage conversation state between runs.

--------------------------------

### OpenAI Agents Python/realtime/config.py/Tracing Configuration/group_id

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/config

The `group_id` is an instance attribute that provides a group identifier for tracing. This ID is used to link multiple traces together, allowing for easier analysis and correlation of events across different parts of a realtime model session or related operations.

--------------------------------

### Processor Interface > shutdown

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/processor_interface

The `shutdown` method is called when the application stops. It should perform any necessary cleanup operations, such as flushing queued traces or spans, closing connections, and releasing any acquired resources to ensure data integrity and prevent resource leaks.

--------------------------------

### TracingProcessor

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

The `TracingProcessor` is an abstract base class that defines the interface for processing and monitoring traces and spans within the OpenAI Agents system. Any custom tracing processor must implement this interface. Processors are designed to receive notifications at key points in the tracing lifecycle: when traces and spans begin and end. This allows them to actively collect, process, and potentially export the tracing data, providing insights into the execution flow and performance of agents.

--------------------------------

### Realtime Configuration > threshold

Source: https://openai.github.io/openai-agents-python/ref/realtime/config

The `threshold` attribute defines the threshold for voice activity detection, which is crucial for accurately identifying speech in realtime audio streams.

--------------------------------

### Tracing > Sensitive data

Source: https://openai.github.io/openai-agents-python/tracing

Certain spans may capture potentially sensitive data. The `generation_span()` stores the inputs/outputs of the LLM generation, and `function_span()` stores the inputs/outputs of function calls. These may contain sensitive data, so you can disable capturing that data via `RunConfig.trace_include_sensitive_data`. Similarly, Audio spans include base64-encoded PCM data for input and output audio by default. You can disable capturing this audio data by configuring `VoicePipelineConfig.trace_include_sensitive_audio_data`.

--------------------------------

### src/agents/tracing/create.py > get_current_span

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

Retrieves the currently active span. If there is an active span in the current context, this function will return it. Otherwise, it returns `None`.

--------------------------------

### openai_github_io_openai-agents-python > custom_span

Source: https://openai.github.io/openai-agents-python/ref/tracing/create

The `custom_span` function allows you to create a new custom span, to which you can add your own metadata. It's important to note that the span will not be started automatically. You need to either use a `with custom_span() ...` block or manually call `span.start()` followed by `span.finish()` to manage its lifecycle. This function accepts several parameters: `name` (required) for the span's identifier, `data` for arbitrary structured data, `span_id` (optional, with a recommendation to use `util.gen_span_id()` for proper formatting), `parent` to specify a parent trace or span (defaults to the current one), and `disabled` to prevent the span from being recorded. It returns a `Span[CustomSpanData]` object representing the newly created custom span.

--------------------------------

### AgentOutputSchema dataclass

Source: https://openai.github.io/openai-agents-python/ja/ref/agent_output

The `AgentOutputSchema` class provides methods to interact with the output schema and validated data. The `is_plain_text` method checks if the output is intended to be simple text rather than a structured JSON object. The `is_strict_json_schema` method returns the status of the strict JSON schema mode. The `json_schema` method returns the generated JSON schema for the output type; it raises an error if the output type is plain text, as no schema is applicable in that case. Finally, the `validate_json` method takes a JSON string, validates it against the defined output type using the internal type adapter, and returns the validated object. If the JSON is invalid or does not conform to the expected structure (especially if wrapping was applied), it raises a `ModelBehaviorError`.

--------------------------------

### openai-agents-python/create.py > custom_span

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/create

The `custom_span` function allows you to create a new custom span to which you can add your own metadata. This span does not start automatically. You must either use a `with custom_span() ...` block or manually call `span.start()` followed by `span.finish()` to manage its lifecycle. The function accepts several parameters, including `name` (required) for the span's identifier, `data` for arbitrary structured metadata, `span_id` for an optional specific ID (or it will be generated), `parent` to link it to an existing trace or span (or it will automatically use the current context), and `disabled` to prevent the span from being recorded if set to `True`.

--------------------------------

### BatchTraceProcessor

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/processors

The `BatchTraceProcessor` is designed for efficient handling of tracing data by batching operations. It utilizes a `queue.Queue` for thread-safe storage of spans and traces, ensuring that concurrent operations do not corrupt the data. To prevent performance degradation, a dedicated background thread is employed to manage the export of these batched spans. This asynchronous approach allows the main application thread to continue its work without being blocked by the export process. Spans are held in memory within the queue until they are ready for export.

--------------------------------

### OpenAIVoiceModelProvider > OpenAIVoiceModelProvider

Source: https://openai.github.io/openai-agents-python/zh/ref/voice/models/openai_provider

The `OpenAIVoiceModelProvider` class is a concrete implementation of `VoiceModelProvider` that leverages OpenAI's models for speech-related tasks. It allows for the integration of OpenAI's speech-to-text (STT) and text-to-speech (TTS) capabilities into your applications.

The provider can be initialized in a few ways:

*   **Using an existing `AsyncOpenAI` client:** If you already have an `AsyncOpenAI` client instance configured, you can pass it directly to the `OpenAIVoiceModelProvider` constructor. This is useful if you are managing the OpenAI client's lifecycle elsewhere.
*   **Providing API key and other credentials:** Alternatively, you can initialize the provider by supplying your OpenAI API key, base URL, organization, and project. If you don't provide these, the provider will attempt to use default credentials.

--------------------------------

### Source code in src/agents/tracing/create.py

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/create

The `function_span` function is used to create a new function span for tracing purposes. It's important to note that this span is not started automatically. You need to explicitly start and finish it either by using a `with` statement (e.g., `with function_span() ...`) or by manually calling `span.start()` and `span.finish()` methods. The function accepts several parameters to define the span, including its `name`, `input`, and `output`. An optional `span_id` can be provided, or one will be generated. You can also specify a `parent` span or trace, and a `disabled` flag to prevent recording the span. The function returns a `Span` object, specifically a `Span[FunctionSpanData]`, which represents the newly created function span.

--------------------------------

### OpenAI Agents Python/realtime/config.py/User Input Types/RealtimeUserInputText/type

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/config

The `type` attribute for `RealtimeUserInputText` is an instance attribute that serves as a type identifier, specifically set to 'input_text'. This clearly distinguishes this input type from other potential user input formats.

--------------------------------

### Source code in src/agents/tracing/traces.py

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/traces

The `export` method is intended to export the trace data as a dictionary. However, for the `NoOpTrace` implementation, which is used when tracing is disabled, this method always returns `None`. This signifies that there is no trace data to export because no operations were recorded.

--------------------------------

### Runner

Source: https://openai.github.io/openai-agents-python/ja/ref/run

The `Runner.run` method accepts several parameters to control the execution of an agent workflow. These include the `starting_agent` and the initial `input`. Optional parameters allow for specifying the `context`, setting a `max_turns` limit, providing `hooks` for lifecycle event callbacks, configuring global `run_config` settings, and managing `previous_response_id` and `auto_previous_response_id` for seamless continuation of conversations, particularly when using OpenAI's Responses API. Additionally, a `conversation_id` can be provided to utilize OpenAI's conversation state management, allowing agents to access and write to conversation history. A `session` object can also be passed for automatic conversation history management.

--------------------------------

### Sessions > Session types > SQLAlchemy sessions

Source: https://openai.github.io/openai-agents-python/sessions

Production-ready sessions can be implemented using any SQLAlchemy-supported database. The `SQLAlchemySession` class allows you to connect to various database backends, such as PostgreSQL, MySQL, or others, by providing a database URL. This offers robust and scalable solutions for managing conversation history in production environments. You can also configure it to automatically create the necessary tables if they don't exist.

--------------------------------

### MultiProvider

Source: https://openai.github.io/openai-agents-python/ref/models/multi_provider

The `get_model` method within `MultiProvider` is responsible for determining the appropriate `ModelProvider` and retrieving the requested `Model`. It first parses the `model_name` to extract any prefix. If a prefix is present and a custom `provider_map` has been configured, it attempts to find a provider associated with that prefix in the map. If no custom provider is found or if no prefix is used, it falls back to a default provider lookup. This fallback mechanism ensures that either the `OpenAIProvider` (for "openai/" or no prefix) or a dynamically created provider for other prefixes (like "litellm") is used to obtain the `Model`.

--------------------------------

### SQLiteSession

Source: https://openai.github.io/openai-agents-python/ref/memory/sqlite_session

This implementation stores conversation history in a SQLite database. By default, it uses an in-memory database that is lost when the process ends. For persistent storage, you can provide a file path.

--------------------------------

### openai-agents-python/agents.py > Agent class > get_conversation_turns

Source: https://openai.github.io/openai-agents-python/ref/extensions/memory/advanced_sqlite_session

The `get_conversation_turns` method provides a way to retrieve a list of user messages within a specific branch. It queries the database for messages of type 'user', ordered by their turn number within the branch. For each turn, it extracts the user's message content, providing both a truncated preview and the full content. This information is valuable for user interfaces that display conversation history or for implementing branching logic based on previous user inputs.

--------------------------------

### Agents > Output types

Source: https://openai.github.io/openai-agents-python/agents

By default, agents produce plain text (i.e. `str`) outputs. If you want the agent to produce a particular type of output, you can use the `output_type` parameter. A common choice is to use Pydantic objects, but we support any type that can be wrapped in a Pydantic TypeAdapter - dataclasses, lists, TypedDict, etc.

When you pass an `output_type`, that tells the model to use structured outputs instead of regular plain text responses.

--------------------------------

### run `async` `classmethod`

Source: https://openai.github.io/openai-agents-python/ko/ref/run

The `run` class method initiates a workflow starting with a specified agent. This process involves a loop where the agent is invoked with the provided input. The loop continues until a final output is produced, as indicated by the agent's `output_type`. If the agent performs a handoff to another agent, the loop restarts with the new agent. Otherwise, if tool calls are involved, they are executed, and the loop continues. The execution can be terminated prematurely if the `max_turns` limit is reached, resulting in a `MaxTurnsExceeded` exception, or if a guardrail tripwire is activated, raising a `GuardrailTripwireTriggered` exception. It's important to note that guardrails are only applied to the initial agent's input.

--------------------------------

### speech_group_span

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `speech_group_span` function is used to create a new speech group span. It's important to note that the span is not automatically started. You need to either use a `with` statement, like `with speech_group_span() ...`, or manually call `span.start()` followed by `span.finish()`.

The function accepts several parameters:
- `input`: The text that will be used for the speech request. It's an optional string.
- `span_id`: An optional string to identify the span. If not provided, an ID will be generated. It's recommended to use `util.gen_span_id()` for correctly formatted IDs.
- `parent`: An optional `Trace` or `Span` object to define the parent of this span. If omitted, the current trace or span will be used as the parent.
- `disabled`: A boolean flag. If set to `True`, a `Span` object will be returned, but it will not be recorded.

--------------------------------

### Agent Class > Methods > as_tool

Source: https://openai.github.io/openai-agents-python/ko/ref/agent

The `as_tool` method transforms an `Agent` instance into a `Tool` that can be invoked by other agents. This process differs from agent handoffs in two key aspects. Firstly, when an agent is converted to a tool, it receives generated input directly, whereas in a handoff, the new agent inherits the conversation history. Secondly, when acting as a tool, the agent is called as a discrete unit, and the conversation's continuation is managed by the original agent that invoked the tool. This method allows for customization of the tool's name, description, and output extraction, among other parameters.

--------------------------------

### SQLAlchemySession

Source: https://openai.github.io/openai-agents-python/ko/ref/extensions/memory/sqlalchemy_session

For convenience, `SQLAlchemySession` offers a class method `from_url` that allows for session initialization directly from a database connection URL string. This simplifies the setup process by abstracting away the explicit creation of the SQLAlchemy engine. The provided URL should be a valid SQLAlchemy asynchronous URL, such as `postgresql+asyncpg://user:pass@host/db`. This method also accepts `engine_kwargs` for further customization of the engine's behavior and `**kwargs` to pass additional arguments to the `SQLAlchemySession` constructor.

--------------------------------

### RealtimeSession

Source: https://openai.github.io/openai-agents-python/ref/realtime/session

To establish and utilize a `RealtimeSession`, you can employ the `RealtimeRunner`. The `runner.run()` method returns an `async` context manager, through which the `session` object is made available. Within this context, you can send messages using `session.send_message()` and audio data with `session.send_audio()`. Furthermore, you can iterate over the `session` object asynchronously to receive and process events streamed from the model, such as audio data, by checking the `event.type`.

--------------------------------

### VoicePipeline

Source: https://openai.github.io/openai-agents-python/zh/ref/voice/pipeline

The `VoicePipeline` class can be initialized with a `workflow`, and optionally, speech-to-text (`stt_model`) and text-to-speech (`tts_model`) models. If the `stt_model` or `tts_model` are not explicitly provided, the pipeline will default to using OpenAI's standard models. A `config` object can also be supplied to customize the pipeline's behavior; otherwise, a default configuration is applied. The `workflow` argument is mandatory and should be an instance of `VoiceWorkflowBase`.

--------------------------------

### to_input_item

Source: https://openai.github.io/openai-agents-python/ko/ref/items

The `to_input_item` method converts the tool output into an input item for the next model turn. It handles stripping the `status` field from hosted tool outputs, which is used for SDK bookkeeping but not accepted by the Responses API. The original raw item is kept intact.

--------------------------------

### OpenAI Agents Python API Reference > is_enabled

Source: https://openai.github.io/openai-agents-python/ja/ref/handoffs

Whether the handoff is enabled. Either a bool or a callable that takes the run context and agent and returns whether the handoff is enabled. You can use this to dynamically enable or disable a handoff based on your context or state.

--------------------------------

### Creating traces/spans > get_current_trace

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/create

The `get_current_trace()` function returns the currently active trace, if one exists. This is useful for accessing trace information within the current execution context, such as adding spans or metadata to an ongoing trace.

--------------------------------

### Session Memory

Source: https://openai.github.io/openai-agents-python/sessions

Session memory allows an agent to remember previous messages in a conversation, enabling more coherent and context-aware interactions. The `agents` library provides built-in session implementations, such as `SQLiteSession`, which persists conversation history to a SQLite database. When using a `session` object with the `Runner.run` method, the agent automatically loads past messages and saves new ones, maintaining context across multiple turns of a conversation.

--------------------------------

### AgentOutputSchema `dataclass`

Source: https://openai.github.io/openai-agents-python/zh/ref/agent_output

The `AgentOutputSchema` dataclass is designed to manage the JSON schema of an agent's output. It not only captures this schema but also handles the crucial tasks of validating and parsing JSON data generated by a Large Language Model (LLM) into the expected output type. This ensures that the output conforms to a predefined structure and can be reliably used by downstream processes. The class is initialized with the desired `output_type` and an optional `strict_json_schema` flag, which is strongly recommended to be set to `True` to enhance the accuracy of JSON input. Internally, it determines whether the output type needs to be wrapped in a dictionary to be representable as a JSON Schema object. This wrapping is typically applied to types that are not plain text or cannot inherently be represented as a JSON Schema object. The class provides methods to check if the output is plain text, if strict JSON schema validation is enabled, and to retrieve the generated JSON schema itself.

--------------------------------

### FunctionTool `dataclass` > `is_enabled` `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ja/ref/tool

The `is_enabled` attribute provides a mechanism to dynamically control whether a tool is available for use. It can be set to a boolean value (`True` or `False`) for static enablement, or it can be a callable. This callable receives the current run context and the agent instance, and should return a boolean indicating whether the tool should be enabled in the current situation. This allows for context-aware tool activation and deactivation.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

Frequency and presence penalties (`frequency_penalty` and `presence_penalty`) are used to discourage the model from repeating itself. The `frequency_penalty` reduces the likelihood of a token appearing again based on how often it has already appeared, while the `presence_penalty` does so based on whether the token has appeared at all.

--------------------------------

### Model Settings > parallel_tool_calls

Source: https://openai.github.io/openai-agents-python/ref/model_settings

Controls whether the model can make multiple parallel tool calls in a single turn. If not provided (i.e., set to None), this behavior defers to the underlying model provider's default. For most current providers (e.g., OpenAI), this typically means parallel tool calls are enabled (True). Set to True to explicitly enable parallel tool calls, or False to restrict the model to at most one tool call per turn.

--------------------------------

### RealtimeAgent > hooks

Source: https://openai.github.io/openai-agents-python/ref/realtime/agent

The `hooks` parameter provides a way to integrate callback functions that are triggered at various stages of the `RealtimeAgent`'s lifecycle. This allows for custom logic to be executed during agent initialization, execution, or completion, enabling fine-grained control and monitoring of agent behavior.

--------------------------------

### Model > RealtimePlaybackTracker

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/model

The `RealtimePlaybackTracker` class is designed for scenarios with custom playback logic, delays, or variable audio speeds. When using this class, you are responsible for monitoring the audio playback progress. You need to explicitly call `on_play_bytes` or `on_play_ms` to inform the system about the amount of audio that has been played by the user. This ensures accurate tracking of playback state even in non-standard playback environments.

--------------------------------

### Models > Non-OpenAI models > Other ways to use non-OpenAI models

Source: https://openai.github.io/openai-agents-python/models

If you do not have an API key from `platform.openai.com`, it is recommended to disable tracing using `set_tracing_disabled()` or to configure an alternative tracing processor. In many examples, the Chat Completions API/model is used because most LLM providers currently lack support for the Responses API. However, if your LLM provider supports it, using the Responses API is recommended.

--------------------------------

### Model > RealtimePlaybackTracker > on_play_bytes

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/model

The `on_play_bytes` method within `RealtimePlaybackTracker` should be invoked when a specific amount of audio data (in bytes) has been successfully played. It takes the `item_id`, `item_content_index`, and the `bytes` of audio played. Internally, it calculates the duration in milliseconds using `calculate_audio_length_ms` based on the provided audio format and then calls `on_play_ms` to update the playback state.

--------------------------------

### Streaming nested agent runs

Source: https://openai.github.io/openai-agents-python/tools

Pass an `on_stream` callback to `as_tool` to listen to streaming events emitted by the nested agent while still returning its final output once the stream completes.
Event types mirror `StreamEvent["type"]`: `raw_response_event`, `run_item_stream_event`, `agent_updated_stream_event`.
Providing `on_stream` automatically runs the nested agent in streaming mode and drains the stream before returning the final output.
The handler may be synchronous or asynchronous; each event is delivered in order as it arrives.
`tool_call_id` is present when the tool is invoked via a model tool call; direct calls may leave it `None`.

--------------------------------

### Agent Attributes > model

Source: https://openai.github.io/openai-agents-python/ref/agent

The `model` attribute specifies which language model implementation should be used for the agent's operations. If this attribute is not explicitly set, the agent will default to using the model configured in `agents.models.get_default_model()`, which is currently set to 'gpt-4.1'. This allows for easy configuration and overriding of the default LLM.

--------------------------------

### RealtimeAgent > hooks

Source: https://openai.github.io/openai-agents-python/ref/realtime/agent

The `hooks` attribute provides a mechanism to receive callbacks during various stages of an agent's lifecycle. This allows for custom logic to be executed at specific events.

--------------------------------

### TracingProcessor

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/processor_interface

Implementing a custom `TracingProcessor` involves defining how to handle lifecycle events for traces and spans. For instance, a custom processor might store active traces and spans in dictionaries, process completed traces and spans by removing them from active collections, and perform cleanup operations during `shutdown`. The `force_flush` method can be implemented to ensure any queued processing tasks are completed. Crucially, all methods within a custom processor must be thread-safe, avoid long blocking operations, and handle errors gracefully to prevent disruption to the agent's execution.

--------------------------------

### VoicePipeline > _run_single_turn

Source: https://openai.github.io/openai-agents-python/ko/ref/voice/pipeline

The `_run_single_turn` method is an internal implementation for processing a single, non-streaming audio input. It leverages a `TraceCtxManager` to handle the lifecycle of a trace, ensuring that tracing is properly initiated and concluded. The audio input is first transcribed into text using `_process_audio_input`. Then, a `StreamedAudioResult` object is prepared to handle the output. The transcribed text is fed into the `self.workflow.run` method, and each resulting text event is added to the `StreamedAudioResult`. Once the workflow is complete, `_turn_done` and `_done` are called on the output object.

--------------------------------

### RunResult dataclass > raw_responses instance-attribute

Source: https://openai.github.io/openai-agents-python/ko/ref/result

The `raw_responses` attribute holds a list of all the raw responses generated directly by the language model (LLM) during the agent's execution. These are the immediate outputs from the LLM before any further processing, filtering, or formatting is applied by the agent's logic. Examining these raw responses can be helpful for debugging or understanding the LLM's internal thought process.

--------------------------------

### Span > ended_at

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/spans

The `ended_at` property returns the ISO format timestamp indicating when the span finished execution. It returns `None` if the span has not yet finished.

--------------------------------

### Source code in src/agents/tracing/traces.py

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/traces

The `export` method for the `NoOpTrace` class is designed to return `None`. This signifies that when tracing is disabled, there is no trace data to export. It adheres to the `Trace` interface by providing an `export` method but indicates the absence of any recorded information.

--------------------------------

### OpenAI Agents Python > run_sync

Source: https://openai.github.io/openai-agents-python/ko/ref/run

The `run_sync` method accepts several parameters to configure the agent execution. The `starting_agent` and `input` are mandatory, defining the initial agent and the first piece of data. Optional parameters include `context` for carrying state across turns, `max_turns` to limit the number of execution cycles, and `hooks` for monitoring lifecycle events. `run_config` provides global settings, `previous_response_id` and `auto_previous_response_id` help manage conversation history with OpenAI's Responses API, and `conversation_id` and `session` are used for automatic conversation history management.

--------------------------------

### src/agents/tracing/create.py > get_current_span

Source: https://openai.github.io/openai-agents-python/ref/tracing

Retrieves the currently active span. If there is no span currently in progress, this function will return `None`. This is useful for inspecting or interacting with the span that is currently being executed within the trace.

--------------------------------

### Input > StreamedAudioInput

Source: https://openai.github.io/openai-agents-python/zh/ref/voice/input

`StreamedAudioInput` represents audio input as a stream. You can pass this to the `VoicePipeline` and then add audio data incrementally using the `add_audio` method. This is useful for real-time audio processing where data arrives over time.

--------------------------------

### Automatic conversation management with Sessions

Source: https://openai.github.io/openai-agents-python/running_agents

Sessions provide an automatic way to manage conversation history without manually calling `.to_input_list()`. When using Sessions, the SDK automatically retrieves the conversation history before each run and stores new messages after each run. This ensures that the agent maintains context across multiple turns, and it can handle separate conversations for different session IDs.

--------------------------------

### Results > RunResultBase dataclass

Source: https://openai.github.io/openai-agents-python/ko/ref/result

The `RunResultBase` class includes utility methods for data transformation. The `to_input_list` method is designed to create a comprehensive list of input items by merging the original `input` with all `new_items` generated during the agent's execution. Each `new_item` is converted into an input item format. Furthermore, the `last_response_id` property provides a quick way to retrieve the identifier of the most recent model response, returning `None` if no responses were recorded.

--------------------------------

### Input > AudioInput > to_audio_file

Source: https://openai.github.io/openai-agents-python/zh/ref/voice/input

The `to_audio_file` method of `AudioInput` allows you to convert the audio data into a format suitable for saving as an audio file. It returns a tuple containing the filename, the audio data as bytes, and the content type.

--------------------------------

### Agent Attributes > mcp_config

Source: https://openai.github.io/openai-agents-python/ko/ref/agent

This attribute holds the configuration settings for the MCP servers used by the agent. It is initialized with a default `MCPConfig` if no specific configuration is provided.

--------------------------------

### openai-agents-python/src/agents/realtime/config.py > playback_tracker

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/config

The playback tracker to use when tracking audio playback progress. If not set, the model will use a default implementation that assumes audio is played immediately, at realtime speed. A playback tracker is useful for interruptions. The model generates audio much faster than realtime playback speed. So if there's an interruption, its useful for the model to know how much of the audio has been played by the user. In low-latency scenarios, it's fine to assume that audio is played back immediately at realtime speed. But in scenarios like phone calls or other remote interactions, you can set a playback tracker that lets the model know when audio is played to the user.

--------------------------------

### Function schema > FuncSchema dataclass > takes_context class-attribute instance-attribute

Source: https://openai.github.io/openai-agents-python/zh/ref/function_schema

The `takes_context` attribute is a boolean flag, defaulting to `False`. If set to `True`, it indicates that the function expects a `RunContextWrapper` object as its first argument. This allows functions to access runtime context information.

--------------------------------

### AgentOutputSchema `dataclass`

Source: https://openai.github.io/openai-agents-python/ref/agent_output

The `AgentOutputSchema` dataclass is designed to manage the structure and validation of output generated by language models. It captures the JSON schema of the expected output and uses this schema to validate and parse JSON data produced by the LLM. This ensures that the output conforms to a predefined structure and type, making it easier to work with programmatically.

The class supports both plain text outputs and structured JSON outputs. For structured outputs, it generates a JSON schema based on the provided Python type. It also includes an option to enforce a strict JSON schema, which is highly recommended for improving the accuracy of the generated JSON. If the output type is not inherently JSON serializable or would not naturally form a JSON object, `AgentOutputSchema` can wrap it in a dictionary to ensure compatibility with JSON schema standards.

--------------------------------

### BatchTraceProcessor

Source: https://openai.github.io/openai-agents-python/ref/tracing/processors

The `BatchTraceProcessor` class is initialized with several parameters to control its batching and exporting behavior.

*   `exporter`: The `TracingExporter` instance responsible for sending the batched data.
*   `max_queue_size`: The maximum number of spans that can be held in the internal queue. If the queue reaches this capacity, incoming spans will be dropped.
*   `max_batch_size`: The maximum number of spans to include in a single export batch.
*   `schedule_delay`: The interval in seconds at which the background thread checks for spans to export, even if the batch is not full.
*   `export_trigger_ratio`: A threshold (as a ratio of `max_queue_size`) that, when reached by the queue size, triggers an immediate export.

--------------------------------

### Handoffs > Customizing handoffs via the `handoff()` function

Source: https://openai.github.io/openai-agents-python/handoffs

The `handoff()` function lets you customize things. You can override the `agent`, `tool_name_override`, `tool_description_override`, specify a callback function for `on_handoff` which is executed when the handoff is invoked, define the `input_type`, set an `input_filter` to filter input to the next agent, and control `is_enabled` status.

--------------------------------

### TracingProcessor

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/processor_interface

The `TracingProcessor` is an abstract class that defines the interface for processing and monitoring traces and spans within the OpenAI Agents system. Any custom tracing processor must implement this interface. Processors are designed to receive notifications at key events in the lifecycle of traces and spans, specifically when they start and end. This allows them to collect, process, and export tracing data as needed. The interface includes methods like `on_trace_start`, `on_trace_end`, `on_span_start`, and `on_span_end`, which custom implementations will override to define their specific behavior.

--------------------------------

### Advanced SQLite sessions

Source: https://openai.github.io/openai-agents-python/sessions

Enhanced SQLite sessions offer advanced features for managing conversations. These sessions provide capabilities such as conversation branching, which allows you to diverge from a specific point in a conversation to explore alternative paths. Additionally, they include usage analytics to track token consumption and structured queries for more organized data retrieval. This makes them suitable for complex conversational applications requiring detailed insights and control over conversation flow.

--------------------------------

### Model > RealtimePlaybackTracker > on_play_bytes

Source: https://openai.github.io/openai-agents-python/ref/realtime/model

The `on_play_bytes` method in `RealtimePlaybackTracker` is invoked to report that a specific chunk of audio has been played. It takes the `item_id`, `item_content_index`, and the `bytes` of audio that were played. Internally, it calculates the duration of the played audio in milliseconds using `calculate_audio_length_ms` and then calls `on_play_ms` to update the playback state.

--------------------------------

### speech_group_span

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

The `speech_group_span` function creates a new speech group span. This span is not automatically started; you must either use a `with` statement (e.g., `with speech_group_span() ...`) or manually call `span.start()` followed by `span.finish()`. The function accepts several parameters: `input` for the speech request text, `span_id` for an optional span identifier (it's recommended to generate this using `util.gen_span_id()` for correct formatting), `parent` to specify a parent trace or span (defaults to the current trace/span if not provided), and `disabled` (a boolean that, if `True`, prevents the span from being recorded.

--------------------------------

### SQLAlchemySession > from_url

Source: https://openai.github.io/openai-agents-python/ref/extensions/memory/sqlalchemy_session

The `from_url` class method provides a convenient way to initialize `SQLAlchemySession` by directly specifying a SQLAlchemy database URL string. This method handles the creation of the `AsyncEngine` from the provided URL, simplifying the setup process when you have a database connection string readily available. It accepts the `session_id`, the database `url`, optional `engine_kwargs` for fine-tuning the engine configuration, and any other keyword arguments that are passed directly to the `SQLAlchemySession` constructor.

--------------------------------

### RunResult dataclass

Source: https://openai.github.io/openai-agents-python/ja/ref/result

The `RunResult` dataclass inherits from `RunResultBase` and provides a comprehensive structure to hold the results of an agent's execution. It includes attributes for the last agent run, references to agents, and various types of guardrail results. The `RunResult` also offers methods to manage agent references and retrieve information like the last agent's ID.

--------------------------------

### VoicePipeline

Source: https://openai.github.io/openai-agents-python/ref/voice/pipeline

The `VoicePipeline` is initialized with a `workflow` object, which defines the agent's behavior. Optional parameters include `stt_model` for speech-to-text and `tts_model` for text-to-speech. If these models are not explicitly provided, the pipeline will use default OpenAI models configured through `config.model_provider`. A `config` object can also be passed to customize various aspects of the pipeline's operation, such as transcription and synthesis settings, and tracing options. If no configuration is provided, a default `VoicePipelineConfig` is used.

--------------------------------

### ModelSettings > parallel_tool_calls

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

Controls whether the model can make multiple parallel tool calls in a single turn. If not provided (i.e., set to None), this behavior defers to the underlying model provider's default. For most current providers (e.g., OpenAI), this typically means parallel tool calls are enabled (True). Set to True to explicitly enable parallel tool calls, or False to restrict the model to at most one tool call per turn.

--------------------------------

### mcp_tools_span

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/create

Create a new MCP list tools span. The span will not be started automatically, you should either do `with mcp_tools_span() ...` or call `span.start()` + `span.finish()` manually.

Parameters:
`server`: The name of the MCP server.
`result`: The result of the MCP list tools call.
`span_id`: The ID of the span. Optional. If not provided, we will generate an ID. We recommend using `util.gen_span_id()` to generate a span ID, to guarantee that IDs are correctly formatted.
`parent`: The parent span or trace. If not provided, we will automatically use the current trace/span as the parent.
`disabled`: If True, we will return a Span but the Span will not be recorded.

--------------------------------

### Mixing and matching models

Source: https://openai.github.io/openai-agents-python/models

Also, when you use OpenAI's Responses API, there are a few other optional parameters (e.g., `user`, `service_tier`, and so on). If they are not available at the top level, you can use `extra_args` to pass them as well.

--------------------------------

### `RealtimeSession`

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/session

The `RealtimeSession` class represents a connection to a realtime model. It facilitates bidirectional communication, allowing you to stream events from the model and send messages or audio to it. This class inherits from `RealtimeModelListener`, suggesting it can listen for and process model-generated events.

--------------------------------

### RealtimePlaybackTracker > set_audio_format

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/model

The `set_audio_format` method is used by the model to communicate the audio format being used for playback to the `RealtimePlaybackTracker`. This information is crucial for accurately calculating the duration of audio data when reported in bytes, enabling precise time tracking.

--------------------------------

### TracingProcessor

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

The `TracingProcessor` is an abstract class that defines the interface for processing and monitoring traces and spans within the OpenAI Agents system. Any custom tracing processor must implement this interface. Processors are notified when traces and spans begin and end, which allows them to collect, process, and export tracing data. Implementing classes should ensure their methods are thread-safe, do not block for extended periods, and handle errors gracefully to avoid interrupting the agent's execution. An example `CustomProcessor` demonstrates how to track active traces and spans, process completed traces and spans, and manage resources during shutdown and flushing.

--------------------------------

### SQLiteSession

Source: https://openai.github.io/openai-agents-python/zh/ref/memory/sqlite_session

This implementation stores conversation history in a SQLite database. By default, it uses an in-memory database that is lost when the process ends. For persistent storage, you can provide a file path to the database.

--------------------------------

### MCP Util > ToolFilterStatic

Source: https://openai.github.io/openai-agents-python/zh/ref/mcp/util

ToolFilterStatic defines a static configuration for filtering tools using allowlists and blocklists. It allows specifying `allowed_tool_names` to whitelist specific tools, ensuring only those listed are available. Alternatively, `blocked_tool_names` can be used to blacklist certain tools, filtering them out from the available set. This provides a straightforward way to manage tool access without complex logic.

--------------------------------

### SQLAlchemySession

Source: https://openai.github.io/openai-agents-python/ko/ref/extensions/memory/sqlalchemy_session

The `SQLAlchemySession` can be initialized directly with an asynchronous SQLAlchemy engine. The engine must be configured to use an asynchronous driver, such as `postgresql+asyncpg`, `mysql+aiomysql`, or `sqlite+aiosqlite`. Additionally, users can specify whether to automatically create the required database tables and indexes by setting the `create_tables` parameter to `True`. This is a convenient option for development environments where manual schema management might not be desired. The table names for sessions and messages can also be customized using the `sessions_table` and `messages_table` arguments, respectively, providing flexibility in database schema design.

--------------------------------

### Conditional tool enabling

Source: https://openai.github.io/openai-agents-python/tools

You can conditionally enable or disable agent tools at runtime using the `is_enabled` parameter. This allows you to dynamically filter which tools are available to the LLM based on context, user preferences, or runtime conditions.

--------------------------------

### MultiProvider

Source: https://openai.github.io/openai-agents-python/zh/ref/models/multi_provider

The `get_model` method in `MultiProvider` is responsible for retrieving the appropriate `Model` based on the provided model name. It first parses the model name to extract any prefix. If a prefix is present and a custom provider mapping exists for that prefix, the request is delegated to the corresponding provider. Otherwise, it falls back to using either the default `OpenAIProvider` (if the prefix is "openai" or absent) or a dynamically created fallback provider for other prefixes. This mechanism ensures that models are correctly routed based on their naming conventions.

--------------------------------

### Agent Attributes > hooks

Source: https://openai.github.io/openai-agents-python/ref/agent

The `hooks` attribute allows for integration with various lifecycle events of an agent. By providing an `AgentHooks` instance, you can define callback functions that are triggered at specific points during the agent's execution, such as initialization, before/after execution, or during error handling. This facilitates custom monitoring, logging, or modification of agent behavior.

--------------------------------

### RunConfig `dataclass` > handoff_history_mapper `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/zh/ref/run

The `handoff_history_mapper` attribute provides an optional function that can be used to map the normalized transcript (including history and handoff items) to the input history that should be passed to the next agent. This function is only executed when `nest_handoff_history` is `True`. If `handoff_history_mapper` is `None`, the runner defaults to collapsing the transcript into a single assistant message, similar to the behavior when `nest_handoff_history` is `True` and no custom mapper is provided.

--------------------------------

### Handoff dataclass

Source: https://openai.github.io/openai-agents-python/zh/ref/handoffs

A `Handoff` is a mechanism by which one agent can delegate a task to another agent within the system. This is particularly useful for creating complex agentic workflows where different agents specialize in distinct areas. For instance, in a customer support application, a primary 'triage agent' could analyze an incoming user request and then decide to hand off the task to a specialized sub-agent. These sub-agents could be designed for specific functions such as handling billing inquiries, managing account details, or providing technical support. The `Handoff` class itself is a dataclass that encapsulates the details necessary for this delegation process.

--------------------------------

### Trace Class > trace_id

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/traces

The `trace_id` property provides the unique identifier for a trace. This ID is a string formatted as 'trace_<32_alphanumeric>' and is globally unique. It is crucial for linking spans to their parent trace and can be used to look up specific traces in the dashboard.

--------------------------------

### BatchTraceProcessor

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/processors

The `BatchTraceProcessor` constructor initializes several key parameters: `exporter` is the `TracingExporter` responsible for sending the data, `max_queue_size` limits the number of spans/traces held in memory before dropping new ones, `max_batch_size` defines the maximum number of items in a single export batch, `schedule_delay` sets the interval for checking the queue for export, and `export_trigger_ratio` determines the queue occupancy that triggers an immediate export. It also sets up a shutdown event and a lock for managing the background worker thread.

--------------------------------

### Handoff dataclass

Source: https://openai.github.io/openai-agents-python/ja/ref/handoffs

A handoff is when an agent delegates a task to another agent. For example, in a customer support scenario you might have a "triage agent" that determines which agent should handle the user's request, and sub-agents that specialize in different areas like billing, account management, etc.

--------------------------------

### SingleAgentWorkflowCallbacks > on_run

Source: https://openai.github.io/openai-agents-python/ref/voice/workflow

The `on_run` method is part of the `SingleAgentWorkflowCallbacks` interface. It is invoked when the workflow execution begins. This method provides access to the `workflow` instance and the initial `transcription` received. Its primary purpose is to allow for custom actions to be performed at the start of a workflow run, such as logging or setting up state.

--------------------------------

### Agent Class Attributes > model

Source: https://openai.github.io/openai-agents-python/ko/ref/agent

The `model` attribute specifies the language model implementation used for invoking the LLM. If this attribute is not explicitly set, the agent defaults to using the model configured via `agents.models.get_default_model()`, which is currently set to 'gpt-4.1'.

--------------------------------

### get_current_span

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

Returns the currently active span, if present.

--------------------------------

### OpenAI Agents Python > Tracing > create.py > response_span

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

Creates a new response span. Similar to `mcp_tools_span`, this span is not started automatically. You should manage its lifecycle using a `with` statement (e.g., `with response_span() ...`) or by manually calling `span.start()` and `span.finish()`. The `response` parameter takes the OpenAI Response object. An optional `span_id` can be supplied, or one will be generated (it's advisable to use `util.gen_span_id()` for correct formatting). The `parent` parameter designates a parent span or trace, defaulting to the active one if not specified. If `disabled` is set to `True`, a Span object will be returned but will not be recorded.

--------------------------------

### Processor Interface > shutdown

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `shutdown` method is called when the application is stopping. It is intended for cleaning up any resources allocated by the processor. This typically includes actions such as flushing any queued traces or spans, closing network connections, and releasing other system resources.

--------------------------------

### Model Settings > extra_headers

Source: https://openai.github.io/openai-agents-python/ko/ref/model_settings

`extra_headers`: Additional headers to provide with the request. Defaults to None if not provided.

--------------------------------

### VoicePipeline

Source: https://openai.github.io/openai-agents-python/zh/ref/voice/pipeline

The `_process_audio_input` method takes an `AudioInput` object and uses the configured speech-to-text model to transcribe it into text. This process utilizes the `transcribe` method of the `STTModel`, passing along any specific settings defined in the `VoicePipelineConfig`, as well as flags to control the inclusion of sensitive data in traces. The output of this method is the transcribed text.

--------------------------------

### RealtimeSession

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/session

To utilize the `RealtimeSession`, you can instantiate a `RealtimeRunner` with your agent and then enter an `async with` block to obtain a session object. Within this context, you can send messages using `session.send_message()` and audio data with `session.send_audio()`. The session also acts as an asynchronous iterator, allowing you to receive events from the model using an `async for` loop. You can then process these events, such as checking their type and handling them accordingly, for example, by processing incoming audio data.

--------------------------------

### Classes > Agent > Attributes > trace_include_sensitive_data

Source: https://openai.github.io/openai-agents-python/zh/ref/run

The `trace_include_sensitive_data` attribute controls whether potentially sensitive data, such as inputs and outputs of tool calls or LLM generations, is included in the traces. When set to `False`, spans for these events are still created, but the sensitive data itself is omitted, enhancing privacy and security while still providing structural information about the agent's execution.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/zh/ref/model_settings

The `top_logprobs` parameter specifies the number of top tokens for which log probabilities should be returned. Setting this value will automatically trigger the inclusion of log probability data in the response, typically under `message.output_text.logprobs`.

--------------------------------

### Source code in `src/agents/tracing/traces.py` > `name` `property`

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/traces

The `name` property of the `NoOpTrace` class returns the string "no-op". This property represents the workflow name associated with the trace. When tracing is disabled, this name signifies that the current trace is a placeholder or a no-operation trace, rather than a trace corresponding to an active workflow execution. This helps in identifying and filtering out no-op traces from actual workflow traces in logs or monitoring systems.

--------------------------------

### SQLiteSession

Source: https://openai.github.io/openai-agents-python/ko/ref/memory

This implementation stores conversation history in a SQLite database. By default, it uses an in-memory database that is lost when the process ends. For persistent storage, you can provide a file path to the database.

The `SQLiteSession` class is designed to manage conversation sessions using a SQLite backend. It allows for both transient (in-memory) and persistent storage of chat histories. The class is initialized with a unique `session_id` and an optional `db_path` for persistent storage. It also allows customization of table names for session metadata and message data.

--------------------------------

### Agents > as_tool

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

The `as_tool` method transforms an agent into a tool that can be called by other agents. This differs from agent handoffs in two key aspects. Firstly, when an agent is used as a tool, it receives generated input rather than the full conversation history. Secondly, the agent acting as a tool is invoked as a distinct step within the original agent's workflow, allowing the conversation to be continued by the original agent after the tool's execution, unlike a handoff where the new agent fully takes over the conversation.

--------------------------------

### Model context protocol (MCP) > Choosing an MCP integration > 1. Hosted MCP server tools > Basic hosted MCP tool

Source: https://openai.github.io/openai-agents-python/mcp

Create a hosted tool by adding a `HostedMCPTool` to the agent's `tools` list. The `tool_config` dict mirrors the JSON you would send to the REST API. The hosted server exposes its tools automatically; you do not add it to `mcp_servers`.

--------------------------------

### Usage > total_tokens

Source: https://openai.github.io/openai-agents-python/zh/ref/usage

The `total_tokens` attribute aggregates both input and output tokens, giving a complete count of all tokens processed in both directions for all requests.

--------------------------------

### MCP Util > ToolFilter

Source: https://openai.github.io/openai-agents-python/zh/ref/mcp/util

ToolFilter represents a mechanism for filtering tools. It can be either a ToolFilterCallable (a function that dynamically decides tool availability), a ToolFilterStatic (a predefined configuration for allowing or blocking tools), or None (indicating no filtering is applied). This flexibility allows for both dynamic and static control over tool access.

--------------------------------

### OpenAI Agents Python > Lifecycle events (hooks)

Source: https://openai.github.io/openai-agents-python/agents

You can observe the lifecycle of an agent by hooking into its events. This is useful for logging or pre-fetching data when specific events occur. To implement this, you subclass the `AgentHooks` class and override the methods for the events you are interested in.

--------------------------------

### Classes > Agent > Attributes > group_id

Source: https://openai.github.io/openai-agents-python/zh/ref/run

The `group_id` attribute provides a grouping identifier for tracing, which is useful for linking multiple traces that belong to the same conversation or process. For example, a chat thread ID could be used as a `group_id` to associate all agent interactions within that specific conversation.

--------------------------------

### Run context > AgentHookContext dataclass > usage class-attribute instance-attribute

Source: https://openai.github.io/openai-agents-python/ref/run_context

The `usage` instance attribute of `AgentHookContext` stores the usage statistics of the agent run. For streamed responses, this data may not be fully up-to-date until the entire stream has been received.

--------------------------------

### openai-agents-python/agents.py > Agent > get_conversation_turns

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/memory/advanced_sqlite_session

The `get_conversation_turns` method retrieves user messages for a specified branch, allowing for easy browsing and decision-making regarding branching. If no `branch_id` is provided, it defaults to the current branch. The method uses a synchronous helper function, `_get_turns_sync`, to interact with the database. This helper queries the `message_structure` and `agent_messages` tables to fetch the branch turn number, message data, and creation timestamp for all user messages within the given session and branch. It then processes these results, extracting the 'content' from the JSON message data, truncating it to 100 characters for a concise display while also providing the `full_content`. Each turn is returned as a dictionary containing the turn number, truncated content, full content, timestamp, and a flag indicating that branching is always possible (`can_branch: True`).

--------------------------------

### RunResult dataclass

Source: https://openai.github.io/openai-agents-python/ref/result

The `RunResult` dataclass is a core component for storing the outcomes of an agent's execution. It inherits from `RunResultBase` and includes several key attributes and properties to provide detailed information about the agent run. These include the last agent that was executed (`last_agent`), the initial input provided to the agent (`input`), and any new items generated during the run, such as messages or tool calls (`new_items`). It also captures the raw language model responses (`raw_responses`) and the final output of the agent (`final_output`). Furthermore, `RunResult` stores guardrail results for both inputs and outputs, as well as for tool executions, providing a comprehensive view of the agent's interaction with safety mechanisms. A `context_wrapper` is also included for managing the agent's execution context.

--------------------------------

### SQLAlchemySession

Source: https://openai.github.io/openai-agents-python/ref/extensions/memory/sqlalchemy_session

The `SQLAlchemySession` class provides a persistent memory backend for agents using SQLAlchemy. It implements the `SessionABC` interface, allowing agents to store and retrieve conversation history in a relational database. This implementation supports asynchronous operations, making it suitable for use with modern Python web frameworks and asynchronous applications. The session is identified by a unique `session_id`, and it utilizes a provided SQLAlchemy `AsyncEngine` for database interactions. Key configuration options include `create_tables` for automatic schema generation, and the ability to specify custom table names for sessions and messages.

--------------------------------

### Processor Interface > on_span_start

Source: https://openai.github.io/openai-agents-python/ref/tracing

The `on_span_start` method is triggered synchronously at the beginning of a new span's execution. It receives a `Span` object, which contains details about the operation and its context. Similar to `on_trace_start`, this method should execute quickly to prevent blocking and relies on automatic nesting of spans under the current trace or span.

--------------------------------

### openai-agents-python/result.py > input_guardrail_results

Source: https://openai.github.io/openai-agents-python/ja/ref/result

Guardrail results for the input messages.

--------------------------------

### VoicePipeline

Source: https://openai.github.io/openai-agents-python/ja/ref/voice/pipeline

Internally, the `VoicePipeline` manages the retrieval of STT and TTS models. The `_get_stt_model` and `_get_tts_model` methods ensure that the appropriate models are loaded and available for transcription and synthesis, respectively. If a model hasn't been instantiated yet, it will be fetched from the configuration's model provider.

--------------------------------

### Configuring the SDK > Tracing

Source: https://openai.github.io/openai-agents-python/config

It is possible to set a tracing API key on a per-run basis without altering the globally configured exporter. This is achieved by providing a `RunConfig` object during the execution of a run, where the tracing configuration, including the API key, can be specified.

```python
from agents import Runner, RunConfig

await Runner.run(
    agent,
    input="Hello",
    run_config=RunConfig(tracing={"api_key": "sk-tracing-123"}),
)
```

--------------------------------

### Results > RunResultBase dataclass

Source: https://openai.github.io/openai-agents-python/zh/ref/result

The `RunResultBase` is an abstract base class for representing the results of an agent run. It stores the original input, any new items generated during the run (such as messages or tool calls), the raw responses from the language model, and the final output. It also includes guardrail results for inputs, outputs, and tool inputs/outputs, along with a context wrapper. The class provides methods for releasing strong references to agents to help with garbage collection and a convenience method `final_output_as` to cast the final output to a specific type.

--------------------------------

### Classes > Agent > Attributes > model_settings

Source: https://openai.github.io/openai-agents-python/zh/ref/run

The `model_settings` attribute allows for the configuration of global model settings. Any non-null values provided here will override the agent-specific model settings, enabling centralized control over model behavior across different agent configurations.

--------------------------------

### Session ID naming

Source: https://openai.github.io/openai-agents-python/sessions

Meaningful session IDs are crucial for organizing and managing conversations effectively. Using a clear naming convention helps in identifying the context of a conversation at a glance. Recommendations include user-based IDs (e.g., `user_12345`), thread-based IDs (e.g., `thread_abc123`), or context-based IDs (e.g., `support_ticket_456`). This practice simplifies debugging, user support, and data retrieval.

--------------------------------

### OpenAI Agents Python API Reference > nest_handoff_history (class-attribute)

Source: https://openai.github.io/openai-agents-python/ja/ref/handoffs

Override the run-level `nest_handoff_history` behavior for this handoff only.

--------------------------------

### OpenAI Agents Python > Tracing > Processor Interface > on_span_start

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

The `on_span_start` method is called synchronously at the beginning of a new span's execution. It receives the `Span` object, which contains details about the operation and its context. Implementers should aim for a quick return from this method to prevent blocking. It's important to note that spans are automatically nested within the current trace or parent span.

--------------------------------

### Realtime Configuration > Model Configuration > url

Source: https://openai.github.io/openai-agents-python/ref/realtime/config

The `url` setting in Model Configuration specifies the endpoint for connecting to a realtime model. If this is not set, the model defaults to a standard URL, like the default OpenAI WebSocket URL for OpenAI models.

--------------------------------

### Agent Attributes > mcp_servers

Source: https://openai.github.io/openai-agents-python/ko/ref/agent

This attribute contains a list of `MCPServer` objects, representing Model Context Protocol servers. When the agent runs, it dynamically incorporates tools provided by these servers into its available toolset. It is crucial to manage the lifecycle of these servers: `server.connect()` must be called before passing them to the agent, and `server.cleanup()` should be invoked when they are no longer required.

--------------------------------

### MCPServerSse > name

Source: https://openai.github.io/openai-agents-python/ko/ref/mcp/server

The `name` property provides a readable name for the `MCPServerSse` instance. If a name is explicitly provided during initialization, that name is used. Otherwise, a default name is generated based on the server's URL, typically formatted as `sse: [server_url]`.

--------------------------------

### Quickstart > Run the pipeline

Source: https://openai.github.io/openai-agents-python/voice/quickstart

This section demonstrates how to run the voice pipeline. It involves creating an `AudioInput` object, typically from microphone data or a pre-recorded buffer, and then passing it to the `pipeline.run()` method. The result is streamed back as audio, which can then be played using `sounddevice`.

--------------------------------

### Span Class > error

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `error` property returns any error details that occurred during span execution. It returns `None` if no error occurred.

--------------------------------

### Agent Attributes

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

The `hooks` attribute allows for integration of custom logic at various points in an agent's lifecycle. By providing an `AgentHooks` instance, you can define callback functions that are triggered during specific events, such as initialization, before/after tool use, or before/after response generation.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/ja/ref/model_settings

The `extra_headers` parameter enables you to append custom HTTP headers to the request sent to the model provider. These are passed directly to the underlying API.

--------------------------------

### MCPServerStdio

Source: https://openai.github.io/openai-agents-python/zh/ref/mcp/server

The `name` property provides a human-readable identifier for the `MCPServerStdio` instance. If a custom name is not provided during initialization, it automatically generates a name based on the command used to start the server, prefixed with "stdio:". This helps in distinguishing between different server instances, especially when multiple `MCPServerStdio` objects are managed within an application.

--------------------------------

### RealtimeAgent > get_system_prompt

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/agent

The `get_system_prompt` method retrieves the system prompt for the agent. If `instructions` is a string, it's returned directly. If `instructions` is a callable function, it's invoked with the run context and agent instance to generate the prompt, supporting both synchronous and asynchronous functions. Errors are logged if `instructions` is neither a string nor a function.

--------------------------------

### Context management > Local context

Source: https://openai.github.io/openai-agents-python/context

Local context is managed using the `RunContextWrapper` class and its `context` property. The process involves:
1. Creating a Python object (e.g., a dataclass or Pydantic object) to hold your context data.
2. Passing this object to the `Runner.run` method using the `context` parameter.
3. All subsequent tool calls, lifecycle hooks, and callbacks will receive a `RunContextWrapper` object, which allows access to your original context object via the `.context` attribute.

It's essential that all components within a single agent run utilize the same type of context object. Local context can store user-specific data, dependencies like loggers or data fetchers, and helper functions. Importantly, this local context is **not** sent to the LLM; it's exclusively for your local code execution.

--------------------------------

### function_tool

Source: https://openai.github.io/openai-agents-python/ja/ref/tool

The `function_tool` decorator is used to wrap a Python function and convert it into a `FunctionTool` that can be used by an agent. By default, it automatically parses the function's signature to generate a JSON schema for its parameters and uses the function's docstring to provide a description for the tool and its arguments. The decorator attempts to auto-detect the docstring style, but this can be manually overridden if needed. If the function's first argument is a `RunContextWrapper`, its type must precisely match the context type of the agent that will be utilizing this tool.

--------------------------------

### Span > ended_at

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/spans

The `ended_at` property returns the timestamp indicating when the span finished execution. The timestamp is in ISO format. If the span has not yet finished, it returns `None`.

--------------------------------

### DaprSession > ping

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/memory/dapr_session

Tests connectivity to Dapr by attempting to read and, if necessary, write a test key (`__ping__`) to the configured state store. It first tries to read the key. If that fails (e.g., due to an uninitialized store), it attempts to save the key with a value of 'ok' and then tries to read it again. If both attempts fail, it indicates that Dapr is not reachable and returns `False`; otherwise, it returns `True`.

--------------------------------

### MCP Util > ToolFilterStatic > allowed_tool_names

Source: https://openai.github.io/openai-agents-python/zh/ref/mcp/util

The `allowed_tool_names` attribute within ToolFilterStatic is an optional list of tool names that are permitted for use. If this list is provided, only the tools whose names appear in this list will be considered available. This acts as a whitelist, restricting access to a specific subset of tools.

--------------------------------

### openai-agents-python > src > agents > tracing > create.py > response_span

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/create

Creates a new response span. This span is not started automatically; you must either use `with response_span() ...` or manually call `span.start()` followed by `span.finish()`. The `response` parameter takes the OpenAI Response object. The `span_id` is optional and will be generated if not provided, though using `util.gen_span_id()` is recommended for correct formatting. The `parent` parameter allows specifying a parent span or trace, otherwise the current trace/span is used. If `disabled` is True, the span is created but not recorded.

--------------------------------

### openai-agents-python/agent.py

Source: https://openai.github.io/openai-agents-python/ko/ref/agent

Transform this agent into a tool, callable by other agents. This is different from handoffs in two ways: 1. In handoffs, the new agent receives the conversation history. In this tool, the new agent receives generated input. 2. In handoffs, the new agent takes over the conversation. In this tool, the new agent is called as a tool, and the conversation is continued by the original agent.

--------------------------------

### Input > AudioInput > frame_rate

Source: https://openai.github.io/openai-agents-python/zh/ref/voice/input

The `frame_rate` instance attribute of `AudioInput` specifies the sample rate of the audio data. It defaults to 24000, which is a common sample rate for audio processing.

--------------------------------

### Tracing Processor Interface > shutdown

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/processor_interface

The `shutdown` method is called when the application stops, and it's responsible for cleaning up any resources used by the tracing processor. This includes flushing any queued traces or spans that haven't been processed yet, closing any network connections that might be open, and releasing any other resources that were allocated during the tracing process.

--------------------------------

### Model > TTSModel > model_name

Source: https://openai.github.io/openai-agents-python/ref/voice/model

The `model_name` is an abstract property that must be implemented by any concrete subclass of `TTSModel`. It represents the unique identifier or name of the specific text-to-speech model being used.

--------------------------------

### OpenAI Agents Python > as_tool

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

The `as_tool` method transforms an agent into a tool that can be invoked by other agents. This differs from agent handoffs in two key aspects. Firstly, when used as a tool, the agent receives generated input directly, whereas in a handoff, it receives the entire conversation history. Secondly, an agent acting as a tool is called within the context of the original agent's turn, and the conversation flow is managed by the original agent. In contrast, a handoff involves the new agent taking over the conversation completely.

--------------------------------

### OpenAI Agents Python > session_input_callback

Source: https://openai.github.io/openai-agents-python/ref/run

The `session_input_callback` attribute defines how session history is managed when new input is provided. If set to `None` (the default), the new input is simply appended to the existing history. However, you can provide a custom `SessionInputCallback` function, which receives both the history and the new input, and returns the desired combined list of items for the session.

--------------------------------

### Agent > clone

Source: https://openai.github.io/openai-agents-python/ref/agent

The `clone` method creates a copy of the agent, allowing for modifications to specific attributes without altering the original agent. It utilizes `dataclasses.replace`, which performs a shallow copy. This means that mutable attributes like `tools` and `handoffs` are shallow-copied. New list objects for these attributes are only created if they are explicitly overridden during the `clone` operation. Otherwise, the contents of these mutable attributes are shared between the original and the cloned agent. To ensure independent modification of these shared contents, new lists should be passed when calling `clone()`.

--------------------------------

### OpenAI Agents Python API Reference > strict_json_schema

Source: https://openai.github.io/openai-agents-python/ja/ref/handoffs

Whether the input JSON schema is in strict mode. We strongly recommend setting this to True because it increases the likelihood of correct JSON input.

--------------------------------

### MCPServerSse > name

Source: https://openai.github.io/openai-agents-python/ref/mcp/server

The `name` property provides a human-readable identifier for the `MCPServerSse` instance. If a name is not explicitly provided during initialization, it is automatically generated based on the server's URL, prefixed with 'sse:'. This helps in distinguishing between different MCP server instances when managing multiple connections.

--------------------------------

### spans.py > SpanError

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

The `SpanError` TypedDict represents an error that occurred during span execution. It includes a `message` attribute for a human-readable error description and an optional `data` attribute for additional error context.

--------------------------------

### RealtimePlaybackTracker

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/model

The `RealtimePlaybackTracker` class is designed for scenarios where custom playback logic is needed or when audio playback might involve delays or varying speeds. Users are responsible for tracking the audio playback progress and signaling when audio has been played by calling either `on_play_bytes` or `on_play_ms`. This allows the system to maintain an accurate record of playback status, especially in non-standard playback environments.

--------------------------------

### Release process/changelog > Breaking change changelog > 0.5.0

Source: https://openai.github.io/openai-agents-python/release

Version 0.5.0 includes new features and significant under-the-hood updates, although it does not introduce visible breaking changes. Key updates include added support for `RealtimeRunner` to handle SIP protocol connections and a substantial revision of the internal logic of `Runner#run_sync` to ensure compatibility with Python 3.14.

--------------------------------

### SQLiteSession

Source: https://openai.github.io/openai-agents-python/ko/ref/memory/sqlite_session

The `SQLiteSession` class provides a SQLite-based implementation for session storage. It stores conversation history within a SQLite database. By default, it utilizes an in-memory database which means the data is lost once the process terminates. To ensure persistent storage of conversation history, you can specify a file path for the database. This allows for the retrieval of past conversations even after the application has been restarted.

--------------------------------

### openai-agents-python > agent.py > as_tool

Source: https://openai.github.io/openai-agents-python/ref/agent

Further customization for the `as_tool` method includes the `is_enabled` parameter, which can be a boolean or a callable that dynamically determines if the tool is active. Disabled tools are hidden from the language model during runtime. The `on_stream` parameter allows for the registration of a callback function to handle streaming events from the nested agent run, enabling real-time event processing. Additionally, a `failure_error_function` can be supplied to generate an error message that is sent to the LLM in case of a tool run failure, rather than raising an exception.

--------------------------------

### SingleAgentVoiceWorkflow

Source: https://openai.github.io/openai-agents-python/ja/ref/voice/workflow

The `SingleAgentVoiceWorkflow` class is designed for straightforward voice interactions, processing user input through a single agent and ensuring that each transcription and its corresponding result are added to the conversation history. If you require more advanced functionalities such as multiple `Runner` calls, custom message history management, bespoke logic implementation, or custom configurations, you should subclass `VoiceWorkflowBase` and define your own implementation details.

--------------------------------

### Classes > Agent > Attributes > workflow_name

Source: https://openai.github.io/openai-agents-python/zh/ref/run

The `workflow_name` attribute defines a human-readable name for the agent run, which is primarily used for tracing purposes. Assigning a logical name, such as 'Code generation workflow' or 'Customer support agent', makes it easier to identify and categorize different agent executions in monitoring and debugging tools.

--------------------------------

### OpenAI Agents Python/realtime/config.py/playback_tracker

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/config

The `playback_tracker` is an instance attribute used for tracking audio playback progress. If not provided, a default implementation assumes audio plays immediately at realtime speed. A playback tracker is particularly useful for handling interruptions, as the model generates audio much faster than realtime playback. Knowing how much audio the user has consumed helps the model manage interruptions effectively. While assuming immediate realtime playback is acceptable for low-latency scenarios, in situations like phone calls, a custom playback tracker allows the model to be aware of actual audio playback timing.

--------------------------------

### RunConfig `dataclass` > model `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/zh/ref/run

The `model` attribute within `RunConfig` specifies the model to be used for the entire agent run. If this attribute is set, it will override any model settings defined for individual agents. It's important that the `model_provider` configured can resolve the model name specified here. This provides a way to enforce a consistent model across all agents in a run.

--------------------------------

### Model > RealtimePlaybackTracker > set_audio_format

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/model

The `set_audio_format` method is called by the model to inform the `RealtimePlaybackTracker` about the audio format being used for playback. This information is essential for accurately calculating the duration of audio in milliseconds when `on_play_bytes` is called, as the byte length directly correlates to duration based on the audio format (sample rate, bit depth, channels).

--------------------------------

### MCP Util > ToolFilterContext > run_context

Source: https://openai.github.io/openai-agents-python/zh/ref/mcp/util

The `run_context` attribute within ToolFilterContext holds the current run context. This object provides detailed information about the ongoing execution, which can be leveraged by tool filters to adjust tool availability based on the specific state of the agent's operation.

--------------------------------

### RealtimeAgent > mcp_config

Source: https://openai.github.io/openai-agents-python/ja/ref/realtime/agent

The `mcp_config` attribute holds configuration settings for Model Context Protocol servers, allowing for customization of their behavior.

--------------------------------

### TracingProcessor

Source: https://openai.github.io/openai-agents-python/ref/tracing/processor_interface

The `TracingProcessor` is an abstract base class defining the interface for processing and monitoring traces and spans within the OpenAI Agents system. Any custom tracing processor must implement the methods defined in this interface. These processors are notified when traces and spans begin and end, enabling them to collect, process, and export tracing data effectively. The interface includes methods like `on_trace_start`, `on_trace_end`, `on_span_start`, and `on_span_end`, along with `shutdown` and `force_flush` for resource management and data export.

When implementing a custom `TracingProcessor`, it is crucial to adhere to certain guidelines. All methods should be thread-safe to ensure proper operation in concurrent environments. Furthermore, methods should not introduce significant delays by blocking for extended periods, as this could disrupt agent execution. Errors encountered during processing should be handled gracefully to prevent them from impacting the overall agent's functionality.

--------------------------------

### RealtimeAgent > hooks

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/agent

The `hooks` attribute allows for integration with `RealtimeAgentHooks`, a class designed to receive callbacks during various lifecycle events of the agent. This enables custom actions or monitoring at different stages of the agent's operation.

--------------------------------

### openai-agents-python/agents.py > Agent class

Source: https://openai.github.io/openai-agents-python/ref/extensions/memory/advanced_sqlite_session

The `Agent` class is the central component for managing conversations. It handles the creation of new sessions, copying existing message structures to new branches, and retrieving conversation turns. The class interacts with a database to store and retrieve message data, ensuring persistence and enabling complex branching strategies. It uses asynchronous operations with `asyncio.to_thread` to perform database operations without blocking the main event loop.

--------------------------------

### RunResultStreaming dataclass

Source: https://openai.github.io/openai-agents-python/ja/ref/result

The `RunResultStreaming` class provides several key attributes for managing and monitoring agent runs. `current_agent` refers to the agent currently executing, while `current_turn` indicates the ongoing turn number in the agent's sequence of operations. `max_turns` sets the upper limit for the number of turns an agent can undertake, preventing indefinite execution. The `final_output` attribute holds the agent's ultimate result, which is only populated once the agent has completed its run; prior to completion, it remains `None`. An `is_complete` boolean flag indicates whether the agent has finished its execution cycle.

--------------------------------

### RealtimeAgent > hooks

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/agent

The `hooks` attribute allows for the integration of callbacks that respond to various lifecycle events of the agent. By providing a `RealtimeAgentHooks` object, custom logic can be executed at different stages of the agent's operation.

--------------------------------

### RunConfig `dataclass` > trace_id `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ja/ref/run

A custom `trace_id` can be provided in `RunConfig` to uniquely identify a specific tracing session. If no custom ID is supplied, a new trace ID will be automatically generated for the run.

--------------------------------

### ReasoningItem `dataclass` > to_input_item

Source: https://openai.github.io/openai-agents-python/ko/ref/items

The `to_input_item` method for `ReasoningItem` converts the item into a format suitable for model input. If the `raw_item` is a dictionary, it's returned directly. If it's a Pydantic `BaseModel`, it's converted to a dictionary, excluding unset fields. An exception is raised for unexpected `raw_item` types.

--------------------------------

### OpenAI Agents Python > create_branch_from_content

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/memory/advanced_sqlite_session

The `create_branch_from_content` method provides a way to create a new branch by searching for a specific text string within user messages. It finds all turns containing the search term and uses the earliest matching turn to create the new branch. If no turns match the search term, it raises a `ValueError`. This method effectively allows users to branch off from a point in the conversation identified by its content.

--------------------------------

### Results > RunResultBase dataclass

Source: https://openai.github.io/openai-agents-python/ko/ref/result

The `RunResultBase` is an abstract base class representing the outcome of an agent's operation. It meticulously records all aspects of the run, starting with the initial `input` which might have been pre-processed by input filters. It captures `new_items` that were generated during the run, such as new messages or tool calls, and stores the `raw_responses` directly from the language model. The `final_output` attribute holds the ultimate result produced by the agent. Additionally, it tracks `input_guardrail_results`, `output_guardrail_results`, `tool_input_guardrail_results`, and `tool_output_guardrail_results` to provide insights into the safety and integrity of the agent's operations. A `context_wrapper` is also included for managing runtime context.

--------------------------------

### SQLAlchemy Sessions > Installation

Source: https://openai.github.io/openai-agents-python/sessions/sqlalchemy_session

SQLAlchemy sessions require the `sqlalchemy` extra. To install it, run: `pip install openai-agents[sqlalchemy]`.

--------------------------------

### run `async` `classmethod`

Source: https://openai.github.io/openai-agents-python/ja/ref/run

The `run` class method orchestrates the execution of an agent workflow. It initiates the process with a `starting_agent` and an initial `input`. The workflow proceeds iteratively: the agent is invoked, and if a final output is produced, the process concludes. If the agent initiates a handoff to another agent, the loop continues with the new agent. Otherwise, any pending tool calls are executed, and the loop then repeats. This method also incorporates mechanisms to prevent infinite loops or problematic behavior by raising exceptions if `max_turns` is exceeded or if a `guardrail` is triggered. It's important to note that only the guardrails of the very first agent in the sequence are evaluated.

--------------------------------

### Tracing Utilities > get_current_trace

Source: https://openai.github.io/openai-agents-python/ref/tracing

The `get_current_trace()` function returns the currently active trace, if one is present. This is a utility function for accessing the current tracing context.

--------------------------------

### SingleAgentVoiceWorkflow

Source: https://openai.github.io/openai-agents-python/ref/voice/workflow

The `SingleAgentVoiceWorkflow` class represents a straightforward voice workflow designed to execute a single agent. It automatically appends each transcription and its corresponding result to the input history. For scenarios requiring more advanced functionality, such as multiple `Runner` calls, custom message history management, custom logic implementation, or custom configurations, developers should subclass `VoiceWorkflowBase` and define their own logic.

--------------------------------

### Agent Attributes > mcp_config

Source: https://openai.github.io/openai-agents-python/ref/agent

This attribute allows for configuration of MCP servers. It defaults to a new MCPConfig instance.

--------------------------------

### engine

Source: https://openai.github.io/openai-agents-python/ref/extensions/memory/sqlalchemy_session

Access the underlying SQLAlchemy AsyncEngine. This property provides direct access to the engine for advanced use cases, such as checking connection pool status, configuring engine settings, or manually disposing the engine when needed. Returns: The SQLAlchemy async engine instance.

--------------------------------

### OpenAI Agents Python > model_settings

Source: https://openai.github.io/openai-agents-python/ref/run

The `model_settings` attribute allows for the configuration of global model settings. Any settings provided here that are not null will override the model-specific settings defined for individual agents. This is useful for establishing a consistent baseline for model behavior across multiple agents.

--------------------------------

### Span > set_error

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

Set an error for the span. This method is used to record any error that occurred during the span's execution.

--------------------------------

### RunConfig `dataclass` > handoff_history_mapper `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ja/ref/run

The `handoff_history_mapper` in `RunConfig` is an optional function that can process the normalized transcript (including history and handoff items) before it's passed to the next agent. If not provided (`None`), the runner collapses the transcript into a single assistant message. This mapper function is only utilized when `nest_handoff_history` is set to `True`.

--------------------------------

### Agent Attributes > model_settings

Source: https://openai.github.io/openai-agents-python/ref/agent

Model-specific tuning parameters, such as `temperature` and `top_p`, are configured through the `model_settings` attribute. It utilizes a factory pattern, defaulting to `get_default_model_settings()`, to provide sensible initial values. This allows for fine-grained control over the LLM's generation process.

--------------------------------

### openai-agents-python/src/agents/tracing/create.py > response_span

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

Create a new response span. Similar to `mcp_tools_span`, this span is not started automatically, requiring either a `with response_span() ...` context or manual `span.start()` and `span.finish()` calls. Key parameters are `response` for the OpenAI Response object, `span_id` for an optional unique identifier (recommend using `util.gen_span_id()`), `parent` to link to an existing trace or span (defaults to the current one), and `disabled` to control whether the span is recorded.

--------------------------------

### Custom output extraction

Source: https://openai.github.io/openai-agents-python/tools

In certain cases, you might want to modify the output of the tool-agents before returning it to the central agent. This may be useful if you want to:
  * Extract a specific piece of information (e.g., a JSON payload) from the sub-agent's chat history.
  * Convert or reformat the agent’s final answer (e.g., transform Markdown into plain text or CSV).
  * Validate the output or provide a fallback value when the agent’s response is missing or malformed.
You can do this by supplying the `custom_output_extractor` argument to the `as_tool` method.

--------------------------------

### NoOpTrace

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/traces

The `NoOpTrace` class is a no-operation implementation of the `Trace` class. It is utilized when tracing is disabled, allowing trace-related operations to function without recording or exporting any data. This ensures proper context management even when tracing is inactive, maintaining the integrity of operations that might otherwise rely on tracing functionalities.

--------------------------------

### stream_events

Source: https://openai.github.io/openai-agents-python/ref/result

Stream deltas for new items as they are generated. We're using the types from the OpenAI Responses API, so these are semantic events: each event has a `type` field that describes the type of the event, along with the data for that event. This will raise a `MaxTurnsExceeded` exception if the agent exceeds the max_turns limit, or a `GuardrailTripwireTriggered` exception if a guardrail is tripped.

--------------------------------

### OpenAI Agents SDK > Why use the Agents SDK

Source: https://openai.github.io/openai-agents-python/index

The SDK has two driving design principles: Enough features to be worth using, but few enough primitives to make it quick to learn. It works great out of the box, but you can customize exactly what happens.

--------------------------------

### Model > TTSModelSettings > dtype

Source: https://openai.github.io/openai-agents-python/ref/voice/model

The `dtype` attribute in TTSModelSettings specifies the data type for the audio data that will be returned. It defaults to `np.int16`, indicating a 16-bit integer format for the audio samples.

--------------------------------

### OpenAI Agents Python > create_branch_from_content

Source: https://openai.github.io/openai-agents-python/ref/extensions/memory/advanced_sqlite_session

The `create_branch_from_content` method allows for the creation of a new branch by searching for a specific text string within user messages. It finds all turns containing the search term and uses the earliest matching turn to create the new branch. If no turns match the search term, it raises a `ValueError`. This function acts as a convenience wrapper around `create_branch_from_turn`, simplifying the process of branching based on conversational content.

--------------------------------

### DaprSession > __aexit__

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/memory/dapr_session

Exits the asynchronous context manager for the DaprSession. Upon exiting, it ensures that the Dapr client connection is properly closed by calling the `close` method.

--------------------------------

### Configuration options > Audio settings

Source: https://openai.github.io/openai-agents-python/realtime/quickstart

Audio settings are crucial for managing the input and output of voice-based interactions. The `input_audio_format` can be set to formats like `pcm16`, `g711_ulaw`, or `g711_alaw`. Similarly, `output_audio_format` determines the format of the audio streams sent back to the user. The `input_audio_transcription` setting allows for configuration of the speech-to-text model used for processing user input.

--------------------------------

### Source code in `src/agents/tracing/traces.py` > `export`

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/traces

The `export` method in the `NoOpTrace` class is designed to return `None`. As this class represents a no-operation trace, it does not collect or store any data that can be exported. Therefore, calling the `export` method will yield no data, aligning with the purpose of `NoOpTrace` which is to execute operations without recording any trace information. This behavior is consistent with the overall design of disabling tracing.

--------------------------------

### Handoff dataclass > agent_name instance-attribute

Source: https://openai.github.io/openai-agents-python/zh/ref/handoffs

The `agent_name` attribute stores the name of the specific agent to which the task is being handed off. This provides a clear and direct reference to the target agent within the system. It's essential for identifying which specialized agent will take over the execution of the task, ensuring that the request is routed to the most appropriate handler.

--------------------------------

### Agent Attributes > clone

Source: https://openai.github.io/openai-agents-python/ko/ref/agent

This method creates a copy of the agent, allowing for modifications to its arguments. It utilizes `dataclasses.replace`, which performs a shallow copy. This means mutable attributes like `tools` and `handoffs` are shallow-copied; new list objects are only created if these attributes are explicitly overridden during the `clone()` call. Otherwise, the contents of these mutable attributes are shared between the original agent and the cloned one. To ensure independent modification of mutable attributes, new lists should be passed when calling `clone()`. For example, `new_agent = agent.clone(instructions="New instructions")` demonstrates how to change the instructions.

--------------------------------

### Agent `dataclass` > model_settings

Source: https://openai.github.io/openai-agents-python/zh/ref/agent

The `model_settings` parameter is used to configure model-specific tuning parameters, such as temperature and top_p. These settings allow for fine-tuning the behavior and output characteristics of the underlying language model used by the agent.

--------------------------------

### BatchTraceProcessor

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/processors

The `BatchTraceProcessor` is an implementation of `TracingProcessor` designed for efficient span and trace export. It utilizes a thread-safe queue to store incoming telemetry data. To minimize performance impact on the main application thread, a background worker thread is responsible for exporting these batched spans and traces. The spans and traces are held in memory within the queue until they are processed and exported. This approach helps in reducing the frequency of network requests or file writes associated with telemetry export, leading to better overall application performance.

--------------------------------

### Handoff Input Validation and Signature

Source: https://openai.github.io/openai-agents-python/zh/ref/handoffs

When defining a handoff, there's a crucial validation: you must provide either both `on_handoff` and `input_type`, or neither. If `input_type` is specified, `on_handoff` must be a callable that accepts two arguments: the context and the input. A `TypeAdapter` is used to validate the input against the provided `input_type`, generating a JSON schema for it. If `input_type` is not provided, `on_handoff` should accept only one argument: the context.

--------------------------------

### Input > StreamedAudioInput

Source: https://openai.github.io/openai-agents-python/ref/voice/input

The `StreamedAudioInput` class is designed for audio input that arrives as a stream. You can initialize it and then use the `add_audio` method to push audio data into a queue. This allows for real-time processing of audio by the `VoicePipeline`. Passing `None` to `add_audio` signals the end of the audio stream.

--------------------------------

### `RealtimeSession`

Source: https://openai.github.io/openai-agents-python/zh/ref/realtime/session

You can interact with the `RealtimeSession` by sending messages or audio data to the model using methods like `send_message()` and `send_audio()`. Additionally, you can asynchronously iterate over the session to receive events streamed from the model. These events can be of various types, such as audio data, which you can then process accordingly.

--------------------------------

### AgentOutputSchema `dataclass`

Source: https://openai.github.io/openai-agents-python/ko/ref/agent_output

The `AgentOutputSchema` class takes an `output_type` and an optional `strict_json_schema` boolean during initialization. If the `output_type` is `None` or `str`, it's treated as plain text, and no JSON schema is generated. For other types, it determines whether to wrap the output type in a dictionary based on whether it's a subclass of `BaseModel` or `dict`. If wrapping is necessary, it creates a `TypedDict` to accommodate the output type. The `strict_json_schema` parameter, recommended to be `True`, enforces stricter validation rules on the generated JSON schema, increasing the likelihood of correct JSON input from the LLM. If strict mode is enabled and the output type is invalid, a `UserError` is raised.

--------------------------------

### VoicePipeline

Source: https://openai.github.io/openai-agents-python/ja/ref/voice/pipeline

The `VoicePipeline` can be initialized with a `workflow`, an optional speech-to-text (`stt_model`) model, an optional text-to-speech (`tts_model`) model, and a configuration object (`config`). If the `stt_model` or `tts_model` are not explicitly provided, the pipeline will use default OpenAI models. Similarly, if no `config` is provided, a default configuration will be applied.

--------------------------------

### OpenAI Agents Python > create_branch_from_content

Source: https://openai.github.io/openai-agents-python/zh/ref/extensions/memory/advanced_sqlite_session

The `create_branch_from_content` method provides a way to create a new branch by searching for a specific text string within user messages. It utilizes the `find_turns_by_content` method to locate the first occurrence of the `search_term`. If no matching turns are found, it raises a `ValueError`. Upon finding a match, it uses the turn number of the earliest matching turn to call `create_branch_from_turn`, optionally allowing a custom name for the new branch.

--------------------------------

### Input > StreamedAudioInput

Source: https://openai.github.io/openai-agents-python/ja/ref/voice/input

The `StreamedAudioInput` class is designed for audio input that arrives as a stream. You can initialize an instance of this class and then pass it to the `VoicePipeline`. To feed audio data into the pipeline, you use the `add_audio` method, which allows you to push chunks of audio data into a queue. Passing `None` to `add_audio` signals the end of the audio stream.

--------------------------------

### VoicePipeline

Source: https://openai.github.io/openai-agents-python/zh/ref/voice/pipeline

The `_run_single_turn` method orchestrates the execution of the `VoicePipeline` for a single audio input. It begins by initiating a trace using `TraceCtxManager` to manage the lifecycle of the trace, including relevant metadata and configuration. It then transcribes the input audio to text using `_process_audio_input`. Subsequently, it creates a `StreamedAudioResult` object, which will be used to stream the synthesized audio output. The method then defines an asynchronous generator `stream_events` that iterates through the text events produced by the `workflow.run()` method, adding each text event to the `StreamedAudioResult` and signaling the completion of the turn and the overall process.

--------------------------------

### Agent Class > `register_tool` Method > `run_agent` Function

Source: https://openai.github.io/openai-agents-python/ref/agent

The `run_agent` function, generated by the `register_tool` decorator, orchestrates the execution of the agent as a tool. It handles both standard and streaming execution modes. In standard mode, it uses `Runner.run` to execute the agent and returns the final output. In streaming mode, it utilizes `Runner.run_streamed` and manages an event queue to process and dispatch stream events to the `on_stream` callback. After execution, if a `custom_output_extractor` is provided, it's used to process the `RunResult`; otherwise, the `final_output` of the run result is returned.

--------------------------------

### Tool filtering

Source: https://openai.github.io/openai-agents-python/mcp

Each MCP server supports tool filters so that you can expose only the functions that your agent needs. Filtering can happen at construction time or dynamically per run.

--------------------------------

### API Reference > Realtime Models > OpenAIRealtimeSIPModel > build_initial_session_payload

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/openai_realtime

The `build_initial_session_payload` is a static asynchronous method within `OpenAIRealtimeSIPModel`. Its primary purpose is to construct an initial session payload that mimics what a `RealtimeSession` would send upon connection. This is particularly useful for accepting SIP-originated calls, as the returned payload can be forwarded to the Realtime Calls API, thus avoiding the duplication of session setup logic. It merges various configuration settings from the agent, context, model configuration, run configuration, and any overrides to create a comprehensive session configuration.

--------------------------------

### SQLiteSession

Source: https://openai.github.io/openai-agents-python/ja/ref/memory/sqlite_session

The `_get_connection` method handles retrieving the appropriate SQLite database connection. If an in-memory database is being used, it returns the shared connection. For file-based databases, it provides a thread-local connection, creating one if it doesn't already exist for the current thread. The `_init_db_for_connection` method is responsible for creating the necessary tables, `agent_sessions` and `agent_messages`, if they do not already exist within the database.

--------------------------------

### agent_span

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/create

The `agent_span` function is used to create a new agent span. This span is not started automatically; you must either use a `with agent_span() ...` block or manually call `span.start()` and `span.finish()`. The function accepts several parameters to configure the span, including its `name`, optional `handoffs` to other agents, available `tools`, the `output_type` of the agent, an optional `span_id`, and an optional `parent` span or trace. If `disabled` is set to `True`, the span will be created but not recorded. The function returns a `Span[AgentSpanData]` object representing the newly created agent span.

--------------------------------

### Results > RunResultBase dataclass

Source: https://openai.github.io/openai-agents-python/ref/result

The `RunResultBase` is an abstract base class that represents the result of an agent run. It holds various pieces of information generated during the execution, including the original input, new items created (like messages and tool calls), raw language model responses, guardrail results for inputs and outputs, and the final output of the agent.

It also provides methods for managing agent references and accessing the final output in a type-safe manner. The `release_agents` method allows for explicit cleanup of strong references to agents, which can be useful for managing memory. The `__del__` method ensures that agents are released even if `release_agents` is not called explicitly, by leveraging the garbage collection mechanism.

--------------------------------

### OpenAI Agents Python API Reference > input_filter

Source: https://openai.github.io/openai-agents-python/ja/ref/handoffs

A function that filters the inputs that are passed to the next agent. By default, the new agent sees the entire conversation history. In some cases, you may want to filter inputs (for example, to remove older inputs or remove tools from existing inputs). The function receives the entire conversation history so far, including the input item that triggered the handoff and a tool call output item representing the handoff tool's output. You are free to modify the input history or new items as you see fit. The next agent that runs will receive `handoff_input_data.all_items`. IMPORTANT: in streaming mode, we will not stream anything as a result of this function. The items generated before will already have been streamed.

--------------------------------

### RunConfig `dataclass` > model `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ja/ref/run

The `model` attribute within `RunConfig` specifies the model to be used for the entire agent run. If this attribute is set, it will override any model specified at an individual agent level. It's important that the `model_provider` configured is capable of resolving the model name provided here.

--------------------------------

### Streaming > Run item events and agent events

Source: https://openai.github.io/openai-agents-python/streaming

`RunItemStreamEvent`s are higher level events. They inform you when an item has been fully generated. This allows you to push progress updates at the level of "message generated", "tool ran", etc, instead of each token. Similarly, `AgentUpdatedStreamEvent` gives you updates when the current agent changes (e.g. as the result of a handoff). For example, this will ignore raw events and stream updates to the user.

--------------------------------

### LitellmModel

Source: https://openai.github.io/openai-agents-python/zh/ref/extensions/litellm

This class enables using any model via LiteLLM. LiteLLM allows you to acess OpenAPI, Anthropic, Gemini, Mistral, and many other models. See supported models here: litellm models.

--------------------------------

### Agent `dataclass`

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

Model settings provide a way to fine-tune the behavior of the underlying AI model, such as adjusting parameters like `temperature` and `top_p`. These settings are encapsulated within the `model_settings` parameter, which defaults to `get_default_model_settings()`. This allows for customization of the model's response generation characteristics, enabling developers to control the creativity, randomness, and focus of the agent's output.

--------------------------------

### openai-agents-python/tracing/create.py > mcp_tools_span

Source: https://openai.github.io/openai-agents-python/ref/tracing

Create a new MCP list tools span. The span will not be started automatically, you should either do `with mcp_tools_span() ...` or call `span.start()` + `span.finish()` manually. This function takes optional parameters such as `server` name, `result` list, `span_id`, `parent` trace or span, and a `disabled` flag. If `span_id` is not provided, one will be generated. The `parent` parameter allows specifying a parent trace or span; if omitted, the current trace/span will be used. Setting `disabled` to `True` will return a Span object that will not be recorded.

--------------------------------

### VoicePipeline

Source: https://openai.github.io/openai-agents-python/ref/voice/pipeline

The `VoicePipeline` is an opinionated voice agent pipeline designed to process audio input and generate audio output through a defined workflow. It operates in three distinct steps:

1.  **Transcription**: It first transcribes the incoming audio input into text.
2.  **Workflow Execution**: The transcribed text is then passed to a provided `workflow`, which processes it and produces a sequence of text responses.
3.  **Speech Synthesis**: Finally, these text responses are converted into streaming audio output.

This pipeline simplifies the creation of voice-enabled agents by abstracting the complexities of speech-to-text, natural language processing (via the workflow), and text-to-speech.

Source code is located in `src/agents/voice/pipeline.py`.

--------------------------------

### traces.py > NoOpTrace

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/traces

The `NoOpTrace` class is a no-operation implementation of the `Trace` abstract base class. It is utilized when tracing is disabled, ensuring that trace-related operations can still be called without error. This class maintains proper context management but does not record or export any actual trace data, making it a lightweight placeholder.

--------------------------------

### OpenAI Agents Python

Source: https://openai.github.io/openai-agents-python/ref/model_settings

The `resolve` method produces a new `ModelSettings` object by overlaying any non-None values from an `override` object onto the current instance. If `override` is `None`, the original `ModelSettings` instance is returned. The method specifically handles `extra_args` by merging dictionaries if both the current instance and the override have them, rather than simply replacing them. This ensures that any provided arguments from both sources are combined.

--------------------------------

### traces.py > NoOpTrace

Source: https://openai.github.io/openai-agents-python/ref/tracing/traces

The `NoOpTrace` class is a no-operation implementation of the `Trace` abstract base class. It is utilized when tracing functionality is disabled, ensuring that trace-related operations can still be called without errors. This class maintains proper context management but does not record or export any trace data, making it a lightweight placeholder.

--------------------------------

### Results > RunResultBase dataclass

Source: https://openai.github.io/openai-agents-python/ref/result

The `RunResultBase` provides utility methods for interacting with the run results. The `final_output_as` method allows for type-safe casting of the `final_output` to a specified class, with an option to raise a `TypeError` if the output doesn't match the expected type. The `to_input_list` method is useful for reconstructing a complete list of input items, merging the original input with any new items generated during the run. Additionally, `last_response_id` offers a convenient way to retrieve the identifier of the last model response, if any.

--------------------------------

### Processor Interface > shutdown

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

The `shutdown` method is called when the application is stopping. Its purpose is to clean up any necessary resources that were utilized during the tracing process. This can include actions such as flushing any traces or spans that are still queued for processing, closing any open network connections, and releasing any other acquired resources.

--------------------------------

### openai_agents_python/create.py > speech_span

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing

The `speech_span` function creates a new speech span. This span is not started automatically; you must either use a `with speech_span() ...` block or manually call `span.start()` followed by `span.finish()`. The function accepts several parameters to configure the span, including the model name (`model`), text input (`input`), audio output (`output`), audio format (`output_format`), model configuration (`model_config`), timestamp for the first byte of audio (`first_content_at`), an optional span ID (`span_id`), a parent span or trace (`parent`), and a flag to disable recording (`disabled`). If `span_id` is not provided, an ID will be generated, and it's recommended to use `util.gen_span_id()` for proper formatting. If `parent` is not specified, the current trace or span will be used as the parent.

--------------------------------

### FunctionTool `dataclass` > `tool_input_guardrails` `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ja/ref/tool

The `tool_input_guardrails` and `tool_output_guardrails` attributes allow for the implementation of pre- and post-invocation checks on tool execution. `tool_input_guardrails` is an optional list of guardrail objects that are executed before the `on_invoke_tool` function is called, providing an opportunity to validate or modify the input arguments. Similarly, `tool_output_guardrails` is an optional list of guardrails applied after the tool has been invoked, allowing for validation or transformation of the tool's output before it's returned to the LLM or used elsewhere.

--------------------------------

### Agent Attributes > mcp_servers

Source: https://openai.github.io/openai-agents-python/ref/agent

This attribute is a list of Model Context Protocol (MCP) servers that the agent can utilize. Each time the agent runs, it will incorporate tools from these servers into its available toolset. It is important to manage the lifecycle of these servers yourself, ensuring you call `server.connect()` before passing the server to the agent and `server.cleanup()` when the server is no longer required.

--------------------------------

### TracingProcessor > on_trace_end

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

The `on_trace_end` method is invoked when a trace completes its execution. It is provided with the `trace` object, which by this point contains all the spans and final results. This is an opportune moment to export or perform any necessary processing on the complete trace data. The method should also handle the cleanup of any resources specific to this trace and is called synchronously, so it should execute efficiently.

--------------------------------

### AgentManager

Source: https://openai.github.io/openai-agents-python/zh/ref/extensions/memory/advanced_sqlite_session

The `AgentManager` class is responsible for managing the conversation history, including storing messages, handling branching, and retrieving conversation turns. It interacts with a database to persist this information. The class supports asynchronous operations for database interactions, ensuring non-blocking behavior.

--------------------------------

### openai-agents-python > mcp_tools_span

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing/create

Create a new MCP list tools span. Similar to other spans, this span is not started automatically and requires manual initiation using `with mcp_tools_span() ...` or explicit `span.start()` and `span.finish()` calls. The `server` parameter specifies the name of the MCP server, and `result` holds the outcome of the MCP list tools call. Optional parameters include `span_id` for explicit ID assignment (otherwise generated), `parent` for establishing a trace hierarchy, and `disabled` to prevent span recording.

--------------------------------

### Input > AudioInput dataclass

Source: https://openai.github.io/openai-agents-python/ja/ref/voice/input

The `AudioInput` dataclass represents static audio to be used as input for the `VoicePipeline`. It holds the audio data in a buffer, along with its frame rate, sample width, and number of channels. The `buffer` attribute must be a numpy array of int16 or float32. The `frame_rate` defaults to 24000, `sample_width` to 2, and `channels` to 1. This class provides methods to convert the audio data to a file format or a base64 encoded string.

--------------------------------

### MCP Util > ToolFilterContext > server_name

Source: https://openai.github.io/openai-agents-python/zh/ref/mcp/util

The `server_name` attribute within ToolFilterContext specifies the name of the MCP server. This information can be used by tool filters to apply server-specific rules or to differentiate tool availability based on the deployment environment.

--------------------------------

### Results > Other information > Raw responses

Source: https://openai.github.io/openai-agents-python/results

The `raw_responses` property holds the `ModelResponse` objects generated directly by the LLM.

--------------------------------

### OpenAI Agents Python > Usage Statistics

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/memory/advanced_sqlite_session

The `get_usage` method retrieves aggregated usage statistics for a given session, optionally filtered by a specific branch. It sums up requests, input tokens, output tokens, total tokens, and the number of turns from the `turn_usage` table. If `branch_id` is provided, it filters usage for that specific branch; otherwise, it aggregates usage across all branches associated with the session. The method handles potential `None` values by returning 0 for counts and sums, ensuring consistent data retrieval.

--------------------------------

### Realtime Configuration > Model Configuration > playback_tracker

Source: https://openai.github.io/openai-agents-python/ref/realtime/config

The `playback_tracker` in Model Configuration is an optional component for managing audio playback progress, particularly useful in scenarios with interruptions or when audio generation speed differs significantly from playback speed. If not provided, a default implementation assumes immediate playback at realtime speed. A custom playback tracker can inform the model about how much audio has actually been played to the user, which is beneficial in applications like phone calls or remote interactions where audio delivery might be delayed or interrupted.

--------------------------------

### Input filters

Source: https://openai.github.io/openai-agents-python/handoffs

When a handoff occurs, a new agent takes over the conversation and sees the entire previous conversation history. To modify this behavior, an `input_filter` can be set. An input filter is a function that accepts existing input via `HandoffInputData` and must return a new `HandoffInputData`. By default, the runner collapses the prior transcript into a single assistant summary message, which appears within a `<CONVERSATION HISTORY>` block. This block accumulates new turns if multiple handoffs happen in the same run. For custom message generation without a full `input_filter`, a mapping function can be provided via `RunConfig.handoff_history_mapper`. This default behavior is applied only when neither the handoff nor the run specifies an `input_filter`, preserving existing customized payloads. The nesting behavior for a single handoff can be overridden by passing `nest_handoff_history=True` or `False` to `handoff(...)`, which modifies `Handoff.nest_handoff_history`. If only the wrapper text for the generated summary needs adjustment, `set_conversation_history_wrappers` (and optionally `reset_conversation_history_wrappers`) can be called before running agents. Common patterns, such as removing all tool calls from history, are pre-implemented in `agents.extensions.handoff_filters`.

--------------------------------

### Session > clear_session

Source: https://openai.github.io/openai-agents-python/ko/ref/memory/session

The `clear_session` asynchronous method removes all conversation history associated with the current session, effectively resetting it.

--------------------------------

### FunctionTool `dataclass` > strict_json_schema `class-attribute` `instance-attribute`

Source: https://openai.github.io/openai-agents-python/ref/tool

The `strict_json_schema` attribute, a boolean defaulting to `True`, controls whether the JSON schema for the tool's parameters is enforced strictly. Setting this to `True` is highly recommended as it significantly increases the probability that the LLM will generate correctly formatted JSON input for the tool.

--------------------------------

### openai-agents-python/src/session.py > SQLiteSession > store_run_usage

Source: https://openai.github.io/openai-agents-python/ko/ref/extensions/memory/advanced_sqlite_session

The `store_run_usage` method is responsible for persisting usage data associated with a particular conversation turn. It's intended to be invoked after the `Runner.run()` method has successfully completed. The method first checks if there's any usage information available from the `result.context_wrapper`. If usage data exists, it retrieves the current turn number for the active branch and then calls `_update_turn_usage_internal` to store this turn-level usage. Session-level usage can be computed later by aggregating data from individual turns. Any exceptions encountered during this process are logged as errors.

--------------------------------

### OpenAI Python Agents > __init__

Source: https://openai.github.io/openai-agents-python/ref/models/multi_provider

The `__init__` method creates a new OpenAI provider. You can configure it by providing a `provider_map` for custom model mappings, or by specifying OpenAI API credentials such as `openai_api_key`, `openai_base_url`, `openai_organization`, and `openai_project`. Alternatively, you can pass in an existing `AsyncOpenAI` client. The `openai_use_responses` flag controls whether to utilize the OpenAI responses API. If no `provider_map` is provided, a default mapping will be used.

--------------------------------

### Configuring the SDK > API keys and clients

Source: https://openai.github.io/openai-agents-python/config

The SDK allows customization of the OpenAI API endpoint used. The default is the OpenAI Responses API. To switch to using the Chat Completions API, utilize the `set_default_openai_api()` function and pass the string `"chat_completions"`.

```python
from agents import set_default_openai_api

set_default_openai_api("chat_completions")
```

--------------------------------

### RealtimeAgent > clone

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/agent

The `clone` method creates a copy of the agent, allowing for modifications to specific arguments such as `instructions`. This is useful for creating variations of an agent without altering the original instance, facilitating experimentation and customization.

--------------------------------

### RunResult dataclass > context_wrapper instance-attribute

Source: https://openai.github.io/openai-agents-python/ko/ref/result

The `context_wrapper` attribute holds an instance of `RunContextWrapper`, which provides access to the execution context for the agent run. This context might contain shared state, configuration, or other resources that the agent can utilize during its operation. It plays a role in managing the environment in which the agent operates.

--------------------------------

### Run context > AgentHookContext dataclass > context instance-attribute

Source: https://openai.github.io/openai-agents-python/ko/ref/run_context

The `context` instance attribute in `AgentHookContext` refers to the context object, potentially `None`, that was passed to `Runner.run()`.

--------------------------------

### AgentOutputSchema dataclass

Source: https://openai.github.io/openai-agents-python/ja/ref/agent_output

The `AgentOutputSchema` dataclass is designed to manage the JSON schema of an agent's output, enabling both validation and parsing of JSON data generated by a Large Language Model (LLM) into the expected output type. It encapsulates the output type itself, a type adapter for validation, and the generated JSON schema. The `strict_json_schema` parameter, recommended to be set to `True`, enforces stricter validation rules, increasing the reliability of the LLM's JSON output. The schema generation logic handles cases where the output type might not be directly representable as a JSON object, by wrapping it in a dictionary if necessary. This ensures that even complex types can be processed correctly within a JSON-based interaction.

--------------------------------

### ModelSettings

Source: https://openai.github.io/openai-agents-python/zh/ref/model_settings

The `max_tokens` parameter specifies the maximum number of output tokens the model should generate. This is useful for controlling the length of the response and managing costs.

--------------------------------

### Direct model access

Source: https://openai.github.io/openai-agents-python/realtime/guide

You can access the underlying model to add custom listeners or perform advanced operations:
This gives you direct access to the `RealtimeModel` interface for advanced use cases where you need lower-level control over the connection.

--------------------------------

### Agent > clone

Source: https://openai.github.io/openai-agents-python/ja/ref/agent

The `clone` method provides a way to create a copy of an existing agent instance. It utilizes `dataclasses.replace`, which performs a shallow copy of the agent's attributes. This means that mutable attributes, such as `tools` and `handoffs`, are shallow-copied. New list objects for these attributes are only created if they are explicitly overridden during the `clone` call. Otherwise, the contents of these mutable attributes are shared between the original agent and the cloned agent. To ensure independent modification of these mutable attributes, new lists should be passed when calling the `clone` method.

--------------------------------

### Creating traces/spans > get_current_span

Source: https://openai.github.io/openai-agents-python/zh/ref/tracing/create

The `get_current_span()` function returns the currently active span, if one exists. Spans represent individual operations within a trace. This function allows you to access and manipulate the active span, for example, by adding events or attributes to it.

--------------------------------

### cancel

Source: https://openai.github.io/openai-agents-python/zh/ref/result

The `cancel` function is used to stop a streaming run. It supports two modes: `immediate` and `after_turn`. 

- `immediate`: This is the default mode. It stops the run immediately by canceling all active tasks and clearing any pending queues. This ensures a quick halt to the process.
- `after_turn`: This mode allows for a graceful shutdown. It lets the current turn of the LLM response complete, executes any pending tool calls, properly saves the session state, and accurately tracks usage before stopping. The run will halt before the beginning of the next turn, ensuring that ongoing operations are finished cleanly.

--------------------------------

### Creating traces/spans > get_current_span

Source: https://openai.github.io/openai-agents-python/ref/tracing/create

The `get_current_span()` function returns the currently active span, if one is present. Spans represent individual operations or units of work within a trace, and this function allows you to access the current span context.

--------------------------------

### SQLAlchemy Session > get_items async

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/memory/sqlalchemy_session

The `get_items` asynchronous method is used to retrieve the conversation history stored within a `SQLAlchemySession`. You can optionally specify a `limit` to fetch only the latest N items in chronological order. If `limit` is not provided, all items in the conversation history will be returned. This method ensures that the conversation history is retrieved in the correct chronological sequence, even when a limit is applied.

--------------------------------

### SQLAlchemy Session > from_url classmethod

Source: https://openai.github.io/openai-agents-python/ja/ref/extensions/memory/sqlalchemy_session

The `from_url` class method allows you to create a `SQLAlchemySession` instance directly from a database URL string. This is a convenient way to configure your session, especially when the database connection details are provided externally. It handles the creation of the underlying SQLAlchemy engine using the provided URL and any additional engine keyword arguments. Furthermore, it accepts other keyword arguments that are forwarded to the main constructor, enabling customization like table creation or specifying custom table names.

--------------------------------

### Span > error

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing/spans

The `error` property returns any error that occurred during the span's execution. If an error was recorded using `set_error()`, its details will be returned here; otherwise, it will be `None`.

--------------------------------

### Classes > Agent > Attributes > model_provider

Source: https://openai.github.io/openai-agents-python/zh/ref/run

The `model_provider` attribute specifies which model provider to use when looking up string model names. It defaults to OpenAI, ensuring that OpenAI's models are used by default for language generation tasks within the agent.

--------------------------------

### RealtimeModelConfig > playback_tracker

Source: https://openai.github.io/openai-agents-python/ko/ref/realtime/model

The `playback_tracker` option is used to monitor the progress of audio playback. If this is not set, the model assumes audio playback occurs instantly at realtime speed. A playback tracker is particularly useful for managing interruptions, as models can generate audio much faster than it can be played back. It helps the model understand how much audio the user has actually heard. While in low-latency scenarios assuming immediate playback is acceptable, in applications like phone calls or other remote interactions, a playback tracker informs the model about the user's audio consumption.

--------------------------------

### openai-agents-python/openai_agents/message.py > _classify_message_type

Source: https://openai.github.io/openai-agents-python/ko/ref/extensions/memory/advanced_sqlite_session

The `_classify_message_type` method determines the role or type of a given message item. It checks if the item is a dictionary and then inspects the 'role' or 'type' keys to categorize it as 'user', 'assistant', or a specific type defined in the item. If none of these conditions are met, it defaults to 'other'.

--------------------------------

### handoff_span

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `handoff_span` function is used to create a new handoff span. This span is not started automatically, meaning you need to manually start and finish it using `span.start()` and `span.finish()`, or by using it within a `with` statement like `with handoff_span() ...`. The function takes several parameters: `from_agent` specifies the name of the agent performing the handoff, and `to_agent` specifies the name of the agent receiving it. An optional `span_id` can be provided; if not, one will be generated, and it's recommended to use `util.gen_span_id()` for correct formatting. The `parent` parameter allows you to specify a parent span or trace, defaulting to the current one if not provided. The `disabled` boolean flag, if set to `True`, will create a Span object but prevent it from being recorded. The function returns a `Span[HandoffSpanData]` object representing the newly created handoff span.

--------------------------------

### openai-agents-python/src/langchain_openai/chat_models/orm.py > SQLiteSession > _get_next_turn_number, _get_next_branch_turn_number

Source: https://openai.github.io/openai-agents-python/zh/ref/extensions/memory/advanced_sqlite_session

Methods like `_get_next_turn_number` and `_get_next_branch_turn_number` are crucial for maintaining conversational state. They query the `message_structure` table to find the maximum existing turn or branch turn number for a given session and branch, and then return the next sequential number. This ensures that each turn and branch within a conversation has a unique and ordered identifier, which is essential for reconstructing the conversation flow accurately.

--------------------------------

### spans.py > Span > finish

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

Finish the span.

Args:
    reset_current: If true, the span will be reset as the current span.

--------------------------------

### Agent Attributes > clone

Source: https://openai.github.io/openai-agents-python/ref/agent

This method creates a copy of the agent, allowing specific arguments to be modified. It utilizes `dataclasses.replace`, which performs a shallow copy. Mutable attributes such as `tools` and `handoffs` are also shallow-copied; new list objects are only generated if these attributes are overridden. Otherwise, their contents (tool functions and handoff objects) are shared with the original agent. To independently modify these mutable attributes, you should provide new lists when calling `clone()`. For instance, `new_agent = agent.clone(instructions="New instructions")` would create a new agent with updated instructions.

--------------------------------

### OpenAI Agents Python > Tracing > Processor Interface > on_trace_start

Source: https://openai.github.io/openai-agents-python/ko/ref/tracing

The `on_trace_start` method is invoked synchronously when a new trace begins execution. It receives the `Trace` object as a parameter, which includes the workflow name and associated metadata. Implementers should ensure this method returns quickly to avoid blocking the main execution flow. Any errors encountered within this method should be handled internally to prevent disruptions.

--------------------------------

### MCPServerSse

Source: https://openai.github.io/openai-agents-python/ref/mcp/server

The `MCPServerSse` class is an implementation of the MCP server that utilizes the HTTP with SSE (Server-Sent Events) transport. This allows for efficient, one-way communication from the server to the client. Detailed specifications for this transport can be found at the provided link. The `__init__` method configures the server with necessary parameters, including the server URL, headers, timeouts, and options for caching tools lists, filtering tools, and handling structured content. It also allows for retry attempts and backoff strategies for network operations.

--------------------------------

### Classes > Agent > Attributes > handoff_history_mapper

Source: https://openai.github.io/openai-agents-python/zh/ref/run

The `handoff_history_mapper` attribute is an optional function that receives the normalized transcript (including history and handoff items) and returns the input history that should be passed to the next agent. If this is left as `None`, the runner collapses the transcript into a single assistant message. This mapper function only runs when `nest_handoff_history` is set to `True`, providing a way to customize how history is passed during agent handoffs.

--------------------------------

### Tracing > trace_id

Source: https://openai.github.io/openai-agents-python/ja/ref/tracing

The `trace_id` is a unique identifier for a trace, formatted as 'trace_<32_alphanumeric>'. These IDs are globally unique and are crucial for linking spans to their parent trace. They can also be used to look up specific traces in the dashboard for monitoring and debugging purposes.