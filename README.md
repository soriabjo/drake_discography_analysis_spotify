# Analyzing Drake's Discography

![Drake](https://people.com/thmb/KgS-U2MoKqWX3YWAbmhoGtkszIE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(959x305:961x307)/drake-annouces-tour-031423-c2f3a04d41bc41048f91dda62543b072.jpg)

## Introduction

A 5-time Grammy Awards winner, 29-time Billboard Music Award winner, 2021's Favorite Rap/Hip-Hop Male Artist and pop culture superstar.

The most impressive accolade? The 2010's Artist of the Decade.

Aubrey Graham, otherwise known as "Drake", has cemented a legendary career in the music industry spanning over 17 years.

The Canadaian rapper began his incredible run after his start in TV. Appearing in Degrassi (2001-2015), Drake played the character Jimmy.

![Degrassi](https://helios-i.mashable.com/imagery/articles/03ITsWM4FicmwQeU5DxaUMr/hero-image.fill.size_1248x702.v1611614194.jpg)

As a Drake fan, I've listened to his music for over a decade. His ability to stay relevant in the ever-competitive music industry speaks to natural talent to keep his followers entertained with new flows.

This data project was inspired by Spotify's annual Unwrapped project. Unwrapped has been a well received concept from Spotify that aims at unveiling fun insights from their user data every year without being too intrusive. 

I must admit that last year was an extreme for my Drake fix, proven by one of the stories Spotify Unwrapped showed me:

![Unwrapped](unwrapped.png)

#### I know. That's an **insane number**.

 I'd consider this pretty impressive, considering that of his over 70 million monthly followers on Spotify, only around 42,000 people listen to Drake more than me!

11,380 minutes roughly translates to 190 hours of streaming. You can typically find me with AirPods in, but especially in 2022 with all the new music he put out.

![Unwrapped2](unwrapped2.png)

This translates to around ~4 hours of streaming a day 😮

Take what you will from that information!

## Data

To collect the data, I utilized Spotify's Web API. You first have to create an app in order to authorize your requests to the API as well as obtaining an access token. If you'd like to peform analysis for other artists, check their documentation [here](https://developer.spotify.com/documentation/web-api).

Some of the final dataset had to be preprocessed/feature engineered. While the Web API provides most of the core features, I had to do some further cleansing. Date variables, track length, artists on tracks are just some that I had to play around with to get it ready for analysis. To check out the entire data wrangling process, see the Python notebook in the repo.

**NOTICE:** 

* Spotify's API does not provide the number of streams for a given track, so I had to manually enter the number of streams for all songs on Drake albums through the Spotify app. It was time consuming but I did not have any other alternative. Spotify on web browser also hides this data so my attempt at web-scraping was unsuccessful. The values for the ```Plays``` variable was entered on **April 26th, 2023**. This snapshot of how many times each song has been streamed is no longer accurate.


* I removed the album **Nothing Was The Same (2013)** since the deluxe contained all of the original songs. Keeping the original album would have been redundant.

* Fans might argue that **Dark Lane Demo Tapes (2020)** was not an album, but rather a mixtape of individual songs packaged into a collection. I decided to keep the 'album'. Stringing to the same tune, **Care Package (2019)** is also not considered a true album as it's a compilation of songs between 2010-2016. I decided to keep this.


Lets dig in!

## Analysis (Popularity)

```
data.head()
```

![Head](/screenshots/head.png)

More features are not shown in this snapshot. Drake's album discography contains 14 albums, 243 songs with the final dataset containing 31 features - 

```

data.info()

Data columns (total 31 columns):
 #   Column                    Non-Null Count  Dtype  
---  ------                    --------------  -----  
 0   Album                     243 non-null    object 
 1   Release Date              243 non-null    object 
 2   Release Year              243 non-null    int64  
 3   Release Month             243 non-null    int64  
 4   Release Month (Name)      243 non-null    object 
 5   Release Day               243 non-null    int64  
 6   Release Day (Name)        243 non-null    object 
 7   Album ID                  243 non-null    object 
 8   Number of Album Songs     243 non-null    int64  
 9   Song Name                 243 non-null    object 
 10  Plays                     243 non-null    int64  
 11  Artist                    243 non-null    object 
 12  Song ID                   243 non-null    object 
 13  Track Duration            243 non-null    object 
 14  Track Duration (Minutes)  243 non-null    int64  
 15  Track Duration (Seconds)  243 non-null    int64  
 16  Track Number              243 non-null    int64  
 17  Number of Artists         243 non-null    int64  
 18  Danceability              243 non-null    float64
 19  Energy                    243 non-null    float64
 20  Key                       243 non-null    int64  
 21  Loudness                  243 non-null    float64
 22  Speechiness               243 non-null    float64
 23  Acousticness              243 non-null    float64
 24  Instrumentalness          243 non-null    float64
 25  Liveness                  243 non-null    float64
 26  Valence                   243 non-null    float64
 27  Tempo                     243 non-null    float64
 28  Artist 1                  243 non-null    object 
 29  Artist 2                  95 non-null     object 
 30  Artist 3                  19 non-null     object 
dtypes: float64(9), int64(10), object(12)

```

Summary Statistics - 

```
data.describe()
```

![Describe](/screenshots/describe.png)

Now that the data has been introduced, let's investigate some questions regarding his catalog.


### How Are Album's Ranked?

![Album Popularity](graphs/q1.png)

Not surprising to see Scorpion and Views taking the top 2 most popular Drake albums. Some of his most popular tracks appear in these albums, from *God's Plan, In My Feelings, One Dance and Hotline Bling*. Do you remember where you were when these songs released? 

[![Watch the video](https://cdn.theatlantic.com/thumbor/pfZ0QSpdaJ31DdOaJ9sce8gcdoc=/112x0:1712x900/1600x900/media/img/mt/2018/02/drake_gods_plan/original.png)](https://www.youtube.com/watch?v=xpVfcZ0ZcFM&source_ve_path=MTc4NDI0&ab_channel=DrakeVEVO)


Part of the reason why Drake has sustained mainstream status in the music industry is thanks to catchy, iconic hits like these songs. Whether by lyrics, memes, or music videos, his relatability to the pop culture scene is uncanny. Staying relevant for this long is no easy feat, as most have just a few hits before vanishing from mainstream music.

However, it's worthy to note some of his worst peforming albums. His most recent albums, Her Loss and Honestly, Nevermind just released last year. It would be immature to take this graph at face value without understanding context. Give these albums time. Especially Her Loss, which is without a doubt been given positive feedback by most of his audience.

<iframe style="border-radius:12px" src="https://open.spotify.com/embed/album/5MS3MvWHJ3lOZPLiMxzOU6?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>


Speaking of popularity, what are his most popular songs?

### Top Tracks

![Song Popularity](graphs/q2.png)

At first glance, I'm actually surprised One Dance is his most popular song. I thought it would be God's Plan because of how it exploded across streaming sites in addition to it's music video that was released.

It's also interesting that the majority of songs in this list are either released as a Single or EP(extended play). To my knowledge, God's Plan (Scary Hours), One Dance, Hotline Bling, and Toosie Slide are considered a Single/EP. It's almost as if Drake knew these tracks would be a hit!

Unfortunately, I couldn't seem to have the chart color-coded without having it grouped by album in plotly. Regardless, here it is:

![Song Popularity 2](graphs/q3.png)

As expected, his most popular tracks are also featured in his most popular albums. Toosie Slide is the exception, as this was a single that took the music industry by storm with the catchy, Tik-Tok friendly track. During lockdown, Drake delivered with a fun, danceable track. He also produced a music video, showcasing his _ridiculuously_ beautiful $100 million Canadian home estate. Check it out below!


[![Toosie Slide](https://static.onecms.io/wp-content/uploads/sites/6/2020/04/03/drake-2.jpg)](https://www.youtube.com/watch?v=xWggTb45brM&ab_channel=DrakeVEVO)

Here's the list with his most popular song on each album:

```
q3 = pysqldf("SELECT Album, [Song Name], MAX(Plays) AS Streams 
                FROM data
                GROUP BY Album 
                ORDER BY MAX(Plays) DESC"
            )
```
![Popular Song By Album](/screenshots/top_tracks_by_album.png)

## Analysis (Artists)

Artists such as Travis Scott, Kanye West, 21 Savage, and Rihanna have appeared on Aubrey's discography. Featuring other artists on albums can prove effective in joining fanbases, providing an alternative sound to the album, and increase hype. Personally, I try to listen to songs with features first before exploring solos whenever Drake drops an album. They tend to be the most listened to.

How do Drake songs perform when comparing between solos and songs with features?

###