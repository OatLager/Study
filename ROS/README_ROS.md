- 강의 : https://puzzling-cashew-c4c.notion.site/ROS-2-for-G-Camp-6f86b29e997e445badb69cc0af825a71

- 설치 : https://www.youtube.com/watch?v=9S0W8iCTWMQ&list=PLieE0qnqO2kTNCznjLX_AaXe2hNJ-IpVQ&index=2


# ROS2 
- 기존 ROS의 문제점 제기로 기존 ROS의 수정보다 새로운 ROS를 만듬
    - RTOS 사용 불가
    - TCPROS 사용으로 실시간성 저해
    - Python2 사용 등
- ROS와 차이점
    - DDS를 사용하여 개별 노드들을 Application Layer에서 독립 실행 가능
    - 다양한 OS 지원 (Linux, windows, MacOS, RTOS) : ROS는 Linux만 지원
    - 성능 향상


# ROS 장점
- Topic : 노드간 데이터를 주고 받을 때 Topic이란 형태로 프로토콜 정의 및 모듈화로 인한 사용편리, 개발시간 단축
- 편리한 디버깅 도구 및 시각화 도구
    - Rviz, RQt : 데이터 시각화 도구
    - tf_tree : tf 관계도 확인 
    - rqt_graph : 노드간 상관관계 확인
    - plotjuggler : 데이터 그래프 

    - Simulation : Gazebo, Ignition, ISSAC, webots
    - Embedded : rosserial, micro-ROS

- 많은 사용자
    - 커뮤니티 활성화 
    - 공개된 노드가 많아 개발시간 단축