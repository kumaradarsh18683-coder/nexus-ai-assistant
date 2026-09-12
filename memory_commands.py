from memory import remember, recall, get_all_memory, forget

def handle_memory(command):

    command = command.lower().strip()

        # Natural memory
    if command.startswith("my ") and " is " in command:

        text = command.replace("my ", "", 1)

        key, value = text.split(" is ", 1)

        remember(key.strip(), value.strip())

        return f"Theek hai Boss, maine yaad rakh liya ki aapka {key} {value}."
    

        # I live in ...
    elif command.startswith("i live in "):

        city = command.replace("i live in ", "").strip()

        remember("city", city)

        return f"Theek hai Boss, mujhe yaad rahega ki aap {city} me rehte ho."

    # I study in ...
    elif command.startswith("i study in "):

        college = command.replace("i study in ", "").strip()

        remember("college", college)

        return f"Theek hai Boss, mujhe yaad rahega ki aap {college} me padhte ho."

    # Save memory
    if command.startswith("remember "):

        text = command.replace("remember ", "", 1)

        if " is " not in text:
            return "Remember command ka format hai: remember city is Delhi"

        key, value = text.split(" is ", 1)

        remember(key.strip(), value.strip())

        return f"Okay Boss, mujhe yaad rahega ki {key} {value}."
    
        # Where do I live?
    elif command == "where do i live":

        city = recall("city")

        if city:
            return f"Aap {city} me rehte ho."

        return "Mujhe nahi pata aap kahan rehte ho."

    # Where do I study?
    elif command == "where do i study":

        college = recall("college")

        if college:
            return f"Aap {college} me padhte ho."

        return "Mujhe nahi pata aap kahan padhte ho."
    
        # What's my ...
    elif command.startswith("what's my "):

        key = command.replace("what's my ", "").strip()

        value = recall(key)

        if value:
            return f"Your {key} is {value}"

        return "Mujhe ye yaad nahi hai."

    elif command.startswith("what is my "):

        key = command.replace("what is my ", "").strip()

        value = recall(key)

        if value:
            return f"Your {key} is {value}"

        return "Mujhe ye yaad nahi hai."

    # Recall memory
    elif command.startswith("what is "):

        key = command.replace("what is ", "", 1).strip()

        value = recall(key)

        if value:
            return f"{key} is {value}"

        return "Mujhe ye yaad nahi hai."
    
        # Tell me about me
    elif command == "tell me about me":

        data = get_all_memory()

        if not data:
            return "Boss, mujhe abhi aapke baare me kuch yaad nahi hai."

        answer = "Boss, mujhe aapke baare me ye yaad hai:\n\n"

        for key, value in data.items():
            answer += f"{key.title()} : {value}\n"

        return answer
    
        # Who am I?    # Who am I?
    elif command == "who am i":

        data = get_all_memory()

        if not data:
            return "Boss, mujhe abhi aapke baare me kuch yaad nahi hai."

        if "name" in data:
            return f"Aap {data['name']} ho."

        return "Boss, mujhe abhi aapka naam yaad nahi hai."
    elif command == "who am i":

        data = get_all_memory()

        if not data:
            return "Boss, mujhe abhi aapke baare me kuch yaad nahi hai."

        if "name" in data:
            return f"Aap {data['name']} ho."

        return "Boss, mujhe abhi aapka naam yaad nahi hai."
    
    
        # Forget memory
    elif command.startswith("forget my "):

        key = command.replace("forget my ", "").strip()

        if forget(key):

            return f"Okay Boss, maine {key} bhool gaya."

        return f"Mujhe {key} yaad hi nahi tha."

    elif command.startswith("forget "):

        key = command.replace("forget ", "").strip()

        if forget(key):

            return f"Okay Boss, maine {key} bhool gaya."

        return f"Mujhe {key} yaad hi nahi tha."

    return None