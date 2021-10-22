# OSS Tools
## Testing and Debugging in Python

Pytho debugger: pdb  
커맨드 라인이나, 비주얼스튜디오 코드에서 가능

어떻게?
1. breakpoint()함수 써서 하드코딩 방법
2. -m pdb 옵션 주기

## Unit testing

모든 라인이나 path 테스트 하기  
tools: unittest, pytest, tox  
<img witdh="50%" src="https://user-images.githubusercontent.com/86250281/138449567-71cb375c-0bbb-4d26-a61d-78dd0b5ff7a7.png"/>  

if문과 같이 모든 case분석하지 못하는 경우도 있음->coverage monitor라는 툴도 사용한다

## pdb
```python
# sample.py

import pathutil
def get_file_name(full_fname):
    fname = pathutil.get_path(full_fname)
    return fname
print('[(my ' + __name__ +' module)]'+ ' in '+ __file__)
fullname = __file__
filename = get_file_name(fullname)
print(f'my file name: {filename}')
```

```python
# pathutil.py

import os
def get_path(fn):
    print('[(my ' + __name__ +' module)]'+ ' in '+ __file__) 
    breakpoint() # import pdb; pdb.set_trace()
    head, tail = os.path.split(fn)
    for char in head: 
        pass   # test          
    return tail
```

<img width="70%" src="https://user-images.githubusercontent.com/86250281/138450701-248ff7a0-52ec-4ea0-94e3-494a234518ef.png"/>  

5번째줄에서 breakpoint, -> (다음에 실행될 line)

<img witdh="70%" src="https://user-images.githubusercontent.com/86250281/138451517-86caaf4d-3fa9-4953-a963-ae64dc2194c5.png"/>

* bt or w : 현재 call stack frame 보여준다 (> : 가장 최근의 frame)

<img width="70%" src="https://user-images.githubusercontent.com/86250281/138452021-2e0346ff-b1bc-48f5-83ac-3d1da5550b17.png"/>

* step : 현재 실행해야하는 함수 속으로 들어가기
* u : 현재 스텍프레임에서 up
* d : 현재 스텍프레임에서 down

<img width="70%" src="https://user-images.githubusercontent.com/86250281/138452949-b35a106c-0e65-4de7-93cc-cc2989342384.png"/>
<img width="70%" src="https://user-images.githubusercontent.com/86250281/138453015-95d21744-ceab-49b0-9189-57528bb875ad.png"/>

* l : 현재 문장 중심으로 11개 line 보여줌  
* l . : 다시 현재 위치로 복귀  
* l 숫자 : 지정한 숫자 중심으로 보기  
* ll : 함수단위로 보기  

<img width="60%" src="https://user-images.githubusercontent.com/86250281/138453994-77185031-0552-42a6-9d2c-eafde940f49e.png"/>

* a : 현재 frame에서의 인자 출력  
* p : 어떤 값 print  
* pp : 좀더 이쁘게 출력  
* whatis arg : 현재 프레임 인자의 타입 출력  
* display [expression] : 자동으로 값 바뀌면 보여줌 

<img width="70%" src="https://user-images.githubusercontent.com/86250281/138454596-a708cb31-9867-483d-8110-e40633169084.png">

다양한 breakpoint 설정 방법

* b : 모든 breakpoint 보여줌

<img width="60%" src="https://user-images.githubusercontent.com/86250281/138454772-2c851116-666e-4f0b-9857-bd17e7040744.png"/>

* cl : breakpoint 지우기

<img with="60%" src="https://user-images.githubusercontent.com/86250281/138455397-a0611d53-db8f-4ef1-8862-831e78564aa3.png"/>
<img width="60%" src="https://user-images.githubusercontent.com/86250281/138455658-c347aeb5-9e8d-4f7c-9a63-986e458721e3.png"/>

* n : 다음 라인 실행
* r : 현재 함수에서 return까지 수행
* c : breakpoint 만날때까지 실행
* unt(until) [lineno] : 지정한 line번호까지 실행(반복문 같은 경우에서 유용)

<img width="70%" src="https://user-images.githubusercontent.com/86250281/138457757-0cbc9038-e6fd-48d8-bb84-770955b01857.png"/>

특정 조건에서 breakpoint 설정해주기

* b(break) [ ([filename:]lineno | function) [,condition] ] 

설정한 breakpoint 바꾸고싶다면  
ex) condition 1 char == 'n'