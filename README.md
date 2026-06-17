# asymmetric-secure-chat
A secure client-server chat implementation demonstrating asymmetric encryption using Python sockets.
# Asymmetric Secure Chat

A lightweight, secure client-server chat application built from scratch utilizing Python sockets and end-to-end asymmetric cryptography. This project demonstrates the core fundamentals of network programming, secure key exchange, and data privacy.

---

## Security Disclaimer
> **IMPORTANT:** This repository is created strictly for educational, research, and portfolio purposes. The cryptographic implementations and key exchanges contained herein are intended to demonstrate concepts of asymmetric encryption and network security under laboratory conditions. Do not deploy this software in untrusted or production environments.

---

## Features
* **Socket-Based Architecture:** Low-level network communication implemented via Python's standard `socket` library.
* **Asymmetric Cryptography:** True end-to-end encryption (E2EE) ensuring that only the intended recipient can decrypt the messages.
* **Secure Key Exchange:** Automated generation and distribution of public keys upon client-server handshake.
* **Zero-Trust Principles:** The transport layer handles the data but has zero knowledge of the plaintext content.

---

## 📊 Architecture & Data Flow

Below is a conceptual overview of how the secure handshake and message exchange are handled:
[ Client A ]                                   [ Server ]                                   [ Client B ]
|                                              |                                             |
| ---- 1. Generate Keypair & Send PubKey ----> |                                             |
|                                              | <---- 2. Forward Client A's PubKey -------- |
|                                              |                                             |
|                                              | <---- 3. Generate Keypair & Send PubKey ----|
| <---- 4. Forward Client B's PubKey --------- |                                             |
|                                              |                                             |
| ======================== SECURE CHANNEL ESTABLISHED ========================              |
|                                              |                                             |
| ---- 5. Encrypt msg with B's PubKey -------> |                                             |
|                                              | ---- 6. Relay Encrypted Data -------------> |
|                                              |                                             | [ Decrypts with ]
|                                              |                                             | [ own PrivateKey]

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Core Modules:** `socket`, `threading`
* **Cryptography:** `cryptography` (or `rsa` / built-in libraries depending on implementation)

---

## 💻 Installation & Usage

### 1. Clone the repository
```bash
git clone [https://github.com/asadeld/asymmetric-secure-chat.git](https://github.com/asadeld/asymmetric-secure-chat.git)
cd asymmetric-secure-chat
