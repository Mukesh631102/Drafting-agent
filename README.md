
🛡️ EduFinance: Autonomous Agentic Drafting SystemEduFinance is a multi-agent financial reporting platform designed to bridge the gap between raw institutional data and audit-ready documentation. By utilizing a "Drafter-Auditor" workflow, the system ensures 100% accuracy and strict institutional formatting for official financial reconciliation.


🚀 Key FeaturesAgentic Orchestration: 
A dual-agent loop (Drafter & Auditor) that generates and verifies reports autonomously.
WYSIWYG A4 Preview: Real-time browser rendering that mirrors physical A4 paper dimensions ($210mm \times 297mm$).
Grounded Intelligence: RAG-inspired logic that anchors AI responses to a secure SQLite "Source of Truth" to eliminate hallucinations.
Deterministic PDF Kernel: Custom-built export engine with Unicode sanitization for crash-proof, institutional-grade PDF generation.
Forensic Tracing: Full transparency into the AI's reasoning process via a system-level audit trail.
Tech Stack
Interface: Streamlit (Mission Control Dashboard)

Intelligence: Python-based Agentic Workflows

Database: SQLite3 & Pandas (Data Grounding & Normalization)

Document Engine: FPDF2 (Metric-based Rendering)

Styling: Custom CSS3 (Metric-based Layouts)

🧠 System Architecture
Data Ingestion: Raw ledger data is pulled from the SQLite database.

Autonomous Drafting: The Drafter Agent synthesizes the data into a structured report.

Audit Loop: The Auditor Agent checks for mathematical variances and tone compliance.

Mirror Rendering: The UI renders the report in an A4-simulated CSS container.

Validated Export: The user downloads a sanitized, professional PDF.
