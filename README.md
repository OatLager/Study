# Study

## ROS
 - 예정


## Coding  
- WEB 개발 (HTML/CSS/JavaScript)
- Desktop App(일렉트론)
- Python

## GitHub
 - GitHub Desktop 사용으로 관리
 - 참고강의 : https://www.youtube.com/watch?v=0YsMEPxi_wc&list=PLeNJ9AVv90q36cH_SMBTZ26MMXgyNtE9W
   - 01. repository 생성 또는 가져오기(clone) 
   - 02. (in VS Code) 코드 생성 및 수정 (Open in Visual Studio Code in GitDesktop app)
   - 03. (in GitHub Desktop) 변경사항(Changes) Summary 및 Description 작성 -> Commit to main 
   - 04. (in GitHub Desktop) Push origin -> Github에 수정사항 반영
   - 05. (in GitHub Desktop) Fetch origin - 다른곳에서 변경된 소스코드 받아오기(from Github) 
  
## Docker
 - 어플리케이션 구동에 필요한 모든것들이 컨테이너에 포함됨. 
 - 어떤 pc에서 언제든지 구동 가능. 
 
  컨테이너 구성 
  1. Dockerfile 만들기
    - 어플리케이션 구동에 필요한 파일
    - 프레임워크, 라이브러리 설치
    - 필요 환경변수
    - 구동에 필요한 스크립트 작성 가능
  2. image 생성
    - Dockerfile을 통한 어플리케이션 image 생성
    - 어플리케이션 실행에 필요한 코드, 런타임환경, 시스템툴, 시스템라이브러리 등 모든 세팅 포함
    - 변경 불가
  3. Container
    - image를 고립된 개별 환경에서 image를 통해 어플리케이션 동작 
    
    
 Docker engine 설치   
  - Download Docker Desktop : https://www.docker.com/     
  
 Dockeerfile 만들기
  - Layer 형식으로 작성, 제일 빈번히 변경되는 파일일 수록 마지막에 작성.
  - 변경된 부분부터 image를 만들기 때문에 시간단축, 효율성이 높음. 
  - docker build 명령어로 image 생성
  
 - docker run 명령어로 컨테이너 실행
 - docker ps 현재 실행중인 컨테이너 확인
 
 
 ## Qt
  - GUI 개발 툴, 크로스 플랫폼
  - 프론트 : QML(자체 언어), 자바스크립트
  - 백엔드 : C++, Python
 
 
 ## 확장자
  - json : javascript object notation / 자바스크립트 오브젝트 표현방식, 설정에 많이 사용됨.
           (https://blog.naver.com/wideeyed/221722164932)
  - xml :  Extensible Markup Language / 데이터의 이동, 구조 및 설정 저장
           (https://ko.eyewated.com/xml-%ED%8C%8C%EC%9D%BC%EC%9D%B4%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9E%85%EB%8B%88%EA%B9%8C/)
  - yaml : YAML Ain't Markup Language / 가독성이 뛰어남
           (https://blog.naver.com/wideeyed/221090209367)
 
