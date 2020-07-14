def howMany(cards):
  cardIdea=[0,0,0,0,0,0,0,0,0,0]#0부터 9까지 나온 카드 수
  cards=list(map(int,cards))#스트링으로 된 cards를 int로 구성된 리스트로 변환
  for i in cards:#골른 카드 한장씩 나올때마다 개수 추가
    cardIdea[i]+=1
  maxOfCardIdea=max(cardIdea)#카드수가 가장 많은 수
  for i in range(9,-1,-1):#가장 많이 나온 카드가 뭔지 위에서부터 찾음 (같은 개수중 가장 큰 수 찾기위함)
    if(cardIdea[i]==maxOfCardIdea):
      return [i,maxOfCardIdea]

T = int(input())#진행 수
A = []
for test_case in range(1, T + 1): #T번 진행
  N=int(input())#뽑을 카드 장수
  cards=input()[:N]#뽑은 카드수
  A.append(howMany(cards))

for test_case in range(1, T + 1): #가장 많은 카드의 숫자와 장 수를 차례로 출력
  print("#"+str(test_case), A[test_case-1][0], A[test_case-1][1])

