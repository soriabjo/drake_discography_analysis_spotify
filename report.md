# What Makes Drake Popular?
Analyzing Drake's Discography

![Drake](https://people.com/thmb/KgS-U2MoKqWX3YWAbmhoGtkszIE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc():focal(959x305:961x307)/drake-annouces-tour-031423-c2f3a04d41bc41048f91dda62543b072.jpg)

## Introduction

A 5-time Grammy Awards winner, 29-time Billboard Music Award winner, 2021's Favorite Rap/Hip-Hop Male Artist and pop culture superstar.

Oh, and the Artist of the Decade.

Aubrey Graham, otherwise known as "Drake", has cemented a legendary career in music spanning over 17 years.

The Canadaian rapper began his incredible run after his start in TV. Appearing in Degrassi (2001-2015), Drake played the character Jimmy.

![Degrassi](https://helios-i.mashable.com/imagery/articles/03ITsWM4FicmwQeU5DxaUMr/hero-image.fill.size_1248x702.v1611614194.jpg)

As a Drake fan, I've listened to his music for over a decade. His ability to stay relevant in the ever-competitive music industry speaks to natural talent to keep his followers entertained with new flows.

This data project was inspired by Spotify's annual Unwrapped project. Unwrapped has been a well received concept from Spotify that aims at unveiling fun insights from their user data without being too intrusive. I always find it interesting to see the type of music people that I know are into, as music can reveal more to their personalities. I must admit that last year was an extreme for my Drake fix, proven by one of the stories Spotify Unwrapped showed me:

![Unwrapped](unwrapped.png)

I know. That's an insane number.

 I'd consider this pretty impressive, considering that of his over 70 million monthly followers on Spotify, only around 42,000 people listen to Drake more than me!

11,380 minutes roughly translates to 190 hours of streaming. You can typically find me with AirPods in, but especially in 2022 with all the new music he put out.

## Data

To collect the data, I utilized Spotify's Web API. You first have to create an app in order to authorize your requests to the API as well as obtaining an access token. If you'd like to peform analysis for other artists, check their documentation [here](https://developer.spotify.com/documentation/web-api).

Some of the final dataset had to be preprocessed/feature engineered. While the Web API provides most of the core features, I had to do some further cleansing. Date variables, track length, artists on tracks are just some that I had to play around with to get it ready for analysis. 

**NOTE:** Spotify's API does not provide the number of streams for a given track, so I had to manually enter the number of streams for all songs on Drake albums through the Spotify app. It was time consuming but I did not really have any other alternative. Spotify on web browser also hides this data so my attempt at web-scraping was unsuccessful. The values for the ```Plays``` variable was entered on **April 26th, 2022**.

Lets dig in!

## Analysis

```
df.head()


```