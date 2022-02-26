from tkinter.messagebox import NO
from contributor import Contributor
from project import Project


def con_builder(c_list, line):
    c_list.append(Contributor(line[0]))
    return int(line[1])  
    
def pro_builder(p_list, line):
    p_list.append(Project(line[0], int(line[1]), int(line[2]), int(line[3])))
    return int(line[4])
    
files = ['a_an_example.in.txt', 'b_better_start_small.in.txt', 'c_collaboration.in.txt',
         'd_dense_schedule.in.txt', 'e_exceptional_skills.in.txt']
def main():
    with open(files[1]) as f:
        lines = f.readlines()
        data_num = lines[0].rstrip()
        num_of_ppl = int(data_num.split(" ")[0])
        num_of_proj = int(data_num.split(" ")[1])
        con_left = True

        contributor_list = []
        project_list = []

        building = False
        skills_count = 0
        
        for i in range(len(lines)):
            if i == 0:
                continue

            line = lines[i].rstrip().split(" ")
            
            if not building:
                building = True
                skills_count = con_builder(contributor_list, line) if len(contributor_list) < num_of_ppl else pro_builder(project_list, line) 
                
            else:
                if con_left:
                    contributor_list[-1].skills[line[0]] = line[1]
                else:
                    project_list[-1].skills[line[0]] = line[1]
                skills_count -= 1
                if skills_count == 0:
                    building = False
                    if len(contributor_list) == num_of_ppl:
                        con_left = False
                     


if __name__ == '__main__':
    main()