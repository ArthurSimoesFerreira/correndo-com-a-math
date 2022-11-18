import random 
def answer(num1, num2, equation, res):
    """
    Opções de resposta:(sempre terão 4 opções de resposta)
    Uma aleatória com valor abaixo da resposta, uma aleatória com valor acima da resposta,
    uma muito próxima da resposta, para confundir, e uma que, de fato, é a resposta.

    """
    if equation == 0:
        option1= random.randint(0,res)
        option2= random.randint(res,99)
        option3= res+1
        option4= res
    elif equation == 1: 
        option1= random.randint(0,res)
        option2= random.randint(res,99)
        option3= res+1
        option4= res
    elif equation == 2:
        option1= random.randint(0,res)
        option2= random.randint(res,99)
        option3= num1*(num2-1)
        option4= res
    elif equation == 3:
        option1= random.randint(0,res)
        option2= random.randint(res,99)
        option3= num1/(num2+1)
        option4= res


    # desenhar as opções de resposta de forma aleatória nos botões
    