import pymysql
import pygal
from datetime import datetime    
from flask import Flask, render_template, url_for, redirect, request, flash

from forms import RegistrationForm, LoginForm, SuprimForm,AjoutForm,ApForm,AchatForm,SaveForm,ModifForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, current_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'




@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/admin", methods=['GET', 'POST'])
def admin():
   
    return render_template('admin.html')



@app.route("/panier", methods=['GET', 'POST'])
def panier():
         form = AchatForm()
         if form.validate_on_submit():
             return render_template('succ.html')
         con=pymysql.connect(host="localhost",user="root",passwd="mysql",db="mypython")
         mycursor=con.cursor()
         mycursor.execute("SELECT ref,nominstr,prix FROM panier;")
         posts=mycursor.fetchall()
         x=0
         for post in posts:
          print(post[2])
          x+=post[2]
         print(x)
         
         return render_template('panier.html',posts=posts,data=x,form=form)



@app.route("/valider", methods=['GET', 'POST'])
def valider():
      form = ApForm()
      if form.validate_on_submit():
          print(form.ref.data)
          con=pymysql.connect(host="localhost",user="root",passwd="",db="mypython")
          mycursor=con.cursor()
          sql= "SELECT * FROM instrument where ref=%s;"
          val=(''+form.ref.data+'')
          mycursor.execute(sql,val)
          instr=mycursor.fetchall()
          x=instr[0]
          print(x)
          ref1=str(x[0])
          print(ref1)
          nom=x[1]
          print(nom)
          prix=str(x[2])
          print(prix)
          sql="INSERT INTO panier(ref,nominstr,prix) VALUES(%s,%s,%s)"
          val=(''+ref1+'',''+nom+'',''+prix+'')
          mycursor.execute(sql,val)
          con.commit()
          con.close()
          return render_template('valider.html',form=form)
      return render_template('valider.html', form=form)







    
@app.route("/graph")
def graph():
    graph = pygal.Line()
    graph.title = '% stock restant'
    con=pymysql.connect(host="localhost",user="root",passwd="",db="mypython")
    mycursor=con.cursor()
    mycursor.execute("SELECT ref FROM instrument;")
    ref=mycursor.fetchall()
    mycursor.execute("SELECT nbvente FROM instrument;")
    nb=mycursor.fetchall()
    listeR = []
    listeN = []
    for ref in ref:
      listeR.append(str(ref[0]))

    for nb in nb:
      listeN.append(int(nb[0]))
      
    graph.x_labels = listeR[0:len(listeR)]
    graph.add('instruments', listeN[0:len(listeN)])
    
    graph_data = graph.render_data_uri()
    return render_template("graph.html", graph_data = graph_data)








@app.route("/suprimer", methods=['GET', 'POST'])
def suprimer():
    form = SuprimForm()
    if form.validate_on_submit():
        
        con=pymysql.connect(host="localhost",user="root",passwd="",db="mypython")
        mycursor=con.cursor()
        sql="DELETE FROM instrument WHERE ref=%s;"
        val=(''+form.reference.data+'')
        mycursor.execute(sql,val)
        con.commit()
        con.close()
        return render_template('suprimer.html', form=form)
    return render_template('suprimer.html', form=form)


@app.route("/ajouter", methods=['GET', 'POST'])
def ajouter():
    form = SaveForm()
    if form.validate_on_submit():
          print(form.ref.data)
          print(form.nominstr.data)
          print(form.prix.data)
          print(form.image.data)
          print(form.lieufab.data)
          print(form.quantiteinit.data)
          con=pymysql.connect(host="localhost",user="root",passwd="",db="mypython")
          mycursor=con.cursor()
          sql="INSERT INTO instrument(ref,nominstr,prix,lieufab,image,quantiteinit) VALUES(%s,%s,%s,%s,%s,%s)"
          val=(''+form.ref.data+'',''+form.nominstr.data+'',''+form.prix.data+'',''+form.lieufab.data+'',''+form.image.data+'',''+form.quantiteinit.data+'')
          mycursor.execute(sql,val)
          con.commit()
          con.close()
          return render_template('ajouter.html', form=form)
    return render_template('ajouter.html', form=form)

    
    
@app.route("/modifier", methods=['GET', 'POST'])
def modifier():

  form = ModifForm()
  if form.validate_on_submit():
          print(form.ref.data)
          print(form.prix.data)
        
          con=pymysql.connect(host="localhost",user="root",passwd="",db="mypython")
          mycursor=con.cursor()
          mycursor.execute("UPDATE instrument SET prix="+form.prix.data+" WHERE ref="+form.ref.data+";")
          
         
          con.commit()
          con.close()
          return render_template('modifier.html', form=form)
  return render_template('modifier.html', form=form)


@app.route("/luth", methods=['GET', 'POST'])
def luth():
    con=pymysql.connect(host="localhost",user="root",passwd="mysql",db="mypython")
    mycursor=con.cursor()
    mycursor.execute("SELECT ref,prix,lieufab,image,sound FROM instrument where nominstr='oud';")
    posts=mycursor.fetchall()
    print(posts);
    form = AjoutForm()
    if form.validate_on_submit():
             return redirect(url_for('valider'))
      
             #con=pymysql.connect(host="localhost",user="root",passwd="",db="mypython")
             #mycursor=con.cursor()
             #sql="INSERT INTO panier(ref,prix) VALUES(%s,%s)"
             #val=(''+ref+'',''+prix+'')
             #mycursor.execute(sql,val)
             #con.commit()
             #con.close()
            
   
    return render_template('luth.html', form=form,posts=posts)
    
    

@app.route("/violon", methods=['GET', 'POST'])
def violon():
    con=pymysql.connect(host="localhost",user="root",passwd="mysql",db="mypython")
    mycursor=con.cursor()
    mycursor.execute("SELECT ref,prix,lieufab,image,sound FROM instrument where nominstr='violon';")
    post=mycursor.fetchall()
    print(post)
   
    form = AjoutForm()
    if form.validate_on_submit():
             return redirect(url_for('valider'))
      
             #con=pymysql.connect(host="localhost",user="root",passwd="",db="mypython")
             #mycursor=con.cursor()
             #sql="INSERT INTO panier(ref,prix) VALUES(%s,%s)"
             #val=(''+ref+'',''+prix+'')
             #mycursor.execute(sql,val)
             #con.commit()
             #con.close()
            
   
    return render_template('violon.html', form=form,posts=post)



@app.route("/piano", methods=['GET', 'POST'])
def piano():
    con=pymysql.connect(host="localhost",user="root",passwd="mysql",db="mypython")
    mycursor=con.cursor()
    mycursor.execute("SELECT ref,prix,lieufab,image,sound FROM instrument where nominstr='piano';")
    posts=mycursor.fetchall()
   
    form = AjoutForm()
    if form.validate_on_submit():
             return redirect(url_for('valider'))
      
             #con=pymysql.connect(host="localhost",user="root",passwd="",db="mypython")
             #mycursor=con.cursor()
             #sql="INSERT INTO panier(ref,prix) VALUES(%s,%s)"
             #val=(''+ref+'',''+prix+'')
             #mycursor.execute(sql,val)
             #con.commit()
             #con.close()
            
   
    return render_template('piano.html', form=form,posts=posts)


@app.route("/percussion", methods=['GET', 'POST'])
def percussion():
    con=pymysql.connect(host="localhost",user="root",passwd="mysql",db="mypython")
    mycursor=con.cursor()
    mycursor.execute("SELECT ref,prix,lieufab,image,sound FROM instrument where nominstr='percussion';")
    posts=mycursor.fetchall()
   
    form = AjoutForm()
    if form.validate_on_submit():
             return redirect(url_for('valider'))
      
             #con=pymysql.connect(host="localhost",user="root",passwd="",db="mypython")
             #mycursor=con.cursor()
             #sql="INSERT INTO panier(ref,prix) VALUES(%s,%s)"
             #val=(''+ref+'',''+prix+'')
             #mycursor.execute(sql,val)
             #con.commit()
             #con.close()
            
   
    return render_template('percussion.html', form=form,posts=posts)









@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
    
        con=pymysql.connect(host="localhost",user="root",passwd="",db="mypython")
        mycursor=con.cursor()
        sql="INSERT INTO user(username,email,password) VALUES(%s,%s,%s)"
        val=(''+form.username.data+'',''+ form.email.data+'',''+ form.password.data+'')
        mycursor.execute(sql,val)
        con.commit()
        con.close()
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'manou@site.com' and form.password.data == 'password':
            
            return redirect(url_for('admin'))
        else:
            flash('barawah hhh. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)





if __name__ == '__main__':
    app.run(debug=True)
