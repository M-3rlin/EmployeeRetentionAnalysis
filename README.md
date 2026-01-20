# Employee Retention Intelligence System

> **"Why do our best people leave, and how can we stop them before they hand in their notice?"**
>
> **This project is not just a prediction model; it is a strategic intervention tool designed to answer that specific business question. By leveraging historical employee data, I built an intelligence system that moves HR from *reactive* damage control to *proactive* retention.**
> 
> ---

## The Business Challenge
Employee turnover is an invisible tax on revenue. Recruitment costs, lost productivity, and knowledge drain cost companies billions annually. The core problem isn't just that people leave—it's that **it isn't seen until it's too late.**
The goal was to identify the "silent signals" of attrition — the combination of factors (commute, age, role, salary) that statistically predict a resignation.

## The Solution: A "What-If" Intelligence Engine
An interactive dashboard that serves as a risk-assessment calculator for HR managers.
* **Input:** Manager configures an employee profile (e.g., "Sales Executive, 30 years old, travels frequently").
* **Process:** The system runs this profile through a **Random Forest Classifier** trained on thousands of historic data points.
* **Output:** A real-time probability score (e.g., "64% Risk of Attrition"), allowing managers to intervene *before* the resignation letter lands.

---

## Technical Architecture & Logic
This isn't just a script; it's a full-stack data product.

### The "Ghost Column" Challenge
One of the hardest  hurdles was bridging the gap between a simple user input (7 sliders) and a complex trained model (35+ features).
* **The Problem:** The model was trained on a dataset with "One-Hot Encoded" variables (e.g., `EducationField_Medical`, `MaritalStatus_Single`). A user simply selecting "Sales" in the app doesn't automatically generate these background columns, causing the model to crash.
* **The Fix (The "Template" Strategy):** I engineered a logic layer using an LLM that clones a "reference employee" from the dataset to act as a background template. The system then overwrites *only* the user's specific inputs and uses **Pandas Reindexing** to force the data structure to match the model's memory exactly. This ensures zero-crash inference.

---

## Project Structure

```text
├── app.py                     # The "Brain": Frontend UI and Prediction Logic
├── model.pkl                  # The "Memory": Pre-trained Random Forest Model
├── README.md                  # You are here
├── data/                      # Raw Material: clean_employee_data.csv
├── notebooks/                 # The Lab: Training, testing, and 92% accuracy validation
└── docs/                      # The Pitch: Presentation drafts and business case
