{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "EJERCICIO 1"
      ],
      "metadata": {
        "id": "j6XDsJycnTFa"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "WUWbvnp0nQT_"
      },
      "outputs": [],
      "source": [
        "# Programa 1: Contar palabras en un texto\n",
        "\n",
        "def contar_palabras(texto):\n",
        "    palabras = texto.split()\n",
        "    return len(palabras)\n",
        "\n",
        "# Ingreso del texto por el usuario\n",
        "texto_usuario = input(\"Ingrese un texto: \")\n",
        "\n",
        "# Contar las palabras\n",
        "cantidad_palabras = contar_palabras(texto_usuario)\n",
        "print(f\"El texto tiene {cantidad_palabras} palabras.\")\n",
        "\n",
        "# Programa 2: Slice de un string desde el elemento 1 al penúltimo\n",
        "\n",
        "# Ingreso del string por el usuario\n",
        "string_usuario = input(\"Ingrese un string: \")\n",
        "\n",
        "# Obtener el slice desde el elemento 1 al penúltimo\n",
        "slice_resultado = string_usuario[1:-1]\n",
        "print(f\"El slice del string desde el elemento 1 al penúltimo es: {slice_resultado}\")"
      ]
    }
  ]
}