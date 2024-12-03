def main():

     hike_for_jb_3 = 15.0
     hike_for_jb_4 = 7.0
     hike_for_jb_5 = 5.0

    
     job_level = int(input("Plese enter the job level? : "))
     old_salary = float(input(f"Please enter old salary of employee with job level {job_level} : "))
     new_sal = 0.0
     sal_hike = 0.0

     if job_level == 3:
          hike_percentage = 0.15
          sal_hike = float(old_salary) * hike_percentage
     elif job_level == 4:
          hike_percentage = 0.07
          sal_hike = float(old_salary) * hike_percentage
     elif job_level == 5:
          hike_percentage = 0.05
          sal_hike = float(old_salary) * hike_percentage

    

     new_sal = old_salary + sal_hike
          
     print(f'New salary of job level {job_level} would be : {new_sal:.2f}')







main()