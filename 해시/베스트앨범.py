from collections import defaultdict
def solution(genres, plays):
    genre_play = defaultdict(int)
    song_play = defaultdict(list)
    
    for i in range(len(genres)):
        genre_play[genres[i]] += plays[i]
        song_play[genres[i]].append((i,plays[i]))
    
    genre_lst = sorted(genre_play.items(),key=lambda x:x[1],reverse=True)
    answer = []
    for genre,_ in genre_lst:
        musics = sorted(song_play[genre],key=lambda x:x[1],reverse=True)[:2]
        for idx,nplay in musics:
            answer.append(idx)
    return answer
