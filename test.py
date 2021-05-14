from bs4 import BeautifulSoup


with open('test.html', 'r') as html:
    content = html.read()
    #print(content)
    
    soup = BeautifulSoup(content, 'lxml')
    
    tags = soup.find_all('div', class_='QA')



with open('answers.txt', 'w') as ans:
    for tag in tags:
        question = tag.find('p').text
        answer = tag.find('a', class_='true').text
        text = f'''{question} :
{answer}\n'''
        ans.writelines(text)