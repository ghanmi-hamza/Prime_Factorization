from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)

"""def factors(n):
    li = []
    while n > 1:
        for i in range(2, int(n + 1)):
            if n % i == 0:
                n /= i
                li.append(i)
                #yield i
    return(li)"""
def factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors



@app.route('/',methods = ['POST','GET'])
def home():
    if request.method == 'POST':
        name = request.form['author']
        content = request.form['content']
        n = int(content)
        result = factors(n)
        return render_template('post.html',name=name,result=result,n=n)
    return render_template('home.html')




if __name__=='__main__':
    app.run(debug=True)