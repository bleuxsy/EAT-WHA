from flask import Flask, render_template, request
import sys
application = Flask(__name__)


@application.route("/")
def index():
    return render_template("index.html")


@application.route("/login")
def login():
    return render_template("login.html")

@application.route("/signup")
def signup():
    return render_template("signup.html")

@application.route("/register_restaurant")
def register_restaurant():
    return render_template("register_restaurant.html")

@application.route("/register_mainmenu")
def register_mainmenu():
    return render_template("register_mainmenu.html")

@application.route("/view_restaurantlist")
def view_restaurantlist():
    return render_template("view_restaurantlist.html")

@application.route("/map")
def map():
    return render_template("map.html")

@application.route("/recommend")
def recommend():
    return render_template("recommend.html")

@application.route("/mypage")
def mypage():
    return render_template("mypage.html")

@application.route("/view_one_restaurant")
def view_one_restaurant():
    return render_template("view_one_restaurant.html")


@application.route("/result", methods=['GET','POST'])
def result():
    image_file=request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form
    return render_template("result.html",data=data,image_file=image_file.filename)



# ~~~~~~~~유미~~~~~~~~~~~~
@application.route("/register_mainmenu", methods=['GET','POST'])
def reg_register_mainmenu():
    image_file=request.files["file"]
    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form
    return render_template("register_mainmenu.html", data=data, image_file=image_file.filename) 
#나중에 view_mainmenu와 image_file=image_file.filename 으로 바꾸고 추가해야 함.   , image_file=image_file.filename

@application.route("/view_mainmenu", methods=['GET','POST'])
def reg_view_mainmenu():    
# #    image_file=request.files["file"]
# #    image_file.save("static/image/{}".format(image_file.filename))
#	if request.method=='POST':
        result=request.form
        return render_template("view_mainmenu.html")
#후기~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
@application.route("/write_review", methods=['GET','POST'])
def reg_write_review():
#    image_file=request.files["file"]
#    image_file.save("static/image/{}".format(image_file.filename))
    data=request.form
    return render_template("view_review.html", data=data)

@application.route("/view_review", methods=['GET','POST'])
def reg_view_review():
        result=request.form
        return render_template("view_review.html")

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug = True)
