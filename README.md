# HSN Code Validation Agent (Google ADK Framework)

This is an intelligent agent built using **Google ADK (Agent Developer Kit)** that validates **Harmonized System Nomenclature (HSN)** codes using a master Excel dataset.

---

## 🧠 What the Agent Does

- Accepts user input containing an HSN code (2, 4, 6, or 8 digits).
- Validates:
  - Whether the format is correct (numeric and allowed lengths).
  - Whether the code exists in the master dataset.
- Returns:
  - ✅ Confirmation and description for valid codes.
  - ❌ Error and reason for invalid or unrecognized codes.

---

## 💡 Technologies Used

- **Google ADK** – Conversational agent framework
- **Python**
- **pandas** – For reading and processing the Excel dataset
- **Regular Expressions** – For format validation

---

## 📁 Project Structure

```
HSN_CODE_VALIDATION_AGENT/
├── agent.py                 # Root agent definition
├── HSN_Master_Data.xlsx     # Master data file with HSN codes
├── README.md                # You are here
├── requirements.txt
├── .env
├── .gitignore
```

---

## 🚀 How to Run

1. **Install ADK**

   ```bash
   pip install google-adk
   ```

2. **Navigate to the agent folder**

   ```bash
   cd HSN_CODE_VALIDATION_AGENT
   ```

3. **Run the agent**

   ```bash
   adk web
   ```

4. Open your browser and go to:
   ```
   http://127.0.0.1:8000
   ```

---

## 📝 Sample Queries

| Input    | Output                                          |
| -------- | ----------------------------------------------- |
| `0101`   | ✅ Valid: LIVE HORSES, ASSES, MULES AND HINNIES |
| `123456` | ❌ Not found in the master dataset              |
| `12ab`   | ❌ Invalid format                               |

---

## 📽️ Demo & Explanation

Watch the full explanation and demo here: [Google Drive Video Link](https://drive.google.com/file/d/15w9A7bVahPl6clkm-a1kw_wcYKkHu3jb/view?usp=sharing)

---

## 📌 Author

- Built for internship evaluation
- Candidate open to full-time relocation to Chennai
