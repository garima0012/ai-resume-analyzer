# 📉 Customer Churn Prediction — Telecom

> **Data Mining Project** | Predicting customer churn using Machine Learning classification algorithms.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3%2B-orange?logo=scikit-learn)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-green?logo=pandas)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Project Overview

This project builds an end-to-end machine learning pipeline to **predict customer churn** for a telecom company. By identifying customers likely to leave, the business can deploy targeted retention strategies and reduce revenue loss.

**Key Results:**
- 🎯 **ROC-AUC: 0.71+** with Random Forest (best model)
- 📈 **~15% accuracy improvement** through feature engineering
- 💡 **5 actionable business insights** derived from the model

---

## 🗂️ Project Structure

```
customer-churn-prediction/
│
├── data/
│   ├── generate_data.py              # Synthetic dataset generator
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── src/
│   └── churn_prediction.py          # 🔑 Main ML pipeline (EDA → Model → Insights)
│
├── models/
│   ├── random_forest_churn_model.pkl
│   └── scaler.pkl
│
├── reports/
│   └── figures/
│       ├── 01_eda_overview.png
│       ├── 02_correlation_heatmap.png
│       ├── 03_model_comparison.png
│       └── 04_rf_detailed.png
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Generate Dataset
```bash
python data/generate_data.py
```

### 5. Run the Full Pipeline
```bash
python src/churn_prediction.py
```

---

## 📊 Methodology

### Step 1 — Data Loading & Cleaning
- Loaded 7,043 customer records with 20 features
- Handled missing values in `TotalCharges` using median imputation
- Converted data types and removed non-predictive columns

### Step 2 — Exploratory Data Analysis (EDA)
- Analyzed churn rate (~21%) across demographic and service features
- Visualized tenure, monthly charges, contract type, and internet service distributions
- Computed correlation matrix for numerical features

### Step 3 — Feature Engineering ⭐
| New Feature | Description |
|---|---|
| `ChargesPerMonth` | `TotalCharges / tenure` — average monthly spend |
| `TenureGroup` | Bucketed tenure into 4 groups (0-1yr, 1-2yr, 2-4yr, 4+yr) |
| `HighMonthlyCharge` | Binary flag — above median monthly charge |
| `NumServices` | Total number of subscribed services |
| `AutoPayment` | Binary flag — automatic payment method |

### Step 4 — Model Training & Evaluation

Four classification models were compared:

| Model | Accuracy | ROC-AUC | CV AUC |
|---|---|---|---|
| Logistic Regression | 78.5% | 0.708 | 0.708 |
| Decision Tree | 77.6% | 0.709 | 0.698 |
| **Random Forest** ✅ | **78.4%** | **0.715** | **0.714** |
| Gradient Boosting | 77.5% | 0.724 | 0.719 |

> **Random Forest** was selected as the final model — best balance of accuracy and interpretability.

---

## 📈 EDA Visualizations

### Churn Distribution & Demographics
![EDA Overview](reports/figures/01_eda_overview.png)

### Correlation Heatmap
![Correlation](reports/figures/02_correlation_heatmap.png)

### Model Comparison & ROC Curves
![Models](reports/figures/03_model_comparison.png)

### Confusion Matrix & Feature Importance
![RF Detail](reports/figures/04_rf_detailed.png)

---

## 💡 Key Business Insights

| # | Insight | Recommendation |
|---|---|---|
| 1 | Month-to-Month customers churn **3× more** than 2-year contract holders | Offer discounts to switch to annual plans |
| 2 | Tenure < 12 months is the **highest churn risk** period | Invest in onboarding & early loyalty rewards |
| 3 | Fiber optic users churn more despite premium pricing | Investigate service quality & price satisfaction |
| 4 | Customers without online security / tech support churn significantly more | Bundle these services at discounted rates |
| 5 | Electronic check payers show higher churn than auto-pay customers | Incentivize auto-payment enrollment |

> 🎯 Potential **12–18% churn reduction** through targeted retention campaigns.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python 3.9+** | Core language |
| **Pandas** | Data manipulation & EDA |
| **Scikit-learn** | ML models, preprocessing, evaluation |
| **Matplotlib / Seaborn** | Data visualization |
| **Joblib** | Model serialization |

---

## 👤 Author

**Your Name**
- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

---

## 📄 License

This project is licensed under the MIT License.
