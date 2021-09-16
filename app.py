from flask import Flask, render_template, request, redirect, url_for

# 调试用的数据，实际应该来自数据库
students = [
    {'name': 'zhansan', 'chinese': '65', 'math': '44', 'english': '76'},
    {'name': 'lisi', 'chinese': '35', 'math': '54', 'english': '66'},
    {'name': 'wangwu', 'chinese': '55', 'math': '64', 'english': '78'},
    {'name': 'zhaoliu', 'chinese': '75', 'math': '77', 'english': '86'}
]

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=['POST', 'GET'])
def login():
    # request 对象用于获得页面数据
    if request.method == 'POST':
        username = request.form.get('username')
        pws = request.form.get('password')
        print(username, pws)
        # 链接数据库校验密码

        # 成功后重定向 ，这里指的是路由函数/admin，不是admin.html，文件是通过路由调用的。
        return redirect('/admin')

    return render_template('login.html')


@app.route('/admin')
def admin():
    return render_template('admin.html', students=students)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        username = request.form.get('username')
        chinese = request.form.get('chinese')
        math = request.form.get('math')
        english = request.form.get('english')
        print(username,chinese,math,english)
        students.append({'name': username, 'chinese': chinese, 'math': math, 'english': english})
        return redirect('/admin')
    return render_template('add.html')

@app.route('/delete')
def del_student():
    # 后台需要拿到学员id或名字
    username=request.args.get('name')
    print(username)
    #找的并删除
    for stu in students:
        if stu['name']==username:
            #删除用pop remove
            students.remove(stu)

    return redirect('/admin')

@app.route('/change',methods=['GET','POST'])
def change_student():
    # 先显示再修改提交
    username=request.args.get('name')

    # post是修改后写，get是读取对应的数据
    if request.method=='POST':
        username=request.form.get('username')
        chinese = request.form.get('chinese')
        math = request.form.get('math')
        english = request.form.get('english')
        #找到对应的学生，赋值
        for stu in students:
            if stu['name'] == username:
                stu['chinese'] = chinese
                stu['math']=math
                stu['english']=english
        # 修改完后返回列表
        return redirect('/admin')
    #get显示读取数据
    for stu in students:
        if stu['name']==username:
            #修改,需要在change.html中显示学生信息
            return render_template('change.html',student=stu)

if __name__ == '__main__':
    app.run(debug=True)
