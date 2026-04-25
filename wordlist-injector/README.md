# 🔧 Auth Wordlist Injector

## 📌 Description

`wordlist-injector.py` is a simple but powerful Python utility designed to **modify wordlists by injecting a specific value at fixed intervals**.

It was built to support testing scenarios where authentication mechanisms reset after successful logins — a common **logic flaw in brute-force protections**.

This tool helps simulate controlled request patterns such as:

```
fail → fail → success → fail → fail → success
```

---

## 🧠 Why This Tool Exists

Many applications implement protections like:

* Account lockouts after *N failed attempts*
* Rate limiting or temporary blocking

However, poorly designed systems may:

* **Reset the failure counter after a successful login**
* Allow attackers to bypass protections by inserting valid credentials periodically

👉 This tool automates that behavior at the wordlist level.

---

## ⚙️ How It Works

The script:

1. Reads a wordlist file (usernames or passwords)
2. Takes a **value to inject** (valid username/password)
3. Takes a **position (interval)**
4. Writes a new wordlist where the value is inserted after every *N lines*

### 🔁 Example

#### Input Wordlist:

```
pass1
pass2
pass3
pass4
```

#### Injection Settings:

* Value: `peter`
* Position: `2`

#### Output:

```
pass1
pass2
peter
pass3
pass4
peter
```

---

## 🧩 Use Cases

### 🔐 1. Authentication Bypass Testing

* Exploit login systems where:

  * Counters reset after successful login
* Combine with tools like Burp Suite Intruder

---

### ⚡ 2. Brute-Force Logic Flaw Simulation

* Test applications for:

  * Improper rate limiting
  * Weak lockout implementations
  * Session-based reset issues

---

### 🧪 3. Security Research & Labs

* Especially useful for:

  * PortSwigger Web Security Academy labs
  * CTF challenges involving authentication flaws

---

### 🔄 4. Controlled Request Sequencing

* Helps maintain strict request order like:

```
attempt → attempt → reset → attempt → attempt → reset
```

---

## 🚀 How to Use

### ▶️ Run the Script

```bash
python wordlist-injector.py
```

---

### 🧾 Inputs Explained

| Input                 | Description                            |
| --------------------- | -------------------------------------- |
| Path To Wordlist      | File containing usernames or passwords |
| The Password/Username | Value to inject (valid credential)     |
| Line Position         | After how many lines to inject         |
| Output Filename       | Optional (auto-generated if blank)     |

---

### 💡 Example Run

```bash
Path To Wordlist: passwords.txt
The Password/Username: peter
At What Number of Line: 2
Output: injected.txt
```

---

## ⚠️ Important Notes

### 🔹 Sequential Execution Matters

This tool is most effective when used with tools configured to send **one request at a time**.

If multiple requests are sent in parallel:

* The injected “reset” request may not occur at the correct position
* This breaks the intended bypass logic

---

### 🔹 Input Validation Features

* Checks if file exists
* Ensures non-empty injection value
* Validates numeric interval
* Auto-generates output filename

---

## 📎 Example Workflow (Real Use Case)

1. Generate injected wordlist using this tool
2. Load into Burp Suite Intruder
3. Configure username/password positions
4. Set resource pool to **1 request**
5. Run attack and monitor responses
6. Identify successful login patterns

---

## 🎯 Key Takeaway

This tool highlights an important concept:

> Security mechanisms can fail not because they are missing — but because they are implemented incorrectly.

---

## ⚠️ Disclaimer

This tool is intended for educational purposes and authorized security testing only.  
The author is not responsible for any misuse or damage caused by this script.  
Always ensure you have proper permission before testing any system.

---

## 👤 Author

ctrl-sid2099
