from flask import Flask,render_template , request , send_from_directory , flash ,redirect
from flask_sqlalchemy import SQLAlchemy
import os
import secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pdfs.db'
db = SQLAlchemy(app)

class PdfFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
with app.app_context():
  db.create_all()
@app.route('/')
def myp():
  return render_template('index.html')
@app.route('/contact.html')
def contact():
  return render_template('contact.html')
@app.route('/about.html')
def about():
  return render_template('about.html')
@app.route('/upload.html')
def upload():
  return render_template('upload.html')
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'pdf_file' in request.files:
        pdf_file = request.files['pdf_file']
        if pdf_file.filename != '':
            new_pdf = PdfFile(filename=pdf_file.filename)
            uploads_dir = os.path.join(app.root_path, 'uploads')
            os.makedirs(uploads_dir, exist_ok=True)
            db.session.add(new_pdf)
            db.session.commit()
            file_path = os.path.join(uploads_dir, pdf_file.filename)
            pdf_file.save(file_path)
            flash('File uploaded successfully!', 'success')

    return render_template('upload.html')
@app.route('/view.html')
def view():
  pdfs = PdfFile.query.all()
  return render_template('view.html', pdfs=pdfs)
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)
@app.route('/delete.html')
def delete():
    pdfs = PdfFile.query.all()
    return render_template('delete.html', pdfs=pdfs)
@app.route('/delete', methods=['POST'])
def delete_pdfs():
    pdf_ids = request.form.getlist('delete_pdf')
    for pdf_id in pdf_ids:
        pdf = PdfFile.query.get(pdf_id)
        if pdf:
            db.session.delete(pdf)
            db.session.commit()
    flash('Selected PDFs deleted successfully!', 'success')
    return redirect('/delete.html')


    
  

if __name__=='__main__':
  app.secret_key = secrets.token_hex(16)
  app.run(host='0.0.0.0',debug=True)