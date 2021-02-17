"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
def average_score(students_list, flag):
	
	if flag == "school":															#подсчет по школе
		average_classes = 0															#среднее по классам
		for student in students_list:
			sum_raiting = 0															#сумма оценок ученика
			for one_rating in student["scores"]:
				sum_raiting += one_rating
			average_classes += sum_raiting/len(student["scores"])					#суммируем средние оценки учеников
		return average_classes/len(students_list)
	else:																			#подсчет по классам
		average_classes = 0 														#среднее по классам
		class_count = 0																#количество учеников одного класса
		for student in students_list: 
			if str(flag) in student["school_class"]:								#проверяем по выбраным классам
				class_count += 1													#подсчет количества классов
				sum_raiting = 0
				for one_rating in student["scores"]:
					sum_raiting += one_rating
				average_classes += sum_raiting/len(student["scores"])
		return average_classes/class_count

def main():
	"""
	Эта функция вызывается автоматически при запуске скрипта в консоли
	В ней надо заменить pass на ваш код
	"""
	students_list = [
		{'school_class': '4a', 'scores': [5,5,5,5,5]}, 		
		{'school_class': '4б', 'scores': [5,5,5,5,5]},
		{'school_class': '4в', 'scores': [5,5,5,5,5]},
		{'school_class': '4в', 'scores': [1,1,1,1,1]},
		  ]
	class_list = []
	for new_class in students_list:
		if not (new_class["school_class"] in class_list):
			class_list.append(new_class["school_class"])							#создаю список классов, которые существуют в школе
	print("Средний балл по школе: {:.2f}\n".format(
		average_score(students_list, "school")))
	for class_number in class_list:													#вывод по классам
		print("Средний балл по {} классу: {:.2f}\n".format(
			class_number, average_score(students_list, class_number)))
	
if __name__ == "__main__":
	main()
