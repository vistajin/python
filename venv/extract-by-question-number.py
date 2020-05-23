# ~~~~parameters~~~~~
# the src file with answer
src = '/home/vistajin/Desktop/test-aws-saa-with-answer.txt'
# the question numbers to extract
question_numbers = [9, 93, 100, 102, 146, 176, 177, 203, 227, 240, 241, 244, 251, 252, 262, 284, 293, 304, 309, 312,
                    318, 319, 323, 329, 333, 343, 345, 346, 368]

flag = False
num = 1
with open(src, 'r', encoding='UTF-8') as f:
    all_content = f.readlines()
    for line in all_content:
        if line.strip() == "":
            continue
        for question_number in question_numbers:
            if line.strip() == "Question " + str(question_number):
                flag = True
                print("================= %0d ==================" % num)
                num = num + 1
        if not flag:
            continue
        print(line.strip())
        if line.find("Answer: ") != -1:
            flag = False
