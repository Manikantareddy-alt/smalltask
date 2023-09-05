from flask import Flask, render_template

app = Flask(__name__)

# Configure Flask to serve static files (images) from the 'static' folder
app.static_url_path = '/static'

# Define a route to display the "task.html" template
@app.route('/task')
def task_view():
    # Render the "task.html" template
    return render_template('task.html')

if __name__ == '__main__':
    app.run(debug=True)
