import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    #calculo duración 

    tiempo_explicacion = 25
    tiempo_practica = 15
    tiempo_pausa = 10
    duracion_total = tiempo_explicacion + tiempo_practica + tiempo_pausa

    print(str(duracion_total), "min")

    return


if __name__ == "__main__":
    app.run()
