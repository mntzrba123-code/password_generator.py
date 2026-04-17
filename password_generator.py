# 🧪 Lab Exercise: Random Password Generator

## 📋 Task Description

In this exercise, you will build a Python program that generates **100,000 random passwords** by combining personal information in various ways.

> **🎯 Learning Objective:** Understand why using personal information (such as name, birth year, hobbies) as a basis for passwords is dangerous, and how easily they can be generated programmatically.

---

## 📦 Given Data

```python
name     = ["Ali", "Mustafa"]
year     = ["1990"]
football = ["Messi"]
car      = ["Nissan"]
cat      = ["Siri"]
son      = ["Ahmed"]
```

---

## 📝 Requirements

Write a Python program that does the following:

### 1. Password Generation

Combine elements from the lists above in different ways to create varied passwords, such as:

- `Ali1990`
- `Messi@1990`
- `Nissan_Ahmed`
- `Siri2024!`
- And other combinations...

### 2. Conditions to Apply

- [ ] The program must include at least **5 different patterns** for generating passwords
- [ ] Must add **random numbers** (0–9999) in some patterns
- [ ] Must add **special characters** (`@`, `#`, `_`, `!`, `$`) in some patterns
- [ ] Some passwords must use **mixed uppercase and lowercase** letters
- [ ] Must save the output to a text file named `passwords.txt`
- [ ] The file must contain **exactly 100,000 passwords** (no duplicates)

### 3. Program Output

```
✅ Successfully generated 100000 passwords!
📁 Saved to: passwords.txt
⏱️  Time elapsed: X.XX seconds
```

---

---

## 📊 Grading Criteria

| Criterion                                     | Grade |
| --------------------------------------------- | ----- |
| Generate 100,000 passwords with no duplicates | 30%   |
| Pattern variety (at least 5)                  | 25%   |
| Adding numbers and special characters         | 20%   |
| Saving results to a file                      | 15%   |
| Code cleanliness and comments                 | 10%   |

---

## ⚠️ Important Security Note

> This exercise is for **educational and awareness purposes only.**
> Its goal is to demonstrate that passwords based on personal information **can be easily guessed** through Dictionary Attacks.
> **Never use** your name, birth year, or names of loved ones as the basis for your real passwords!

---

## 📤 Submission

- Python file named: `password_generator.py`
- Results file: `passwords.txt`
- Deadline: 17-4-2026