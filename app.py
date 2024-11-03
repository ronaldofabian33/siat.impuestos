from flask import Flask, render_template, request, send_file
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    return fib_sequence[:n]

@app.route('/', methods=['GET', 'POST'])
def home():
    sequence = []
    if request.method == 'POST':
        n = int(request.form['number'])
        sequence = fibonacci(n)
        
        # Crear la gráfica
        plt.figure()
        plt.plot(sequence, marker='o')
        plt.title('Serie Fibonacci')
        plt.xlabel('Índice')
        plt.ylabel('Valor')
        plt.grid(True)
        
        # Guardar la gráfica como imagen
        graph_file = 'static/fibonacci_plot.png'
        plt.savefig(graph_file)
        plt.close()

        return render_template('index.html', sequence=sequence, graph_file=graph_file)

    return render_template('index.html', sequence=sequence)

if __name__ == '__main__':
    app.run(debug=True)
