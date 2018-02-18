import scrapy


class HabrUserArticlesSpyder(scrapy.Spider):

    name = "habrarticles"
    start_urls = [
        'https://habrahabr.ru/users/olegchir/posts/page1/',
    ]

    def parse(self, response):

        username = response.css('div[class = user-info__links] a::text').extract_first()
        yield {'user': username}
        yield scrapy.Request('https://habrahabr.ru/users/olegchir/posts/page1/', self.parse_page)


    def parse_page(self, response):  

        for post in response.css('h2[class=post__title]'):
            title = post.css('a::text').extract_first()
            url = post.css('a::attr(href)').extract_first()
            yield {
                'post__title': title,
                'post_url': url,
            }

        next_page = response.css('li[class = arrows-pagination__item] a[id = next_page]::attr("href")').extract_first()
        
        
        if next_page != None:
            yield response.follow(next_page, self.parse_page)

        

    def parse_art(self, response):
        yield {'a' :'aaa'} 

    
