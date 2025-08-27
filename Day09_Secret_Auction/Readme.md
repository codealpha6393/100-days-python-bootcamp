# 🏆 Secret Auction Bidding Program  

A simple Python project from **Day 9 of Angela Yu’s 100 Days of Code** course.  
This program allows multiple users to place secret bids and determines the highest bidder.  

---
## 💻 Code Screenshot  

Here’s the core implementation of the Secret Auction program:  

![Code Screenshot](./Day09_Secret_Auction/bidding.png)

## 🚀 Features  
- Collects bids from multiple users  
- Uses **dictionaries** to store bidder names and bid amounts  
- Finds the **highest bidder** automatically  
- Clears the console to keep bids secret (for fairness)  
- Demonstrates **loops, functions, and data structures**  

---

## 🛠️ Tech Stack  
- **Python 3**  

---

## 📂 How It Works  
1. The program asks each participant for their **name** and **bid amount**.  
2. After each entry, it checks if there are more bidders.  
3. Console is cleared (to hide previous bids).  
4. When no more bidders remain, the program compares bids and declares the **winner**.  

---

## 📜 Example Run  

Welcome to the secret auction program!
What is your name?: Alice
What's your bid?: $200
Are there any other bidders? Type 'yes' or 'no': yes

(Next bidder enters…)

The winner is Bob with a bid of $350


---

## 📖 Concepts Learned  
- Dictionaries in Python  
- Functions & loops  
- Program flow control  
- Clearing console outputs  

---

## ▶️ How to Run  
```bash
# Clone this repository
git clone https://github.com/your-username/secret-auction.git  

# Navigate to the folder
cd secret-auction  

# Run the program
python main.py  
