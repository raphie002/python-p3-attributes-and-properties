#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name=None, job=None):

        name_error_message = "Name must be string between 1 and 25 characters."

        is_name_valid = False
        if isinstance(name, str) and (1 <= len(name) <= 25):
            is_name_valid = True
            self.name = name.title() 
        elif name is not None:
            print(name_error_message)
            self.name = None 
        else:
            self.name = None 
            
        job_error_message = "Job must be in list of approved jobs."

        if job and job not in APPROVED_JOBS:
            print(job_error_message)
            self.job = None
        elif job:
            self.job = job
        else:
            self.job = None