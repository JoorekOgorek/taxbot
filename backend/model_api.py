from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage

main_model = "SpeakLeash/bielik-11b-v2.3-instruct:Q5_K_M"

# main_model = "codellama:latest"

llm = Ollama(model=main_model, request_timeout=60, temperature=0.1)


def run_ollama(question):
    messages = [
        ChatMessage(
            role="system", content="Jesteś pracownikiem urzędu skarbowego w Polsce. Twoim celem jest pomoc płatnikom w wypełnieniu formularza PCC-3. Uźywaj formalnego języka i pisz proste, ale dokładne instrukcje."

        ),
        ChatMessage(role="user", content=question),
    ]
    response = llm.chat(messages)
    print(type(response))
    print(response)
    return response.__str__()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # main_model = "codellama:latest"
    run_ollama(main_model, "hi there")

