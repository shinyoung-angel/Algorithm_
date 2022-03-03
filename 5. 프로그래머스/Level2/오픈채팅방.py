
name_dict = {}
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):

    for tmp in record:
        command = tmp.split()
        if command[0] == 'Enter' or command[0] == 'Change':
            com, id, name = command[0], command[1], command[2]
            name_dict[id] = name

    result = []
    for tmp in record:
        command = tmp.split()
        if command[0] == 'Enter':
            result.append("{}님이 들어왔습니다.".format(name_dict[command[1]]))

        elif command[0] == 'Leave':
            result.append("{}님이 나갔습니다.".format(name_dict[command[1]]))

    return result

tmp = solution(record)
print(tmp)