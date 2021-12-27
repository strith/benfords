import csv
import math
import os
from flask import Blueprint, render_template, request
from flask import current_app as app
from werkzeug.utils import secure_filename

# Config
home_bp = Blueprint(
  'home_bp', __name__,
  template_folder='templates',
  static_folder='static'
)

@home_bp.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("upload.html")

    if request.method == 'POST':
        f = request.files['file']
        file_name = secure_filename(f.filename)

        if file_name == '':
          return 'Invalid file, please try again'
        
        base_dir = os.path.join(app.config['UPLOADS_FOLDER'], file_name)

        # if os.path.isfile(base_dir):
        #   return 'That file already exists, please try again'

        f.save(base_dir)

        input_file = csv.DictReader(open(base_dir), delimiter='\t')
        keys_list = [*next(input_file)]

        # Find the first n lines of the file so the user can click
        # on the column that contains the data
        sample_data = []
        sample_size = 10
        row_count = 0
        first_ints = []

        for el in input_file:
          row_count += 1
          if(row_count > sample_size):
            break
          sample_data.append(dict(el))

        # find the first integer of each element in the selected column
        # of the dataset
        # firstInt = math.floor(val / math.pow(10, math.floor(math.log10(val))))

        return render_template('data_selection.html', col_data=keys_list, row_data=sample_data)

        # Make it do something useful
        # return 'file uploaded successfully'
