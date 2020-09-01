# Gukwon-Petition
>국원청원 시스템을 온전히 웹으로 사용할 수 있도록 재개발하는 프로젝트입니다.

## 사용된 패키지
>- python: pyjwt
>- python: bcrypt
>- python: flask
>- python: sqlalchemy
>- python: mysql-connector-python
>- python: smtplib
>- python: openpyxl
>- JavaScript: JQuery

## Production에 사용중인 패키지
>- Python: flask-twisted
>- Python: flask_script

## Configuration
  1. Backend/ 디렉터리 하위에 'config' 디렉터리를 만드세요.
  2. Backend/config/ 디렉터리 하위에 config.expire_left 파일을 만들고, 청원 만료일 초깃값을 첫 줄에 넣어주세요.
  3. Backend/config/ 디렉터리 하위에 config.pass_ratio 파일을 만들고, 청원 동의 임계 비율 초깃값을 첫 줄에 넣어주세요.
  4. Backend/config/ 디렉터리 하위에 config.py 파일을 만들고, 다음 정보를 채워주세요.

  > db = {
  >     'user':[MySQL username],
  >     'password':[MySQL Password],
  >     'host':[MySQL Address],
  >     'port':[MySQL Port],
  >     'database':[MySQL DB Name]
  > }

  > DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"

  > JWT_SECRET_KEY = [임의의 문자열]

  > mail_server = [SMTP Server ADDR]
  > port = [SMTP Port]
  > email = [Your Email ADDR]
  > id_email = [Your Email ADDR]
  > authcode = [SMTP Password or Key]

  > fp = open("config/config.expire_left", 'r')
  > expire_left = int(fp.readline())
  > fp.close()

  > fp = open("config/config.pass_ratio", 'r')
  > pass_ratio = int(fp.readline())
  > fp.close()

