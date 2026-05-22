# 📚 Blockchain Security Re-Engineering

This repository documents the structural and theoretical re-engineering of an academic project on blockchain security. It shows how an initial presentation-focused project was reworked into a more formal, concept-driven security analysis.

The goal is not to inflate significance, but to separate practical demonstration from theoretical abstraction and system-level modeling.

---

## 🔗 Materials

- **Original Presentation(PDF) 🌐Korean :** [📑 View Original Presentation](https://github.com/ulsidae/RSVP-systems/blob/main/%F0%9F%93%9ABlockchain%20Security%20Re-Engineering/%EB%B8%94%EB%A1%9D%EC%B2%B4%EC%9D%B8%EB%B0%9C%ED%91%9C%EC%9A%A9%20%EC%9E%90%EB%A3%8C.pdf)  
- **Blockchain Security Analysis:** [📄 Read Paper via GitHub Pages](https://ulsidae.github.io/dev_logs/Security%20&%20Crypto/Blockchain%20Security%20Analysis/)
- **Result:** [📑 Blockchain Security Analysis](https://github.com/ulsidae/dev_logs/tree/main/Security%20%26%20Crypto/Blockchain%20Security%20Analysis)  
  
---

## 1. Problem

A university presentation was developed with the goal of explaining blockchain concepts combined with security topics in a way that non-technical audiences could understand.

However, several constraints were identified:

- Difficulty in making distributed system and cryptographic concepts accessible to non-technical audiences  
- Limited space for formal security modeling or deeper theoretical explanation  
- Structural complexity of blockchain systems made purely intuitive explanation difficult  

---

## 2. Approach

To address these constraints, the project was designed around a practical, demonstration-first structure.

- Built a simplified centralized simulation system (“JetCoin”) to represent transaction flows  
- Used this model to demonstrate concurrency issues and double-spending behavior in a controlled environment  
- Focused on visual intuition and system behavior rather than formal mathematical modeling  

The goal was to reduce cognitive load and make the core idea accessible to a general audience.

---

## 3. Implementation

The presentation was delivered as a practice-oriented demonstration.

- The JetCoin model was used to simulate centralized transaction processing  
- Concurrency-related issues such as race conditions and TOCTOU behavior were illustrated in simplified form  
- The presentation received positive feedback from the supervising professor, particularly regarding clarity and structure  
- Audience response was generally neutral to positive, with no critical breakdown in understanding  

Overall, the project succeeded in communicating the core system behavior effectively.

---

## 4. Insights

After completion, several limitations became clear in the original approach:

- The explanation prioritized intuition over formal system structure  
- Security mechanisms were simplified, reducing theoretical depth  
- Higher-level abstractions such as consensus models and cryptographic guarantees were not fully developed  

As a result, the project was later revisited and restructured into a formal analysis of blockchain security, focusing on:

- Blockchain as a distributed state machine  
- Cryptographic integrity models and consensus mechanisms  
- Application-layer vulnerabilities such as smart contract re-entrancy  

This re-engineered version is documented in the linked HTML paper.

A secondary reflection from the original presentation was the importance of introducing brief conceptual warm-up steps before technical explanation, in order to improve audience transition into complex topics.
