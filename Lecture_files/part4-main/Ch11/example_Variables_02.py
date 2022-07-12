from flask import Flask
app = Flask(__name__)

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' %postID

@app.route('/rev/<float:revNO>')
def revision(revNO):
   return 'Revision Number %f' %revNO

if __name__ == '__main__':
   app.run(debug = True)
