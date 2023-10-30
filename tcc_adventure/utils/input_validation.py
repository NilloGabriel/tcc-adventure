def get_valid_alpha_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.isalpha():
            return user_input
        else:
            print("Entrada inválida. Deve conter apenas letras. Tente novamente.")


def get_valid_numeric_input(prompt, data_list):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            user_input = int(user_input)
            if 1 <= user_input <= len(data_list):
                return user_input
        print("Opção inválida. Tente novamente.")
