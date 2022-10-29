import matplotlib.pyplot as pyplot

def generate_pie_chart():
    labels = ['A','B','C']
    values = [200,34,120]

    # obtener la figura y coordenadas desde subplots
    fig, ax = pyplot.subplots()
    # generar pie chart con los valores y labels
    ax.pie(values, labels=labels)
    # generar y guardar una imagen
    pyplot.savefig('pie.png')
    # cerrar el proceso
    pyplot.close()
