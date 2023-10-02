import requests , json
from bs4 import BeautifulSoup
import urllib

def searchMovie(searchText : str) -> str : 

    mobile_headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'
    }
    parsed_search_name = urllib.parse.quote(searchText)
    html_content = ''

    html_content = requests.get(f'https://tamilyogi.band/?s={parsed_search_name}&submit=Search' , timeout=10 , headers=mobile_headers).text

    parsed_html = BeautifulSoup(html_content , 'html.parser')
    all_results = parsed_html.select('#post-results a')
    result = []
    if len(all_results) == 0 : 
        return "No results found for the search query"

    for i in range(min(3 , len(all_results))) : 
        movie_link = all_results[i].get('href')
        movie_name = all_results[i].select_one('.post-title').text
        movie_name = movie_name.replace('Watch Online' , '')

        movie_page = requests.get(movie_link , timeout=10 , headers=mobile_headers).text

        parsed_movie_page = BeautifulSoup(movie_page , 'html.parser')
        partial_download_link_element_page = parsed_movie_page.select_one('.rez iframe')
        partial_download_link_page = partial_download_link_element_page.get('src')
        full_download_link_page = 'https://embed.icu/embed-' + partial_download_link_page.split('-')[-1]
        final_movie_page = requests.get(full_download_link_page , timeout=10 , headers=mobile_headers).text
        
        parsed_final_movie_page = BeautifulSoup(final_movie_page , 'html.parser') 
        final_link_elements = parsed_final_movie_page.select('.download_links')
        final_links = []
        available_quality = ['720p' , '360p' , '240p']
        for i , link in enumerate(final_link_elements) : 
            final_links.append({
                'quality' : available_quality[i] , 
                'link' : link.get('href')
            })
        result.append({
            'movie-name' : movie_name , 
            'links' : final_links
        })
    return json.dumps(result)