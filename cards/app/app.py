from flask import Flask
app = Flask(__name__)

@detail_card_router.route('/')
def hello():
	return "Hello World!!!!!!!!!!!!!!!!!!!!!"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)

