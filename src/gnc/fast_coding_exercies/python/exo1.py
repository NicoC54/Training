#test writing a class

#version python

class Student:


    def __init__(self,age,name,mark):
        self.age = age
        self.name = name
        self.mark = mark



student = Student(18,"Nico",15)
print(f"{student.age} {student.name} {student.mark}")

# version c++

class Student {

    public:

        Student(int number, double note, std::string nom) : name(nom), age(number), mark(note){};

    private:

        std::string name = "";
        int age = 0;
        double mark = 0;
};

Student student(20,18.7,"Nico");