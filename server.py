from flask import Flask, render_template
from duplicateRemover import DuplicateRemover
from duplicateCounter import DuplicateCounter

app = Flask(__name__)


@app.route('/')
def index():
    nums = [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6]
    remove_nums = DuplicateRemover(nums)
    nums = remove_nums.remove_duplicates()

    # noinspection PyUnresolvedReferences
    return render_template('index.html', nums=nums)


@app.route('/count')
def count():
    nums = [1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6]
    count_nums = DuplicateCounter(nums)
    count = count_nums.count_duplicates()


    return render_template("count.html", count = count)