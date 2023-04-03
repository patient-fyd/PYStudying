# 需求拆分:
"""
1.展示学生管理系统的功能有哪些,引导用户键入序号选择功能
2.获取用户键入的功能
3.分析具体要执行哪一项功能
4.执行功能
"""


def show_menu():
    """用户功能界面展示"""
    print('*' * 50)
    print('欢迎使用学生管理系统')
    print('1.添加学生')
    print('2.删除学生')
    print('3.修改学生')
    print('4.查询学生')
    print('5.显示所有学生')
    print('6.退出系统')
    print('*' * 50)


def get_num():
    """引导用户输入功能序号，并获取序号"""
    num = input('请输入你用执行的功能序号:')
    return num


def add_student():
    pass


def del_student():
    pass


def modify_student():
    pass


def search_student():
    pass


def show_all_student():
    pass


def exit_system():
    pass


#
def analysis_num(num):
    """分析用户输入的序号"""
    if num == '1':
        add_student()
    elif num == '2':
        del_student()
    elif num == '3':
        modify_student()
    elif num == '4':
        search_student()
    elif num == '5':
        show_all_student()
    elif num == '6':
        exit_system()
    else:
        print('输入错误，请重新输入')


while True:
    show_menu()
    num = get_num()
    analysis_num(num)
    input('按任意键继续...')
