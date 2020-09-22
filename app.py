from dotenv import load_dotenv
from flask import Flask, jsonify, request
import pymongo
from pymongo import MongoClient
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
load_dotenv()

app.config['MONGO_DBNAME'] = os.getenv('MONGO_DBNAME')
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

@app.route('/add_noticia', methods=['POST'])
def add_noticia():
    autores = mongo.db.autores
    noticias = mongo.db.noticias
    
    autor = request.json['autor']
    titulo = request.json['titulo']
    texto = request.json['texto']
    
    o_autor = autores.find_one({'autor': autor})
    
    noticias_id = noticias.insert({'titulo': titulo, 'texto': texto, 'autor_id': o_autor['_id']})
    nova_noticia = noticias.find_one({'_id': noticias_id})
    
    output = {'titulo': nova_noticia['titulo'], 'texto': nova_noticia['texto'], 'autor_id': str(nova_noticia['autor_id'])}
    
    return jsonify({'results': output})
    
@app.route('/get_all_noticias', methods=['GET'])
def get_all_noticias():
    autores = mongo.db.autores
    noticias = mongo.db.noticias
        
    output = []
    
    for a in autores.find():
        for n in noticias.find({'autor_id': a['_id']}):
            output.append({'titulo': n['titulo'], 'texto': n['texto'], 'autor': a['autor'], 'autor_id': str(a['_id'])})
        
    return jsonify({'result': output})

@app.route('/get_noticias_autor', methods=['GET'])
def get_noticias_autor():
    autores = mongo.db.autores
    
    autor = request.json['autor']
    
    o_autor = autores.find_one({'autor': autor})
    
    noticias = mongo.db.noticias
    
    output = []
    
    try:
        for n in noticias.find({'autor_id': o_autor['_id']}):
            output.append({'titulo': n['titulo'], 'texto': n['texto'], 'autor': o_autor['autor'], 'autor_id': str(o_autor['_id'])})
    except Exception as e:
        output = (f'Erro: {e} -- Autor não encontrado')
        
    return jsonify({'result': output})

@app.route('/get_noticias_titulo', methods=['GET'])
def get_noticias_titulo():
    autores = mongo.db.autores
    noticias = mongo.db.noticias
    titulo = request.json['titulo']
       
    output = []
    
    try:
        for n in noticias.find({'titulo': titulo}):
            o_autor = autores.find_one({'_id': n['autor_id']})
            output.append({'titulo': n['titulo'], 'texto': n['texto'], 'autor': str(o_autor['autor']), 'autor_id': str(o_autor['_id'])})
    except Exception as e:
        output = (f'Erro: {e} -- Notícia não encontrada')
        
    return jsonify({'result': output})    

@app.route('/get_noticias_texto', methods=['GET'])
def get_noticias_texto():
    autores = mongo.db.autores
    noticias = mongo.db.noticias
    texto = request.json['texto']
       
    output = []
    
    try:
        for n in noticias.find({'texto': texto}):
            o_autor = autores.find_one({'_id': n['autor_id']})
            output.append({'titulo': n['titulo'], 'texto': n['texto'], 'autor': str(o_autor['autor']), 'autor_id': str(o_autor['_id'])})
    except Exception as e:
        output = (f'Erro: {e} -- Notícia não encontrada')
        
    return jsonify({'result': output})

@app.route('/put_noticia', methods=['PUT'])
def update():
    autores = mongo.db.autores
    noticias = mongo.db.noticias
    
    autor = request.json['autor']
    titulo = request.json['titulo']
    texto = request.json['texto']
    
    o_autor = autores.find_one({'autor': autor})
    
    atualizacao = noticias.find_one({'titulo': titulo})
    atualizacao['autor_id'] = o_autor['_id']
    atualizacao['titulo'] = titulo
    atualizacao['texto'] = texto
    
    noticias.save(atualizacao)
    
    return 'Notícia atualizada'

@app.route('/del_noticia', methods=['DELETE'])
def delete():
    noticias = mongo.db.noticias
    
    titulo = request.json['titulo']
            
    deletar = noticias.find_one({'titulo': titulo})
        
    noticias.delete_one(deletar)
    
    return 'Notícia apagada'

if __name__ == '__main__':
    app.run(debug=True)