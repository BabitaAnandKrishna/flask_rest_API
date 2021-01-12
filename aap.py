from flask import Flask, jsonify

app = Flask(__name__)

courses = [
            {
                    "name": "Python",
                    "course_id": "0",
                    "Description": "Python programming certification helps you learn"
                                    "Python in the structured learning path with innovative",
                    'price': "Visit Edureka.co",
            },
            {
                    "name": "Flutter",
                    "course_id": "1",
                    "Description": "Python programming certification helps you learn"
                                    "Python in the structured learning path with innovative",
                    'price': "Visit Edureka.co",
            },
            {
                    "name": "Java",
                    "course_id": "2",
                    "Description": "Python programming certification helps you learn"
                                    "Python in the structured learning path with innovative",
                    'price': "Visit Edureka.co",
            },
            {
                    "name": "Data Science",
                    "course_id": "3",
                    "Description": "Python programming certification helps you learn"
                                    "Python in the structured learning path with innovative",
                    'price': "Visit Edureka.co",
            },
            {
                    "name": "HTML",
                    "course_id": "4",
                    "Description": "Python programming certification helps you learn"
                                    "Python in the structured learning path with innovative",
                    'price': "Visit Edureka.co",
            },
]


@app.route('/')
def index():
    return "Welcome to Flask API"

@app.route('/courses', methods=['GET'])
def get():
    return jsonify({"Courses": courses})

@app.route('/courses/<int:course_id>', methods = ['GET'])
def get_course(course_id):
    return jsonify({"course": courses[course_id]})


@app.route('/courses', methods = ['POST'])
def create():
    course ={
            "name": "AI and ML",
            "course_id": "5",
            "Description": "Python programming certification helps you learn"
                           "Python in the structured learning path with innovative",
            'price': "Visit Edureka.co",
        },
    courses.append(course)
    return jsonify({'Created': course})


@app.route('/courses/<int:course_id>', methods = ['PUT'])
def course_update(course_id):
    courses[course_id]['Description'] = "XYZKJ HGHHHJH"
    return jsonify({'course': courses[course_id]})



@app.route("/courses/<int:course_id>",methods=['DELETE'])
def delete(course_id):
    courses.remove(courses[course_id])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=105)