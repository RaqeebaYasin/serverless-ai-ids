# AI-Driven Intrusion Detection for Serverless Architectures
[![DOI](https://zenodo.org/badge/1204681672.svg)](https://doi.org/10.5281/zenodo.19468334)

## 📌 Project Overview
This repository contains the independent research and prototype implementation of a lightweight **Intrusion Detection System (IDS)** specifically designed for serverless computing environments (FaaS). 

Our research addresses the critical vulnerability of **Denial-of-Wallet (DoW)** and **Event-Injection attacks**, which exploit the auto-scaling nature of cloud functions to cause financial and operational exhaustion.

## 🏗️ System Architecture
The proposed framework operates out-of-band to ensure zero latency impact on the primary application logic. It captures metadata (telemetry) and uses an AI engine to classify behavior as benign or malicious.

(https://github.com/RaqeebaYasin/serverless-ai-ids/raw/main/docs/image_dab19f.png)

## 🚀 Key Research Contributions
- **Lightweight Behavioral Analysis:** Utilizes metadata (duration, memory, invocation frequency) instead of resource-heavy Deep Packet Inspection (DPI).
- **Semi-Supervised Learning:** Implements an **Autoencoder** trained only on "normal" traffic to detect novel attack patterns via reconstruction error.
- **Stateless Design:** Ensures the security layer scales horizontally alongside the serverless functions.

## 📂 Repository Structure
- **/docs**: Contains the full technical research paper (IEEE Format) and architectural diagrams.
- **/model**: Python implementation of the Autoencoder anomaly detection logic.
- **/middleware**: Prototype Node.js/Flask wrapper for metadata extraction.

## 🧪 Prototype Status
This code is a **Proof of Concept (PoC)**. It demonstrates the feasibility of using reconstruction loss as a trigger for blocking malicious triggers in a serverless pipeline.

## 👥 Authors
- **Raqeeba Yasin** — [raqeebayasin@gmail.com](mailto:raqeebayasin@gmail.com)
- **Syeda Faiza Sajjad** — [faizasyed76sfs@gmail.com](mailto:faizasyed76sfs@gmail.com)

*University of the Punjab, Lahore, Pakistan*

---
### 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
