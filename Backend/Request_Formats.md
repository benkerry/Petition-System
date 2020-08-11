 Login Request Format
 {
   "id":<str>,
   "pwd":<str>
 }

 Register Request Format
 {
   "id":<str>,
   "pwd":<str>,
   "pwd_chk":<str>,
   "nickname":<str>,
   "stdid":<int>,
   "authcode":<str>
 }

 get_petition Request Format
 {
   "count":<int>,
   "type":<str:'newest'/'hottest'/'oldest'
 }

 change_my_pwd Request Format
 {
     "pwd":<str>,
     "pwd_chk":<str>,
     "token":<str>
 }

 change_my_info Request Format
 {
   "email":<str>,
   "nickname":<str>,
   "token":<str>
 }


 write_petition Request Format
 {
   "title":<str>,
   "description":<str>,
   "token":<str>
 }

 write_debate Request Format
 {
   "petition_id":<int>,
   "description":<str>,
   "token":<str>
 }

 support_petition Reuqest Format
 >
 >
 >

