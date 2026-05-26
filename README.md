# StyleQuiz — Communication Style Assessment

A digital version of the communication style assessment from Pierre Casse's
*Teaching for the Cross-Cultural Mind* (SIETAR, 1981). Built because the
original only existed as a PDF — useful in a workshop, unusable at scale.

## Why I built this

This project started as a real-life pain point. I first encountered Casse's
framework in a communication workshop and found the assessment genuinely
insightful — but completing it meant working through a printed PDF and tallying
scores by hand. There was no way to share results, aggregate data across a team,
or revisit your profile later.

I used it as an opportunity to build a proper digital version using Claude Code.

## What it does

40 pairs of statements. Choose the one that feels most like you. No right or
wrong answers.

The quiz identifies your dominant communication style across four types:

| Style | Focus | Traits |
|---|---|---|
| **Action** | Results & objectives | Direct, decisive, energetic |
| **Process** | Strategies & facts | Systematic, logical, detail-oriented |
| **People** | Relationships & teamwork | Empathetic, warm, collaborative |
| **Idea** | Concepts & innovation | Creative, visionary, imaginative |

Tied scores across multiple styles are shown together.

## Where it's heading

The individual quiz is the foundation. The bigger vision is a company-wide
tool where:
- Every team member takes the assessment
- A manager dashboard shows team style distribution at a glance
- Managers can set completion goals and send reminders
- Aggregated data helps teams understand how they communicate collectively

## How it was built

- Built the initial version with a Flask + Python backend using Claude Code
- Explored Loveable for UI prototyping but found it lacked enough design control
- Moved to Figma Make to design the UI and expanded features (dashboard and
  manager views) with full control over the design decisions

## Run it locally

```bash
git clone https://github.com/JoannaKmiec11/stylequiz.git
cd stylequiz
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
echo SECRET_KEY=your-secret-key-here > .env
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.
