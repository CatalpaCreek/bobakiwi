from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

popular_tea = [
    "1",
    "2",
    "4",
]

result_tea = []
curdata = []
search_name = ""

data = {
    "1": {
        "id": "1",
        "title": "Gong Cha",
        "Image": "https://assets.simpleviewinc.com/simpleview/image/upload/crm/frisco/Gong-Cha-c627501b5056a36_c62751aa-5056-a36a-072fb3b6f5362966.jpg",
        "description": "Gong cha is an international beverage franchise specializing in freshly prepared bubble tea. With a successful business model and proven track record, it has opened over 1,650 Cafes in 20 countries.Gong cha is known across the world for its signature Milk Foam. Its creamy, sweet and savory flavor balance and whipped texture make it the perfect complement to our freshly brewed teas. Our delicious milk foam is hand-crafted for each customer and made from the freshest milk and highest quality, signature ingredients.",
        "location": "Flatbush",
        "address": "1570 Flatbush Avenue, Brooklyn, NY 11210",
        "hours": "Open 10:30am to 9:30pm daily",
        "rating": "5",
        "popular_orders": ["Lemon Wintermelon Basil Seeds Milk Tea", "Taro Milk Tea", "Watermelon Milk Tea"]
        },
    
    "2": {
        "id": "2",
        "title": "Tiger Sugar",
        "Image": "https://www.mercurynews.com/wp-content/uploads/2021/07/SJM-L-TIGERSUGAR-0711-01_85963174.jpg?w=978",
        "description": "The original brown sugar bubble tea with fresh cream and a unique tiger stripe design. Often sporting hour-long lines, this popular spot for bubble tea is well-known for its Brown Sugar Boba. That is a drink where boba is cooked with brown sugar, and then cold milk is poured on top. It's a refreshing cold drink that is creamy and delicious.",
        "location": "Chinatown",
        "address": "197 Canal St, New York, NY 10013",
        "hours": "Open 11:30 am to 8:30 pm Monday to Thursday, 11 am to 9 pm Friday to Sunday",
        "rating": "5",
        "popular_orders": ["Brown Sugar Boba", "Brown Sugar Boba + Pearl with Cream mousse"]
        },

    "3": {
        "id": "3",
        "title": "I'Milky",
        "Image": "https://images.squarespace-cdn.com/content/v1/5dec7a6f0803c10a0120212c/6f886fd7-8c42-45b1-9394-90ca22b309d0/KC_iMilky-1398.jpg?format=2500w",
        "description": "This women-led store offers fresh milk and fruit teas using premium tea leaves, local farm-fresh milk, and cane sugar. I'Milky focuses using fresh and non artificial ingredients. The philosophy is to keep flavors natural and authentic. Their menu includes Brown Sugar Bubble Milk, Yogurt Green Tea, Strawberry, Mango, and Taro Milk. Customers can also buy bubble tea kits and bento boxes.",
        "location": "Midtown",
        "address": "992 6th Ave, New York, NY 10018",
        "hours": "Open 10:30am to 9:30pm Monday to Thursday, 10:30am to 10pm Friday, 12 to 9:30pm Saturday, 12 to 8pm Sunday.",
        "rating": "4",
        "popular_orders": ["Brown Sugar Bubble Milk", "Yogurt Green Tea", "Strawberry Milk", "Mango Milk", "Taro Milk"]
        },

    "4": {
        "id": "4",
        "title": "The Alley",
        "Image": "http://images.summitmedia-digital.com/spotph/images/2019/05/10/the-alley-640-1557501747.jpg",
        "description": "The Alley is a modern bubble tea chain known for their Brown Sugar Deerioca (tapioca pearl) drinks. Founded by graphic designer Mao-ting Chiu in 2015, this newer brand has grown to more than 300 locations across China, Japan, Canada, France, Australia, and USA. The Alley's trendy and unique branding features their signature logo: a male deer or buck head, which has made it a social media darling.",
        "location": "Cooper Square",
        "address": "68 Cooper Sq, New York, NY 10003",
        "hours": "Open 12 to 8 pm Monday to Thursday, 12 to 9 pm Friday to Sunday",
        "rating": "5",
        "popular_orders": ["Royal No.9 Milk Tea", "Brown Sugar Deerioca Milk"]
        },
    
    "5": {
        "id": "5",
        "title": "Kung Fu Tea",
        "Image": "https://d1ralsognjng37.cloudfront.net/281ebbce-1a1d-495d-9b6f-fef70842acb9.jpeg",
        "description": "This popular boba chain store has over 35 locations across New York City. Customers can customize drinks with fun toppings, sugar levels, and ice levels. Choose from toppings such as pudding, nata jelly, red bean, and tapioca. In addition, its new Hot Boba Summer menu offers Mango Creamsicle, Caramel Milk tea, and Lemon Almond Pie.",
        "location": "Elmhurst",
        "address": "86-12 Justice Ave, Elmhurst NY 11373",
        "hours": "Open 12 to 8 pm Monday to Sunday",
        "rating": "3",
        "popular_orders": ["Kung Fu Milk Tea", "Lychee Punch", "Honey Green Milk Tea"]
        },

    "6": {
        "id": "6",
        "title": "If Cha Tea",
        "Image": "https://pbs.twimg.com/media/DwhGccEX4AEZrfo.jpg",
        "description": "If Cha Teas is known for their fresh fruit teas, topped to the brim with sliced fruits. Check out their fun toppings like rainbow jelly and popping mango, juice-filled bubbles that pop in your mouth! They have a good selection of oolongs as well as pu-erh's. Good new little tea place and not too expensive.",
        "location": "Flushing",
        "address": "136-11 38th Ave, Flushing, NY 11354",
        "hours": "Open 11 am to 8 pm daily",
        "rating": "3",
        "popular_orders": ["Peach Black Tea", "Orange Black Tea"]
        },

    "7": {
        "id": "7",
        "title": "Tea and Milk",
        "Image": "https://cdn.viewing.nyc/assets/media/b24247582fcac9bfae347713d0ef2bdb/elements/dcc49d3e0ca8beb8e07e40c459602ec0/e2d3ed18-fb54-45f6-a845-3a4aa0b927aa.jpg",
        "description": "Tea and Milk’s signature homemade Taro Root Milk tea is popular and perfect for taro lovers. The store offers unique flavors from around the world. Such as Fuji Apple Chia Green Tea, Nilgiri Black tea from India, and Grandma's Masala Chai. An additional location opened recently in Chelsea Market.",
        "location": "Astoria",
        "address": "32-02 34th Avenue, Astoria, New York 11106",
        "hours": "Open 12 to 8 pm Sunday to Wednesday, 12 to 9 pm Thursday to Saturday",
        "rating": "4",
        "popular_orders": ["Signature Taro Root Milk tea", "Fuji Apple Chia Green Tea"]
        },

    "8": {
        "id": "8",
        "title": "PaTea",
        "Image": "https://media.timeout.com/images/105259515/750/422/image.jpg",
        "description": "Pa Tea is a bubble tea shop located in Union Square. It offers fruit-flavored teas, milk teas, brown sugar milk, and slushies. Their unique flavors include Rose Milk Tea, Salted Caramel Oolong Milk Tea, and Hazelnut Milk Tea. They offer a free upgrade to stubby, a size bigger than large, for those who order a large.",
        "location": "Union Square",
        "address": "227 E 14th St, New York, NY 10003",
        "hours": "Open 12 to 9 pm Sunday to Thursday, 12 to 10 pm Friday and Saturday",
        "rating": "4",
        "popular_orders": ["Rose Milk Tea", "Salted Caramel Oolong Milk Tea", "Hazelnut Milk Tea"]
        },

    "9": {
        "id": "9",
        "title": "Yaya Tea",
        "Image": "https://images.squarespace-cdn.com/content/v1/5e6fafa57e34847ae52727f1/1624297888880-8CQTQ2XQJG63NTCL8ZUJ/1+Yaya.jpg",
        "description": "Yaya Tea has an impressive selection of fruit teas, milk teas, and a customizable menu where you can choose a tea and add up to 3 flavors. They give very unique names to their bubble tea. Their popular teas include Better Life (Strawberry, Lychee, and Pineapple Green Tea), Sunrise (Strawberry and Mango White Tea), and Boyfriend (Mango and Lychee White Tea). In addition, get 10% off any small drink when you reuse their glass bottles!",
        "location": "Chinatown",
        "address": "51 Chrystie St, New York, NY 10002",
        "hours": "Open 10:30am to 8:30pm daily.",
        "rating": "4",
        "popular_orders": ["Better Life", "Sunrise", "Boyfriend"]
        },

    "10": {
        "id": "10",
        "title": "M Tea",
        "Image": "https://offloadmedia.feverup.com/secretnyc.co/wp-content/uploads/2020/01/10105030/mtea_lonelycoffeer.jpg",
        "description": "MTea LIC is the place where great cooking and fantastic vibes meet. The food is nutritious, delicious, and affordable, and they welcome diners young and old. M Tea is popular for its signature Fruit Teas, Dragon Fruit Tea, Golden Pineapple Tea, and Avocado Tea, as well as the classic milk and creme brulee teas. In addition to their bubble tea, they offer beautifully prepared french style pastries such as Lychee Mousse, Tiramisu, and Jello Cakes. ",
        "location": "Long Island City",
        "address": "23-01 41st Ave Store 1D, Queens, NY 11101",
        "hours": "Open 11 am to 9 pm daily. ",
        "rating": "3",
        "popular_orders": ["Dragon Fruit Tea", "Golden Pineapple Tea", "Avocado Tea", "Lychee Mousse", "Tiramisu", "Jello Cakes"]
        },
}



# ROUTES

@app.route('/')
def homepage():
   return render_template('homepage.html', data = data, popular_tea = popular_tea, result_tea = result_tea, search_name = search_name) 

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/addItem',methods=["POST"])
def addItem():
    global data
    datalength = len(data) + 1

    title = request.form.get("title")
    Image = request.form.get("Image")
    description = request.form.get("description")
    location = request.form.get("location")
    address = request.form.get("address")
    hours = request.form.get("hours")
    rating = request.form.get("rating")
    popular_orders = request.form.get("popular_orders")
    
    obj = dict();
    obj["id"] = str(datalength)
    obj["title"] = title
    obj["Image"] = Image
    obj["description"] = description
    obj["location"] = location
    obj["address"] = address
    obj["hours"] = hours
    obj["rating"] = rating
    obj["popular_orders"] = popular_orders.split(",")
    data[str(datalength)] = obj
    return jsonify({"num": datalength})


@app.route('/edit/<id>')
def edit_data(id=None):
    global data
    global curdata
    curdata.clear()
    for item in data:
        if data[item]['id'] == id:
            curdata.append(data[item])
    return render_template('edit.html', data=curdata)


@app.route('/update/<id>',methods=["POST"])
def update(id=None):
    global data

    title = request.form.get("title")
    Image = request.form.get("Image")
    description = request.form.get("description")
    location = request.form.get("location")
    address = request.form.get("address")
    hours = request.form.get("hours")
    rating = request.form.get("rating")
    popular_orders = request.form.get("popular_orders")

    obj = data[id]
    if title:
        obj["title"] = title
    if Image:
        obj["Image"] = Image
    if description:
        obj["description"] = description
    if location:
        obj["location"] = location
    if address:
        obj["address"] = address
    if hours:
        obj["hours"] = hours
    if rating:
        obj["rating"] = rating
    if popular_orders:
        obj["popular_orders"] = popular_orders.split(",")
    data[id] = obj

    return render_template('view.html', id = id, data = data, result_tea = result_tea, search_name = search_name)


@app.route('/view/<id>')
def view_data(id = None):
    return render_template('view.html', id = id, data = data, result_tea = result_tea, search_name = search_name) 
  

@app.route('/search_results')
def search_results():
    return render_template('search_results.html', data = data, result_tea = result_tea, search_name = search_name) 


@app.route('/search/<search_name>', methods=['GET', 'POST'])
def search_now(search_name = None):
    return render_template('search_results.html', data = data, result_tea = result_tea, search_name = search_name) 


@app.route('/search_name', methods=['GET', 'POST'])
def search_tea():
    global data 
    global result_tea
    global search_name

    json_data = request.get_json()   
    search_name = json_data["search_name"] 
    search_name = search_name.lower()
    
    result_tea = []

    for item in data:
        titlestring = data[item]['title'].lower()
        if search_name in titlestring:
            result_tea.append(data[item]['id'])

    for item in data:
        currid = data[item]['id']
        currentorder = data[item]['popular_orders']
        string_list = [each_string.lower() for each_string in currentorder]
        for curr in string_list:
            if search_name in curr:
                if currid not in result_tea:
                    result_tea.append(currid)
    
    for item in data:
        currid = data[item]['id']
        locationstring = data[item]['location'].lower()
        if search_name in locationstring:
            if currid not in result_tea:
                result_tea.append(data[item]['id'])

    return jsonify(result_tea = result_tea, search_name = search_name)


if __name__ == '__main__':
   app.run(debug = True)

