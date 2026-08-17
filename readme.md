# Concurrent Multi-Process File Encryption Engine

A high-performance, multi-process file encryption and decryption engine built in **C++17**, designed to handle concurrent batch file operations securely across directories.

## 🚀 Key Features
* **Multi-Process Architecture:** Leverages low-level Linux process management (`sys/wait.h`) to spawn and coordinate background worker processes for high-throughput execution.
* **Universal File Support:** Securely processes and transforms arbitrary file formats (text, media, binaries) using standard C++ file streams.
* **Modular Design:** Cleanly decoupled architecture dividing responsibilities into process management, file I/O operations, and encryption logic.
* **Cross-Environment Compatibility:** Configured and tested for Linux/WSL development with strict memory management and standard-compliant compilation.

## 🛠️ Tech Stack
* **Language:** C++17
* **Environment:** Linux (WSL), GCC, Make
* **Core Concepts:** Process Control, System Calls, File Streams, Exception Safety

## ⚙️ Getting Started & Compilation

Clone the repository and compile the binaries using `make`:

```bash
git clone [https://github.com/krishpandey910-code/encrypty-wsl.git](https://github.com/krishpandey910-code/encrypty-wsl.git)
cd encrypty-wsl
make
