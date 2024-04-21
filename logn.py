from flask import render_template,Flask, request
app = Flask(__name__)

@app.route('/login/<username>/<password>')
def login(username,password):
    if username=="admin" and password=="admin":
        return 'welcome %s'%username
    else:
        return 'login fail'

@app.route("/")
def loginpage():
    return render_template('login.html')
@app.route("/validate",methods=['post'])
def validate():
    # login("admin","admin")
    # return 'invalidation';
    user=request.form['username']
    pwd=request.form['password']
    if user== 'admin' and pwd=='admin':
         return 'welcome %s'%(user)
    else:
        return 'login Failed'
        # return '%s %s' %(user,pwd)
   
if __name__ =='__main__':
    app.run(debug=True)