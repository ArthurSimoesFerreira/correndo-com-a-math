import random 
def answer(num1, num2, equation, res):
    """
    Opções de resposta:(sempre terão 4 opções de resposta)
    Uma aleatória com valor abaixo da resposta, uma aleatória com valor acima da resposta,
    uma muito próxima da resposta, para confundir, e uma que, de fato, é a resposta.

    """

    if equation == 0:
        option1= random.randint(0,(res - 1))
        option2= random.randint((res+1),(res + 50))
        option3= res + random.randint(1, 5)
        option4= res
    elif equation == 1: 
        option1= random.randint((res - 50),(res- 1))
        option2= random.randint((res + 1),res + 50)
        option3= res + random.randint(1, 5)
        option4= res
    elif equation == 2:
        option1= random.randint(-2,round(res) - 1)
        option2= random.randint((round(res)+1),(round(res) + 50))
        option3= num1*(num2-1)
        option4= res
    elif equation == 3:
        option1= random.randint(-2 ,res - 1)
        option2= random.randint((res+1),(res + 50))
        option3= round(num1/(num2+1))
        option4= res

    equations_options = [option1, option2, option3, option4]

    return equations_options

    # desenhar as opções de resposta de forma aleatória nos botões
    # comparar as respostas para ver qual ta certa
    