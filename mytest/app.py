from flask import Flask, render_template
import games
from time import sleep
#from games import sort_function
app = Flask(__name__)
gameObjs= []
i=0
@app.route("/")
def hello():
	games.main()
	names = [game for game in games.Game.games]
	global gameObjs
	gameObjs = games.Game.games.values()
	return render_template("something.html", name='Oren', l=names)

@app.route("/something_else")
def something_else():
	global gameObjs
	global i
	game = gameObjs[i]
	i+=1
	return render_template("something_else.html", game=game, players=game.players, length=len(game.players),num=i)
@app.route("/farewell")
def farewell():
	global i
	i=0
	return render_template("farewell.html")

if __name__ == "__main__":
    app.run(debug=True)