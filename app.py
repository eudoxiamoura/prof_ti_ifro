from flask import Flask, render_template, jsonify

app = Flask(__name__)

PROFESSOR = [{
  'id': 1,
  'nome': 'Lucinano Topolnix',
  'habilidade': 'Controle absoluto sobre o gelo e metais raros. Consegue congelar até frequências de rádio.',
  'salario': 'R$ 15.000'
}, {
  'id': 2,
  'nome': 'Euxodia Vottie',
  'habilidade': 'Telepatia, manipulação de conhecimento, criação de campos de concentração cognitiva — faz qualquer um entender SQL à força.',
  'salario': 'R$ 30.000'
}, {
  'id': 3,
  'nome': 'Andreyron',
  'habilidade': 'Um ciborgue com consciência humana, mistura de Tony Stark com Visão. Tem um núcleo de energia que dá poderes de controle magnético.',
  'salario': 'R$ 40.000'
}, {
  'id': 4,
  'nome': 'Marcos Thanos',
  'habilidade': 'Herdeiro distante de Thanos, mas decidiu trilhar o caminho oposto: usa a Joia do Conhecimento (inédita!) para restaurar ordem e sabedoria.',
  'salario': 'R$ 50.000'
}, {
  'id': 5,
  'nome': 'Vagner Chewbacca',
  'habilidade': 'Consegue manipular todo tipo de rede — física, lógica ou neural. Derruba firewalls com um gesto e encripta mentes com um piscar de olhos.',
  'salario': 'R$ 133.400'
}]


@app.route("/")
def hello():
  return render_template("home.html", professor=PROFESSOR)


@app.route("/professor")
def lista_prof():
  return jsonify(PROFESSOR)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
