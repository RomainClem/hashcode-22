from tkinter.messagebox import NO

from numpy import True_
from contributor import Contributor
from project import Project


def con_builder(c_list, line):
    c_list.append(Contributor(len(c_list), line[0]))
    return int(line[1])  
    
def pro_builder(p_list, line):
    p_list.append(Project(line[0], int(line[1]), int(line[2]), int(line[3])))
    return int(line[4])

def skill_builder(skill, index, skill_level, skills_dict):
    if skill in skills_dict:
        if skill_level in skills_dict[skill]:
            skills_dict[skill][skill_level].append(index)
        else:
            skills_dict[skill][skill_level] = [index]
    else:
        skills_dict[skill] = {}
        skills_dict[skill][skill_level] = [index]
        
def add_con(skills_dict, skill, s_l, contributor_list, day, project_build, project_team_skills, project, added_con):
    for c_i in skills_dict[skill][s_l]:
        if contributor_list[c_i].last_project_end <= day:
            project_build.append(contributor_list[c_i].name)
            added_con.append(contributor_list[c_i])
            contributor_list[c_i].last_project_end = day + project.duration
            project_team_skills.update(contributor_list[c_i].skills)
            return True, c_i
    return False, c_i

def add_con_mentored_lvl_0(skill, contributor_list, day, project_build, project_team_skills, project, added_con):
    for c_i in contributor_list:
        if c_i.last_project_end <= day:
            project_build.append(c_i.name)
            added_con.append(contributor_list[c_i])
            c_i.last_project_end = day + project.duration
            project_team_skills.update(c_i.skills)
            c_i.skills[skill] = 1
        return True, c_i
    return False, -1


def update_skills_dict(skills_dict, updated_con_skill, contributor_list):
    for ci in updated_con_skill:
        skill = contributor_list[ci].last_updated_skill
        skill_level = contributor_list[ci].skills[skill]
        skill_builder(skill, ci, skill_level, skills_dict)
        skills_dict[skill][skill_level-1].remove(ci)
        if len(skills_dict[skill][skill_level-1]) == 0:
            del skills_dict[skill][skill_level-1]

        
    ...
files = ['a_an_example.in.txt', 'b_better_start_small.in.txt', 'c_collaboration.in.txt',
         'd_dense_schedule.in.txt', 'e_exceptional_skills.in.txt', 'f_find_great_mentors.in.txt']
# files = ['a_an_example.in.txt']
'''
skills_dict = {
    "skill_name" = {
        "skill_level" = [list_of_contributors]
    }
}
'''

def main():
    contributor_list = None
    project_list = None
    skills_dict = None
    
    for j in range(len(files)):
        
        with open(files[j]) as f:
            lines = f.readlines()
            data_num = lines[0].rstrip()
            num_of_ppl = int(data_num.split(" ")[0])
            num_of_proj = int(data_num.split(" ")[1])
            con_left = True

            contributor_list = []
            contributor_list_single_skill = []
            project_list = []
            skills_dict = {}
            
            building = False
            skills_count = 0
            
            for i in range(len(lines)):
                if i == 0:
                    continue

                line = lines[i].rstrip().split(" ")
                
                if not building:
                    building = True
                    skills_count = con_builder(contributor_list, line) if len(contributor_list) < num_of_ppl else pro_builder(project_list, line) 
                    if skills_count == 1:
                        contributor_list_single_skill.append(contributor_list[-1])
                else:
                    if con_left:
                        contributor_list[-1].skills[line[0]] = int(line[1])
                        skill_builder(line[0], len(contributor_list)-1, int(line[1]), skills_dict)
                    else:
                        project_list[-1].skills[line[0]] = int(line[1])
                    skills_count -= 1
                    if skills_count == 0:
                        building = False
                        if len(contributor_list) == num_of_ppl:
                            con_left = False
            
        # project_list.sort(key=lambda x: x.best_beforeproject_build # Might not be required
        
        day = 0
        project_days = []
        project_output_list = []
        
        while True:
            successful_project = []

            for i in range(len(project_list)):
                project = project_list[i]
                project_team_skills = {}
                project_build = [project.name]
                added_con = []
                updated_con_skill = []
                con_found = False
                project_impossible = False
                
                for skill, skill_level in project.skills.items():
                    
                    if skill_level in skills_dict[skill]:
                        con_found, c_i = add_con(skills_dict, skill, skill_level, contributor_list, day, project_build, project_team_skills, project, added_con)
                        if con_found:
                            con_found = False
                            contributor_list[c_i].skills[skill] += 1
                            contributor_list[c_i].last_updated_skill = skill
                            updated_con_skill.append(c_i)
                            continue
                    
                    if len(project.skills) > 1 and skill in project_team_skills:
                        if project_team_skills[skill] >= skill_level:
                            if skill_level == 1:
                                con_found, c_i = add_con_mentored_lvl_0(skill, contributor_list_single_skill, day, project_build, project_team_skills, project, added_con)
                                if con_found:
                                    con_found = False
                                    contributor_list[c_i].last_updated_skill = skill
                                    updated_con_skill.append(c_i)
                                    continue
                                
                            elif skill_level - 1 in skills_dict[skill]:
                                con_found, c_i = add_con(skills_dict, skill, skill_level - 1, contributor_list, day, project_build, project_team_skills, project, added_con)
                                if con_found:
                                    con_found = False
                                    contributor_list[c_i].skills[skill] += 1
                                    contributor_list[c_i].last_updated_skill = skill
                                    updated_con_skill.append(c_i)
                                continue

                    keys_gt_list = [k for k in skills_dict[skill].keys() if k >= skill_level]
                    keys_gt_list.sort()
                    
                    if len(keys_gt_list) > 0:
                        for s_l in keys_gt_list:
                            for c_i in skills_dict[skill][s_l]:
                                con_found, c_i_ph = add_con(skills_dict, skill, s_l, contributor_list, day, project_build, project_team_skills, project, added_con)
                                if con_found == True:
                                    break
                            if con_found == True:
                                con_found = False
                                break       
                
                    else:
                        project_impossible = True
                        break
                
                if project_impossible or len(project_build) -1 != len(project.skills):
                    for ci in added_con:
                        ci.last_project_end -= project.duration
                    for ci in updated_con_skill:
                        contributor_list[ci].skills[contributor_list[ci].last_updated_skill] -= 1
                        project_impossible = False
                
                elif len(project.skills) == 1 and len(project_build) == 1:
                    continue
                
                else:
                    project_output_list.append(project_build)
                    project_days.append(project.duration)
                    successful_project.append(i)
                    if len(updated_con_skill) > 0:
                        update_skills_dict(skills_dict, updated_con_skill, contributor_list)
                    
        
            if len(project_days) > 0:
                project_days.sort()
                day = project_days.pop(0)
                for index in sorted(successful_project, reverse=True):
                    del project_list[index]
                successful_project = []
                

            else:
                break

        
        print(project_output_list)
        
        file_output = ['sol_a.txt', 'sol_b.txt', 'sol_c.txt','sol_d.txt', 'sol_e.txt', 'sol_f.txt']
    
        with open(f'solution/{file_output[j]}', 'w') as f:
            f.write(f"{len(project_output_list)}\n")
            for project_output in project_output_list:
                f.write(project_output[0])
                f.write('\n')
                for i in range(len(project_output)):
                    if i == 0:
                        continue
                    f.write(project_output[i])
                    f.write(' ')
                f.write('\n')
        
if __name__ == '__main__':
    main()