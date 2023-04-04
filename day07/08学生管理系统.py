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
    """删除学生"""
    # 1.获取用户输入的学生id
    stu_id = input('请输入要删除的学生ID:')
    # 2.判断学生id是否存在
    if stu_id in [stu['id'] for stu in students_list]:
        # 3.如果存在，删除学生信息
        for stu in students_list:
            if stu['id'] == stu_id:
                students_list.remove(stu)
                break
        print('删除成功！')
    else:
        print('该学生ID不存在！')


def modify_student():
    """修改学生"""
    # 1.获取用户输入的学生id
    stu_id = input('请输入要修改的学生ID:')
    # 2.判断学生id是否存在
    if stu_id in [stu['id'] for stu in students_list]:
        # 3.如果存在，修改学生信息
        for stu in students_list:
            if stu['id'] == stu_id:
                # 3.1 获取用户输入的学生信息
                name = input('请输入学生姓名:')
                age = input('请输入学生年龄（数字）:')
                mobile = input('请输入学生手机号:')
                # 3.2 修改学生信息
                stu['name'] = name
                stu['age'] = age
                stu['mobile'] = mobile
                break
        print('修改成功！')
    else:
        print('该学生ID不存在！')


def search_student():
    """查询学生"""
    # 1.获取用户输入的学生id
    stu_id = input('请输入要查询的学生ID:')
    # 2.判断学生id是否存在
    if stu_id in [stu['id'] for stu in students_list]:
        # 3.如果存在，查询学生信息
        for stu in students_list:
            if stu['id'] == stu_id:
                print('学生ID\t学生姓名\t学生年龄\t学生手机号')
                print('%s\t%s\t%s\t%s' % (stu['id'], stu['name'], stu['age'], stu['mobile']))
                break
    else:
        print('该学生ID不存在！')


def show_all_student():
    """显示所有学生"""
    # 1.判断学生列表是否为空
    if len(students_list) == 0:
        print('没有学生信息，请先添加学生信息！')
    else:
        # 2.如果不为空，显示所有学生信息
        print('学生ID\t学生姓名\t学生年龄\t学生手机号')
        for stu in students_list:
            print('%s\t%s\t%s\t%s' % (stu['id'], stu['name'], stu['age'], stu['mobile']))
        print('共有%d名学生' % len(students_list))


def exit_system():
    """退出系统"""
    print('退出系统成功！')
    exit()


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
