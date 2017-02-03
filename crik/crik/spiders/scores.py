import scrapy
import time 
import subprocess

count=1
prev_score1=-1
prev_score2=-1
index=0
teams1=[]
teams2=[]
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'http://www.espncricinfo.com/ci/engine/match/index.html'
    ]

    def sendmessage(self, message):
        subprocess.Popen(['notify-send', message])
        return

#    count=1
    def parse(self, response):
        li=response.css('div.matches-wrapper')
        li1=li[0].css('div.matches-container')
        li2=li1[0].css('section.matches-day-block')
        li3=li1[0].css('div.innings-info-1')
        li4=li1[0].css('div.innings-info-2')
        #print count
        global count
        global index
        global teams1
        global teams2
        global prev_score1
        global prev_score2
        
        if(count==1):
            for match in li3:
                score=match.css('div.innings-info-1::text').extract()
                st=""
                flag=0
                for i in range(0,len(score)-1):
                    st+=score[i]
                    #print score[i]
                teams1.append(score[0].strip())
            for match in li4:
                score=match.css('div.innings-info-2::text').extract()
                st=""
                flag=0
                for i in range(0,len(score)-1):
                    st+=score[i]
                    #print score[i]
                teams2.append(score[0].strip())

            for i in range(0,len(teams2)):
                print ("%s %s vs %s" %(i+1, teams1[i], teams2[i]))

            """for match in li4:
                print match.css('span.bold::text').extract_first().strip()"""


            print "Enter the match index you wanted to see"
            index=int(input(""))

        exit=False
        while exit==False:
            print ("%s %s" %(teams1[index-1], li3[index-1].css('span.bold::text').extract_first().strip()))
            score1=li3[index-1].css('span.bold::text').extract_first().strip()
            print ("%s %s" %(teams2[index-1], li4[index-1].css('span.bold::text').extract_first().strip()))
            score2=li4[index-1].css('span.bold::text').extract_first().strip()
            
       

            if str(prev_score1)!=score1 and count!=1:
                wick=score1.split("/")
                wick=wick[1].split(" ")
                wick=wick[0]

                prev_wick=prev_score1.split("/")
                prev_wick=prev_wick[1].split(" ")
                prev_wick=prev_wick[0]

                if prev_wick!=wick:
                    #q=QuotesSpider()
                    st="Wickets have fallen!\nCurrent Score is " + score1
                    self.sendmessage(st)

            
            if str(prev_score2)!=score2 and count!=1:
                wick=score2.split("/")
                wick=wick[1].split(" ")
                wick=wick[0]

                prev_wick=prev_score2.split("/")
                prev_wick=prev_wick[1].split(" ")
                prev_wick=prev_wick[0]

                if prev_wick!=wick:
                    #q=QuotesSpider()
                    st="Wickets have fallen!\nCurrent Score is " + score2
                    self.sendmessage(st)

            #if prev_score2!=score2:

            prev_score1=score1
            prev_score2=score2
            t_end = time.time() + 10
            while time.time() < t_end:
                i=0

            st=teams1[index-1] + " " + li3[index-1].css('span.bold::text').extract_first().strip() + "\n" + teams2[index-1] + " " + li4[index-1].css('span.bold::text').extract_first().strip()
            self.sendmessage(st)

            
            count=count+1
            next_page='http://www.espncricinfo.com/ci/engine/match/index.html'
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse,dont_filter=True)
            exit=True


