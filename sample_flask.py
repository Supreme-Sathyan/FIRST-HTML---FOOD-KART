from flask import Flask, redirect, url_for, request,render_template
import mysql.connector as a
mycon=a.connect(host='localhost',user='root',password='Saraswathi',database='cake')
cursor=mycon.cursor()
app = Flask(__name__)

 
@app.route('/success/<name>')
def success(name):
    return render_template('home.html')
 
 
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        pas = request.form['pwd']
        query="insert into accounts values('{}','{}');".format(user,pas)
        cursor.execute(query)
        mycon.commit()                                                                                       
        '''f=open('server.txt','a')
        u=user+'\t'+pas+'\n'
        f.write(u)
        f.close()'''
        return redirect(url_for('success', name=user))
 
if __name__ == '__main__':
    app.run(debug=True)

