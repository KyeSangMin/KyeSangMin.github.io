#햇님달님

import random
import time


# def


def print_if_died():

    print(' ▄·▄▌      ▄• ▄▌    ·▄▄▄▄  ▪  ▄▄▄ .▄▄▄▄  ')
    print('▐█▪██▌▪     █▪██▌    ██▪ ██ ██ ▀▄.▀ ██▪ ██ ')
    print('▐█▌▐█▪ ▄█▀▄ █▌▐█▌    ▐█·▐█▌▐█ ▐▀▀▪▄▐█·▐█▌')
    print(' ▐█▀·.▐█▌▐▌▐█▄█▌    ██. ██ ▐█▌▐█▄▄▌██. ██ ')
    print('  ▀ •  ▀█▄▀▪ ▀▀▀     ▀▀▀▀▀• ▀▀▀ ▀▀▀ ▀▀▀▀▀• ')


def loading():

    print('▄▄          ▄▄▄· ▄▄▄▄  ▪   ▐ ▄  ▄▄ • ')
    time.sleep(1)
    print('██•  ▪     ▐█ ▀█ ██▪ ██ ██ •█▌▐█▐█ ▀ ▪')
    time.sleep(1)
    print('██▪   ▄█▀▄ ▄█▀▀█ ▐█·▐█▌▐█ ▐█▐▐▌▄█ ▀█▄')
    time.sleep(1)
    print('▐█▌▐▌▐█▌.▐▌▐█ ▪▐▌██. ██ ▐█▌██▐█▌▐█▄▪▐█')
    time.sleep(1)
    print('.▀▀▀  ▀█▄▀▪ ▀  ▀ ▀▀▀▀▀• ▀▀▀▀▀ █▪·▀▀▀▀ ')

def GameOver():
    
    print(' ▄▄ •  ▄▄▄· • ▌ ▄ ·. ▄▄▄ .         ▌  ▐·▄▄▄ .▄▄▄  ')
    print('▐█ ▀ ▪▐█ ▀█ ·██ ▐███▪▀▄.▀·    ▪    █·█▌▀▄.▀·▀▄ █·')
    print('▄█ ▀█▄▄█▀▀█  ▐█ ▌▐▌▐█·▐▀▀▪▄    ▄█▀▄ ▐█▐█•▐▀▀▪▄▐▀▀▄ ')
    print('▐█▄▪▐█▐█ ▪▐▌ ██ ██▌▐█▌▐█▄▄▌    ▐█▌.▐▌ ███ ▐█▄▄▌▐█•█▌')
    print('·▀▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀      ▀█▄▀▪. ▀   ▀▀▀ .▀  ▀')

def intro():

    print('옛날 어느 산골에 사이좋은 오누이가 어머니와 함께 살고 있었어요.')
    time.sleep(2)
    print('하루는 어머니가 고개넘어 부자집 잔치를 도와주기로 하였지요.')
    time.sleep(2)
    print('어머니:누가와서 문을 열어달라고 해도 함부로 열어주지 말거라')
    time.sleep(2)
    print('어머니는 오누이에게 몇번씩 당부를 하고 집을 나섰어요.')
    time.sleep(1)

def tiger():

    print('⊂_? ')
    print('　 ＼＼ Λ＿Λ') 
    print("　　 ＼ ('ㅅ')  ") 
    print('　　   >  ⌒? ')
    print('　　　/ 　 へ＼ ')
    print('　　 /　　/　＼＼ ')
    print('　　 ?　ノ　　 ?_つ ')
    print('　　/　/ ')
    print('　 /　/| ')
    print('　(　(? ')
    print('　|　|、＼') 
    print('　| ? ＼ ⌒)') 
    print('　| |　　) / ')
    print(' (`ノ ')

#value

play_type = 0
rand_num = random.randint(1, 2)

# main

intro()


loading()

while True:
    print('플레이할 캐릭터를 고르시오.')
    time.sleep(1)
    print('호랑이 (1) / 오누이(2)')

    play_type = input()
    
    if play_type == '1':
        print('')

        print("나는 호랑이 배가 고프다")

        time.sleep(1)
        
        print("마침 떡을 들고 가는 사람이 보인다")
        time.sleep(1)
        print("지나가는 사람에게 가볼까?")
        print("네 or 아니요")

        answer_1 = input()

        if answer_1 == '네':
            tiger()
            time.sleep(1)
            print("호랑이:어흥!, 떡하나 주면 안잡아 먹지!")
            time.sleep(1)
            print("떡을 얻었다.")
            time.sleep(3)
            print("아직 배가 고프니 먼저가서 기다리자")
            
        elif answer_1 == '아니요':
            print("호랑이가 굶어 죽었습니다.")
            time.sleep(1)
            print_if_died()
            continue
        else:
            print("다시 입력해 주세요")
            continue   

        print("다시 가서 위협할까?")
        print("네 or 아니요")

        answer_2 = input()

        if answer_2 =='네':
            tiger()
            time.sleep(1)
            print("호랑이:어흥!, 떡하나 주면 안잡아 먹지!")
            time.sleep(1)
            print("떡을 얻었다.")
            time.sleep(3)
            print("아직 배가 고프니 먼저가서 기다리자")

        elif answer_2 == '아니요':
            print("조금 미안하니 그러지 말자")
            time.sleep(3)
            time.sleep(3)
            print("........")
            time.sleep(2)
            print("호랑이가 굶어 죽었다.")
            time.sleep(1)
            print_if_died()
            
            continue

        else:
            print("다시 입력해 주세요")
            continue
        print("아직 배가 고픈데 다시 가서 위협할까?")

        answer_3 = input()

        if answer_3 == '네':
            tiger()
            time.sleep(1)
            print("호랑이:어흥!, 떡하나 주면 안잡아 먹지!")
            time.sleep(2)
            print("어머니:더 이상 떡이 없어요")
            time.sleep(2)
            print("호랑이:어흥!, 그럼 너를 잡아 먹겠다.")
            time.sleep(2)
            print("호랑이:이제 적당히 배가 부르군!")
            
        elif answer_3 == '아니요':
            print("호랑이:적당히 배가 부르긴 한데 그만둘까")
            time.sleep(2)
            print("오누이의 어머니가 무사히 집으로 돌아갔습니다.")
            time.sleep(2)
            GameOver()
            continue
            
        else:
            print("다시 입력해 주세요")
            continue

        print("오누이의 어머니를 잡아먹었다, 오누이의 집으로 찾아가자")
        loading()
        time.sleep(3)
        loading()
        print("오누이를 속이기 위해 옷을 입을까?")
        print("네 or 아니요")
        
        answer_4 = input()

        if answer_4 == '네':
            time.sleep(1)
            loading()
            time.sleep(2)
            print("오누이의 집에 도착했다.")
            print("호랑이:애들아 엄마다.")

        elif answer_4 == '아니요':
            print("오빠:앗! 호랑이다!")
            time.sleep(1)
            print("호랑이:앗! 들켰다!")
            time.sleep(1)
            print("오누이가 도망가 버렸다")
            GameOver()
            time.sleep(3)
            continue
            
        else:
            print("다시 입력해 주세요")
            continue
        print("오빠:우리 엄마 목소리는 그렇지 않은걸요?")
        time.sleep(2)
        print("호랑이:추운 고개를 넘어 오느라 감기에 걸려서 그렇지")
        time.sleep(2)
        print("오빠:목소리만으로는 엄마인지 아닌지 모르니까 손을 내밀어 보세요")
        time.sleep(2)
        print("손을 내밀까?")
        time.sleep(2)
        print("(1)분명 들킬꺼야 손을 주지 말자")
        time.sleep(2)
        print("(2)일단 줘본다")
        time.sleep(2)
        print('1or2')

        answer_5 = input()

        if answer_5 == '1':
            print("오빠:너 우리 엄마가 아니구나!")
            time.sleep(2)
            print("오누이가 도망쳤다!")
            time.sleep(2)
            GameOver()
            continue
        
        elif answer_5 =='2':
            print("오빠:이건 우리 엄마 손이 아니에요")
            time.sleep(1)
            print("오빠:우리 엄마 손은 이렇지 않아요")
            time.sleep(2)
            print("호랑이:하루종일 힘들게 일해서 그래")

        else:
            print("다시 입력해 주세요")
            continue

        print("오빠:그럼 눈을 보여주세요")
        time.sleep(2)
        print("구멍으로 눈을 보여주었다")
        time.sleep(2)
        print("오빠:우리 엄마 눈은 이렇지 않은데")
        time.sleep(2)
        print("호랑이:하루종일 힘들게 일을 해서 그렇단다.")
        time.sleep(3)
        time.sleep(2)
        print("방안에 반응이 없다.")
        time.sleep(1)
        print("방안에 들어가 볼까?")
        print("네 or 아니요")

        answer_6 = input()

        if answer_6 == '네':
            print("방문을 열었다.")
            time.sleep(2)
            print("오누이가 도망친다 쫒아가자.")

        elif answer_6 == '아니요':
            print("오누이가 도망갔다.")
            time.sleep(1)
            GameOver()
            continue
        
        else:
            print("다시 입력해 주세요")
            continue
        print("오누이가 나무 위로 올라갔다.")
        time.sleep(1)
        print("호랑이:거기 있었구나 너희들 거기 어떻게 올라갔니?")
        time.sleep(2)
        print("오빠:손에다 참기름을 바르고 올라왔지")
        time.sleep(1)
        print("부엌으로 가보자")
        time.sleep(1)
        print("부엌에 참기름과 도끼가 있다.")
        time.sleep(1)
        print("무엇을 가져갈까?")
        time.sleep(1)
        print("(1)참기름")
        time.sleep(1)
        print("(2)도끼")

        answer_7 = input()

        if answer_7 == '1':
            print("참기름을 발바닥에 발랐다")
            time.sleep(1)
            print("나무를 올라가 보자")
            time.sleep(1)
            print("얍")
            time.sleep(3)
            print("얍")
            time.sleep(3)
            print("얍")
            time.sleep(3)
            print("얍")
            time.sleep(3)
            print("앗!")
            time.sleep(1)
            print("발이 미끄러워 나무에서 떨어졌다!")
            time.sleep(1)
            print_if_died()
            time.sleep(2)
            print("도끼를 사용해보자.")
            continue

        elif answer_7 == '2':
            print("호랑이:내가 멍청이도 아니고 당연히 도끼지.")

        else:
            print("무엇이든 가져가야한다, 다시 생각하자.")
            continue
        
        print("바로 나무로 가서 도끼를 사용하자")
        time.sleep(1)
        loading()
        time.sleep(2)
        print("나무앞")
        time.sleep(1)
        print("도끼를 사용하자")
        time.sleep(1)
        print("뚝")
        time.sleep(1)
        print("딱")
        time.sleep(1)
        print("뚝")
        time.sleep(1)
        print("딱")
        time.sleep(1)
        print("오누이가 동아줄을 타고 도망친다!")

        loading()

        print("두개의 동아줄이 있다 어느 것을 타고 올라갈까?")
        print("1 or 2")
        
        answer_8 = input()

        if answer_8 == '1' and rand_num == '1':

            print("새 동아줄이다!")
            time.sleep(1)
            print("올라가자.")
            loading()
            time.sleep(2)
            print("드디어 오누이를 잡았다!")
            time.sleep(1)
            print("오누이:살려주세요!")
            time.sleep(2)
            print("오누이를 잡아먹었다!")
            time.sleep(1)
            print("이로써 호랑이는 오누이를 잡아먹는데 성공했답니다!")
            time.sleep(1)
            print("END")

            quit()
            
        
        elif answer_8 == '1' and rand_num == '2':
            
            print("올라가자.")
            loading()
            time.sleep(2)
            print("호랑이:앗! 썩은 동아줄이다!")
            time.sleep(1)
            print("동아줄이 끊어졌다!")
            time.sleep(1)
            print("호랑이;으아아아아!")
            time.sleep(1)
            print_if_died()

            quit()

        elif answer_8 == '2' and rand_num == '1':

            print("새 동아줄이다!")
            time.sleep(1)
            print("올라가자.")
            loading()
            time.sleep(2)
            print("드디어 오누이를 잡았다!")
            time.sleep(1)
            print("오누이:살려주세요!")
            time.sleep(2)
            print("오누이를 잡아먹었다!")
            time.sleep(1)
            print("이로써 호랑이는 오누이를 잡아먹는데 성공했답니다!")
            time.sleep(1)
            print("END")

            quit()
            

        elif answer_8 == '2' and rand_num == '2':
                  
            print("올라가자.")
            loading()
            time.sleep(2)
            print("호랑이:앗! 썩은 동아줄이다!")
            time.sleep(1)
            print("동아줄이 끊어졌다!")
            time.sleep(1)
            print("호랑이;으아아아아!")
            time.sleep(1)
            print_if_died()

            quit()

    elif play_type == '2':
        print('미구현')
        continue
    
    else:
        print('다시 입력해 주십시오')
        continue

