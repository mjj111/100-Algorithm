List<Member> members = submitRepository.findAll();
Queue<Member> koreaQueue = new Queuue<>();
Queue<Member> englishQueue = new Queuue<>();
Queue<Member> japanQueue = new Queuue<>();
List<Queue> preferLanguages = new ArrayyList<Queue>();
preferLanguage.append(koreaQueue);
preferLanguage.append(englishQueue);
preferLanguage.append(japanQueue);


// 선호 언어별 큐에 인원들 삽입 
for (Member member : members){
    switch(member.preferLanguage)
    case "korea" : preferLanguages.KoreaQueue.append(member)
    case "english" : preferLanguages.japanQueue.append(member)
    case "japan" : preferLanguages.englishQueue.append(member)
}

for (int i = 0 ; i < preferLanguages.length; i++){
    for (int j = 0; j < )
}
