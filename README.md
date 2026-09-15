# Cryptography Lab

A collection of Python implementations for classical and modern cryptographic algorithms, pseudo-random number generators, network security mechanisms, and cybersecurity assessment tools — developed as part of a Cryptography & Network Security laboratory course.

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
├── Experiment 8/   → Honeypot & TCP Client-Server Communication
├── Experiment 9/   → Intrusion Detection System (Snort IDS)
├── Experiment 10/  → Firewall Rule Implementation (iptables)
├── Experiment 11/  → Vulnerability Assessment (Metasploit Framework)
└── Experiment 12/  → Man-in-the-Middle (MITM) Socket Simulation
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

### Experiment 8 — Network Security & Honeypots
- **8.a** — Basic TCP Honeypot (`Honey-pot.py` & `Client.py`) with real-time intruder connection detection and logging
- **8.b** — Interactive TCP Honeypot (`Honey-pot1.py` & `client2.py`) with two-way banner exchange, input capturing, and session termination

### Experiment 9 — Intrusion Detection System (IDS)
- Demonstration of Snort IDS on Windows — network interface selection, packet sniffing, payload hex/ASCII dumping, packet logging, and custom rule configuration (`rules/local.rules`) to alert on ICMP ping traffic

### Experiment 10 — Firewall Rule Configuration (iptables)
- Stateful packet filtering using Linux/WSL `iptables` — loopback traffic, established/related connection tracking, service port access (SSH:22, HTTP:80, Custom:8080), unauthorized port blocking (DROP:9090), and deny-by-default chain policies

### Experiment 11 — Vulnerability Assessment (Metasploit Framework)
- Exploration of the Metasploit Framework (`msfconsole`) — command navigation, module search, detailed vulnerability inspection for Windows exploits (such as MS17-010 EternalBlue and MS08-067 NetAPI), payload options, and target architecture analysis

### Experiment 12 — Man-in-the-Middle (MITM) Concept
- Safe laboratory MITM relay simulation using Python TCP socket programming (`server.py`, `mitm.py`, `client-mitm.py`) — demonstrating how an unencrypted communication channel allows an intermediate proxy to capture, inspect, and forward client-server traffic

## 🛠️ Requirements

```bash
pip install pycryptodome numpy
```

- **Python 3.8+** (required for `pow(a, -1, m)` modular inverse syntax used in Experiments 1, 4, and 5)
- **Tkinter** (bundled with standard Python; required for Experiment 7)
- **Linux / WSL Environment** (required for Experiment 6 privilege escalation check and Experiment 10 `iptables` firewall)
- **Snort IDS** (installed for Windows in `C:\Snort` for Experiment 9)
- **Metasploit Framework** (`msfconsole` installed in Linux/WSL for Experiment 11)
- **Multi-Terminal Sessions**:
  - Two terminal sessions required for running server/client pairs in Experiment 8
  - Three terminal sessions required for running Server, MITM Relay, and Client in Experiment 12

## ▶️ How to Run

### Standalone Experiments (1–7, 9–11)
Run any experiment notebook (`.ipynb`) or standalone script directly:

```bash
python "Experiment 1/1A.ipynb"
```

### Experiment 8 (Honeypot)
Open two separate Command Prompt or Terminal windows:

1. **Terminal 1 (Server)**:
   ```bash
   cd "Experiment 8"
   python Honey-pot.py
   ```
2. **Terminal 2 (Client)**:
   ```bash
   cd "Experiment 8"
   python Client.py
   ```

### Experiment 9 (Snort IDS)
1. **Terminal 1 (Administrator)**:
   ```cmd
   cd C:\Snort
   bin\snort.exe -A console -q -i 5 -R rules\local.rules
   ```
2. **Terminal 2 (Test Traffic)**:
   ```cmd
   ping 8.8.8.8
   ```

### Experiment 10 (iptables Firewall)
In an Ubuntu/WSL terminal:

```bash
cd "Experiment 10"
chmod +x iptables_rules.sh
sudo ./iptables_rules.sh
```

### Experiment 11 (Metasploit)
In an authorized security testing terminal:

```bash
msfconsole
search type:exploit platform:windows
info exploit/windows/smb/ms17_010_eternalblue
```

### Experiment 12 (MITM Socket Demonstration)
Open three separate terminal windows and run strictly in sequence:

1. **Terminal 1 (Test Server - Port 9000)**:
   ```bash
   cd "Experiment 12"
   python server.py
   ```
2. **Terminal 2 (MITM Proxy Relay - Port 8000)**:
   ```bash
   cd "Experiment 12"
   python mitm.py
   ```
3. **Terminal 3 (Client)**:
   ```bash
   cd "Experiment 12"
   python client-mitm.py
   ```

## 📖 Course Context

These experiments cover foundational and applied topics in Cryptography and Network Security, including number theory, classical ciphers, modern symmetric/asymmetric encryption, cryptographic hashing, digital signatures, packet filtering firewalls, intrusion detection, vulnerability assessment, and controlled network traffic interception.

## 👤 Author

**Elangumaran05**
