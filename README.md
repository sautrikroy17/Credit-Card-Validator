<div align="center">
  <img src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" alt="C++" />
  <img src="https://img.shields.io/badge/Algorithm-Luhn-blueviolet?style=for-the-badge" alt="Algorithm" />
  <img src="https://img.shields.io/badge/GSSoC'26-Open_Source-orange?style=for-the-badge&logo=girlscript" alt="GSSoC" />
  
  <br />
  <br />

  <h1>💳 Credit Card Validator</h1>
  <p><strong>A Lightning-Fast C++ Implementation of the Luhn Algorithm</strong></p>
</div>

---

## 📖 Overview

The **Credit Card Validator** is a highly efficient, terminal-based C++ program designed to validate credit card numbers in real-time. It not only verifies the mathematical authenticity of a card number using the industry-standard **Luhn Algorithm**, but also identifies the card's issuing network (e.g., Visa, MasterCard, American Express).

*A perfect example of low-level string manipulation, algorithmic logic, and performant C++ architecture.*

---

## ✨ Features

- **✅ Luhn Algorithm Validation:** Computes the checksum mathematically to verify card legitimacy.
- **🌐 Network Identification:** Automatically detects and displays the card provider based on IIN (Issuer Identification Number) prefixes.
- **⚡ Zero Dependencies:** Written in pure, standard C++ (C++11 and above).
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

## 💻 Compilation & Usage

This program requires a standard C++ compiler (like `g++` or `clang++`).

### 1. Compile the code
```bash
g++ -std=c++11 -o validator validator.cpp
```

### 2. Run the executable
```bash
./validator
```
*(You will be prompted to enter a credit card number in the terminal)*

---

## 🤝 Contributing (GSSoC Welcome!)

Contributions make the open-source community an amazing place. If you are participating in **GirlScript Summer of Code (GSSoC)** or simply want to improve this tool, please consider contributing!

**Ideas for Contribution:**
- Add a GUI using Qt or ImGui.
- Implement file-based batch validation (read from `.txt` or `.csv`).
- Optimize the core loop for massive datasets.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

---

<div align="center">
  <sub>Built with C++ & ❤️ by Sautrik Roy</sub>
</div>
