# Communication Style Finder

A web app that helps you identify your dominant communication style through a 40-question self-assessment.

## About the Quiz

The quiz is based on the work of **Pierre Casse** — *"Teaching for the Cross-Cultural Mind"* (Washington, DC, SIETAR, 1981).

You are presented with 40 pairs of statements and asked to pick the one that feels most like you. There are no right or wrong answers — just choose as spontaneously as possible. At the end, your answers are tallied to reveal your dominant communication style across four types:

| Style | Focus | Key traits |
|---|---|---|
| **Action** | *What* — results & objectives | Direct, decisive, impatient, energetic |
| **Process** | *How* — strategies & facts | Systematic, logical, cautious, detail-oriented |
| **People** | *Who* — relationships & teamwork | Empathetic, warm, spontaneous, collaborative |
| **Idea** | *Why* — concepts & innovation | Imaginative, charismatic, creative, big-picture |

You may score equally across more than one style — in that case, all tied styles are shown as your result.

## Running Locally

```bash
# Clone and set up
git clone https://github.com/YoYoSuperStar/stylequiz.git
cd stylequiz
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Set your secret key
echo SECRET_KEY=your-secret-key-here > .env

# Start the app
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.
