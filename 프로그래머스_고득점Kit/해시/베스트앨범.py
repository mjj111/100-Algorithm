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

#장르에 대해서 내림차순으로 접근할 수 있도록 각 장르의 종합 플레이 횟수를 저장한다.
#장르별로 접근하게 되는데, 각 장르에 해당하는 곡들은 자신의 인덱스와 재생 수를 갖고있다.
# 각 장르별로 저장되어 딕셔너리를 리스트화한 뒤에, 해당 리스트를 재생수별로 정렬한다.
#정렬된 리스트별로 하나씩 접근하여answer에 담는다 .
 