# test.py
from main import StudentsInMLOps

def test_enrollStudents():
    classroom = StudentsInMLOps()
    classroom.enrollStudents(5)
    assert classroom.getTotalStrength() == 5

def test_dropStudents():
    classroom = StudentsInMLOps()
    classroom.enrollStudents(5)
    classroom.dropStudents(2)
    assert classroom.getTotalStrength() == 3

def test_getTotalStrength():
    classroom = StudentsInMLOps()
    classroom.enrollStudents(3)
    assert classroom.getTotalStrength() == 3

def test_getClassName():
    classroom = StudentsInMLOps()
    assert classroom.getClassName() == "MLOps Essentials"
