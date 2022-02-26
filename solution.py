from tkinter.messagebox import NO
from contributor import Contributor


def create_con():
    ...
    

def main():
    with open('a_an_example.in.txt') as f:
        lines = f.readlines()
        data_num = lines[0].rstrip()
        num_of_ppl = int(data_num.split(" ")[0])
        num_of_proj = int(data_num.split(" ")[1])

        contributor_list = []
        project_list = []

        building_con = False
        skills_count = 0
        
        for i in range(len(lines)):
            if i == 0:
                continue

            line = lines[i].rstrip().split(" ")
            
            if len(contributor_list) < num_of_ppl:
            
                if not building_con:                
                    building_con = True
                    contributor_list.append(Contributor(line[0]))
                    skills_count = int(line[1])
                
                elif building_con and skills_count != 0:
                    contributor_list[-1].skills[line[0]] = line[1]
                    skills_count -= 1
                    if skills_count == 0:
                        building_con = False
                        
            else:
                print(line)
            
    print()






            



if __name__ == '__main__':
    main()