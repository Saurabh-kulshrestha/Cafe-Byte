# ☕ Cafe Byte  – Python Console Simulation

**Experience the aroma of coding and coffee combined!** This terminal-based Python project lets users simulate a coffee machine — complete with drink selections, cash payments (₹), real-time resource management, and special admin-only commands. Built for learning, practicing logic, and having fun.

---

## 🚀 Features

- 🧾 **Drink Options** – Choose from Espresso, Latte, or Cappuccino.
- 💸 **Real Cash Simulation** – Pay using ₹100, ₹50, ₹20, and ₹10 denominations.
- 🛠️ **Resource Management** – The machine tracks milk, water, coffee, and money.
- 🧠 **Auto Check** – Not enough ingredients? Get an instant alert.
- 💰 **Smart Refunds** – Get your extra change back instantly.
- 👨‍💻 **Admin Mode**
  - `report` → View the machine's current resource status
  - `off` → Shutdown the machine safely
- 🎨 Beautiful ASCII Art Logo and Divider for enhanced console UI

---

## 🧩 Project Structure

```bash
VirtualCoffeeMachine/
├── main.py          # Main game logic – handles UI, resources, and transactions
├── game_data.py     # Contains resources, menu, logo, and formatting tools
├── screenshot.png   # Console screenshot preview of the working program
└── README.md        # This file – full documentation of the project
```

---

## 🖥️ How to Play

1. Run the program using:

```bash
python main.py
```

2. When prompted, type your drink choice:
   - `espresso`, `latte`, or `cappuccino`
3. Insert currency when asked (₹100/₹50/₹20/₹10).
4. If payment is sufficient and ingredients are available, enjoy your virtual drink ☕
5. Use admin commands for more control:
   - `report` → Shows current resources
   - `off` → Turns off the machine

---

## 🧠 What I Learned

- Structured programming with real-time input handling
- Modular coding with clear separation of UI and logic
- Simulating a real-world system with cash handling
- Improved user experience with ASCII art and clear formatting
- How to write admin features and status-based decision-making

---

## 👨‍💻 Developer Highlight

This project includes a hidden **admin mode** for developers. Type `report` to access a full resource report, and `off` to turn off the machine. Ideal for debugging and showcasing control features in software systems.

---

## 🙌 Developed By

**Saurabh Kulshrestha**\
`Python Developer | Terminal Game Creator | Learning by Building`

---