

def load_server_instructions():
    try:
        with open("src/clinicaltrials/instructions/server_instructions.txt", "r", encoding="utf-8") as file:
            server_instruction_text = file.read()
        print("Server instructions loaded successfully.")
        return server_instruction_text
    except FileNotFoundError:
        print("Warning: server_instructions.txt not found. Continuing without instructions.")
        return None

if __name__ == "__main__":
    load_server_instructions()