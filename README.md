<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Algorithm-Luhn-blueviolet?style=for-the-badge" alt="Algorithm" />
  <img src="https://img.shields.io/badge/GSSoC'26-Open_Source-orange?style=for-the-badge&logo=girlscript" alt="GSSoC" />
  
  <br />
  <br />

  <h1>💳 Credit Card Validator</h1>
  <p><strong>An Elegant, Object-Oriented Python Implementation of the Luhn Algorithm</strong></p>
</div>

---

## 📖 Overview

The **Credit Card Validator** is a highly efficient, terminal-based Python program designed to validate credit card numbers in real-time. It verifies the mathematical authenticity of a card number using the industry-standard **Luhn Algorithm**, and identifies the card's issuing network (e.g., Visa, MasterCard, American Express).

*A perfect example of object-oriented design, robust error handling, and clean Python architecture.*

---

## ✨ Features

- **✅ Luhn Algorithm Validation:** Computes the checksum mathematically to verify card legitimacy.
- **🌐 Network Identification:** Automatically detects and displays the card provider based on IIN (Issuer Identification Number) prefixes.
- **⚡ OOP Architecture:** Written in standard Python with strict type hinting, docstrings, and a modular class structure.
- **🛡️ Robust Input Handling:** Gracefully handles invalid characters, spaces, and edge cases in user input.

---

## 🧠 How It Works (The Luhn Algorithm)

1. Drop the last digit (the check digit).
2. Reverse the remaining sequence of digits.
3. Multiply the digits in odd positions (1st, 3rd, 5th, etc.) by 2.
4. Subtract 9 from any product that is greater than 9.
5. Sum all the digits.
6. The total modulo 10 must equal the check digit.

---

## 💻 Usage

This program requires Python 3.6 or higher.

### 1. Run the script
```bash
python3 credit.py
```
*(You will be prompted to enter a credit card number in the terminal)*

---

## 🤝 Contributing (GSSoC Welcome!)

Contributions make the open-source community an amazing place. If you are participating in **GirlScript Summer of Code (GSSoC)** or simply want to improve this tool, please consider contributing!

**Ideas for Contribution:**
- Add a GUI using Tkinter or PyQt.
- Implement file-based batch validation (read from `.txt` or `.csv`).
- Optimize the core loop for massive datasets using NumPy.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

---

<div align="center">
  <sub>Built with Python & ❤️ by Sautrik Roy</sub>
</div>
