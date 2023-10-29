import json
import os
from fastapi import FastAPI, HTTPException # importei o fastapi e o HTTP é pra dizer que pode ter erro se tiver algo maior qu e alista 
import random  # gera numeros pseu aleatorios 

app = FastAPI() # segue as normas do fastapi, isso tudo dentro de app 

BOOKS_FILE = "books.json"
BOOK_DATABASE = [
    " Harry Potter and the Chamber of Secrets",
    " The Godfather ",
    " The Green Mile",
    " The Graduate",
    " The Hangover",
    " Lord of the Rings"


]

if os.path.exists(BOOKS_FILE):  #PARA VER SE O CAMINHO EXISTE
    with open (BOOKS_FILE, "r") as f: # quero abrir o arquivo para leitura e to chamdno de f
        BOOK_DATABASE = json.load(f) # tudo que tem no arquivo f carregando em f e colocando no book database
    

# NOME DAS ROTAS QUE IREI USAR, LEMBRE-SE DE SER CONSISTENTE
#/ -> boas vindas 
@app.get("/")
async def home():
    return "Welcome to my bookstore"
#/list-books -> listar todos os livros
@app.get("/list-books")
async def lista_books():
    return { "books available" : BOOK_DATABASE}  # esse colchete é uma lista 
#/list-book-by-index {index} ( esse entre chaves é um parametro) -> listar um livro
@app.get("/list-book-by-index {index}")
async def book_by_index(index: int):
    if index< 0 or index >= len(BOOK_DATABASE):
        raise HTTPException(404, "Index out of range") # 
    else:
        return { "Books": BOOK_DATABASE[index]}

#/get - random - book -> livro aleatorio 
@app.get("/get-random-book ")
async def get_random_book ():
    return random.choice.BOOK_DATABASE  # selecione um elemento aleatorio (o choice) 
#/add-book -> adicionar um novo livro 
@app.post("/add-book ")
async def add_book(book:str):
    BOOK_DATABASE.append(book) # append adiciona no final da lista
    with open(BOOKS_FILE, "w") as f: # quero abrir o arquivo para escrever a lista de livros e to chamdno de f
        json.dump(BOOK_DATABASE,f) # dump é pegar tudo da database e colocar em f
    return {"message" : f'Book {book} was added'} # quandp coloca esse f e aspas simples vc consegue adicionar o nome da variavel na msg
