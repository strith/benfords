from ast import literal_eval
import csv
import math
import os
from flask import Blueprint, redirect, render_template, request
from flask import current_app as app
from werkzeug.utils import secure_filename

benford_eval_bp = Blueprint(
  'benford_eval_bp', __name__,
  template_folder='templates',
  static_folder='static'
)

@benford_eval_bp.route("/benford_eval", methods=['GET', 'POST'])
def benford_eval():

  if request.method == 'GET':
    return redirect('/')

  if request.method == 'POST':
    file_name = secure_filename(request.form['file_name'])
    data_col = request.form['col_name']
    value_count = 0
    file_path = os.path.join(app.config['UPLOADS_FOLDER'], file_name)
    labels = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    benfords_dist = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
    distribution = [0] * 9
    percents = [0] * 9

    data_set = csv.DictReader(open(file_path), delimiter='\t')

    for el in data_set:
      val = literal_eval(dict(el)[data_col])

      if val != 0:
        first_int = math.floor(val / math.pow(10, math.floor(math.log10(val))))
        value_count += 1
        distribution[first_int - 1] += 1
    
    i = 0
    while i < len(distribution):
      percents[i] = round(distribution[i] / value_count * 100, 1)
      i += 1


    return render_template('benford_evaluation.html', labels=labels, benfords_dist=benfords_dist, dist=distribution, percents=percents)
