import sys
from typing import Optional

class CreditCardValidator:
    """
    A professional, object-oriented utility to validate credit card numbers
    using the Luhn Algorithm and determine their issuing network.
    """

    NETWORK_PREFIXES = {
        "Visa": ("4",),
        "Mastercard": ("51", "52", "53", "54", "55"),
        "American Express": ("34", "37"),
        "Discover": ("6011",)
    }

    def __init__(self, raw_number: str):
        """
        Initializes the validator and sanitizes the input by removing spaces and dashes.
        """
        self.raw_number = raw_number
        self.card_number = raw_number.replace(" ", "").replace("-", "")

    def is_valid_format(self) -> bool:
        """
        Checks if the card number contains only digits and has a valid length.
        Standard credit cards range between 13 and 19 digits.
        """
        if not self.card_number.isdigit():
            return False
        if not (13 <= len(self.card_number) <= 19):
            return False
        return True

    def get_network(self) -> str:
        """
        Determines the issuing network of the credit card based on its IIN prefix.
        
        Returns:
            str: The name of the network (e.g., 'Visa', 'Mastercard') or 'Unknown'.
        """
        for network, prefixes in self.NETWORK_PREFIXES.items():
            if self.card_number.startswith(prefixes):
                return network
        return "Unknown"

    def validate_luhn(self) -> bool:
        """
        Validates the credit card number using the Luhn Algorithm.
        
        Returns:
            bool: True if the card passes the Luhn check, False otherwise.
        """
        total = 0
        # Reverse the digits for easier index-based calculation
        reverse_digits = self.card_number[::-1]

        for i, char in enumerate(reverse_digits):
            digit = int(char)

            # Double every second digit
            if i % 2 == 1:
                digit *= 2
                # If doubling results in a number > 9, subtract 9 (equivalent to summing digits)
                if digit > 9:
                    digit -= 9
            
            total += digit

        return total % 10 == 0

    def validate(self) -> None:
        """
        Executes the full validation flow and prints the result to stdout.
        """
        if not self.is_valid_format():
            print("❌ INVALID - Check length and characters.")
            return

        if self.validate_luhn():
            network = self.get_network()
            print(f"✅ VALID - Detected network: \033[94m{network}\033[0m")
        else:
            print("❌ INVALID - Failed Luhn algorithmic check.")


def main() -> None:
    """
    Main entry point for the terminal application.
    """
    print("\n" + "="*40)
    print("💳 Credit Card Validator Engine")
    print("="*40)
    
    try:
        raw_input = input("\nEnter credit card number (or 'q' to quit): ").strip()
        if raw_input.lower() in ('q', 'quit', 'exit'):
            sys.exit(0)
            
        validator = CreditCardValidator(raw_input)
        validator.validate()
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()