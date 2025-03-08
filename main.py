# Импорт библиотек
import requests
import json

req = requests.get('https://portal.unn.ru/ruzapi/schedule/group/44940?start=2025.03.03&finish=2025.04.09&lng=1')
allInfo = json.loads(req.text) # allInfo - массив со всеми данными расписания

# Цикл перебора расписания:

for oL in allInfo: # oL (one lesson) - массив с одной парой
    print(f"{oL['dayOfWeekString']}\n{oL['date']}\n{oL['lessonNumberStart']} пара ({oL['beginLesson']} - {oL['endLesson']})\n{oL['auditorium']} ({oL['building']})\n{oL['discipline']} ({oL['kindOfWork']})\nПреподаватель: {oL['lecturer']} ({oL['lecturer_rank']})\nГруппа(ы): {oL['stream']}")
