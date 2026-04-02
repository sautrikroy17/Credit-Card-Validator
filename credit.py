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

def main():
    raw_input = input("Enter credit card number: ")
    card_number = raw_input.replace(" ", "").replace("-", "")
    
    if not card_number.isdigit() or len(card_number) < 13 or len(card_number) > 19:
        print("INVALID - Check length and characters")
        return
        
    network = get_card_network(card_number)
    print(f"Format check passed. Detected network: {network}")

if __name__ == "__main__ ":
    main()