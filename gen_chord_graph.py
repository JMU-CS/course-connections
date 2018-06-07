

def load_graph_data():
    lines = map(lambda x: x.strip(), open('graph-data.txt','r').readlines())
    courses = []
    tags = {}
    course = None
    for line in lines: 
        if line.startswith("CS"):
            course = line
            courses.append(course)
            tags[course] = set()
        elif line.startswith("#"):
            tags[course].add(line)
    return courses, tags

def all_tags(courses, tags):
    tagSet = set()
    for course in courses:
        tagSet = tagSet | tags[course]
    retList = list(tagSet)
    retList.sort()
    return retList

def gen_graph(courses, tags):
    matrixStr = "var matrix = ["
    for i in range(len(courses)):
        matrixStr += "["
        for j in range(len(courses)):
            if i != j:
                weight = len(tags[courses[i]] & tags[courses[j]])
            else:
                weight = 0
            matrixStr += str(weight)
            if j < len(courses)-1:
                matrixStr += ","
        matrixStr += "]"
        if i < len(courses)-1:
            matrixStr += ",\n"
    matrixStr += "];\n\n"

    coursesStr = "var courseLabels = [\n"
    titlesStr = "var courseTitles = [\n"
    for i in range(len(courses)):
        if i != 0:
            coursesStr += ",\n"
            titlesStr += ",\n"
        coursesStr += "    \"" + courses[i][0:6] + "\""
        titlesStr += "    \"" + courses[i][7:] + "\""
    coursesStr += "\n];\n\n"
    titlesStr += "\n];\n\n"

    tagStr = "var tags = [\n"
    tagList = all_tags(courses, tags)
    for i in range(len(tagList)): 
        if i != 0:
            tagStr += ",\n"
        tagStr += "    \"" + tagList[i] + "\""
    tagStr += "\n];\n\n"

    return matrixStr + coursesStr + titlesStr + tagStr

courses, tags = load_graph_data()
print(gen_graph(courses, tags))
