{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "file1.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOOPHs+0UyR0QzSCvQccuKB",
      "include_colab_link": true
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
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/DashaBelskaya/project_01/blob/main/file1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 36,
      "metadata": {
        "id": "PZ8Oy4KJVV78"
      },
      "outputs": [],
      "source": [
        "# Задача 1\n",
        "# Создайте список \"города\" с именами любых городов\n",
        "# Количество элементов в списке \"города\" не меньше 3!\n",
        "\n",
        "# Создайте список списков населения перечисленных городов\n",
        "\n",
        "# Выведите на консоль население второго города в списке в формате\n",
        "# Население Москвы - ХХ человек\n",
        "\n",
        "# Выведите на консоль общий размер населения перечисленных городов как сумму населения всех городов\n",
        "# Итого размер населения - ХХ человек\n",
        "\n",
        "города = [\"Питер\", \"Барнаул\", \"Рим\"]"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "население = [[\"население Питера - 7 млн человек\"], [\"население Барнаула - 0.6 млн человек\"], [\"население Рима - 2.9 млн человек\"]]\n",
        "\n",
        "население[1]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "l3D58jRwVvmb",
        "outputId": "187cc366-dddf-449c-91aa-4010a0be03d7"
      },
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['население Барнаула - 0,6 млн человек']"
            ]
          },
          "metadata": {},
          "execution_count": 37
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "сумма_населения = [7, 0.6, 2.9]\n",
        "\n",
        "x = sum([7, 0.6, 2.9])\n",
        "x"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OCjQ0wmUiRu5",
        "outputId": "d00db6a4-0616-426a-edde-07d96f86b737"
      },
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "10.5"
            ]
          },
          "metadata": {},
          "execution_count": 42
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x = \"Итого размер населения - 10.5 человек\"\n",
        "x"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "9-shF52pnd-m",
        "outputId": "127a5c3c-5a32-4ab0-e2c6-5c4c1b53ba6b"
      },
      "execution_count": 44,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Итого размер населения - 10.5 человек'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 44
        }
      ]
    }
  ]
}