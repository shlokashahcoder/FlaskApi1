from flask import Flask, jsonify, request
 
app = Flask(__name__)

data=[
{
    "name":"shloka",
    "grade":9,
    "school":"zydus school"
},
{
    "city":"Ahmedabad",
    "state":"Gujarat",
    "country":"India"
}
]

@app.route("/post-data",methods=["POST"])
def myData3():
    newData={
        "hobby":"reading",
        "favFood":"Pizza"
    }
    data.append(newData)
    return({
        "NewData":data,
        "message":"uploaded the new data!"
    })

@app.route("/")
def myData():
    return "this is my first api and i am adding some data to it!"

@app.route("/data")
def myData2():
    return ({
        "MyData":data,
        "message":"success" 
    })

if __name__ == "__main__":
    app.run()