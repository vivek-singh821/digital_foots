from flask import Flask, render_template, request

from github_api import get_github_data
from reddit_api import get_reddit_data

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    github = None
    reddit = None

    github_error = ""
    reddit_error = ""
    form_error = ""

    score = 0

    if request.method == "POST":

        github_user = request.form["github"].strip()

        reddit_user = request.form["reddit"].strip()

        if not github_user and not reddit_user:

            form_error = "Please enter at least one username"

        if github_user:

            github = get_github_data(github_user)

            if github:

                user = github["profile"]

                score += (
                    user["followers"] +
                    user["public_repos"] * 2 +
                    github["total_stars"]
                )

            else:

                github_error = "GitHub user not found"

        if reddit_user:

            reddit = get_reddit_data(reddit_user)

            if reddit:

                score += reddit["karma"] // 100

            else:

                reddit_error = "Reddit user not found"

    return render_template(
        "index.html",
        github=github,
        reddit=reddit,
        score=score,
        github_error=github_error,
        reddit_error=reddit_error,
        form_error=form_error
    )

if __name__ == "__main__":

    app.run(debug=True)