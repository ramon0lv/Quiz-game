import pandas as pd

# Perguntas e respostas
questions = [
    ["Qual é o maior mamífero terrestre?", "Elefante", "Rinoceronte", "Leão", "Girafa", 1],
    ["Quantas patas tem uma aranha?", "6", "8", "10", "12", 2],
    ["O que os morcegos usam para se orientar no escuro?", "Antenas", "Olfato aguçado", "Ecolocalização", "Visão noturna", 3],
    ["Qual é o maior felino do mundo?", "Leão", "Tigre", "Leopardo", "Onça-pintada", 2],
    ["Quais animais formam uma colônia chamada 'colônia de formigas'?", "Leões", "Golfinhos", "Formigas", "Abelhas", 3],
    ["Qual é o maior réptil do mundo?", "Iguana", "Cobra", "Crocodilo", "Tartaruga", 3],
    ["Qual é o animal mais veloz do mundo?", "Leopardo", "Peregrino", "Guepardo", "Águia", 3],
    ["Quais animais são conhecidos por sua capacidade de camuflagem?", "Camaleões", "Zebra", "Pandas", "Girafas", 1],
    ["Qual é o único mamífero capaz de voar?", "Morcego", "Pássaro", "Borboleta", "Esquilo", 1],
    ["Qual é o maior peixe do mundo?", "Tubarão-branco", "Baleia-azul", "Arraia", "Peixe-lua", 2],
    ["Quais animais são marsupiais e originários da Austrália?", "Kangurus", "Elefantes", "Leões", "Gorilas", 1],
    ["Qual é o nome do processo de transformação de uma lagarta em borboleta?", "Metamorfose", "Evolução", "Mutação", "Adaptação", 1],
    ["Qual é o animal símbolo da China?", "Panda", "Dragão", "Tigre", "Macaco", 1],
    ["Qual é o maior primata do mundo?", "Orangotango", "Gorila", "Chimpanzé", "Bonobo", 2],
    ["Quais animais são conhecidos por migrar grandes distâncias?", "Golfinhos", "Borboletas", "Pássaros", "Renas", 3],
    ["Qual é o mamífero marinho mais pesado?", "Baleia-azul", "Orca", "Tubarão", "Golfinho", 1],
    ["Quais animais são conhecidos por viver em tocas subterrâneas?", "Cobras", "Esquilos", "Toupeiras", "Coelhos", 3],
    ["Qual é o único mamífero que pode voar para trás?", "Morcego", "Pássaro", "Borboleta", "Beija-flor", 4],
    ["Quais animais são considerados animais de estimação comuns?", "Leões", "Cães", "Elefantes", "Girafas", 2],
    ["Qual é o animal mais velho do mundo?", "Tartaruga", "Elefante", "Baleia", "Tubarão", 1],
]

# DataFrame do pandas
df = pd.DataFrame(questions, columns=['Perguntas', 'Opcao 1', 'Opcao 2', 'Opcao 3', 'Opcao 4', 'Resposta'])
# Salvar no arquivo Excel
df.to_excel('questions.xlsx', index=False)

print('Perguntas inseridas com sucesso!')
