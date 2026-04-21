from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = "false9secret"

LESSONS = [
    {
        "id": 1,
        "title": "Soccer Positions 101",
        "subtitle": "Understanding the numbered system before anything else",
        "body": [
            "Before you can understand the False 9, you need to understand how soccer positions work. Every player on the field has a role, and traditionally those roles are associated with <strong>jersey numbers</strong> — a system that dates back to the early days of the sport.",
            "In modern soccer, a team fields <strong>11 players</strong>. These players are divided into three main groups: <em>defenders</em>, <em>midfielders</em>, and <em>forwards</em> (also called attackers). Each group has a different area of the pitch to cover and a different job to do.",
            "The <strong>goalkeeper (#1)</strong> is the last line of defense — the only player allowed to use their hands, guarding the goal. Then come the <strong>defenders (#2–#6)</strong>, whose primary job is to stop the other team from scoring. In the middle you have the <strong>midfielders (#6–#8)</strong>, who connect defense to attack and control the tempo of the game. Finally, the <strong>forwards (#7–#11)</strong> are the attacking players tasked with creating chances and scoring goals.",
            "These numbers aren't random — they reflect a player's role on the pitch. A #4 is typically a central defensive midfielder. A #10 is the creative playmaker behind the strikers. And the <strong>#9</strong>? That's the center forward — the main striker, the goal scorer, the player whose job is to put the ball in the net."
        ],
        "diagram": None,
        "number_chart": True,
        "visual": "🔢",
        "visual_caption": "Numbers 1–11 map to specific roles — from goalkeeper to striker",
        "key_idea": "Soccer positions follow a numbered system. Defenders protect the goal (#1–5), midfielders control the game (#6–8), and forwards attack (#9–11)."
    },
    {
        "id": 2,
        "title": "The Traditional Number 9",
        "subtitle": "What a striker is actually supposed to do",
        "body": [
            "The <strong>number 9</strong> is one of the most iconic positions in soccer. Historically, it belongs to the center forward — the player who lines up highest on the pitch, closest to the opponent's goal. Their job is brutally simple: <em>score goals</em>.",
            "A traditional #9 is physical, strong in the air, and good at holding up the ball with their back to goal. They act as a target for long passes and crosses. Think of players like <strong>Didier Drogba, Zlatan Ibrahimović, or Robert Lewandowski</strong> — big, powerful strikers who dominate defenders and finish chances.",
            "The #9 stays in the opponent's half for most of the game. They don't drop deep to help in midfield — that's not their job. Their job is to be a constant <strong>threat near the goal</strong>, occupying center-backs, winning headers, and converting chances when they come.",
            "The entire team is often built around serving the #9. Wingers (the #7 and #11) cross the ball into the box. Midfielders (the #8 and #10) play passes into their feet. The #9 is the final destination of the attack — the player who finishes the move.",
            "Understanding this traditional role is key — because the <strong>False 9</strong> breaks every single one of these expectations."
        ],
        "diagram": "false9_diagram.png",
        "diagram_caption": "A traditional #9 stays high near the opponent's goal. Notice where the 'False 9' label appears in this diagram — much deeper than expected.",
        "visual": "🎯",
        "visual_caption": "The #9: stay high, receive the ball, score goals — simple in theory",
        "key_idea": "A traditional #9 is a physical, goal-hungry striker who stays near the opponent's goal and acts as the final target of every attack."
    },
    {
        "id": 3,
        "title": "What Is a False 9?",
        "subtitle": "When the striker refuses to stay up front",
        "body": [
            "Now that you know what the #9 is supposed to do, here's where it gets interesting. The <strong>False 9</strong> is a striker who deliberately breaks those expectations. Instead of staying high near the opponent's goal, the False 9 <em>drops deep into midfield</em> to collect the ball, link play, and create chances.",
            "The 'False' in the name refers to the deception: when the number 9 drops deep, they become false — they're not where a #9 should be. Defenders who are trained to mark the striker suddenly don't know where to look.",
            "The center-back faces an impossible decision. <strong>If they follow</strong> the False 9 into midfield, they leave a massive gap behind them — empty space that attacking midfielders can run into. <strong>If they don't follow</strong>, the False 9 picks up the ball with time and space to create danger. Either way, the defense is in trouble.",
            "This is the genius of the position: the act of <em>not being where you're supposed to be</em> is itself an attacking weapon. By simply moving away from goal, the False 9 creates chaos in the opponent's defensive shape without even touching the ball."
        ],
        "diagram": None,
        "visual": "💡",
        "visual_caption": "Drop deep → defenders confused → space opens up → attack succeeds",
        "key_idea": "The False 9 drops deep into midfield instead of staying up front, forcing defenders into impossible decisions and creating space for teammates."
    },
    {
        "id": 4,
        "title": "Messi & Guardiola: The Blueprint",
        "subtitle": "How Barcelona made the False 9 famous",
        "body": [
            "The modern False 9 was popularized by <strong>Pep Guardiola</strong> at Barcelona starting in the 2008–09 season. Guardiola needed to fit Lionel Messi into his system — Messi was too talented to be a winger, but Samuel Eto'o was the established #9. The solution: play Messi as a striker who doesn't act like one.",
            "The results were historic. Barcelona's <strong>6–2 win over Real Madrid</strong> at the Bernabéu in May 2009 shocked the world. Messi dropped between the lines, collecting the ball from deep, and Madrid's center-backs had no idea whether to follow him or hold their position. They chose wrong every time.",
            "<strong>Why Messi was the perfect False 9:</strong> His close control let him receive in tight spaces. His vision let him pick the right pass. His acceleration allowed him to drive forward once he had the ball. And because he was a genuine goal threat, defenders couldn't simply ignore him — they had to follow, and that following opened up the spaces Barcelona needed.",
            "Guardiola's system required every player to understand their role. The wingers (Henry, then Villa) stayed wide and made forward runs into the space Messi vacated. Midfielders like Xavi and Iniesta kept the ball moving quickly. The whole system was a machine — and Messi as False 9 was the engine."
        ],
        "diagram": None,
        "visual": "🏆",
        "visual_caption": "Messi at Barcelona 2008–2012 — the False 9 at its historical peak",
        "key_idea": "Guardiola's Barcelona used Messi as a False 9 to create the most dominant team of the era, winning La Liga, the Champions League, and every major title."
    },
    {
        "id": 5,
        "title": "The False 9 Today",
        "subtitle": "Legacy, evolution, and where it lives now",
        "body": [
            "The classic Guardiola-era False 9 is less common today — defenses have studied it, adapted to it, and developed counter-strategies like using a midfielder to man-mark the False 9 instead of a center-back, preventing the defensive line from being dragged out of position.",
            "But the ideas behind the False 9 are <em>everywhere</em> in modern football. The <strong>inverted winger</strong> (like Mohamed Salah or Arjen Robben) uses similar principles — cutting inside from wide positions to create numerical advantages. The <strong>second striker</strong> in a 4-4-2 borrows the deep-dropping movement. Even modern playmakers like Kevin De Bruyne and Bruno Fernandes play with False 9-like tendencies.",
            "Guardiola himself has revived it at Manchester City when lacking a natural striker — deploying <strong>Bernardo Silva</strong> and even De Bruyne in the role with great success. The position rewards intelligence and technical quality over raw physicality.",
            "The deeper legacy of the False 9 is philosophical: it proved that <strong>space is more valuable than presence</strong>. A striker who drops deep and drags defenders with them can be more dangerous than one who simply stands at the back post waiting for a cross. That idea — that absence creates opportunity — has permanently changed how coaches think about attacking football."
        ],
        "diagram": None,
        "visual": "🌍",
        "visual_caption": "From Barcelona 2009 to a global tactical philosophy",
        "key_idea": "The False 9 evolved into the DNA of modern football — its principles of space creation and positional fluidity appear in every top team today."
    }
]

QUIZ = [
    {
        "id": 1,
        "question": "What jersey number is traditionally associated with the center forward — the main striker?",
        "options": [
            "#7",
            "#10",
            "#9",
            "#11"
        ],
        "answer": 2,
        "explanation": "The #9 is the traditional center forward. It's one of the most iconic numbers in soccer, associated with physical goal-scoring strikers like Lewandowski, Drogba, and Ibrahimović."
    },
    {
        "id": 2,
        "question": "Which group of players does the #6 typically belong to?",
        "options": [
            "Goalkeepers",
            "Defenders or defensive midfielders",
            "Attacking midfielders",
            "Wingers"
        ],
        "answer": 1,
        "explanation": "Numbers 4–6 are typically defenders or defensive midfielders. The #6 in particular is often a holding midfielder whose job is to protect the back line."
    },
    {
        "id": 3,
        "question": "What does the 'False' in False 9 mean?",
        "options": [
            "The player is pretending to be injured",
            "The player wears the wrong jersey number",
            "The striker is not where a traditional #9 would be — they drop deep instead of staying up front",
            "The position was invented as a trick that only works once"
        ],
        "answer": 2,
        "explanation": "The 'False' refers to the deception — the #9 isn't where defenders expect them to be. By dropping into midfield, they break the rules defenders are trained to follow."
    },
    {
        "id": 4,
        "question": "When a False 9 drops deep and a center-back follows them, what happens?",
        "options": [
            "The False 9 scores a goal immediately",
            "A large gap opens up behind the center-back that attacking midfielders can exploit",
            "The offside trap is triggered",
            "Nothing changes — the defense stays organized"
        ],
        "answer": 1,
        "explanation": "When a center-back follows the False 9 into midfield, they vacate their defensive position. This creates a gap behind them — exactly the space midfielders like Xavi and Iniesta would run into."
    },
    {
        "id": 5,
        "question": "Which manager is most famous for perfecting the False 9 with Lionel Messi?",
        "options": [
            "Jose Mourinho",
            "Diego Simeone",
            "Jurgen Klopp",
            "Pep Guardiola"
        ],
        "answer": 3,
        "explanation": "Pep Guardiola used Messi as a False 9 at Barcelona from 2008, creating one of the most dominant sides in football history and introducing the tactic to the world stage."
    }
]


@app.route("/")
def home():
    session.clear()
    return render_template("home.html", total_lessons=len(LESSONS))


@app.route("/learn/<int:lesson_num>")
def learn(lesson_num):
    if lesson_num < 1 or lesson_num > len(LESSONS):
        return redirect(url_for("home"))

    lesson = LESSONS[lesson_num - 1]

    if "visited_lessons" not in session:
        session["visited_lessons"] = {}
    session["visited_lessons"][str(lesson_num)] = {
        "entered_at": datetime.now().isoformat(),
        "lesson_title": lesson["title"]
    }
    session.modified = True

    has_next = lesson_num < len(LESSONS)
    has_prev = lesson_num > 1

    return render_template(
        "lesson.html",
        lesson=lesson,
        lesson_num=lesson_num,
        total=len(LESSONS),
        has_next=has_next,
        has_prev=has_prev,
        next_num=lesson_num + 1,
        prev_num=lesson_num - 1
    )


@app.route("/quiz/<int:q_num>")
def quiz(q_num):
    if q_num < 1 or q_num > len(QUIZ):
        return redirect(url_for("home"))

    question = QUIZ[q_num - 1]

    if "quiz_answers" not in session:
        session["quiz_answers"] = {}

    already_answered = str(q_num) in session["quiz_answers"]
    chosen = session["quiz_answers"].get(str(q_num), {}).get("chosen", None)

    return render_template(
        "quiz.html",
        question=question,
        q_num=q_num,
        total=len(QUIZ),
        has_prev=q_num > 1,
        has_next=q_num < len(QUIZ),
        next_num=q_num + 1,
        prev_num=q_num - 1,
        already_answered=already_answered,
        chosen=chosen
    )


@app.route("/quiz/<int:q_num>/answer", methods=["POST"])
def answer(q_num):
    data = request.get_json()
    chosen = data.get("chosen")

    question = QUIZ[q_num - 1]
    correct = (chosen == question["answer"])

    if "quiz_answers" not in session:
        session["quiz_answers"] = {}

    session["quiz_answers"][str(q_num)] = {
        "chosen": chosen,
        "correct": correct,
        "answered_at": datetime.now().isoformat()
    }
    session.modified = True

    return jsonify({
        "correct": correct,
        "correct_index": question["answer"],
        "explanation": question["explanation"]
    })


@app.route("/quiz/results")
def quiz_results():
    answers = session.get("quiz_answers", {})
    score = sum(1 for a in answers.values() if a.get("correct"))
    total = len(QUIZ)

    results = []
    for i, q in enumerate(QUIZ):
        ans = answers.get(str(i + 1), {})
        results.append({
            "question": q["question"],
            "correct_answer": q["options"][q["answer"]],
            "chosen_answer": q["options"][ans["chosen"]] if ans.get("chosen") is not None else "Not answered",
            "correct": ans.get("correct", False),
            "explanation": q["explanation"]
        })

    return render_template("quiz_results.html", score=score, total=total, results=results)


@app.route("/complete")
def complete():
    visited = session.get("visited_lessons", {})
    return render_template("complete.html", visited=visited, total=len(LESSONS))


@app.route("/api/lesson-data")
def lesson_data():
    from flask import jsonify
    return jsonify(LESSONS)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
