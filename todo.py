#간단한 To-Do List 프로그램
todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"'{task}'이(가) 추가되었습니다!")

def show_tasks():
    if not todo_list:
        print("할 일이 없습니다.")
    else:
        print("할 일 목록:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def delete_task(number):
    if 0 < number <= len(todo_list):
        removed = todo_list.pop(number - 1)
        print(f"'{removed}'이(가) 삭제되었습니다!")
    else:
        print("잘못된 번호입니다.")

# 테스트해보기
add_task("파이썬 공부하기")
add_task("깃허브에 올리기")
show_tasks()
delete_task(1)
$show_tasks()$