from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        print(request.form)
        self.scores.append(score)

    def calculate_avg(self):
        if not self.scores:
            return None
        return sum(self.scores) / len(self.scores)

    def judge(self):
        avg = self.calculate_avg()
        if avg is None:
            return "No scores entered"
        if avg >= 60:
            return "合格"
        else:
            return "不合格"

students = []

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/add_score', methods=['POST'])
def add_score():
    name = request.form['name']
    subject1 = int(request.form['subject1'])
    subject2 = int(request.form['subject2'])
    subject3 = int(request.form['subject3'])
    subject4 = int(request.form['subject4'])
    subject5 = int(request.form['subject5'])
    
    student = None
    for s in students:
        if s.name == name:
            student = s
            break

    if student is None:
        student = Student(name)
        students.append(student)
    
    student.add_score(subject1)
    student.add_score(subject2)
    student.add_score(subject3)
    student.add_score(subject4)
    student.add_score(subject5)

    return redirect(url_for('result'))

@app.route('/result')
def result():
    results = []
    for student in students:
        avg = student.calculate_avg()
        result = student.judge()
        results.append({'name': student.name, 'avg': avg, 'result': result})

        print(results)
    
    return render_template('result.html', students=results)


if __name__ == '__main__':
    app.run(port=5000, debug=True)

