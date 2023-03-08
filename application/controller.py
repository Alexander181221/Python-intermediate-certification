import model
import user_interface
import datetime
import color_text


def klick_menu():
    while True:
        number = user_interface.menu()
        if number == 4:
            g = model.add_task()
            return user_interface.output(g)
        elif number == 1:
            return user_interface.output(model.view_tasks_tabulate())
        elif number == 2:
            number_id = input(
                "\t\t\tВведите номер заметки, которую необходимо найти в записной книжке: ")
            answer = model.find_task_id(number_id)
            return user_interface.output(answer)
        elif number == 3:
            find_day = input("\t\t\tВведите число месяца: ")
            find_month = input("\t\t\tВведите месяц: ")
            find_year = input("\t\t\tВведите год: ")
            result = model.find_task_date(find_day, find_month, find_year)
            dtn = str(datetime.datetime.now())
            with open(f'{find_day}_{find_month}_{find_year}_.txt', 'a', encoding='utf-8') as data:
                data.write("\n" + " список заметок на указанную дату отображен " + f'{dtn}' + "\n-----------"
                                                                                              "-----------------------"
                                                                                              "------------------------"
                                                                                              "------------------\n")
            return user_interface.output(result)
        elif number == 5:
            number_id = input(
                "\t\t\tВведите номер заметки, которую необходимо удалить: ")
            return user_interface.output(model.delete_task(number_id))
        elif number == 6:
            number_id = input(
                "\t\t\tВведите номер заметки, которую необходимо отредактировать: ")
            return user_interface.output(model.edit_task(number_id))
        elif number == 7:
            return 0


def run():
    while klick_menu() != 0:
        klick_menu()
    return user_interface.output("Cпасибо за работу c записной книжкой!!!")
