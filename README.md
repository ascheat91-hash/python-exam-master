# Python Exam Master (Mobile-First College Preparation Website)

A complete, offline-capable, smartphone-optimized educational web application designed specifically for absolute beginners (Level 0) preparing for their college external examination:
- **Course Title:** Python Programming
- **Course Code:** `BSC/BA/CSE/MD/5/DSC/301`
- **Semester:** Semester V
- **Examination Pattern:** 35 Marks, 3 Hours (180 Minutes)
  - Question 1 (Compulsory): 7 Short / Objective questions (1 Mark each = 7 Marks)
  - Unit-I: Answer ANY ONE between Question 2 OR Question 3 (14 Marks)
  - Unit-II: Answer ANY ONE between Question 4 OR Question 5 (14 Marks)

---

## 🌟 Key Modules & Features

1. **Dashboard & Syllabus Hub (`index.html`):**
   - Clean mobile layout with college meta-header.
   - Live preparation progress bar tracking all 31 syllabus topics.
   - Direct launchpads for Unit-I, Unit-II, simulator, and practice tools.

2. **Complete 13-Part Pedagogical Notes (`notes.html` & `topic.html`):**
   - Every single topic from Unit-I and Unit-II divided into small understandable lessons.
   - Dual-mode switch: **Beginner Hinglish Study Mode** vs **14-Mark University Exam Writing Mode**.
   - Includes: Basic Intro, Everyday Analogy, Hinglish Explanation, English Exam Definition, Important Rules, Syntax, Program Code, Line-by-Line Breakdown, Trace Dry-Run Table, Expected Output, Exam Traps, and 1-Mark/14-Mark Questions.

3. **Topic-Wise Question Practice Bank (`practice.html`):**
   - 68 syllabus-targeted questions covering MCQs, Fill-in-the-Blanks, True/False, and Output Predictions.
   - Filterable by Unit-I, Unit-II, and Output Prediction categories.
   - Instant answer verification, detailed reasoning explanations, and score persistence.

4. **Smartphone & Notebook Program Practice (`programs.html`):**
   - 7 core college programs: Simple & Compound Interest, Even/Odd, Largest of 3, Reverse Number/Palindrome, Factorial, Number Triangle Patterns, and List Operations / Linear Search.
   - Smartphone typing scratchpad with handwritten notebook practice instructions and expandable model answers.

5. **Real College Exam Simulator (`exam.html`):**
   - Exact 35-mark, 180-minute countdown timer with auto-submit.
   - Q1 Compulsory (7M) + Unit-I selection (Q2 or Q3) + Unit-II selection (Q4 or Q5).
   - Horizontal question jump palette.
   - Automatic objective scoring + descriptive model answer evaluation checklist.

6. **5 Full Model Papers (`model-papers.html`):**
   - 5 complete 35-mark practice papers with full model answers and mark distributions.

7. **One-Day Exam Revision (`revision.html`):**
   - 10 Golden rules to remember, 12 essential 1-mark definitions, syntax cheat sheets, and operator comparison tables.

8. **Progress Tracker & Local Backup (`progress.html`):**
   - Topic completion tracking, accuracy rates, mock exam history, and offline JSON backup/restore.

9. **Offline PWA (`sw.js` & `manifest.json`):**
   - Service worker caches all HTML, CSS, JS, and JSON data for reliable offline use on Android phones.

---

## 🚀 How to Run Locally

1. Open a terminal in this directory.
2. Start Python's built-in lightweight web server:
   ```bash
   python -m http.server 8000
   ```
3. Open your browser or smartphone browser on the same Wi-Fi network:
   - On this machine: `http://localhost:8000/index.html`
   - On an Android phone: `http://<YOUR_COMPUTER_IP>:8000/index.html`
4. Tap **Add to Home Screen** on Android Chrome to install it as an app.

