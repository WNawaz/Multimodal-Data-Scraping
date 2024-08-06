import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

def write_data(url,filename,keyword,kind,page,fatwa_flag=False):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    article_links = soup.find_all('a', href=True)
    #print(article_links)

    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)

        for link in article_links:
            article_url = link['href']
            if keyword in article_url:
                #print(article_url)
                article_response = requests.get(article_url)
                article_soup = BeautifulSoup(article_response.text, 'html.parser')

                # Extract article title
                article_title_element = article_soup.find('h1', class_='article-title--primary')
                article_title = article_title_element.text.strip() if article_title_element else ''

                # Extract article content
                article_content_element = article_soup.find('div', class_='article-content')
                article_content = article_content_element.text.strip() if article_content_element else ''

                if fatwa_flag:
                  # Extract article question
                  article_question_element = article_soup.find('h2', class_='article-title article-title__question article-title--primary')
                  article_question = article_question_element.text.strip() if article_question_element else ''

                  # Extract article categories
                  categories_div = article_soup.find('div', class_='categories')
                  category_items = categories_div.find_all('a', class_='categories__item')
                  categories = [item.get_text(strip=True) for item in category_items]

                  # Write article title and content to CSV
                  if article_content_element:
                    csvwriter.writerow([article_title, article_question, article_content,keyword,article_url,kind,page,categories])
                    print('wrote: '+article_url)
                else:
                  # Write article title and content to CSV
                  if article_content_element:
                    csvwriter.writerow([article_title,  article_content,keyword,article_url,page])
                    print('wrote: '+article_url)

# binbaaz

def static_web(fname, base_url,list_content): #list_content list of all types in urls to get ['articles','discussions','speeches','pearls']
  pages=[13,10,21,9]#[317,820,380,120]
  for j,sub in enumerate(list_content):#='fatwas/kind/'#
#for j in range(3,5):#5
  tld = base_url+sub#+str(j)
  for i in range(1,pages[j]):
    write_data(tld+'?page=' + str(i),fname+'.csv',keyword_filter,'kind '+str(j),'page '+str(i))#fatwa_flag=True

def organize(org_out_file):
  fatwa_dict = {  
    "kind 1": "مجموع الفتاوى",
    "kind 2": "نور على الدرب",
    "kind 3": "فتاوى الدروس",
    "kind 4": "فتاوى الجامع الكبير"
  }
  content_dict = {
    "articles": "مقالات",
    "discussions": "لقاءات وحوارات",
    "speeches": "خطابات ومراسلات",
    "pearls": "درر"
  }
 df=pd.read_csv(org_out_file)
 df.loc[-1] = df.columns  # adding a row
 df.index = df.index + 1  # shifting index
 df = df.sort_index()  # sorting by index to put new row at the top
 # Assign new column names
 new_header = ["New Col 1", "New Col 2", "New Col 3", "New Col 4", "New Col 5","New Col 6","New Col 7"]
 df.columns = new_header
 df["New Col 5"] = df["New Col 5"].map(fatwa_dict) # content_dict
 df = df[["New Col 1", "New Col 2", "New Col 3", "New Col 7","New Col 5","New Col 6", "New Col 4"]]
 df.columns = ["Title",'Question', "Fatwa", "Fatwa_Category",'Programme', "Page", "URL"]
 df = df.drop_duplicates()
 df.to_csv(org_out_file, index=False)