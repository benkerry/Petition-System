  Register Request Format
 {
   "email":<str>,
   "pwd":<str>,
   "pwd_chk":<str>,
   "nickname":<str>,
   "stdid":<int>,
   "authcode":<str>
 }
 
 Login Request Format
 {
   "email":<str>,
   "pwd":<str>
 }

 get_petition Request Format
 {
   "petition_id":<int>
 }

 get_petition_metadatas Request Format
 {
   "count":<int>,
   "type":<str:'all'/'newest'/'hottest'/'oldest'/'answered'
 }

 change_my_pwd Request Format
 {
     "pwd":<str>,
     "change_pwd":<str>,
     "change_pwd_chk":<str>,
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
   "contents":<str>,
   "token":<str>
 }

 write_debate Request Format
 {
   "petition_id":<int>,
   "contents":<str>,
   "token":<str>
 }

 change_priv Request Format
 {
   "tgt_id":<int>,
   "priv":<int>,
   "token":<str>
 }

 support_petition Reuqest Format
 {
   "petition_id":<int>,
   "token":<str>
 }

 withdraw Request Format
 {
   "pwd":<str>,
   "token":<str>
 }

 delete_user Request Format
 {
   "nicknames":[<int>],
   "token":<str>
 }