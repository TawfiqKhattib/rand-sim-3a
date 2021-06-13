from os import truncate
from csv_manager import CSV_Manager
from manipulator import Manipulator
import json

def filter_CSV(filter_field, value):
    reader = CSV_Manager("./articles.csv")
    articles = reader.get_csv_as_dicts()
    manipulator = Manipulator(articles)

    filtered = manipulator.filter_by(filter_field, value)
    return list(filtered)

def count_articles(filter_field, value):
    articalsArr = filter_CSV(filter_field, value);
    cnt = len(articalsArr);
    return cnt;

def is_article(filter_field, value):
    cnt =count_articles(filter_field, value)
    if(cnt>0):
        return True;
    return False;

def longest_article(filter_field, value):
    articalsArr=filter_CSV(filter_field, value);
    maxPages = 0;
    maxItem={};
    for item in articalsArr:
        if(int(item["pages"])>maxPages):
            maxItem = item;
    return maxItem;

def Mapp_Data():
    reader = CSV_Manager("./articles.csv");
    return reader.manag_properties();
    

# print("Articles with a title of t4:")
# print(filter_CSV("title", "t4"))
# print('')
# print("Articles of a1 author:")
# print(filter_CSV("author", "a1"))
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# print("Articles with a title of t4:")
# print(count_articles("title", "t4"))
# print('')
# print("Articles of a1 author:")
# print(count_articles("author", "a1"))
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# print("Articles with a title of t4:")
# print(is_article("title", "t4"))
# print('')
# print("Articles of a1 author:")
# print(is_article("author", "a0"))
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# print("Articles of a1 author:")
# print(longest_article("author", "a1"))
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
print("Articles of a1 author:")
print(Mapp_Data())