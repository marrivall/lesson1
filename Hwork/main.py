from student import Student
from group import Group
from group_limit import GroupLimitException

def main():
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    gr = Group('PD1')

    try:
        gr.add_student(st1)
        gr.add_student(st2)
    except GroupLimitException as error:
        print (error)

    print(gr)
    assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
    assert gr.find_student('Jobs2') is None, 'Test2'
    assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
    gr.delete_student('Taylor')
    print(gr)
    gr.delete_student('Taylor')  # No error!
    print("Ok")

if __name__ == "__main__":
    main()




