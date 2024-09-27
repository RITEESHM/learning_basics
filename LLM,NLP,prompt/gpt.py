from chatgpt_bot import conversation
conversation = Conversation("some random ID", api_key="YOUR_OPENAI_API_KEY")
conversation.ask("Hi, how are you today?")
conversation.set_metadata({"anything": "here"})
conversation.get_metadata()
{"anything": "here"}
