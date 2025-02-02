from PIL import Image
from collections import Counter
from flask import Flask, render_template, request

app = Flask(__name__)


def color_analyze(image, x):
    image = Image.open(image).convert("RGB")


    counts = Counter(image.getdata())


    top_colors = counts.most_common(x)


    total_pixels = sum(counts.values())
    colors = ["#{:02x}{:02x}{:02x}".format(*color) for color, _ in top_colors]
    percents = [f"{round(count / total_pixels * 100, 2)}%" for _, count in top_colors]

    return colors, percents


picture = "static/img/Picture.png"
starter = "static/img/Starter.png"


@app.route('/')
def home():
    num = 5
    colors, percents = color_analyze(starter, num)
    return render_template("index.html", colors=colors, percents=percents, num=num, photo=starter)


@app.route('/upload', methods=["POST"])
def uploaded():
    file = request.files["picture"]
    num = int(request.form.get("num", 5))
    if file:
        file.save(picture)
    colors, percents = color_analyze(picture, num)
    return render_template("index.html", colors=colors, percents=percents, num=num, photo=picture)


if __name__ == "__main__":
    app.run(debug=True)
