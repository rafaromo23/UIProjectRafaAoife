from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = "false9secret"

LESSONS = [
    {
        "id": 1,
        "title": "Soccer Positions 101",
        "subtitle": "Start with jersey numbers before you study tactics.",
        "body": [
            "You should understand soccer positions before you study the False 9. Each player has a role. For a long time, people have mapped those roles to <strong>jersey numbers</strong>. The mapping started early in soccer history.",
            "A soccer team puts <strong>11 players</strong> on the field. They split into three large groups: <em>defenders</em>, <em>midfielders</em>, and <em>forwards</em>. People also call forwards attackers. Each group works a different part of the field.",
            "The <strong>goalkeeper (#1)</strong> guards the net. Only the keeper may use hands inside the box in normal play. <strong>Defenders</strong> often wear numbers from #2 through #6. They try to stop goals. <strong>Midfielders</strong> around #6 through #8 link defense to attack. They help set the speed of the game. <strong>Forwards</strong> around #7 through #11 attack. They try to score and set up goals.",
            "The numbers are not random. They hint at the job on the field. A #4 is often a defensive midfielder. A #10 is often a playmaker behind the strikers. The <strong>#9</strong> is usually the center forward. That player is the main striker. The job is to score."
        ],
        "diagram": "numberedpossoccer.jpg",
        "diagram_caption": "The chart shows how numbers sit on a typical field. Coaches still use this language when they talk about shape.",
        "number_chart": True,
        "visual": "🔢",
        "visual_caption": "Numbers 1 through 11 still point to familiar jobs, from keeper to striker.",
        "key_idea": "Soccer uses a numbered map. Defenders guard the goal area. Midfielders connect lines. Forwards lead the attack."
    },
    {
        "id": 2,
        "title": "The Traditional Number 9",
        "subtitle": "What coaches expect from a classic striker.",
        "body": [
            "The <strong>number 9</strong> is the classic center forward. That player lines up closest to the other team's goal. The main job is simple: <em>score goals</em>.",
            "A traditional #9 is strong and good in the air. They hold the ball with their back to goal. They give long passes and crosses a target. Think of <strong>Didier Drogba, Zlatan Ibrahimović, or Robert Lewandowski</strong>. They are big strikers who finish chances and bother defenders.",
            "A #9 spends most of the match in the attacking half. They usually do not drop deep to play like a midfielder. They stay a <strong>threat near the goal</strong>. They challenge center-backs. They win headers. They turn half chances into shots.",
            "Teams often build attacks around the #9. Wingers such as #7 and #11 cross into the box. Midfielders feed the striker. The #9 is often the last player the ball finds before a shot.",
            "Academies train classic nines with work near the goal. Drills repeat crosses, cutbacks, rebounds, headers, and shots under pressure. Coaches want strength and fitness so the striker can duel with defenders all game.",
            "Training does not focus on dribbling from midfield. It focuses on instincts near the goal. Read the lane. Attack crosses. Finish before the keeper is set. The clip on this page shows that kind of repetition.",
            "Keep this picture in mind. A <strong>False 9</strong> later breaks most of these habits on purpose."
        ],
        "diagram": "false9_diagram.png",
        "diagram_caption": "The diagram shows a normal #9 high up the field. The False 9 label sits much deeper. That gap is the whole story.",
        "video_embed": "https://www.youtube.com/embed/uQasbpSFFcU",
        "video_caption": "This type of session builds habits around the box. It is not about roaming midfield like a playmaker.",
        "visual": "🎯",
        "visual_caption": "Stay high, get service, finish. That is the textbook job.",
        "key_idea": "A traditional #9 lives near the goal, leads the line, and finishes what the team builds."
    },
    {
        "id": 3,
        "title": "What Is a False 9?",
        "subtitle": "A striker who steps back on purpose.",
        "body": [
            "You now know how a normal #9 behaves. A <strong>False 9</strong> breaks those rules on purpose. They do not stay high near the other goal. They <em>drop toward midfield</em> to get the ball, connect passes, and help create chances.",
            "The word False is about misdirection. The shirt still says nine, but the player is not standing where a nine usually stands. Markers get confused because their training tells them to watch a high striker.",
            "The center-back must choose. <strong>If the defender follows</strong> the False 9, space opens behind the line. Attackers can run into that space. <strong>If the defender stays home</strong>, the False 9 can receive with time and room. Both choices hurt the defense.",
            "Moving away from the goal is the trick. The shape of the defense breaks before the False 9 even passes. <em>Not being where people expect</em> becomes a real weapon."
        ],
        "diagram": "false9example.png",
        "diagram_caption": "The False 9 checks into midfield. That pull can drag defenders and free runners behind them.",
        "visual": "💡",
        "visual_caption": "Step back, stress the line, let teammates attack the space you opened.",
        "key_idea": "A False 9 trades a high position for pockets of space. That choice forces bad answers from defenders and helps teammates run into gaps."
    },
    {
        "id": 4,
        "title": "Messi & Guardiola: The Blueprint",
        "subtitle": "How Barcelona showed the world this role.",
        "body": [
            "<strong>Pep Guardiola</strong> made the modern False 9 famous at Barcelona. That work started in the 2008-09 season. Messi was too good to stay wide forever. Samuel Eto'o still played like a classic #9. Guardiola solved the puzzle by using Messi as a striker who did not stay on the last line.",
            "The team had huge results. In May 2009 Barcelona beat Real Madrid <strong>6-2</strong> at the Bernabéu. Messi picked up the ball between the lines. Madrid's center-backs did not know whether to step out or hold the line. They kept guessing wrong.",
            "Messi fit the role because he could receive in tight space. He could see passes early. He could accelerate with the ball. Defenders still had to respect his shot. They could not leave him alone. When they followed him, Barcelona had room elsewhere.",
            "Everyone else had a job too. Wingers such as Henry and later Villa stayed wide and ran forward when Messi dropped. Midfielders like Xavi and Iniesta moved the ball quickly. The team needed all of those pieces to work together."
        ],
        "diagram": None,
        "video_embed": "https://www.youtube.com/embed/JPeI419Qd0g",
        "video_caption": "This clip shows how Guardiola used Messi in that free central role.",
        "visual": "🏆",
        "visual_caption": "Messi at Barcelona from 2008 to 2012 is still the famous example.",
        "key_idea": "Guardiola let Messi play as a False 9 during one of the strongest club runs ever. The team won La Liga, the Champions League, and more."
    },
    {
        "id": 5,
        "title": "The False 9 Today",
        "subtitle": "The idea did not disappear. It just spread out.",
        "body": [
            "You see the pure Guardiola copy less often now. Teams have watched the film. Some coaches send a midfielder to track the False 9 so the center-backs do not have to step out alone.",
            "The ideas still show up all over the game. An <strong>inverted winger</strong> such as Mohamed Salah or Arjen Robben cuts inside to find extra numbers. A <strong>second striker</strong> in a 4-4-2 also drops to link play. Playmakers like Kevin De Bruyne or Bruno Fernandes sometimes take up similar spaces even if the lineup card says something else.",
            "Guardiola still uses the idea at Manchester City when he lacks a tall target forward. He has used <strong>Bernardo Silva</strong> and De Bruyne in that kind of role. Brains and touch matter as much as size.",
            "The big lesson is simple. <strong>Space can beat static presence.</strong> A striker who steps back and pulls markers can open the game for everyone else. Coaches still teach that lesson even when they never use the words False 9."
        ],
        "diagram": None,
        "visual": "🌍",
        "visual_caption": "What started in Barcelona now shows up in many shapes around the world.",
        "key_idea": "Modern teams borrow the same idea: move off the chalkboard, drag defenders, and let teammates run into the holes."
    }
]

QUIZ = [
    {
        "id": 1,
        "question": "Which jersey number is usually worn by the main center forward, the classic striker?",
        "options": [
            "#7",
            "#10",
            "#9",
            "#11"
        ],
        "answer": 2,
        "explanation": "The #9 is the traditional striker number. Fans still link it to goal scorers such as Lewandowski, Drogba, and Ibrahimović.",
        "review_lesson_ids": [1],
    },
    {
        "id": 2,
        "question": "What does the word False mean in False 9?",
        "options": [
            "The player is pretending to be injured",
            "The player wears the wrong jersey number",
            "The striker is not standing where a normal #9 stands. They drop deep instead of staying high",
            "The trick only works one time in a match"
        ],
        "answer": 2,
        "explanation": "False means misdirection. The player still wears nine, but they show up between the lines. Defenders train for a high striker, so the change causes problems.",
        "review_lesson_ids": [3],
    },
    {
        "id": 3,
        "question": "What happens if a center-back does not follow the False 9 when the nine drops into midfield?",
        "options": [
            "The False 9 is always offside",
            "The False 9 can get the ball with time and room to hurt the defense",
            "The defense always wins the ball",
            "The wingers must drop to defend"
        ],
        "answer": 1,
        "explanation": "If nobody steps out, the False 9 receives in a pocket. They can turn, run at the goal, or play a splitting pass. That is why teams cannot always stay passive.",
        "review_lesson_ids": [3],
    },
    {
        "id": 4,
        "question": "What happens when a center-back follows the False 9 into midfield?",
        "options": [
            "The False 9 scores right away every time",
            "Space opens behind the defender for other attackers to exploit",
            "The offside trap always works",
            "Nothing changes and the defense looks fine"
        ],
        "answer": 1,
        "explanation": "When a center-back chases the nine, somebody has to cover the lane they left open. Attackers timed those runs famously at Barcelona with players like Xavi and Iniesta.",
        "review_lesson_ids": [3],
    },
    {
        "id": 5,
        "question": "Which coach is most tied to Lionel Messi playing as a False 9 at Barcelona?",
        "options": [
            "Jose Mourinho",
            "Diego Simeone",
            "Jurgen Klopp",
            "Pep Guardiola"
        ],
        "answer": 3,
        "explanation": "Pep Guardiola used Messi in that roaming central role starting around 2008. Barcelona won major trophies and millions of fans saw how the shape worked.",
        "review_lesson_ids": [4],
    },
    {
        "id": 6,
        "question": "Look at the image. Pretend the circled player is your number nine. Based only on where they stand, are they acting like a traditional striker or like a False 9?",
        "image": "quizquestionmessi.png",
        "options": [
            "False 9. They have come short between midfield and the back line to link play.",
            "Traditional striker. They are glued on the last line waiting to run in behind.",
            "Inverted winger. They started wide and cut in for a shot.",
            "Box-to-box midfielder. They are making a late run from deep."
        ],
        "answer": 0,
        "explanation": "A classic #9 holds the highest line near the center-backs. This player sits in the pocket between lines. That depth is what you expect from a False 9, not an old-school target man.",
        "review_lesson_ids": [2, 3],
    }
]


def _review_entries(lesson_ids):
    """Build lesson links for wrong-answer study hints."""
    out = []
    for lid in lesson_ids or []:
        if isinstance(lid, int) and 1 <= lid <= len(LESSONS):
            out.append({"num": lid, "title": LESSONS[lid - 1]["title"]})
    return out


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
        prev_num=lesson_num - 1,
        all_lessons=LESSONS,
        visited_lessons=session.get("visited_lessons", {})
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
        chosen=chosen,
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
        "explanation": question["explanation"],
    })


@app.route("/quiz/reset")
def quiz_reset():
    session.pop("quiz_answers", None)
    session.modified = True
    return redirect(url_for("quiz", q_num=1))


@app.route("/quiz/results")
def quiz_results():
    answers = session.get("quiz_answers", {})
    score = sum(1 for a in answers.values() if a.get("correct"))
    total = len(QUIZ)

    results = []
    for i, q in enumerate(QUIZ):
        ans = answers.get(str(i + 1), {})
        got_it_right = ans.get("correct", False)
        results.append({
            "question": q["question"],
            "image": q.get("image"),
            "correct_answer": q["options"][q["answer"]],
            "chosen_answer": q["options"][ans["chosen"]] if ans.get("chosen") is not None else "Not answered",
            "correct": got_it_right,
            "explanation": q["explanation"],
            "review": [] if got_it_right else _review_entries(q.get("review_lesson_ids", [])),
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
