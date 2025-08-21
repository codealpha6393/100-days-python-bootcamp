# 🔐 Caesar Cipher

An implementation of the ancient Caesar Cipher algorithm for encrypting and decrypting messages. This is my solution for **Day 8** of Dr. Angela Yu's [**100 Days of Code: The Complete Python Pro Bootcamp**](https://www.udemy.com/course/100-days-of-code/).

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Complete-success)

## 📖 Table of Contents

- [✨ Overview](#-overview)
- [❓ What is a Caesar Cipher?](#-what-is-a-caesar-cipher)
- [🌟 Features](#-features)
- [🛠️ How It Works](#️-how-it-works)
- [📁 Project Structure](#-project-structure)
- [🎯 What I Learned](#-what-i-learned)
- [🚀 How to Use](#-how-to-use)
- [📸 Screenshots](#-screenshots)

## ✨ Overview

This Python program allows a user to encrypt or decrypt a message using a Caesar Cipher. The user provides the text, a shift value (the key), and specifies the direction (encode or decode). The program handles both uppercase and lowercase letters while preserving numbers, symbols, and spaces. 🧠

This project was a fantastic exercise in manipulating characters based on their ASCII values and understanding fundamental cryptography concepts.

## ❓ What is a Caesar Cipher?

The Caesar Cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. 🏛️

For example, with a shift of 3:
- 'A' becomes 'D'
- 'B' becomes 'E'
- ...
- 'X' becomes 'A' (wrapping around from Z to A)
- 'Y' becomes 'B'
- 'Z' becomes 'C'

## 🌟 Features

- **🔄 Encode or Decode:** Allows the user to either encrypt a message or decrypt a previously encrypted message.
- **🔢 Shift Handling:** Correctly handles shifts larger than 26 by using the modulo operator (`%`).
- **💎 Preserves Formatting:** Maintains spaces, numbers, punctuation, and casing (upper/lower) in the message.
- **👤 User-Friendly Interface:** Guides the user through the process with clear prompts and cool ASCII art.
- **🎨 ASCII Art:** Features a stylish logo for a more engaging user experience.

## 🛠️ How It Works

The core logic involves:
1.  **🔁 Iterating** through each character in the input text.
2.  **✅ Checking** if the character is an alphabetic letter.
3.  **↪️ Shifting** the character's ASCII value by the specified amount.
4.  **🔄 Wrapping Around:** Using modulo 26 to ensure the shift wraps around from 'z' back to 'a' (or 'Z' to 'A').
5.  **🏗️ Rebuilding** the result string with the shifted characters, leaving non-alphabetic characters unchanged.

The formula for a character `char` with shift `s` is essentially:
`new_char = (position(char) + s) % 26`

## 📁 Project Structure

The main logic of the cipher is contained within a single Python file:

├── main.py # The main script containing the cipher logic
├── screenshot #demo img
│── art.py #ascii art of caeser cipher
└── README.md # This file


## 🎯 What I Learned / Key Concepts Practiced

This project was an excellent deep dive into several key Python programming concepts:

- **📦 Functions:** Creating reusable functions for the core encoding/decoding logic (`caesar()`).
- **📨 Parameters & Arguments:** Passing information (text, shift, direction) into functions.
- **⚙️ Control Flow:** Using `if/elif/else` statements to handle user choices and character types.
- **🎨 ASCII Art:** Using multi-line strings to create a visual header for the program.
- **🔤 String Manipulation:** Advanced techniques for working with and modifying individual characters in a string.
- **➗ Modulo Operator (`%`):** Crucial for implementing the "wrap-around" effect of the alphabet.
- **⌨️ User Input & Validation:** Handling user input and guiding them through the program's options.

## 🚀 How to Use

1.  **Ensure you have Python 3 installed** on your system.
2.  **Clone or download** this project to your local machine.
3.  **Navigate to the project directory** in your terminal or command prompt.
4.  **Run the program** using the following command:

```bash
python caesar_cipher.py
```
 ## 📸 Screeshot
 <img src="/Screenshot.png" alt="Caesar Cipher Program Screenshot" width="600"/>
