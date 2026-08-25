# Cryptography Lab

A collection of Python implementations for classical and modern cryptographic algorithms, pseudo-random number generators, and basic cybersecurity tools — developed as part of a Cryptography & Network Security laboratory course.

## 📁 Repository Structure

```
Cryptography_Lab/
├── Experiment 1/   → Number Theory for RSA
├── Experiment 2/   → Pseudo Random Bit Generators
├── Experiment 3/   → Classical Substitution Ciphers
├── Experiment 4/   → Modern Encryption & Hashing Algorithms
├── Experiment 5/   → Digital Signature Algorithm (DSA)
├── Experiment 6/   → Linux Privilege Escalation Checker
├── Experiment 7/   → Keyboard Event Monitoring (Tkinter GUI)
└── Experiment 8/   → Honeypot & TCP Client-Server Communication
```

## 🧪 Experiments

### Experiment 1 — Number Theory for RSA
- **1** — Prime Number Validation for RSA Key Generation
- **1.b** — Coprime Verification using the Euclidean Algorithm (GCD)
- **1.c** — Modular Arithmetic Calculator (addition, subtraction, multiplication, exponentiation)
- **1.d** — Fermat's Little Theorem Primality Test
- **1.e** — Euler's Totient Function & Euler's Theorem Verification
- **1.Extra** — Military Secure Communication using Coprime Verification

### Experiment 2 — Pseudo Random Bit Generators (PRBGs)
- **2.A** — Linear Congruential Generator (LCG)
- **2.B** — Blum Blum Shub (BBS) Generator
- **2.C** — Linear Feedback Shift Register (LFSR)

### Experiment 3 — Classical Substitution Ciphers
- **3.A** — Caesar Cipher
- **3.B** — Playfair Cipher
- **3.C** — Hill Cipher (2×2 key matrix)
- **3.D** — Vigenère Cipher

### Experiment 4 — Modern Cryptographic Algorithms
- **4.A** — DES Symmetric Encryption/Decryption
- **4.B** — RSA Public-Key Encryption/Decryption
- **4.C** — MD5 Hashing
- **4.D** — SHA-1 Hashing

### Experiment 5 — Digital Signatures
- Digital Signature Algorithm (DSA) — key generation, signing, and verification using SHA-256

### Experiment 6 — System Security
- Linux Privilege Escalation Checker — scans for SUID files, sudo misconfigurations, world-writable files, and sensitive file permissions

### Experiment 7 — GUI-Based Monitoring
- Keyboard Event Monitoring application built with Python Tkinter

### Experiment 8 — Network Security
- **8.a** — Basic TCP Honeypot with client connection logging
- **8.b** — Honeypot with two-way TCP client-server message exchange

## 🛠️ Requirements

```bash
pip install pycryptodome numpy
```

- Python 3.8+ (required for `pow(a, -1, m)` modular inverse syntax used in Experiments 1, 4, and 5)
- Tkinter (bundled with standard Python; required for Experiment 7)
- A Linux environment recommended for Experiment 6
- Two terminal sessions required for running server/client pairs in Experiment 8

## ▶️ How to Run

Each experiment folder contains standalone `.py` scripts. Run any file directly:

```bash
python "Experiment 1/prime_validation.py"
```

For Experiment 8 (honeypot), run the server script first, then the client script in a separate terminal window while the server is active.

## 📖 Course Context

These experiments cover foundational and applied topics in Cryptography and Network Security, including number theory, classical ciphers, modern symmetric/asymmetric encryption, hashing, digital signatures, and basic offensive/defensive security tooling.

## 👤 Author

**Elangumaran05**
