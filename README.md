# 🔍 Special Numbers Finder – Prime & Palindromic Checker
### COMP1819 – Algorithms and Data Structures (2023/24)

This Python-based project identifies **special numbers** — integers that are both **prime** and **palindromic** — between two given values. The task was part of our group coursework for the COMP1819 module at the University of Greenwich.

---

## 🚗 Project Summary

Given two user inputs `m` and `n` (`m < n`), the program:
- Finds all numbers between `m` and `n` that are **prime** and **palindromic**.
- If fewer than 6 such numbers exist, displays all of them.
- If 6 or more, displays only the first 3 and last 3.
- Times the execution of the algorithm.
- Includes performance tests, runtime graphs, and optimization strategies.

---

## 👥 Team Members

| Name | Role |
|------|------|
| **Bryan Hernandez Upegui** | Solution 1, performance testing, optimization, report writing |
| **Nikmal Niazi** | Alternate implementation, runtime benchmarking |
| **Louis Anthony Luz** | OOP-based version with class usage |
| **Abdalla Saleh** | Error handling, user interaction improvements |
| **Alana Taiana Alpoim Ferreira do Rosario** | Display logic improvements, performance tweaks |

---

## 📂 Repository Contents

| File | Description |
|------|-------------|
| `solution.py` | Core solution script (Bryan's version) |
| `report.pdf` | Final PDF report (from `10_CW.pdf`) |
| `README.md` | This file |
| `performance_analysis/` | Graphs and benchmark results |
| `other_versions/` | Alternative implementations by other team members |

---

## 🚀 Features

- Efficient primality check using square root method
- Palindromic check using string reversal
- Runtime and performance tracking with Python’s `time` module
- Handles edge cases and invalid user input
- Modular design across all team versions

---

## 📈 Sample Output
- Enter the lower limit (m): 100
- Enter the upper limit (n): 10000
- Total: Special Numbers = 15
- List of special numbers = [101, 131, 151, 797, 919, 929]
- Execution time: 0.009050 seconds
---

## ⚙️ Technologies Used

- Python 3.x
- Standard library: `math`, `time`
- No external libraries required

---

## 📄 License & Acknowledgements

This coursework was submitted as part of an official module at the University of Greenwich.  
Use of this code is limited to educational and demonstration purposes.  
All contributors listed above have approved this public posting.

---

## 📬 Contact

For questions, collaborations, or clarification, feel free to reach out via GitHub or [LinkedIn](https://linkedin.com).


