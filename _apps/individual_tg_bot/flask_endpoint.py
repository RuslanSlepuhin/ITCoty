from flask import Flask, jsonify, request

from service import db
from _apps.individual_tg_bot.settings import APP_HOST,APP_PORT, APP_DEBUG
app = Flask(__name__)


@app.route("/user_requests_vacancies", methods=["GET"])
async def endpoint():
    if request.args is not None:
        selected_direction = request.args.get("selected_direction")[2:-2]
        selected_specializations = request.args.get("selected_specializations")[2:-2]
        selected_level = request.args.get("selected_level")[2:-2]
        selected_location = request.args.get("selected_location")[2:-2]
        selected_work_format = request.args.get("selected_work_format")[2:-2]
        keyword = request.args.get("keyword")
        vacancies = await db.receive_vacancy(
            direction=selected_direction,
            specialization=selected_specializations,
            level=selected_level,
            location=selected_location,
            work_format=selected_work_format,
            keyword=keyword,
        )
        return jsonify(vacancies)



if __name__ == "__main__":
    app.run(host=APP_HOST, port=APP_PORT, debug=APP_DEBUG)
