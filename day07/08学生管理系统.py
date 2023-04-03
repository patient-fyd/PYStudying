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
    """添加学生"""
    # 1.获取用户输入的学生信息
    # 1.1 当用户输入的id值已经存在时，提示用户重新输入
    stu_id = input('请输入学生ID:')
    while True:
        if stu_id in [stu['id'] for stu in students_list]:
            stu_id = input('该学生ID已经存在，请重新输入:')
        else:
            break
    name = input('请输入学生姓名:')

    # 1.2 当用户输入的年龄不是数字时，提示用户重新输入
    age = input('请输入学生年龄（数字）:')
    while True:
        if age.isdigit():
            break
        else:
            age = input('输入的年龄不是数字，请重新输入:')

    # 1.3 当用户输入的手机号不是数字时或者输入的手机号已存在时，提示用户重新输入
    mobile = input('请输入学生手机号:')
    while True:
        # 判断手机号是否是数字
        if mobile.isdigit():
            # 判断手机号是否为11位
            while True:
                if len(mobile) != 11:
                    mobile = input('输入的手机号不是11位，请重新输入:')
                else:
                    break
            # 判断手机号是否已经存在
            if mobile in [stu['mobile'] for stu in students_list]:
                mobile = input('该手机号已经存在，请重新输入:')
            else:
                break
        else:
            mobile = input('输入的手机号不是数字，请重新输入:')

    # 2.将学生信息保存到students_list中
    # 2.1 创建一个字典，用来保存学生信息
    stu_dict = {'id': stu_id, 'name': name, 'age': int(age), 'mobile': mobile}
    # 2.2 将学生信息添加到列表中
    students_list.append(stu_dict)
    print('添加成功！')


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


students_list = [{'id': '001', 'name': 'hanging', 'age': 18, 'mobile': '12345678901'}]
while True:
    show_menu()
    num = get_num()
    analysis_num(num)
    input('按任意键继续...')
