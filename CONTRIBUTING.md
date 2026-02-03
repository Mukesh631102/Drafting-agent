# Contributing to EduFinance Drafting Agent

Thank you for your interest in contributing to **EduFinance Drafting Agent**! 🎉

We welcome contributions of all kinds: new agent capabilities, bug fixes, UI improvements, documentation enhancements, and MCP integrations.

---

## 🧭 Code of Conduct

Please maintain a friendly, inclusive, and professional environment. Respect all contributors regardless of experience level.

---

## 🛠️ Development Setup

1. **Fork and Clone the Repository**:
   ```bash
   git clone https://github.com/Mukesh631102/Drafting-agent.git
   cd Drafting-agent
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   ```bash
   cp .env.example .env
   # Edit .env and supply your GROQ_API_KEY
   ```

5. **Seed the Local Database**:
   ```bash
   python seed_db.py
   ```

6. **Run the Streamlit Dashboard**:
   ```bash
   streamlit run app.py
   ```

---

## 🌿 Branching Strategy & PR Workflow

1. Create a feature branch:
   ```bash
   git checkout -b feature/awesome-agent-improvement
   ```
2. Make your changes with clear, descriptive commit messages.
3. Ensure `.env` and `instance/*.db` files are **never** committed.
4. Test your changes locally before opening a PR.
5. Push to your branch and open a Pull Request against `main`.

---

## 💡 Contribution Ideas

- [ ] Add export formats (DOCX, Markdown bundle, Notion export).
- [ ] Add support for additional LLM providers (Ollama local models, Claude 3.5, DeepSeek).
- [ ] Implement OCR invoice / receipt parser agent.
- [ ] Expand FastMCP tools for real-time ERP accounting database write-backs.

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).
