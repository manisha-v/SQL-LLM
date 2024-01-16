# SQL-LLM 

SQL LLM is a Streamlit application that utilizes Google Gemini's language model to convert natural language queries into SQL commands. This project is built using Python, Streamlit, and the Google Gemini API. The SQL LLM app can be accessed [here](https://sql-llm.streamlit.app/)

---

## Table Structure

The app uses a predefined table stored in the "data.db" file with the following structure:

| Name     | Class   | Marks | Company   |
|----------|---------|-------|-----------|
| Manisha  | MCA     | 90    | Microsoft|
| HARSHIT  | BTech   | 80    | Qualcomm |
| Naren    | MSc     | 75    | Tractrix  |
| Gunjan   | Nursing | 82    | CHO      |
| Disha    | BCA     | 70    | BLC      |

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/manisha-v/SQL-LLM.git
   cd SQL-LLM
   ```

2. Generate a Google Gemini API key and save it as `API_KEY` in your `secrets.toml` file.

3. If you want to use a different table or data then make chnages in "sql.py" accordingly and run it:
   ```bash
   python sql.py
   ```

4. Run the "app.py" script:
   ```bash
   streamlit run app.py
   ```

5. Enjoy exploring natural language to SQL conversion and real-time query results!

---

## Preview

| ![Preview Image 1](preview1.png) | ![Preview Image 2](preview2.png) |
|----------------------------------|----------------------------------|

---

## Deployment

The portfolio website has been deployed and is accessible through the following link: https://sql-llm.streamlit.app/

---

## Contact

I'm always open to new opportunities and collaborations. Feel free to reach out to me through the contact form on my [portfolio website](https://manisha-v.github.io/portfolio/) or via email at [varshney.manisha05@gmail.com](mailto:varshney.manisha05@gmailcom).

Connect me on [LinkedIn](https://www.linkedin.com/in/manisha-varshney-914646191/) <img src="https://cdn.iconscout.com/icon/free/png-256/linkedin-162-498418.png" width="15"> 
