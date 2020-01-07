# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 09:06:06 2018

@author: Pshypher
"""

import datetime

class Schedule(object):
    
    def __init__(self,schedule_name: str,semester: str,year:int,courses: list=[]):
        """Initialises an instance of the Schedule class."""
        self.__schedule_name = schedule_name
        self.__courses = courses    # list of Courses
        self.__semester = semester
        self.__year = year
        
    def get_name_schedule(self):
        """Returns the schedule name."""
        return self.__schedule_name
    
    def get_semester(self):
        """Returns the semester Schedule is designed for."""
        return self.__semester
    
    def get_year(self):
        """Returns the year of the semester Schedule is designed for."""
        return self.__year
    
    def get_courses(self):
        """Returns the courses in a semester for the Schedule."""
        return self.__courses
    
    def __str__(self):
        """String representation of the Schedule class."""
        schedule_str = "Schedule: " + self.__schedule_name + "\nSemester: " \
        + self.__semester + "\nYear: " + self.__year + "\nCourses: "
        for course in self.__courses:
            schedule_str += course.get_title() + " "
            
class CourseSchedule(object):
    
    def __init__(self,weekday: int,time: datetime.time,duration_secs: int):
        """Initialises an instance of the CourseSchedule class."""
        self.__weeks = ["Monday","Tuesday","Wednesday","Thursday","Friday",
                        "Saturday","Sunday"]
        self.__weekday = self.__weeks[weekday]
        self.__time = time
        self.__duration_secs = duration_secs
        
    def get_weekday(self):
        "Return the weekday of the course."
        return self.__weekday
    
    def set_weekday(self,weekday):
        """Adjust the weekday of CourseSchedule."""
        self.__weekday = self.__weeks[weekday]
        
    def get_time(self):
        """Returns the time a Course is scheduled to hold."""
        return self.__time
    
    def set_time(self, time: datetime.time):
        """Adjust the time a Course is scheduled to hold."""
        self.__time = time
        
    def get_duration(self):
        """Return the duration in seconds of Course."""
        return self.__duration_secs
    
    def change_time_duration(self, duration_secs):
        """Change the time duration."""
        self.__duration_secs = duration_secs
            
class Course(object):
        
    def __init__(self,title: str,code: str, course_schedules: set=set()):
        """Initialises an instance of the Course class."""
        self.__title = title
        self.__course_code = code
        self.__course_schedules = course_schedules
        
    def get_title(self):
        """Returns the Course title."""
        return self.__title
    
    def get_course_code(self):
        """Returns the tcourse code."""
        return self.__course_code
    
    def change_course_title(self, title: str):
        """Alter the title of a Course."""
        self.__title = title
    
    def set_duration(self, code: str):
        """Change the Course code."""
        self.__course_code = code
        
    def add_schedule(self,weekday: int,time: datetime.time,duration_secs: int):
        """Add a schedule to an instance of the Course object."""
        course_schedule = CourseSchedule(weekday,time,duration_secs)
        self.__course_schedules.add(course_schedule)
        
    def remove_schedule(self,course_schedule: CourseSchedule):
        """Remove the scheduled time for a Course."""
        self.__course_schedules.remove(course_schedule)
        
    def __str__(self):
        """String representation of an instance of the Course class."""
        return "Course title " + self.__title + " course code " +  \
    self.__course_code