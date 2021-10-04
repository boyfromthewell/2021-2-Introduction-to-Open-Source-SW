# Open source SW overview

## Proprietary software

소유자가 저작권 가짐, 저작권 행사 가능 <-> free s/w

살 수도 없고, 배포 할수도 없다

## Free software

"We would develop a completely free software system" -> GNU 프로젝트라 불림

* 프로그램 어떤 목적이던 실행할수있는 자유
* 소스코드 변경 분석 가능
* 재배포의 자유
* 수정버전 배포 가능
* 이런 자유가 잃어버리면 유저들은 프로그램의 제어 할수 없게됨

* Free Software Foundation(FSF) -> GNU GPL(free s/w  라이센스 유저의 run, study, share, modify 보장해주는)
* stallman(사람이름) copyleft의 개념 퍼뜨림

## GNU/Linux

리눅스 커널이 1991년에 처읆으로 배포됨 under GNU GPL

***

## Open Source Software

많은 소프트웨어 회사들이 free s/w의 개념 거부하기 시작

-> 무조건 무료라는 잘못된 인식 문제, 강한 GPL 규정이 많은 영리기업의 참여 억제

-> The Open Source Initiative(OSL) 이 1998에 설립됨 (open source는 코드를 공개하고 더 실용적인 측면에서 바라봄, 다른 라이센스도 포용하는 결과 부름)

* The cathedral model (성당과 시장 : 에세이)
    * 전문가들이 조심스럽게 쌓아올리는 느낌
* The Bazzaar model
    * 계속 공유됨, 매우 효율적(소란스러운 시장과 같다)

* 에세이의 핵심주제-> 보는눈이 많으면 버그도 줄어든다, 오픈소스 설립에 핵심이됨

# Open source definition

1. 자유로운 재배포
2. 소스코드 필요
3. 프로그램 수정 허용, 재배포 허용
4. 저작자의 소스코드 원형 유지
5. 개인과 그릅의 차별 금지
6. 분야 차별금지
7. 라이센스 배포
8. 특정제품에만 유효 라이센스 금지
9. 다른 s/w 제한 라이센스 금지
10. 기술 중립적이어야함

***

* FOSS - free s/w와 오픈소스 사이의 차이 신경안쓰고 정의 하는 용어

* Freeware - 정확한 정의는 불가하지만, 소스코드 x, 수정안됨 재배포 가능, 수정 x, 수정물 배포 x

* shareware - 사용하는데 있어 기능적인 제약, 일정시간만 사용, 소스코드 제공 x

* 대부븐의 프리웨어와 쉐어웨어는 fs/oss아님

    * binary코드만 제공하기 떄문

    * 저작자가 자신의 고유한 권리들 행사가능

* proprietary s/w로 간주 가능

## Advantages of OSS

* 적은 비용
* 개발시간, 비용 낮음
* 신뢰성 품질
* 다양한 외부 도움
* Vender lock-in 줄여줌

### disadvantages of OSS

* 유저 친화적이지 않을수있다
* 지식 재산권의 위험(특허권 침해 할 수 있음)
* 잠재적인 비용 -> ex) 기존 시스템과 통합하고 커스터 마이징 하는 과정에서
***
# OSS Licenses

* Copyright(저작권) -> 저작권리

    실행, 수정, 공유 -> 다른사람에게 행사할수있는 권한

* License - 창작자가 누군가에세 권한 행사하는 방식, 일종의 계약
    * 몇가지 의무가 있음 
    * 소스코드의 저작권 고지
    * 동일한 조건에서 배포해라

* 소스코드가 라이센스 없다면, 어떤 권리도 없다는 뜻


## Copyleft licenses

free s/w 라이센스 + share alike 라이센스 (진정한 의미의 프리 s/w), 상호주의적

free s/w 퍼뜨리고자 촉진함, 동일 조건에서 배포해라

<img width="60%" src="https://user-images.githubusercontent.com/86250281/135794055-0d7ee131-546b-43fe-a3bf-ce9f0118f294.png"/>

### copyleft vs permissive license (제약의 경중차이)
* copyleft : 파생물을 동일 조건으로 배포해라
* permissive : 수정물 있어도 공개하지 않아도됨

## General Public License (GPL)

첫번째 copyleft 라이센스, 수정 재배포할때 소스코드 공개되어야함, 배포시에만 소스코드 공개하면됨

강한 라이센스 전파력, 하나의 프로그램으로 간주됨(GPL 코드로 인한 파생물)

<img width="60%" src="https://user-images.githubusercontent.com/86250281/135795001-49b6a12a-22e5-4b42-b70b-fe3da39ba968.png"/>
예외) 소켓, 파이프, 시스템콜 사용한경우 

## Affero General Public License (AGPL)

GPL기반의 라이센스지만 더 강력, GPL은 배포할때만 소스코드 공개해야했지만, AGPL은 실행하고 접속할때 공개할수있음

## Lesser General Public License (LGPL)

그전 copyleft 라이센스보다 week함 (LGPL < GPL <AGPL)

같은 파일에서만 수정된 부분으로 공개하면 됨(LGPL파트쪽만 공개)

<img width="60%" src="https://user-images.githubusercontent.com/86250281/135795463-01e7a4a6-8726-4458-8b8a-0f24b487c8fb.png"/>

## Mozilla Public License (MPL)

week copyleft 라이센스, file-level copyleft, MPL 라이센스에서 수정변경 이뤄지면 소스코드 공개, 나머지는 필요 X

***
## Permissive Licenses

no copyleft/no 상호주의, 제약 거의 없음
ex) BSD , MIT, Apache


(정리)

<img width="50%" src="https://user-images.githubusercontent.com/86250281/135795972-91032b23-7180-44c1-9897-78b4d06e7c81.png"/><img width="50%" src="https://user-images.githubusercontent.com/86250281/135795986-705372a0-9faf-48ac-bb25-ae2b866045be.png"/>