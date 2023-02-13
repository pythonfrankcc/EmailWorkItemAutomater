#html tags remover
import re
#regex = re.compile(r'<[^>]+>')
regex = re.compile('<.*?>')
regex1 = re.compile('\t\r\n')


def remove_html(string):
    return regex.sub('', string)
# def remove_whitesapaces(string1):
#     return regex1.sub('',string1)
#using the with keyword to ensure automatic closing of the file once reading is completed
file2 = open(r"myfile1.txt", "a")
with open("myfile.txt") as file:
    for item in file:
        clean_text = remove_html(item)
        #clean_text1 =remove_whitesapaces(clean_text)
        file2.write(clean_text)
file2.close()