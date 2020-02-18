.PHONY: default
default:
	@make help

help:
	@echo type make run to run the game

run:
	pipenv run python game/game.py

test:
	pipenv run python game/modules/tests/tests.py
