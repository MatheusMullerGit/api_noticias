## 📚  Descrição 

API_REST_CRUD para cadastros, atualização, pesquisa e exclusão de notícias.

## 📌Endpoints:

### [POST] /add_noticia

Cadastra uma notícia do objeto JSON abaixo:
```
{
    "autor": "Isaac Asimov",
    "titulo": "Frase 5",
    "texto": "Nunca deixe seu senso moral impedir você de fazer o que é certo!"
}
```
### [GET]/get_all_noticias

Retorna todas as notícias cadastradas. 

### [GET]/get_noticias_autor/<autor>

Retorna as notícias do autor informado.

### [GET]/get_noticias_titulo/<titulo>

Retorna as notícias com título informado.

### [GET]/get_noticias_texto/<texto>

Retorna as notícias com o texto informado.

### [PUT]/put_noticia/

Atualiza os dados da notícia de acordo com o objeto abaixo.
```
{
    "autor": "Isaac Asimov",
    "titulo": "Frase 3"
    "texto": "Espera mil anos e verás que será precioso até o lixo deixado
atrás por uma civilização extinta.",
}
```

### [DELETE]/del_noticia/<titulo>

Apaga a notícia com o titulo informado.


## 🚀 Tecnologias Usadas 

<img src="https://user-images.githubusercontent.com/18649504/66262823-725cd600-e7be-11e9-9cea-ea14305079db.png" width = "100">

<img src="https://user-images.githubusercontent.com/64918635/93954857-ddcbea80-fd24-11ea-89a8-213950b038ca.png" width = "150">

<img src="https://user-images.githubusercontent.com/64918635/93954980-271c3a00-fd25-11ea-91bc-bb3659218fb1.png" width = "200">


## 📌 Estrutura do Projeto 
    |-- app.py
    |-- requirements.txt
    |-- example.env    
    
app.py -> Arquivo principal que contém os Endpoints do projeto.
<br>
requirements.txt -> Bibliotecas utilizadas no python 
<br>
example.env -> Arquivo de configuração do MongoDB
<br>

## 📢 Como executar

Requisitos:

Python 3.8.0<br>

Instalar todas as dependências do python usando o arquivo requirements.txt que está no projeto:  

```bash 
pip install  -r requirements.txt
 ```  
 Executar o app.py no cmd com o comando:

```bash 
python app.py
 ```  
Importar o arquivo collection.JSON utilizando um programa de requisições REST, como o <a href="https://insomnia.rest/download/">Insomnia</a> ou o <a href="https://www.postman.com/downloads/">Postman<a> e informar o IP: http://127.0.0.1:5000/+endpoint , preenchendo o body no formato JSON conforme abaixo:

```
{
    "autor": "Isaac Asimov",
    "titulo": "Frase 5",
    "texto": "Nunca deixe seu senso moral impedir você de fazer o que é certo!"
}
```

## 🔓 Licença 
MIT © [Matheus Muller](https://www.linkedin.com/in/matheus-herrera-bezerra-muller/)
