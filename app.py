from flask import Flask, request, jsonify
import json, random

app = Flask(__name__)

with open("all_questions.json", encoding="utf-8") as f:
    data = json.load(f)

@app.route("/", methods=["GET"])
def home():
    return "題庫 API 運作中"

@app.route("/question/getquestion", methods=["POST"])
def question():
    payload = request.get_json()
    id = payload.get("id")
    cat = payload.get("category")
    exam = payload.get("exam_type")
    year = payload.get("year")

    results = data
    if id:
        results = [q for q in results if q["id"] == id]
    if cat:
        results = [q for q in results if q["category"] == cat]
    if exam:
        results = [q for q in results if q["exam_type"] == exam]
    if year:
        results = [q for q in results if q["year"] == year]

    if not results:
        return jsonify({"error": "找不到符合條件的題目"}), 404

    selected = random.choice(results)
    return jsonify(selected)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
