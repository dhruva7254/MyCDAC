
class Course:
    Agency_creating_course = 'IACSD'

    def __init__(self,course_id,course_name,duration,tot_hrs_syl,contents,staff_count):
        self.course_id = course_id
        self.course_name = course_name
        self.duration = duration
        self.tot_hrs_syl = tot_hrs_syl
        self.contents = contents
        self.staff_count = staff_count

    def display_info(self):
        print(self.course_id, self.course_name)

    @classmethod
    def display_agency(cls):
        print(cls.Agency_creating_course)

c1 = Course(102,'DAC',6,250,'CDAC',3)
c1.display_info()
c1.display_agency()

print(Course.__dict__)
