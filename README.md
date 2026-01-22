# Employee Retention Intelligence System
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://employeeretentionanalysis-m3rlin.streamlit.app/)

> **🔴 Live Demo:** [Click here to use the application](https://employeeretentionanalysis-m3rlin.streamlit.app/)

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
```
---

## User Guide

### Step 1. The Control Panel (Sidebar)
The sidebar on the left acts as your "Scenario Builder." Adjust these sliders and dropdowns to simulate a specific employee profile.
* **Age:** Ranges from 18 to 60.
* **Daily Rate:** The employee's daily income level.
* **Distance From Home:** Commute distance in km (Critical factor).
* **Job Role & Department:** Select from standard corporate roles (e.g., Sales Executive, Research Scientist).
* **Business Travel:** Toggle between Non-Travel, Rare, or Frequent travel.

### Step 2. Generate a Prediction
Once parameters are set, click the **"Predict Retention Risk"** button in the main window.
* The app will process the input through the Random Forest model.
* It will align your inputs with the 35+ training features using the backend reindexing logic.

### Step 3. Interpreting the Results
The system provides a two-tiered output:
* **The Verdict:** A clear text alert indicating **HIGH RISK** (Red) or **LOW RISK** (Green).
* **The Confidence Score:** A percentage showing how sure the model is (e.g., *Confidence: 72.5%*).
* **The Visualisation:** A bar chart breaks down the probability distribution, showing the exact weight the model assigned to "Stay" vs "Leave."

---

## How to Run Locally

If you prefer to run this application on your own machine rather than the cloud, follow these steps.

### 1. Clone the repository
Open your terminal and run:
```bash
git clone https://github.com/M-3rlin/EmployeeRetentionAnalysis.git
cd EmployeeRetentionAnalysis
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Launch the app
```bash
streamlit run app.py
```

---

## AI Implementation Note

Transparency regarding tools used in this project:

* **Logic Layer Assistance:** I utilised an LLM to assist in generating the **"Reference Employee Template"** (the dictionary mapping for the 35+ model features).
* **The Justification:** Manually hard-coding a 35-feature dictionary with perfect one-hot encoding alignment is highly prone to syntax errors and was the reason behind a lot of debugging being needed. Using an LLM to generate the schema ensured the inference dataframe perfectly matched the training data structure.
* **Code Integrity:** All core logic, data cleaning pipeline, and Streamlit architecture were manually engineered and verified. The AI was strictly used as a force multiplier for schema alignment.

---

## Ethical Considerations

Deploying machine learning in Human Resources requires strict ethical governance. This project was built with the following principles in mind:

* **No "Black Box" Decisions:** This tool is designed as a **Decision Support System**, not an automated decision-maker. It provides a probability score to alert managers, but human judgment is required for any intervention.
* **Bias Awareness:** The model is trained on historical data (`IBM HR Analytics`), which may contain inherent biases regarding age, gender, or role. In a real-world deployment, this model would undergo "Fairness Auditing" (e.g., using AIF360) to ensure it does not penalise specific demographics.
* **Data Privacy:** The dataset used is synthetic and anonymised. Real-world implementation would strictly adhere to **GDPR** and employee privacy agreements, ensuring that sensitive personal data (e.g., health, religion) is excluded from the training features.

---

## Future Roadmap

If I were to extend this project further, I would prioritise:

1.  **Explainability:** Integrating **SHAP (SHapley Additive exPlanations)** values to give individualised reasons for each prediction (e.g., *"This specific employee is at risk primarily due to lack of promotion, not pay"*).
2.  **Hyperparameter Tuning:** Implementing `GridSearchCV` to further optimise the Random Forest limits and improve accuracy beyond the current baseline.
3.  **Feature Engineering:** Creating interaction terms (e.g., `Tenure / Age Ratio`) to capture more complex behavioural patterns.

---

## License & Citation

This project is open-source under the **MIT License**.
* **Usage:** You are free to fork, modify, and deploy this project.
* **Attribution:** If you use this code in your own projects or research, you are required to credit **M-3rlin** and link back to this repository.

---

## References & Tech Stack

**Core Technologies:**
* **[Python 3.13](https://www.python.org/)** – The backbone of the application.
* **[Pandas](https://pandas.pydata.org/)** – Used for data manipulation and the "Ghost Column" reindexing logic.
* **[Scikit-Learn](https://scikit-learn.org/)** – Powering the Random Forest Classifier.
* **[Streamlit](https://streamlit.io/)** – The framework used to deploy the web interface.
* **[Jupyter Notebooks](https://jupyter.org/)** – Used for initial EDA and model training.

**Data Source:**
* **Kaggle:** [IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) – The dataset used to train and validate the model.

**Business Intelligence Sources:**
* **Gallup (2019):** ["This Fixable Problem Costs U.S. Businesses $1 Trillion"](https://www.gallup.com/workplace/247391/fixable-problem-costs-businesses-trillion.aspx)

**Educational Resources:**
* **GitHub Training:** [GitHub for Beginners (Playlist)](https://www.youtube.com/playlist?list=PL0lo9MOBetEFcp4SCWinBdpml9B2U25-f) – Referenced for version control and repository management.
* **GitHub Documentation:** [Writing and Formatting on GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github) – Referenced for Markdown syntax and documentation standards.
* **Streamlit Documentation:** [Deployment Guide](https://docs.streamlit.io/) – Referenced for CI/CD pipeline setup.
