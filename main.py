from llama_index.llms.ollama import Ollama

main_model = "SpeakLeash/bielik-11b-v2.3-instruct:Q5_K_M"

def run_ollama(ollama_model):
    llm = Ollama(model=ollama_model, request_timeout=6)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_ollama(main_model)

