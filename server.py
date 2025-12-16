from flask import Flask , render_template

app = Flask(__name__) 

@app.route('/')
def index():
    title = 'Home Page'
    return render_template('index.html',title='Home Page') 

@app.route('/about')
def about():    
    title = 'About Page'
    name = 'Thanapoom Rattanapakdee'
    email = 'Thanapoom@mail.com'
    mobile = '044-444-4444'
    age = 22
    return render_template('about.html',title=title,name=name,email=email,mobile=mobile,age=age)

@app.route('/favorite/foods')
def favorite_foods():
    title = 'Favorite Foods'
    foods = ['หมูทอดกระเทียม','ข้าวมันไก่','ฝัดกระเพรา','หมูกระทะ','พิซซ่า']
    return render_template('favorite_foods.html',title=title,foods=foods)

@app.route('/favorite/spots')
def spots():
    title = 'Favorite Spots'
    spots = ['Football','Batminton','Ping Pong','Swimming','Bike']
    return render_template('spots.html',title=title,spots=spots)
