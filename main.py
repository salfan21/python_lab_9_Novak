def encrypt_caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():  # перевіряємо, чи символ є літерою
            is_upper = char.isupper()  # визначаємо, чи є літера великою
            char = char.lower()  # переводимо літеру в малу
            char_code = ord(char) - ord('a')  # отримуємо числове значення літери (a=0, b=1, ..., z=25)
            shifted_char_code = (char_code + shift) % 26  # зміщуємо зашифроване значення
            shifted_char = chr(shifted_char_code + ord('a'))  # перетворюємо назад в символ
            if is_upper:
                shifted_char = shifted_char.upper()  # відновлюємо велику літеру, якщо була великою
            result += shifted_char
        else:
            result += char  # якщо символ не є літерою, залишаємо його без змін
    return result

# Запитуємо у користувача рядок для шифрування
user_input = input("Введіть рядок для шифрування: ")

# Захищаємося від некоректного введення зсуву
while True:
    try:
        # Запитуємо у користувача значення зсуву
        shift_value = int(input("Введіть значення зсуву (ціле число від 1 до 25): "))
        if 1 <= shift_value <= 25:
            break  # якщо значення зсуву коректне, виходимо з циклу
        else:
            print("Будь ласка, введіть коректне значення зсуву.")
    except ValueError:
        print("Будь ласка, введіть ціле число.")

# Виводимо зашифрований текст
encrypted_text = encrypt_caesar_cipher(user_input, shift_value)
print("Зашифрований текст:", encrypted_text)