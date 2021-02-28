# Features

- user switching - done
- user agent  - not implementing
- ip
- search engine - done
- fake browsing
- watch
- like/dislike/subscribe
- comment
- back/forward

# Flow of Logic

1. Open the GUI
2. wait for input [video title]
3. Get user
4. Load selenium driver and open browser
5. Open Google
6. Sign In
7. Google search video [/w title]
8. Get yt link
9. Start Loop [4 times]
    1. watch video [for 5-10 min [random]]
    2. Fake browsing
10. GOTO step[3] 
