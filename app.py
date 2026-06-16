@app.route("/search")
def search():

    title = request.args.get("title")

    result = task_manager.find_task(title)

    return jsonify(result)