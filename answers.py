dialog={"привет": "И тебе привет!", "как дела": "Лучше всех", "Пока": "Увидимся"}
def  get_answer(phrase, dialog):
	answer=dialog[phrase]
	return answer

print(get_answer("привет".lower(), dialog))