# Epicurious and BeautifulSoup example


import requests, bs4

url = "http://www.epicurious.com/search/Tofu Chili"
page = 1

response = requests.get(url + "?page=" + str(page))
# print(response.content)

page_soup = bs4.BeautifulSoup(response.content, 'lxml')
# print(page_soup.prettify())

# all_a_tags = page_soup.find_all('a')
# print(all_a_tags)

# Underscore (_) after class is needed so that BeautifulSoup can identify that
# it should look for a class since the word "class" is reserved word
# print(page_soup.find_all('article', class_="article-content-card"))
# print(len(page_soup.find_all('article', class_="article-content-card")))

# Use a dictionary in find in order to search for multiple selectors
# .text only shows the text
# print(page_soup.find('article', {"class": "article-content-card"}).text)
# Using len on find will print the number of children of the returned tag
# print(len(page_soup.find('article', {"class": "article-content-card"})))

# We can also use .get instead of .find
# gallery = page_soup.find('article', {"class": "article-content-card"})
# gallery_link = gallery.find('a')
# print("gallery link:", gallery_link)
# link_url = gallery_link.get('href')
# print("link url:", link_url)

# print the children of "common-pagination" tag, one below the other
# print("pages: ", *page_soup.find('nav', class_="common-pagination"),
#   len(page_soup.find('nav', class_="common-pagination")),sep="\n\n" )

total_pages = int(page_soup.find('nav', class_="common-pagination").get("data-total-pages"))
print("Found:", total_pages, "total pages")

while(page < total_pages and (not page_soup.find('article', class_="recipe-content-card"))):
    page += 1
    print("Requesting next page at:", url + "?page=" + str(page))
    response = requests.get(url + "?page=" + str(page))
    page_soup = bs4.BeautifulSoup(response.content, 'lxml')

result_recipe = page_soup.find('article', class_="recipe-content-card")
if(result_recipe):
    print("Found a Recipe with title:", result_recipe.find('a').text)
    print("Found a Recipe with link:", result_recipe.find('a').get('href'))
    print("Found a Recipe with description:", result_recipe.find('p', class_='dek').get_text())
else:
    print("No Recipe found! Please try again!")
