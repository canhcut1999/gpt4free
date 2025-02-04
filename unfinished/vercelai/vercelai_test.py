import vercelai

for token in vercelai.Completion.create('summarize the gnu gpl 1.0'):
    print(token, end='', flush=True)








[if





json_data = {
    'prompt': 'hello\n',
    'model': 'openai:gpt-3.5-turbo',
    'temperature': 0.7,
    'maxTokens': 200,
    'topK': 1,
    'topP': 1,
    'frequencyPenalty': 1,
    'presencePenalty': 1,
    'stopSequences': [],
}








]