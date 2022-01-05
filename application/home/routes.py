import csv
import os
from stat import *
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
        
        file_path = os.path.join(app.config['UPLOADS_FOLDER'], file_name)

        # if os.path.isfile(file_path):
        #   return 'That file already exists, please try again'

        f.save(file_path)
        os.chmod(file_path, 0o664)

        input_file = csv.DictReader(open(file_path), delimiter='\t')
        keys_list = [*next(input_file)]

        # Find the first n lines of the file so the user can click
        # on the column that contains the data
        sample_data = []
        sample_size = 10
        row_count = 0

        for el in input_file:
          row_count += 1
          if(row_count > sample_size):
            break
          sample_data.append(dict(el))

        return render_template('data_selection.html', file_name=file_name, col_data=keys_list, row_data=sample_data)
