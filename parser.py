from bs4 import BeautifulSoup

def parse(page):
    soup = BeautifulSoup(page, 'html.parser')
    attendance_heading = []
    attendance_body_content = []
    result_heading = []
    result_body = []
    examination_heading = []
    examination_body = []
    attendance_message = "0"
    examination_message = "0"
    result_message = "0"
    try:
        attendance = soup.find("div", {"id": "divAttendance"})
        table_head = attendance.find('thead')
        table_head = table_head.find_all('th')
        for element in table_head:
            attendance_heading.append((element.contents[0]).strip())
        attandance_body = attendance.find('tbody')
        attandance_body = attandance_body.find_all('tr')
        for entry in attandance_body:
            temp = entry.find_all('td')
            t = []
            for d in temp:
                t.append(d.contents[0].strip())
            attendance_body_content.append(t)
    except :
        attendance_message = "No Data Availabe"
        pass
    

    try:
        examination = soup.find("div", {"id": "divTestMark"})
        examination = examination.find_all('tbody')
        examination = examination[0].find_all('tr')
        for element in examination[0].find_all('th'):
            examination_heading.append(element.contents[0].strip())
        for element in examination[1:]:
            t = []
            for d in element.find_all('td'):
                t.append(d.contents[0].strip())
            examination_body.append(t)        
        pass
    except :
        examination_message = "No Data Availabe"
        pass


    try:
        result = soup.find("div", {"id": "div37419"})
        result = result.find('tbody')
        result = result.find_all('tr')
        for element in result[0].find_all('th'):
            result_heading.append(element.contents[0].strip())
        for element in result[1:]:
            t = []
            for d in element.find_all('td')[:2]:
                t.append(d.contents[0].strip())
            ele = element.find_all('span')
            for d in ele:
                t.append(d.contents[0].strip())
            result_body.append(t)
        pass

    except :
        result_message = "No Data Available"
        pass

    content = {
        'Attendance':
            {
                'heading': attendance_heading,
                'body': attendance_body_content,
                'message':attendance_message
            },
        'Examination': {
            
                'heading': examination_heading,
                'body': examination_body,
                'message':examination_message
            
            },
        'Result':
            {
                'heading': result_heading,
                'body': result_body,
                'message':result_message
            }
    }
    return content
