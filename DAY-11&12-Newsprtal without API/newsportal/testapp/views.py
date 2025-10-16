from django.shortcuts import render

def news(request):
    return render(request, 'testapp/index.html')


def movies(request):
    heading = "Movie Buzz: New Releases & Box-Office Hits"

    sub1 = """Box-Office Hits & Big Releases:
    - “Mahavatar Narsimha” has confirmed its OTT release after a strong theatrical run, celebrated for its visuals and mythological storytelling.
    - “Saiyaara” crossed ₹350 crore worldwide, becoming one of the biggest global hits for Hindi films."""

    sub2 = """Trending Now / Critical Acclaim:
    - Leonardo DiCaprio’s “One Battle After Another” is being hailed by critics, achieving top Metacritic scores — one of 2025’s most acclaimed films.
    - Kalyani Priyadarshan’s “Lokah: Chapter 1 – Chandra” is now the 12th biggest hit of 2025."""

    sub3 = """Upcoming / Rumors & Developments:
    - Deepika Padukone has been dropped from the “Kalki 2898 AD” sequel due to commitment issues.
    - “Mere Raho,” an Aamir Khan Productions film starring Junaid Khan & Sai Pallavi, is set to release on 12 December 2025."""

    type = 'movies'
    dict = {'heading': heading, 'sub1': sub1, 'sub2': sub2, 'sub3': sub3, 'type': type}
    return render(request, 'testapp/news.html', context=dict)


def sports(request):
    heading = "SPORTS NEWS HIGHLIGHTS"

    sub1 = """Top Performers & Major Results:
    - Jaismine Lamboria won gold in the women’s 57 kg category and Nupur got silver (+80 kg) at the World Boxing Championships in Liverpool.
    - Meghana Sajjanar secured bronze in the women’s 10m air rifle at the ISSF World Cup; India finished fifth overall."""

    sub2 = """Upcoming Matches & Fixtures:
    - Super Four stage of Asia Cup 2025 begins soon; India vs Pakistan scheduled for September 21.
    - India will play Oman in their final Group A match in Asia Cup before the Super Four stage."""

    sub3 = """Noteworthy Stories & Context:
    - India vs Pakistan matches continue to carry strong diplomatic and emotional weight amid regional tensions.
    - India is marking its 250th T20-International match vs Oman in the Asia Cup. Wide interest and record tracking are expected for this milestone."""

    type = 'sports'
    dict = {'heading': heading, 'sub1': sub1, 'sub2': sub2, 'sub3': sub3, 'type': type}
    return render(request, 'testapp/news.html', context=dict)


def politics(request):
    heading = "LATEST POLITICAL UPDATES"

    sub1 = """Top Headlines:
    - EU pressuring to reduce dependency on the US; trade deal with India expected by year-end.
    - U.S. may ease tariffs on Indian goods, reducing import duties and improving relations."""

    sub2 = """Elections & Policy Moves:
    - India’s net direct tax collections rose over 9% year-on-year till mid-September; strong fiscal health.
    - Defence technology firms in India targeted for growth under government push for indigenisation."""

    sub3 = """International Affairs:
    - Discussions ongoing between India and global partners to strengthen strategic trade and tech collaboration.
    - Pakistan-India relations continue under intense media scrutiny, especially in light of sport diplomacy and regional security climate."""

    type = 'politics'
    dict = {'heading': heading, 'sub1': sub1, 'sub2': sub2, 'sub3': sub3, 'type': type}
    return render(request, 'testapp/news.html', context=dict)


def software(request):
    heading = "SOFTWARE & TECH NEWS"

    sub1 = """Latest Releases & Innovations:
    - Apple may manufacture its foldable iPhones in India, with pilot production in Taiwan.
    - Panasonic is planning a new white goods plant in India under the Production-Linked Incentive scheme."""

    sub2 = """Industry Trends & Events:
    - UPITS 2025 will showcase live AI model demos, startup zones, and media displays as Uttar Pradesh pushes itself as a tech hub.
    - India AI Mission has selected more firms for “foundational AI models”, indicating growing investment in core AI infra. (from ETTech reports)"""

    sub3 = """Tools & Ecosystem Updates:
    - Push for domestic manufacturing under PLI schemes across tech & electronics.
    - Startups & government initiatives increasing focus on AI, data centers, and defence tech competencies."""

    type = 'software'
    dict = {'heading': heading, 'sub1': sub1, 'sub2': sub2, 'sub3': sub3, 'type': type}
    return render(request, 'testapp/news.html', context=dict)


def business(request):
    heading = "BUSINESS & MARKET INSIGHTS"

    sub1 = """Stock Market & Economy:
    - India’s stock market has underperformed in 2025, with Sensex & Nifty facing pressure from slow earnings and high valuations.
    - U.S. easing tariffs on Indian imports has stirred optimism in Indian financial markets."""

    sub2 = """Corporate Moves & Policies:
    - Net direct tax collections in India rose over 9% year–on–year for April-Sept period ending mid-September.
    - Defence tech companies targeted by policy to grow; indigenisation & export focus anticipated to drive corporate realignment."""

    sub3 = """Global & Trade Relations:
    - EU-India trade agreement talks are ongoing; diversifying away from reliance on the U.S. is a key driver.
    - PLI schemes and manufacturing policy are shaping India's strategy to attract investment in white goods, electronics, and AI infrastructure."""

    type = 'business'
    dict = {'heading': heading, 'sub1': sub1, 'sub2': sub2, 'sub3': sub3, 'type': type}
    return render(request, 'testapp/news.html', context=dict)
