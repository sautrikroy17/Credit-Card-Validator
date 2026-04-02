def get_card_network(card_number):
    if card_number.startswith('4'):
        return "Visa"
    elif card_number.startswith(('51', '52', '53', '54', '55')):
        return "Mastercard"
    elif card_number.startswith(('34', '37')):
        return "American Express"
    elif card_number.startswith('6011'):
        return "Discover"
    return "Unknown"

def validate_luhn(card_number):
    total = 0
    reverse_digits = card_number[::-1]
    
    for i, char in enumerate(reverse_digits):
        digit = int(char)
        
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
                
        total += digit
        
    return total % 10 == 0

def main():
    raw_input = input("Enter credit card number: ")
    
    card_number = raw_input.replace(" ", "").replace("-", "")
    
    if not card_number.isdigit() or len(card_number) < 13 or len(card_number) > 19:
        print("INVALID - Check length and characters")
        return
        
    if validate_luhn(card_number):
        network = get_card_network(card_number)
        print(f"VALID - Detected network: {network}")
    else:
        print("INVALID - Failed Luhn check")

if __name__ == "__main__":
    main()